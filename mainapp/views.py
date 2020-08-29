from django.shortcuts import render
from rest_framework import viewsets
from . serializers import ProjectSerializer, CampaignSerializer
from .models import Project, campaign
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
from . forms import MyForm

# Create your views here.
# 需要导入相关的模块
#
class ProjectSet(viewsets.ModelViewSet):
	# permission_classes = (
	# 	IsAuthenticated,
	# )
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # permission_classes = (AllowAny,)

class CampaignSet(viewsets.ModelViewSet):
    queryset = campaign.objects.all()
    serializer_class = CampaignSerializer
    # permission_classes = (AllowAny,)

def myform(request):
	if request.method == 'POST':
		form = MyForm(request.POST)
		if form.is_valid():
			myform = form.save(commit=False)
		else:
			form = MyForm()


@api_view(["POST"])
def similarProj(request):
	try:
		#處理資料
		text2vec_df = pd.read_pickle("/Users/hw_students/proj02_data/text2vec_df.pkl")
		df = pd.read_pickle("/Users/hw_students/proj02_data/df.pkl")
		#處理Input
		userdata = request.data
		unit = np.array(list(userdata.values()))
		#unit = unit.reshape(1, -1) #全部放到同一個陣列
		articles = """
		全球首款多效乳清蛋白飲產品，添加獨家維生素D及鎂配方，幫助提案支持者完備吃練睡健康金三角。口味來自各國嚴選食材製作，搭配美國優質乳源乳清蛋白，飽享世界特選味覺體驗。"""

		project_name = 'Body Goals 多效乳清蛋白飲 | 獨家維生素D及鎂配方 | 打造吃、練、睡健康循環'
		# 把使用者的文本放入
		text2vec_df = text2vec_df.append(pd.DataFrame(text2vec.encode(unit[0])).T)
		# 把使用者的專案放入
		titles = df.title.tolist() + [unit[1]]
		cs = cosine_similarity(text2vec_df)

		def getSimiliarArticle(articleid):
			print('查詢募資專案:', titles[articleid])
			data = []
			for pos in cs[articleid].argsort()[::-1][1:]:
				if cs[articleid][pos] >= 0.9:
					#             print('相關募資專案: ',titles[pos],cs[articleid][pos])
					data.append(titles[pos])
			return data

		RETURN_NUMBER = 3

		# 回傳使用者的方案（最後一筆），選10個
		similar_project = getSimiliarArticle(-1)
		result = df[df['title'].apply(lambda x: x in similar_project[:RETURN_NUMBER])]
		result = result.to_dict('index')
		return JsonResponse(result,safe=False)

		####
		# mdl=joblib.load("/Users/sahityasehgal/Documents/Coding/DjangoApiTutorial/DjangoAPI/MyAPI/loan_model.pkl")
		#mydata=pd.read_excel('/Users/sahityasehgal/Documents/Coding/bankloan/test.xlsx')
		# mydata=request.data
		# unit=np.array(list(mydata.values()))
		# unit=unit.reshape(1,-1)
		# scalers=joblib.load("/Users/sahityasehgal/Documents/Coding/DjangoApiTutorial/DjangoAPI/MyAPI/scalers.pkl")
		# X=scalers.transform(unit)
		# y_pred=mdl .predict(X)
		# y_pred=(y_pred>0.58)
		# newdf=pd.DataFrame(y_pred, columns=['Status'])
		# newdf=newdf.replace({True:'Approved', False:'Rejected'})
		# return JsonResponse('Your Status is {}'.format(newdf), safe=False)
	except ValueError as e:
		return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


