<template>
  <div>
    <body>
      <form
        class="container"
        id="app"
        @submit.prevent="checkForm"
        action="/sonwhere"
        method="get"
      >
        <div class="formTitle">
          <h3>填寫募資方案資料</h3>
        </div>
        <div class="row-cols-md-1 text-left">
          <p>募資專案名稱：</p>
          <input class="name" v-model="formData.name" placeholder="請輸入募資專案名稱" />
          <p>募資金額(元)：</p>
          <input
            class="amount"
            v-model.number="formData.amount"
            type="number"
            placeholder="請輸入募資金額"
          />
          <p>類別：</p>
          <select class="type" v-model="formData.type">
            <option v-for="type in types" :key="type.id" :type="type">{{
              type
            }}</option>
          </select>
          <p>內容簡介：</p>
          <textarea
            class="content"
            v-model="formData.content"
            placeholder="請輸入募資專案內容簡介"
          ></textarea>
          <div class="error" v-if="errors.length">
            <img class="error_img" src="https://i.imgur.com/xdZuo8J.png" /><span
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
  font-weight: 550;
  padding: 90px 60px 30px 60px;
}

.name,
.amount,
.type,
.content {
  box-shadow: 0px 3px 10px grey;
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
  border-radius: 15px;
  color: white;
  font-weight: 550;
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
  font-weight: 550px;
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
</style>

<script>
  import api from '../api/index';

export default {
  data() {
    return {
      formData:{
        name:'',
        amount:'',
        type:'',
        content:'',
      },
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
      content: null,
      projects: [],
      errors: []
    };
  },
  methods: {
    // submitNote () {
    //   api.fetchNotes('post', null, this.formData).then(res => {
    //     this.msg = 'Saved'
    //   }).catch((e) => {
    //     this.msg = e.response
    //   })
    // },
    goHome() {
      this.$router.push({ path: "/" });
    },
    checkForm: function(e) {
      //拿到資料跳到結果頁面
      if (this.formData.name && this.formData.amount && this.formData.type && this.formData.content) {
        let project_data = {
          name: this.formData.name,
          amount: this.formData.amount,
          type: this.formData.type,
          content: this.formData.content
        };
        this.projects.push(project_data);
        // 跳轉至最後一頁
        //this.$router.push({ path: "/result" });

        api.fetchNotes('post', null, this.formData).then(res => {
        //this.msg = 'Saved';
          console.log('post');
        }).catch((e) => {
          this.msg = e.response
        })
      }
      //資料有缺則跳出警告
      this.errors = [];
      if (!this.formData.name) this.errors.push("募資專案名稱");
      if (!this.formData.amount) this.errors.push("募資金額");
      if (!this.formData.type) this.errors.push("類別");
      if (!this.formData.content) this.errors.push("內容簡介");



      e.preventDefault();
    }
  }
};
</script>
