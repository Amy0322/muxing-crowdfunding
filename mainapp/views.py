from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProjectSerializer, CampaignSerializer,UserSerializer
from mainapp.models import Project, Campaign, User
from rest_framework import permissions
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
import pickle
import pandas as pd
import text2vec
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import joblib
from rest_framework.permissions import IsAuthenticated
import requests
from .forms import MyForm
from django.db import connection
import json



# Create your views here.
# 需要导入相关的模块
#
camp = pd.read_excel("/Users/hw_students/proj02_data/campaign_0828.xlsx")

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def getSimiliarArticle(articleid, cs, titles):
    data = []
    for pos in cs[articleid].argsort()[::-1][1:]: #????
        if cs[articleid][pos] >= 0.9:
            data.append(titles[pos])

    return data

# def myform(request):
#     if request.method == "POST":
#         form = MyForm(request.POST)
#         if form.is_valid():
#             myform = form.save(commit=False)
#         else:
#             form = MyForm()

def round_up(value):
    return round(value * 100) / 100

# 回饋方案排序
def sorting(proj_id):
    df2 = pd.DataFrame()
    df2 = camp.loc[camp["project"] == proj_id]
    df2.index = range(len(df2))
    # 每個回饋方案募得金額
    fund = []
    for i in range(len(df2)):
        # mul = 0
        mul = df2["campaign_price"][i] * df2["campaign_people"][i]
        fund.append(mul)
    df2["funding_price"] = fund

    # 總額
    total = []
    for i in range(len(df2)):
        t = df2["funding_price"].sum()
        total.append(t)
    df2["total_price"] = total

    # 佔比
    ratio = []
    for i in range(len(df2)):
        r = df2["funding_price"][i] / df2["funding_price"].sum() * 100
        r1 = round_up(r)
        ratio.append(r1)
    df2["ratio"] = ratio

    # 最後排序
    df2 = df2.sort_values("ratio", ascending=False)
    df2.index = range(len(df2))

    return df2


#將所有募資案的回饋方案排序
def campaignlist(df):
    df.index = range(len(df))
    list_of_list = []
    for i in range(len(df)):
        t = df["project_id"][i]
        name = df["title"][i]
        sort = sorting(t)
        list_dict = []
        list_dict = sort.to_dict(orient="records")
        proj = list(Project.objects.filter(id=t).values("id", "title", "author", "description", "img", "url"))
        proj[0]["feedbacks"] = list_dict
        list_of_list.append(proj[0])

    return list_of_list

def campaignlist_origin(df):
    df.index = range(len(df))
    list_of_list = []
    for i in range(len(df)):
        t = df["project_id"][i]
        name = df["title"][i]
        sort = sorting(t)

        list_dict = []
        list_dict = sort.to_dict(orient="records")
        campaign = []
        campaign.append(name)
        campaign.append(list_dict)
        list_of_list.append(campaign)
    return list_of_list

# 募資金額
def funding_target_med(df):
    funding_target_med = int(df["funding_target"].median())
    return funding_target_med
# 募資期間
def days_med(df):
    days_med = int(df["days"].median())
    return days_med
# 回饋方案數
def cam_count_med(df):
    cam_count = []
    for i in df["project_id"]:
        count = Campaign.objects.filter(project__id=i).count()
        cam_count.append(count)
    # df["campaign_count"] = cam_count
    # cam_count_med = df["campaign_count"].median()
    return int(np.median(cam_count))

def funding_target_similar(money,df):
    result = df[df["funding_target"].between(money*0.95,money*1.05)]
    suc = result["status"] == "success"
    result = result[suc]
    result = result.sort_values(by = "funding_target")
    result.index = range(len(result))

    p1 = result["funding_target"] == money
    p2 = result["funding_target"] != money
    part1 = result[p1]
    part2 = result[p2]

    part2.index = range(len(part2))

    if (len(part1)>10):
        result = part1.nlargest(10,"now_funding")
    elif(len(part1)<10):
        num = 10 - len(part1)
        n = len(part2)
        first = 0
        last = n - 1
        while last - first + 1 > num:
            q = abs(part2["funding_target"][first] - money)
            w = abs(part2["funding_target"][last] - money)
            if w >= q:
                last -= 1
            elif w < q:
                first += 1
        part2 = part2[first:last + 1]
        result = pd.concat([part1,part2])

    result = result.sort_values(by = "funding_target")
    return result

def interval(df):
    return {"mininterval":df["funding_target"].min(),"maxinterval":df["funding_target"].max()}

def get_stats(group):
    return {"min":group.min(),"max":group.max()}
def round_up(value):
    return round(value * 100) / 100

