<template>
  <div>
    <body id="app">
      <form
        class="container"
        @submit.prevent="checkForm"
        action="/sonwhere"
        method="post"
      >
        <div class="formTitle">
          <h3>填寫募資方案資料</h3>
        </div>
        <div class="row-cols-md-1 text-left">
          <p>募資方案名稱：</p>
          <input class="name" v-model="name" placeholder="請輸入募資方案名稱" />
          <p>類別：</p>
          <select class="type" v-model="type">
            <option v-for="type in types" :key="type.id" :type="type">{{
              type
            }}</option>
          </select>
          <p>目標金額(元)：</p>
          <input
            class="amount"
            v-model.number="amount"
            type="number"
            placeholder="請輸入目標金額"
          />
          <p>募資期間(天)：</p>
          <input
            class="period"
            v-model.number="period"
            type="number"
            placeholder="請輸入募資期間"
          />
          <p>回饋方案數(種)：</p>
          <input
            class="feedback_num"
            v-model.number="feedback_num"
            type="number"
            placeholder="請輸入回饋方案數"
          />
          <p>內容簡介：</p>
          <textarea
            class="content"
            v-model="content"
            placeholder="請輸入募資方案內容簡介"
          ></textarea>
          <div class="error" v-if="errors.length">
            <img class="error_img" src="https://i.imgur.com/nYqtCEr.png" /><span
              class="error_msg"
              >請輸入<span v-for="(error, index) in errors" :key="error.id"
                ><span>{{ error }}</span
                ><span v-if="index+1 &lt; errors.length">、</span></span
              ></span
            >
          </div>
        </div>
        <div class="row row-cols-1 row-cols-md-1">
          <div>
            <input
              class="purple_button btn_confirm"
              type="submit"
              value="確認"
            />
            <input
              class="purple_button btn_cancel"
              type="reset"
              value="取消"
              @click="goHome"
            />
          </div>
        </div>
      </form>
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
  font-size: 14px;
}

.bg {
  margin: 0;
  padding-top: 30px;
  background-color: #f5f5f5;
}

.formTitle > h3 {
  font-weight: 500;
  padding: 110px 60px 30px 60px;
}

.name,
.amount,
.type,
.period,
.feedback_num,
.content {
  box-shadow: 0 3px 12px 0 rgba(0, 0, 0, 0.2), 0 1px 15px 0 rgba(0, 0, 0, 0.2);
  border: 0px;
  border-radius: 5px;
  padding: 5px 10px;
  margin-bottom: 30px;
}

.name,
.amount {
  width: 50%;
}

.type {
  cursor: pointer;
}

.content {
  width: 100%;
  height: 300px;
}

.purple_button {
  background: #281483;
  border: 0px;
  border-radius: 30px;
  color: white;
  font-weight: 500;
  padding: 10px 40px;
  margin: 30px 40px 40px 40px;
  outline: none;
}

.purple_button:hover {
  background: linear-gradient(to right, #281483 0%, #be78d1 100%);
}

.purple_button:active {
  background: linear-gradient(to right, #281483 0%, #be78d1 100%);
}

.error {
  width: 100%;
  padding: 10px;
  border-radius: 5px;
  background: #fcd4dc;
  font-weight: 500;
}
.error_img {
  width: 20px;
  height: 20px;
  top: -2px;
}

.error_img,
.error_msg {
  margin: 0px 5px;
}

input:focus,select:focus,textarea:focus{
  outline:none
}
</style>

<script>
// import api from '../api/index'
import { getAPI } from '../api/index'
import axios from "axios";
export default {
  data() {
    return {
      name: null,
      amount: null,
      types: [
        "音樂",
        "攝影",
        "出版",
        "時尚",
        "設計",
        "表演",
        "藝術",
        "科技",
        "教育",
        "遊戲",
        "飲食",
        "空間",
        "社會",
        "在地",
        "公共",
        "影視",
        "休閒",
        "運動",
        "旅行",
        "插畫漫畫",
        "電影動畫",
        "地方創生"
      ],
      type: null,
      content: null,
      projects: [],
      errors: [],
      result:'',
      period: null,
      feedback_num: null
    };
  },
  methods: {
    goHome() {
      this.$router.push({ path: "/" });
    },
    checkForm: function(e) {
      //拿到資料跳到結果頁面
      if (
        this.name &&
        this.amount &&
        this.type &&
        this.content &&
        this.period &&
        this.feedback_num
      ) {
        let project_data = {
          "name": this.name,
          "type": this.type,
          "amount": this.amount,
          "period": this.period,
          "feedback_num": this.feedback_num,
          "content": this.content,
        };
        this.projects.push(project_data);
        // api.fetchNotes('post', null, this.projects).then(res => {
        //   // this.msg = 'Saved'
        //   console.log('get input')
        //   console.log(this.projects)
        // }).catch((e) => {
        //   this.msg = e.response
        //   console.log('error happen')
        // })
      // axios({
      //   method: 'post',
      //   url: 'http://127.0.0.1:8000/mainapp/status/',
      //   data: this.projects,
      // });

        getAPI.post('http://127.0.0.1:8000/mainapp/status/',this.projects)
          .then(response => {
            console.log('Post API has recieved data')
            this.result = response.data
            // 跳轉至最後一頁
            this.$router.push({ path: "/result" ,query:this.result});
          })
          .catch(err => {
            console.log(err)
          })


      }
      //資料有缺則跳出警告
      this.errors = [];
      if (!this.name) this.errors.push("募資方案");
      if (!this.type) this.errors.push("類別");
      if (!this.amount) this.errors.push("目標金額");
      if (!this.period) this.errors.push("募資期間");
      if (!this.feedback_num) this.errors.push("回饋方案數");
      if (!this.content) this.errors.push("內容簡介");

      e.preventDefault();
    }
  }
};
</script>
