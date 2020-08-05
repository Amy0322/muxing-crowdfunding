<template>
  <div>
    <body class="bg">
      <div class="container" id="app">
        <!-- 相似案例 -->
        <div class="functionTitle">
          <h3>相似的募資成功案例</h3>
        </div>
        <div class="row row-cols-1 row-cols-md-3">
          <FundraisingCard
            v-for="fundraising in fundraisings"
            :key="fundraising.id"
            :fundraising="fundraising"
          />
        </div>
        <!-- 回饋方案 -->
        <div class="functionTitle2">
          <h3>相似案例的搶手回饋方案</h3>
        </div>
        <FeedbackCard
          v-for="fundraising in fundraisings"
          :key="fundraising.id"
          :fundraising="fundraising"
        />
        <input class="re_button" value="重新評估" @click="goForm()" />
      </div>
    </body>
  </div>
</template>

<style>
* {
  /* border: solid 1px; */
  font-family: "微軟正黑體";
  position: relative;
  transition-duration: 0.3s;
  list-style-type: none;
  letter-spacing: 1.5px;
  line-height: 25px;
  color: #41404b;
  vertical-align: top;
}

.bg {
  margin: 0;
  padding-top: 30px;
  background-color: #f5f5f5;
}

.functionTitle > h3 {
  font-weight: 550;
  padding: 90px 0px 60px 0px;
}

.functionTitle2 > h3 {
  font-weight: 550;
  padding: 40px 0px 60px 0px;
}

.re_button {
  font-family: "微軟正黑體";
  background: #281483;
  border: 0px;
  border-radius: 15px;
  color: white;
  font-weight: 550;
  outline: none;
  padding: 10px 0px;
  text-align: center;
  margin-bottom: 40px;
}

.re_button:hover {
  background: linear-gradient(to right, #281483 0%, #be78d1 100%);
  cursor: pointer;
}

.re_button:active {
  background: linear-gradient(to right, #281483 0%, #be78d1 100%);
}
</style>

<script>
import FundraisingCard from "../components/FundraisingCard.vue";
import FeedbackCard from "../components/FeedbackCard.vue";
export default {
  components: {
    FundraisingCard,
    FeedbackCard
  },
  methods: {
    goForm() {
      this.$router.push({ path: "/form" });
    }
    // Trim(str) {
    //   str表示要轉換的字串
    //   return str.replace(/\n|\r\n/g, "<br/>");
    //   str = str.replace(/(?:\r\n|\r|\n)/g, "<br>");
    // }
  },
  data() {
    return {
      // 募資方案假資料
      fundraisings: [
        {
          id: 1,
          title: "Libratone Track Air+ 真無線藍牙耳機",
          author: "Libratone TW",
          description: "來自北歐丹麥的天籟之音，高端耳機唯一首選！",
          img:
            "https://static.flyingv.asia/static/1024x768/projects/26454/5ef97ce2e7903.jpg",
          url: "https://www.flyingv.cc/projects/26454",
          feedback: {
            id: 1,
            content:
              "Track Air+ 主動降噪耳機 x1 (黑/白)\r早鳥下單加贈原廠矽膠套 x1 (黑/粉)\n募資期間下單【台灣總代理保固兩年】 商品顏色請於結帳頁選購",
            pricing: "6,980",
            donator: 4,
            amountRaised: "27,920",
            amountReached: "100,000",
            img:
              "https://static.flyingv.asia/static/333x/projects/26454/reward/5f052f7de393a.jpg",
            url: "https://www.flyingv.cc/projects/26454",
            proportion: 11.11
          }
        },
        {
          id: 2,
          title:
            "全球首款美膚蓮蓬頭｜ Bollina Wide 超微細奈米泡泡蓮蓬頭｜洗淨保濕保溫",
          author: "W-emoving",
          description:
            "100%日本專利技術製造X原裝進口．極致超微細氣泡洗淨力．肌膚含水量提升8%．肌膚表面溫度提升6倍．最大省水50%水量",
          img:
            "https://static.flyingv.asia/static/1024x768/projects/26111/5ed0d9cd0449d.jpg",
          url: "https://www.flyingv.cc/projects/26415",
          feedback: {
            id: 1,
            content:
              "【 限量早鳥優惠 】◆ AIR6 x 1 ◆ 電源供應器 x 1 ◆ C2C 快充充電線 x 1 -- 未來預計市價 6,900元，現省 3,410 元！ -- 重要提醒：① 台灣本島免運費 ② 海外運費請參考常見問答 ③ 請於回饋調查填寫顏色及數量，若無選擇將隨機出貨 ④ 如需統編請留於備註欄【 限量早鳥優惠 】◆ AIR6 x 1 ◆ 電源供應器 x 1 ◆ C2C 快充充電線 x 1 -- 未來預計市價 6,900元，現省 3,410 元！ -- 重要提醒：① 台灣本島免運費 ② 海外運費請參考常見問答 ③ 請於回饋調查填寫顏色及數量，若無選擇將隨機出貨 ④ 如需統編請留於備註欄",
            pricing: "2,220",
            donator: 2,
            amountRaised: "22,220",
            amountReached: "200,000",
            img:
              "https://static.flyingv.asia/static/333x/projects/26111/reward/5ed8a3f6e3ea0.jpg",
            url: "https://www.flyingv.cc/projects/26415",
            proportion: 22.22
          }
        },
        {
          id: 3,
          title: "Duopresso 隨行膠囊咖啡機 ｜你的隨行咖啡師",
          author: "innohome",
          description:
            "可泡咖啡粉與咖啡膠囊、可泡熱水與冷水、可泡咖啡與茶，想找隨行咖啡機~DUOPRESSO是您最佳的選擇。",
          img:
            "https://static.flyingv.asia/static/1024x768/projects/26415/5ef1cf3b035ff.png",
          url: "https://www.flyingv.cc/projects/26111",
          feedback: {
            id: 1,
            content:
              "限量早鳥價  限量500組 市價$2,880｜超早鳥$2,080 隨行咖啡機*1",
            pricing: "3,330",
            donator: 3,
            amountRaised: "33,330",
            amountReached: "300,000",
            img:
              "https://static.flyingv.asia/static/333x/projects/26415/reward/5ef1d07aac8e9.png",
            url: "https://www.flyingv.cc/projects/26111",
            proportion: 33
          }
        }
      ]
    };
  }
};
</script>