# 金額區間
def funding_table(list_of_list, df):
    colname = ["campaign_price", "campaign_people", "title"]
    table = pd.DataFrame(columns=colname)
    df1 = pd.DataFrame()
    for i in range(len(list_of_list)):
        df1 = pd.DataFrame(list_of_list[i][1])
        # df1 = df1.drop(["campaign_img", "campaign_content", "funding_price", "total_price", "ratio"], axis=1)
        title = []
        for j in range(len(df1)):
            t = list_of_list[i][0]
            title.append(t)
        df1["title"] = title
        table = pd.concat([table, df1])
    table = table.drop(["campaign_img", "campaign_content", "funding_price", "total_price", "ratio"], axis=1)

    table = table.sort_values(by="campaign_price")
    table.index = range(len(table))

    grouping = pd.qcut(table["campaign_price"], 10, labels=False)
    grouped = table["campaign_price"].groupby(grouping)
    test = grouped.apply(get_stats)
    bar = []
    for i in range(10):
        bar.append(str(test[i]["min"]) + "-" + str(test[i]["max"]))

    group = []
    for i in range(len(table)):
        for j in range(10):
            if (table["campaign_price"][i] >= test[j][0]) & (table["campaign_price"][i] <= test[j][1]):
                group.append(j)
    table["group"] = group

    fundraisings = []
    proj_id = df["project_id"]
    color = ["#98d86d", "#61Bf81", "#61bfbf", "#79aad0", "#41709e", "#cda7dd", "#a286c7", "#7154c0", "#aa67d1",
             "#d167b2"]
    for i in range(len(df)):
        print(i)
        proj = proj_id[i]
        name = df["title"][i]
        url = df["url"][i]
        fund = df["funding_target"][i]
        now_fund = df["now_funding"][i]
        fund_ratio = (now_fund / fund) * 100
        round_fund_ratio = round_up(fund_ratio)
        con = table["project"] == proj
        tab1 = table[con]
        tab1 = tab1.drop(["campaign_price", "project", "title","id"], axis=1)
        tab1 = tab1.groupby(["group"]).sum()
        people = []
        number = tab1.index
        for j in range(10):
            if (j in number):
                people.append(int(tab1["campaign_people"][j]))
            else:
                people.append(0)

        # id_num = [1,2,3,4,5,6,7,8,9,10]

        fund = {"id": int(i + 1), "color": color[i], "name": name, "url": url, "data": people,
                "proportion": round_fund_ratio}
        fundraisings.append(fund)
    data1 = interval(df)
    minnum = data1["mininterval"]
    maxnum = data1["maxinterval"]
    chart = {"mininterval": int(minnum), "maxinterval": int(maxnum), "bar": bar, "fundraising": fundraisings}

    return chart

@api_view(["POST"])
def similarProj(request):
    final_result = {"fundraisings":[],"rates":[],"points":[],"chart":[]}
    if request.method == "POST":
        try:
            # 處理資料
            text2vec_df = pd.read_pickle("/Users/hw_students/proj02_data/text2vec_df.pkl")
            df = pd.read_pickle("/Users/hw_students/proj02_data/df.pkl")
            # 處理Input
            userdata = request.data
            print("userdata:")
            print(userdata)
            unit = np.array(list(userdata[0].values()))
            # unit = unit.reshape(1, -1) #全部放到同一個陣列
            # 把使用者的文本放入
            text2vec_df = text2vec_df.append(pd.DataFrame(text2vec.encode(unit[5])).T)
            # 把使用者的專案放入

            print(unit[0])
            titles = df.title.tolist() + [unit[0]]
            # titles = df.title.tolist() + ["-1"]
            cs = cosine_similarity(text2vec_df)

            ###相似案例
            RETURN_NUMBER = 3
            similar_project = getSimiliarArticle(-1, cs, titles)  # 分數>0.9 的所有募資案id(type=list)
            new = df[df["title"].apply(lambda x: x in similar_project[:RETURN_NUMBER])]
            fundraisings = campaignlist(new)
            final_result["fundraisings"] = fundraisings
            # print("similar_project")
            # print(similar_project)
            ###取十筆
            NUMBER = 10
            df_10 = df[df["title"].apply(lambda x: x in similar_project[:NUMBER])]
            ten_proj = []
            for i in range(len(df_10)):
                one_proj = {}
                one_proj["id"] = int(df_10.iloc[i:i+1, :].project_id.values[0])
                one_proj["title"] = str(df_10.iloc[i:i+1, :].title.values[0])
                one_proj["url"] = str(df_10.iloc[i:i+1, :].url.values[0])
                funding_target = int(df_10.iloc[i:i+1, :].funding_target.values[0])
                now_funding = int(df_10.iloc[i:i+1, :].now_funding.values[0])
                one_proj["amountRaised"] = now_funding
                one_proj["amountReached"] = funding_target
                one_proj["proportion"] = round(now_funding / funding_target * 100, 2)
                one_proj["status"] = str(df_10.iloc[i:i+1, :].status.values[0])
                ten_proj.append(one_proj)
            final_result["rates"] = ten_proj

            ###處理落點分布
            CALCULATE_NUMBER = 15
            df_15 = df[df["title"].apply(lambda x: x in similar_project[:CALCULATE_NUMBER])]
            #print(similar_project[:CALCULATE_NUMBER])
            points = {}
            points["averageTarget"] = funding_target_med(df_15)
            points["userTarget"] = unit[2]
            points["averageTime"] = days_med(df_15)
            points["userTime"] = unit[3]
            points["averageFeedback"] = cam_count_med(df_15)
            points["userFeedback"] = unit[4]
            final_result["points"] = points

            ###處理圖表
            # 找出和輸入金額最接近的十筆募資案
            money = int(unit[2])  # 使用者輸入的金額
            df3 = pd.DataFrame()
            df3 = funding_target_similar(money, df)
            # 分割回饋方案
            list3 = campaignlist_origin(df3)

            # print(list3)
            # 相似金額分布
            chart = funding_table(list3, df3)
            final_result["chart"] = chart
            print(final_result)

            return JsonResponse(final_result, safe=False)
        except ValueError as e:
            return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
