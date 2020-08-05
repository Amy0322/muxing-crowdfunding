<template>
  <div>
    <!-- navbar -->
    <nav
      class="navbar navbar-expand-sm navbar-light bg-light fixed-top navbar-top mx-auto border-bottom"
    >
      <div class="container">
        <button class="home-button" @click="goHome">OurName</button>
        <div class="navbar-collapse collapse">
          <button class="navbar-nav ml-auto nav nav-button" @click="goForm">
            開始評估
          </button>
        </div>
      </div>
    </nav>
    <!-- 介紹平台區域 -->
    <section
      class="welcome-area"
      style="margin: 0px; padding-bottom: 0px; padding: 100px;"
    >
      <div class="container">
        <div class="h-100">
          <div class="row row-cols-1 row-cols-md-2">
            <div class="col align-self-center">
              <div class="container-fluid">
                <div class="row">
                  <div class="col welcome-title">
                    <h2>行駛在所有創意的航程</h2>
                    <h2>照亮每一個裝載夢想的可能</h2>
                  </div>
                </div>
                <div class="row">
                  <div class="col align-self-center">
                    <div class="welcome-text">
                      <p>
                        你是否擁有一個創意發想卻不敢真正實行？渴望自己的募資提案可以實現夢想卻因不確定性而仍然卻步？立即使用（名字），我們將透過AI科技，協助你描繪成功的模樣。
                      </p>
                    </div>
                    <button class="welcome-button" @click="goForm">
                      開始評估
                    </button>
                    <!-- <button>開始評估</button> -->
                  </div>
                </div>
              </div>
            </div>
            <div class="col welcome-img">
              <img src="https://i.imgur.com/PVeBkz4.png" />
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- 優點區域 -->
    <section
      class="advantage-area"
      style="margin: 0px; padding-bottom: 0px; padding: 100px;"
    >
      <div class="container">
        <div class="row row-cols-1 row-cols-md-3">
          <div class="col-12 col-md-4 ">
            <div class="advantageCard">
              <img src="https://i.imgur.com/emQF2gl.png" />
              <p class="advantage-title">即時的諮詢評估</p>
              <p class="advantage-description">
                不須多餘等待時間，提供最即時的分析評估
              </p>
            </div>
          </div>
          <div class="col-12 col-md-4 ">
            <div class="advantageCard">
              <img src="https://i.imgur.com/gKUnF9M.png" />
              <p class="advantage-title">完善的資訊彙整</p>
              <p class="advantage-description">
                透過完整數據統計，提供最精確的資料呈現
              </p>
            </div>
          </div>
          <div class="col-12 col-md-4 ">
            <div class="advantageCard">
              <img src="https://i.imgur.com/GRSlC1b.png" />
              <p class="advantage-title">容易操作好上手</p>
              <p class="advantage-description">
                只要輸入基本信息，馬上幫你取得最佳典範
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- 相似案例介紹區域 -->
    <section
      class="fundraising-area"
      style="margin: 0px; padding-bottom: 0px; padding: 100px;"
    >
      <div class="container">
        <div class="h-100">
          <div class="row row-cols-1 row-cols-md-2">
            <div class="col fundraising-img">
              <img src="https://i.imgur.com/jKbjRpu.png" />
            </div>
            <div class="col align-self-center">
              <div class="container-fluid">
                <div class="row">
                  <h2 class="col fundraising-title">
                    最簡單的搜尋，最優秀的範例
                  </h2>
                </div>
                <div class="row">
                  <div class="col align-self-center">
                    <div class="fundraising-text">
                      <p>
                        為什麼他的募資專案廣受好評？他是如何成功募得達標金額？簡單輸入你的創意點子，（名字）將找出那些最優秀的募資者，看看他們如何實踐理想的過程，一起為你縮短夢想和成功的距離！
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- 回饋方案介紹區域 -->
    <section
      class="feedback-area"
      style="margin: 0px; padding-bottom: 0px; padding: 100px;"
    >
      <div class="container">
        <div class="h-100">
          <div class="row row-cols-1 row-cols-md-2">
            <div class="col align-self-center">
              <div class="container-fluid">
                <div class="row">
                  <h2 class="col feedback-title">搶手回饋方案立即看</h2>
                </div>
                <div class="row">
                  <div class="col align-self-center">
                    <div class="feedback-text">
                      <p>
                        一個成功募資專案最大的籌碼便是吸引眾人的回饋方案，而如何訂定內容、設置金額往往都是一大難題。有了（名字），替你統整最齊全的數據、協助你尋找到最適配的組合，成為你募資道路上不可或缺的軍師！
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="col feedback-img">
              <img src="https://i.imgur.com/2vadcZ7.png" />
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  methods: {
    goForm() {
      this.$router.push({ path: "/form" });
    },
    goHome() {
      this.$router.push({ path: "/" });
    }
  }
};
</script>

