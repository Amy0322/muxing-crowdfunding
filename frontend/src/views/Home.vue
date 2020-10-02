<template>
  <div>
    <!-- navbar -->
    <nav
      class="navbar navbar-expand-sm navbar-light bg-light fixed-top navbar-top mx-auto border-bottom"
    >
      <div class="container">
        <button class="home-button" @click="goHome">
          <img src="https://i.imgur.com/RQ7zU1P.png" width="60%" height="" />
        </button>
        <button class="home-button home-name" @click="goHome">募星</button>
        <button class="navbar-nav ml-auto nav nav-button" @click="goForm">
          開始評估
        </button>
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
                        你是否擁有一個創意發想卻不敢真正實行？渴望自己的募資提案可以實現夢想卻因不確定性而仍然卻步？立即使用「募星」，我們將透過的AI科技，協助你描摹出成功的模樣。
                      </p>
                    </div>
                    <button class="welcome-button" @click="goForm">
                      開始評估
                    </button>
                  </div>
                </div>
              </div>
            </div>
            <div class="col welcome-img">
              <img
                src="https://i.imgur.com/e7XNMED.png"
                width="70%"
                height=""
              />
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- 介紹平台區域 end -->
    <!-- 優點區域 -->
    <section
      class="advantage-area"
      style="margin: 0px; padding-bottom: 0px; padding: 100px;"
    >
      <div class="container">
        <div class="row row-cols-1 row-cols-md-3">
          <div class="col-12 col-md-4 ">
            <div class="advantageCard">
              <img src="https://i.imgur.com/AniE8na.png" />
              <p class="advantage-title">即時的諮詢評估</p>
              <p class="advantage-description">
                不須多餘等待時間，提供最即時的分析評估
              </p>
            </div>
          </div>
          <div class="col-12 col-md-4 ">
            <div class="advantageCard">
              <img src="https://i.imgur.com/1pbnq9u.png" />
              <p class="advantage-title">完善的資訊彙整</p>
              <p class="advantage-description">
                透過完整數據統計，提供最精確的資料呈現
              </p>
            </div>
          </div>
          <div class="col-12 col-md-4 ">
            <div class="advantageCard">
              <img src="https://i.imgur.com/tJfHDc2.png" />
              <p class="advantage-title">容易操作好上手</p>
              <p class="advantage-description">
                只要輸入基本資訊，馬上幫你取得最佳典範
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- 優點區域 end -->
    <!-- 相似案例介紹區域 -->
    <section
      class="fundraising-introduce-area"
      style="margin: 0px; padding-bottom: 0px; padding: 100px;"
    >
      <div class="container">
        <div class="h-100">
          <div class="row row-cols-1 row-cols-md-2">
            <div class="col function-img">
              <img
                src="https://i.imgur.com/Y29VBk9.png"
                width="100%"
                height=""
              />
            </div>
            <div class="col align-self-center">
              <div class="container-fluid">
                <div class="row">
                  <h2 class="col function-slogan">
                    最簡單的搜尋，最優秀的範例
                  </h2>
                </div>
                <div class="row">
                  <div class="col align-self-center">
                    <div class="function-text">
                      <p>
                        為什麼他的募資專案廣受好評？他是如何將想法呈現表達呢？簡單輸入你的創意點子，「募星」將找出與你一樣優秀的募資者，看看他們實踐理想的過程，一起為你縮短夢想和成功的距離！
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
    <!-- 相似案例介紹區域 end -->
    <!-- 回饋方案介紹區域 -->
    <section
      class="feedback-introduce-area"
      style="margin: 0px; padding-bottom: 0px; padding: 100px;"
    >
      <div class="container">
        <div class="h-100">
          <div class="row row-cols-1 row-cols-md-2">
            <div class="col align-self-center">
              <div class="container-fluid">
                <div class="row">
                  <h2 class="col function-slogan">方案發想小幫手</h2>
                </div>
                <div class="row">
                  <div class="col align-self-center">
                    <div class="function-text">
                      <p>
                        一個成功募資專案最大的籌碼便是吸引人的回饋方案，而如何訂定內容、設置金額往往都是一大難題。有了「募星」，替你統整最齊全的數據、協助你尋找最適配的組合，成為你募資道路上最好的軍師。
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="col function-img2">
              <img
                src="https://i.imgur.com/CvTrVgR.png"
                width="90%"
                height=""
              />
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- 回饋方案介紹區域 end -->
    <!-- 落點分析介紹區域 -->
    <section
      class="compare-introduce-area"
      style="margin: 0px; padding-bottom: 0px; padding: 100px;"
    >
      <div class="container">
        <div class="h-100">
          <div class="row row-cols-1 row-cols-md-2">
            <div class="col function-img">
              <img
                src="https://i.imgur.com/fa2yrEe.png"
                width="100%"
                height=""
              />
            </div>
            <div class="col align-self-center">
              <div class="container-fluid">
                <div class="row">
                  <h2 class="col function-slogan">
                    落點大調查
                  </h2>
                </div>
                <div class="row">
                  <div class="col align-self-center">
                    <div class="function-text">
                      <p>
                        想知道自己的計劃究竟能否取得成功？立即使用「募星」，讓我們在眾多募資方案中，幫你完善評估各種數據指標，提供精準的落點分析！
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
    <!-- 落點分析介紹區域 end -->
    <!-- 回饋方案金額介紹區域 -->
    <section
      class="price-introduce-area"
      style="margin: 0px; padding-bottom: 0px; padding: 100px;"
    >
      <div class="container">
        <div class="h-100">
          <div class="row row-cols-1 row-cols-md-2">
            <div class="col align-self-center">
              <div class="container-fluid">
                <div class="row">
                  <h2 class="col function-slogan">金額分布圖表化</h2>
                </div>
                <div class="row">
                  <div class="col align-self-center">
                    <div class="function-text">
                      <p>
                        為何訂定相似的目標金額，其他人卻可以獲得更大的迴響呢？讓「募星」利用簡單的長條圖，告訴你適合的回饋方案金額，透過絕佳的金額分布取得眾人的青睞！
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="col function-img">
              <img
                src="https://i.imgur.com/zm0gulB.png"
                width="80%"
                height=""
              />
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- 回饋方案金額介紹區域 end -->
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
  background-image: url(https://i.imgur.com/B7o069f.png);
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

.welcome-img {
  padding: 5% 2%;
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

/* 功能介紹區域 */
.fundraising-introduce-area,
.compare-introduce-area {
  background-color: #efe9f1;
}

.function-slogan {
  text-align: left;
  line-height: 40px;
  padding-bottom: 10px;
}

.function-text > p {
  font-size: 14px;
  text-align: left;
  line-height: 25px;
}

.function-img {
  padding: 7% 3%;
}

.function-img2 {
  padding: 1% 3%;
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
  border: 2px;
  border-color: #fff;
  background-color: rgba(255, 255, 255, 0.3);
  color: #fff;
  font-weight: 550;
  border-radius: 30px;
  cursor: pointer;
  outline: none;
}
.nav-button:hover {
  color: #9b6bc0;
  background-color: #fff;
}

.nav-button:active {
  color: #281483;
  background-color: #fff;
  box-shadow: 0 0px 15px 0 rgba(241, 231, 236, 0.2),
    0 0px 15px 0 rgba(241, 231, 236, 0.19);
}

.home-button {
  padding: 0px;
  margin: 0px;
  border: 10px;
  background-color: rgba(255, 255, 255, 0);
  cursor: pointer;
  outline: none;
}

.home-name {
  color: #fff;
}
</style>