<style scoped>
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

body {
  margin: 0;
  padding: 0;
  background-color: #fafafa;
}

/* 介紹平台區域 */
.welcome-area {
  background-image: url(https://i.imgur.com/CrJXKZ2.png);
  background-size: cover;
}

.welcome-title > h2 {
  text-align: left;
  line-height: 40px;
  color: #ffffff;
}

.welcome-title {
  padding-bottom: 10px;
}

.welcome-text > p {
  font-size: 14px;
  text-align: left;
  line-height: 25px;
  color: #ffffff;
}

.welcome-area > img {
  padding: 40px;
}

/* 優點區域 */
.advantageCard {
  font-size: 14px;
  margin: 0px 10px 50px 10px;
  padding: 15px;
  border: none;
  border-radius: 15px;
  overflow: hidden;
  /* height: 200px; */
  background: #f5f5f5;
  box-shadow: 0 3px 12px 0 rgba(0, 0, 0, 0.2), 0 1px 15px 0 rgba(0, 0, 0, 0.19);
}

.advantageCard > * {
  margin: 10px 30px;
}

.advantage-title {
  font-size: 16px;
  font-weight: 550;
}

/* 相似案例介紹區域 */
.fundraising-area {
  background-color: #f5f5f5;
}

.fundraising-title,
.feedback-title {
  text-align: left;
  line-height: 40px;
  padding-bottom: 10px;
}

.fundraising-text,
.feedback-text > p {
  font-size: 14px;
  text-align: left;
  line-height: 25px;
}

.fundraising-img {
  padding: 100px 50px;
}

.feedback-img {
  padding: 50px 50px;
}

/* 按鈕 */
.welcome-button {
  float: left;
  padding: 5px 50px;
  margin: 10px 0px 0px 10px;
  border: 10px;
  border-color: #fff;
  background-color: #fff;
  color: #281483;
  font-weight: 550;
  border-radius: 30px;
  cursor: pointer;
  outline: none;
}

.welcome-button:hover {
  color: #281483;
  background-color: #fff;
  transform: scale(1.1);
}

.welcome-button:active {
  color: #281483;
  background-color: #fff;
  transform: scale(1.1);
  box-shadow: 0 0px 15px 0 rgba(241, 231, 236, 0.2),
    0 0px 15px 0 rgba(241, 231, 236, 0.19);
}

/* navbar */
nav.navbar {
  transition: 1s;
}
.navbar {
  /* background-color: rgba(0, 0, 0, 0.3) !important; */
  background-color: #281483 !important;
  height: 60px;
}
.navbar a {
  color: #ececec !important;
  transition: 0.5s !important;
  padding: 0 5px;
}
.nav-button {
  padding: 5px 20px;
  margin: 5px;
  border: 10px;
  border-color: #fff;
  background-color: rgba(255, 255, 255, 0);
  color: #fff;
  font-weight: 550;
  border-radius: 30px;
  cursor: pointer;
  outline: none;
}
.nav-button:hover {
  color: #281483;
  background-color: #fff;
}

.nav-button:active {
  color: #281483;
  background-color: #fff;
  box-shadow: 0 0px 15px 0 rgba(241, 231, 236, 0.2),
    0 0px 15px 0 rgba(241, 231, 236, 0.19);
}

.home-button {
  padding: 5px 20px;
  margin: 5px;
  border: 10px;
  border-color: #fff;
  background-color: rgba(255, 255, 255, 0);
  color: #fff;
  font-weight: 550;
  border-radius: 30px;
  cursor: pointer;
  outline: none;
}
</style>
