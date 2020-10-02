<template>
  <div v-if="!fundraisings">Loading Please wait...</div>

  <div v-else>
<!--    <div>{{chartData.fundraising}}</div>-->
    <body class="bg" id="app">
      <!-- 相似案例 -->
      <section
        class="fundraising-area"
        style="margin: 0px; padding: 90px 0px 30px 0px;"
      >
        <div class="container">
          <div class="functionTitle">
            <h3>相似的募資成功案例</h3>
          </div>
          <div class="row row-cols-1 row-cols-md-3">
            <FundraisingCard
              v-for="fundraising in fundraisings"
              v-show="fundraising.id"
              :key="fundraising.id"
              :fundraising="fundraising"
            />
          </div>
        </div>
      </section>
      <!-- 相似案例 end -->
      <!-- 達成率 -->
      <section
        class="rate-area"
        style="margin: 0px; padding-bottom: 0px; padding: 70px 0px 30px 0px;"
      >
        <div class="container">
          <div class="functionTitle">
            <h3>相似案例的募資狀態與達成率</h3>
          </div>
          <div class="rateCard">
            <table class="table">
              <thead>
                <tr class="table-gray">
                  <th scope="col">募資方案</th>
                  <th scope="col">目標金額</th>
                  <th scope="col">募得金額</th>
                  <th scope="col">達成率</th>
                  <th scope="col">募資狀態</th>
                </tr>
              </thead>
              <tbody v-for="rate in rates" :key="rate.id" :rate="rate">
                <tr>
                  <td scope="row" class="table-left">
                    <a
                      class="rate-title"
                      v-bind:href="rate.url"
                      target="_blank"
                      style="text-decoration:none;"
                      >{{ rate.title }}</a
                    >
                  </td>
                  <td >
                    {{ rate.amountReached | point }}
                  </td>
                  <td >
                    {{ rate.amountRaised | point }}
                  </td>
                  <td class="table-rate">{{ rate.proportion }}%</td>
                  <td>
                    <div
                      class="status status-success"
                      v-if="rate.status === 'success'"
                    >
                      募資成功
                    </div>
                    <div
                      class="status status-fall"
                      v-else-if="rate.status === 'fail'"
                    >
                      募資失敗
                    </div>
                    <div class="status status-ing" v-else-if="rate.status === 'ing'">
                      募資中
                    </div>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </section>
      <!-- 達成率 end -->
      <!-- 落點分析 -->
      <section
        class="compare-area"
        style="margin: 0px; padding-bottom: 0px; padding: 70px 0px 30px 0px;"
      >
        <div class="container">
          <div class="functionTitle">
            <h3>落點分析</h3>
          </div>
          <div class="row row-cols-1 row-cols-md-3">
            <!-- 目標金額 -->
            <div class="col-12 col-md-4">
              <div class="compareCard">
                <div class="compare-top">
                  <div class="compare-title">目標金額</div>
                </div>
                <div class="compare-textBlock">
                  <p class="compare-text">與您相似的募資方案，目標金額大致為</p>
                  <div class="averageData" >
                    {{ points.averageTarget | point }}
                  </div>
                  <p class="compare-text">您提出的募資方案，目標金額為</p>
                  <div class="inputData" >
                    {{ points.userTarget | point }}
                  </div>
                  <p class="compare-text">落點在：</p>
                </div>
                <!-- 落點分析圖模型 -->
                <div
                  class="compare-chartBlock"
                  v-if="points.averageTarget > points.userTarget"
                >
                  <div
                    class="user-point"
                    v-bind:style="
                      'left:' +
                        ((100 * points.userTarget) / points.averageTarget -
                          50) +
                        '%'
                    "
                  >
                    <div class="user-point-value">{{ points.userTarget }}</div>
                    <div class="triangle"></div>
                  </div>
                  <div class="longLine"></div>
                  <div
                    class="shortLine"
                    v-bind:style="
                      'width:' +
                        (100 * points.userTarget) / points.averageTarget +
                        '%'
                    "
                  ></div>
<!--                  <div class="min-point">0</div>-->
                  <div class="max-point">{{ points.averageTarget }}</div>
                </div>
                <div
                  class="compare-chartBlock"
                  v-if="points.averageTarget == points.userTarget"
                >
                  <div
                    class="user-point"
                    v-bind:style="
                      'left:' +
                        ((100 * points.userTarget) / points.averageTarget -
                          50) +
                        '%'
                    "
                  >
                    <div class="user-point-value">{{ points.userTarget }}</div>
                    <div class="triangle"></div>
                  </div>
                  <div class="longLine2" v-bind:style="'width: 100%'"></div>
                  <div class="shortLine2" v-bind:style="'width: 100%'"></div>
<!--                  <div class="min-point">0</div>-->
                  <div class="max-point">{{ points.averageTarget }}</div>
                </div>
                <div
                  class="compare-chartBlock"
                  v-if="points.averageTarget < points.userTarget"
                >
                  <div class="user-point" v-bind:style="'left: 50%'">
                    <div class="user-point-value">{{ points.userTarget }}</div>
                    <div class="triangle"></div>
                  </div>
                  <div class="longLine3"></div>
                  <div
                    class="shortLine3"
                    v-bind:style="
                      'width:' +
                        (100 * points.averageTarget) / points.userTarget +
                        '%'
                    "
                  ></div>
<!--                  <div class="min-point">0</div>-->
                  <div
                    class="mid-point"
                    v-bind:style="
                      'left:' +
                        ((100 * points.averageTarget) / points.userTarget -
                          50) +
                        '%'
                    "
                  >
                    {{ points.averageTarget }}
                  </div>
                </div>
                <!-- 落點分析圖模型end -->
              </div>
            </div>
            <!-- 募資期間 -->
            <div class="col-12 col-md-4">
              <div class="compareCard">
                <div class="compare-top">
                  <div class="compare-title">募資期間</div>
                </div>
                <div class="compare-textBlock">
                  <p class="compare-text">與您相似的募資方案，募資期間大致為</p>
                  <div class="averageData">{{ points.averageTime }} 天</div>
                  <p class="compare-text">您提出的募資方案，募資期間為</p>
                  <div class="inputData">{{ points.userTime }} 天</div>
                  <p class="compare-text">落點在：</p>
                </div>
                <!-- 落點分析圖模型 -->
                <div
                  class="compare-chartBlock"
                  v-if="points.averageTime > points.userTime"
                >
                  <div
                    class="user-point"
                    v-bind:style="
                      'left:' +
                        ((100 * points.userTime) / points.averageTime - 50) +
                        '%'
                    "
                  >
                    <div class="user-point-value">{{ points.userTime }}</div>
                    <div class="triangle"></div>
                  </div>
                  <div class="longLine"></div>
                  <div
                    class="shortLine"
                    v-bind:style="
                      'width:' +
                        (100 * points.userTime) / points.averageTime +
                        '%'
                    "
                  ></div>
<!--                  <div class="min-point">0</div>-->
                  <div class="max-point">{{ points.averageTime }}</div>
                </div>
                <div
                  class="compare-chartBlock"
                  v-if="points.averageTime == points.userTime"
                >
                  <div
                    class="user-point"
                    v-bind:style="
                      'left:' +
                        ((100 * points.userTime) / points.averageTime - 50) +
                        '%'
                    "
                  >
                    <div class="user-point-value">{{ points.userTime }}</div>
                    <div class="triangle"></div>
                  </div>
                  <div class="longLine2" v-bind:style="'width: 100%'"></div>
                  <div class="shortLine2" v-bind:style="'width: 100%'"></div>
<!--                  <div class="min-point">0</div>-->
                  <div class="max-point">{{ points.averageTime }}</div>
                </div>
                <div
                  class="compare-chartBlock"
                  v-if="points.averageTime < points.userTime"
                >
                  <div class="user-point" v-bind:style="'left: 50%'">
                    <div class="user-point-value">{{ points.userTime }}</div>
                    <div class="triangle"></div>
                  </div>
                  <div class="longLine3"></div>
                  <div
                    class="shortLine3"
                    v-bind:style="
                      'width:' +
                        (100 * points.averageTime) / points.userTime +
                        '%'
                    "
                  ></div>
<!--                  <div class="min-point">0</div>-->
                  <div
                    class="mid-point"
                    v-bind:style="
                      'left:' +
                        ((100 * points.averageTime) / points.userTime - 50) +
                        '%'
                    "
                  >
                    {{ points.averageTime }}
                  </div>
                </div>
                <!-- 落點分析圖模型end -->
              </div>
            </div>
            <!-- 回饋方案種類 -->
            <div class="col-12 col-md-4">
              <div class="compareCard">
                <div class="compare-top">
                  <div class="compare-title">回饋方案種類</div>
                </div>
                <div class="compare-textBlock">
                  <p class="compare-text">與您相似的募資方案，回饋方案大致有</p>
                  <div class="averageData">{{ points.averageFeedback }} 種</div>
                  <p class="compare-text">您提出的募資方案，回饋方案有</p>
                  <div class="inputData">{{ points.userFeedback }} 種</div>
                  <p class="compare-text">落點在：</p>
                </div>
                <!-- 落點分析圖模型 -->
                <div
                  class="compare-chartBlock"
                  v-if="points.averageFeedback > points.userFeedback"
                >
                  <div
                    class="user-point"
                    v-bind:style="
                      'left:' +
                        ((100 * points.userFeedback) / points.averageFeedback -
                          50) +
                        '%'
                    "
                  >
                    <div class="user-point-value">
                      {{ points.userFeedback }}
                    </div>
                    <div class="triangle"></div>
                  </div>
                  <div class="longLine"></div>
                  <div
                    class="shortLine"
                    v-bind:style="
                      'width:' +
                        (100 * points.userFeedback) / points.averageFeedback +
                        '%'
                    "
                  ></div>
<!--                  <div class="min-point">0</div>-->
                  <div class="max-point">{{ points.averageFeedback }}</div>
                </div>
                <div
                  class="compare-chartBlock"
                  v-if="points.averageFeedback == points.userFeedback"
                >
                  <div
                    class="user-point"
                    v-bind:style="
                      'left:' +
                        ((100 * points.userFeedback) / points.averageFeedback -
                          50) +
                        '%'
                    "
                  >
                    <div class="user-point-value">
                      {{ points.userFeedback }}
                    </div>
                    <div class="triangle"></div>
                  </div>
                  <div class="longLine2" v-bind:style="'width: 100%'"></div>
                  <div class="shortLine2" v-bind:style="'width: 100%'"></div>
<!--                  <div class="min-point">0</div>-->
                  <div class="max-point">{{ points.averageFeedback }}</div>
                </div>
                <div
                  class="compare-chartBlock"
                  v-if="points.averageFeedback < points.userFeedback"
                >
                  <div class="user-point" v-bind:style="'left: 50%'">
                    <div class="user-point-value">
                      {{ points.userFeedback }}
                    </div>
                    <div class="triangle"></div>
                  </div>
                  <div class="longLine3"></div>
                  <div
                    class="shortLine3"
                    v-bind:style="
                      'width:' +
                        (100 * points.averageFeedback) / points.userFeedback +
                        '%'
                    "
                  ></div>
<!--                  <div class="min-point">0</div>-->
                  <div
                    class="mid-point"
                    v-bind:style="
                      'left:' +
                        ((100 * points.averageFeedback) / points.userFeedback -
                          50) +
                        '%'
                    "
                  >
                    {{ points.averageFeedback }}
                  </div>
                </div>
                <!-- 落點分析圖模型end -->
              </div>
            </div>
          </div>
        </div>
      </section>
      <!-- 落點分析 end -->
      <!-- 回饋方案金額 -->
      <section
        class="price-area"
        style="margin: 0px; padding-bottom: 0px; padding: 70px 0px 30px 0px;"
      >
        <div class="container">
          <div class="functionTitle2">
            <h3>回饋方案金額分布</h3>
          </div>
          <h6>目標金額相似的募資方案中，回饋方案的金額分布</h6>
          <div class="price-bg">
            <div class="price-legendBlock">
              <table class="table">
                <thead>
                  <tr class="table-gray">
                    <th scope="col">募資方案</th>
                    <th scope="col">達成率</th>
                  </tr>
                </thead>
                <tbody
                  v-for="legend in chartData"
                  :key="legend.id"
                  :legend="legend"
                >
                  <tr>
                    <td scope="row" class="table-left">
                      <div
                        class="color-circle"
                        v-bind:style="'background-color:' + legend.color"
                      ></div>
                      <a
                        class="legend-title"
                        v-bind:href="legend.url"
                        target="_blank"
                        style="text-decoration:none;"
                      >
                        {{ legend.name }}
                      </a>
                    </td>
                    <td class="legend-proportion">{{ legend.proportion }}%</td>
                  </tr>
                </tbody>
              </table>
            </div>
            <div class="price-chartBlock">
              <highcharts :options="options[0]"></highcharts>
            </div>
          </div>
        </div>
        <button class="re_button" @click="goForm()">
          重新評估
        </button>
      </section>
      <!-- 回饋方案金額 end -->
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

/* 功能區域背景色 */
.rate-area,
.price-area {
  background-color: #efe9f1;
}

/* 功能標題 */
.functionTitle > h3 {
  font-weight: 550;
  padding: 0px 0px 50px 0px;
}

.functionTitle2 > h3 {
  font-weight: 550;
  padding: 50px 0px 20px 0px;
}

/* 重新評估按鈕 */
.re_button {
  padding: 10px 30px;
  margin: 40px 0px;
  border: 2px;
  border-color: #fff;
  background-color: #281483;
  color: #fff;
  font-weight: 500;
  border-radius: 30px;
  cursor: pointer;
  outline: none;
}

.re_button:hover {
  background: linear-gradient(to right, #281483 0%, #be78d1 100%);
  outline: none;
}

.re_button:active {
  background: linear-gradient(to right, #281483 0%, #be78d1 100%);
  outline: none;
}

/* 達成率 */
.rateCard {
  margin: 0px 10px 50px 10px;
  padding: 20px;
  border-radius: 15px;
  overflow: hidden;
  background: #fff;
  box-shadow: 0 3px 12px 0 rgba(0, 0, 0, 0.1), 0 1px 15px 0 rgba(0, 0, 0, 0.1);
}

.table tbody tr td {
  vertical-align: middle;
}

.table-left {
  text-align: left;
}

.table-rate {
  font-size: 16px;
  font-weight: 500;
  color: #fb5252;
}

.rate-title {
  text-align: left;
  font-weight: 500;
  color: #41404b;
  /* 省略字... */
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
  white-space: normal;
}

.rate-title:hover {
  color: #9b6bc0;
}

.status {
  border-radius: 10px;
  padding: 2px 3px;
  color: #fff;
  white-space: nowrap;
}

.status-success {
  background-color: #2abd66;
}

.status-fall {
  background-color: #f34f86;
}

.status-ing {
  background-color: #5696df;
}

/* 落點分析 */
.compareCard {
  margin: 0px 10px 50px 10px;
  border: none;
  border-radius: 15px;
  overflow: hidden;
  height: 450px;
  background: #fff;
  box-shadow: 0 3px 12px 0 rgba(0, 0, 0, 0.1), 0 1px 15px 0 rgba(0, 0, 0, 0.1);
}

.compareCard:hover {
  transform: scale(1.03);
  box-shadow: 0 3px 12px 0 rgba(0, 0, 0, 0.1), 0 1px 15px 0 rgba(0, 0, 0, 0.1);
}

.compare-top {
  background: #9b6bc0;
  height: 50px;
}

.compare-title {
  color: #fff;
  font-weight: 550;
  top: 12.5px;
  font-size: 16px;
}

.compare-textBlock {
  margin: 20px 30px 0px 30px;
}

.compare-text {
  text-align: left;
  font-size: 14px;
}

.averageData,
.inputData {
  padding: 3px 0px 17px 0px;
  font-size: 22px;
  font-weight: 500;
}

.averageData {
  color: #fb5252;
}

.compare-chartBlock {
  margin: 0px 50px;
}

.longLine {
  height: 20px;
  background-color: #ddc7e7;
  border-radius: 30px;
  top: 20px;
}

.shortLine {
  height: 20px;
  background-color: #9b6bc0;
  border-radius: 10px 0px 0px 10px;
}

.longLine2 {
  height: 20px;
  background-color: #ddc7e7;
  border-radius: 10px;
  top: 20px;
}

.shortLine2 {
  height: 20px;
  background-color: #9b6bc0;
  border-radius: 10px;
}

.longLine3 {
  height: 20px;
  background-color: #9b6bc0;
  border-radius: 10px;
  top: 20px;
}

.shortLine3 {
  height: 20px;
  background-color: #ddc7e7;
  border-radius: 10px 0px 0px 10px;
}

/*.min-point {*/
/*  height: 20px;*/
/*  text-align: left;*/
/*  font-size: 10px;*/
/*}*/

.max-point {
  text-align: right;
  /*top: -20px;*/
  right: -10px;
  font-size: 10px;
}

.mid-point {
  text-align: left;
  display: inline;
  /*top: -20px;*/
  font-size: 10px;
}

.user-point {
  display: inline-block;
}

.user-point-value {
  display: inline-block;
  border: 2px solid #ddc7e7;
  border-radius: 5px;
  top: 10px;
  padding: 0px 5px;
  font-size: 12px;
  z-index: 2;
}

.triangle {
  border-right: 6px solid white;
  border-left: 6px solid white;
  border-top: 10px solid #9b6bc0;
  position: absolute;
  top: 37px;
  left: calc(50% - 6px);
}

/* 回饋方案金額 */
.price-bg {
  background-color: #fff;
  margin: 30px 0px;
  padding: 20px;
  border-radius: 15px;
  position: relative;
}

.price-legendBlock {
  margin: 10px 20px 20px 20px;
}

.legendBlock {
  margin: 10px 0px;
}

.table-gray {
  background-color: #f5f5f5;
  white-space: nowrap;
}

.color-circle {
  width: 10px;
  height: 10px;
  border-radius: 100%;
  background-color: black;
  margin: 8px 15px 8px 0px;
  display: inline-block;
}

.legend-title {
  font-weight: 500;
  text-align: left;
  display: inline-block;
  max-width: 90%;
  color: #41404b;
}

.legend-title:hover {
  color: #9b6bc0;
}

.legend-proportion {
  font-weight: 500;
}
</style>

<script>
import FundraisingCard from "../components/FundraisingCard.vue";
import EventService from "../services/EventService.js";
import Highcharts from "highcharts";
import exportingInit from "highcharts/modules/exporting";

export default {
  components: {
    FundraisingCard
  },
  methods: {
    goForm() {
      this.$router.push({ path: "/form" });
    }
  },
  data() {
    return {
      options: [chartOption],
      fundraisings: this.$route.query.fundraisings,
      chartData: this.$route.query.chart.fundraising,
      points: this.$route.query.points,
      rates: this.$route.query.rates
    };
  },
created() {
    this.options[0].xAxis.categories = this.$route.query.chart.bar;
    this.options[0].series = this.$route.query.chart.fundraising;
}
  // EventService.getFundraisings()
    //   .then(response => {
    //     console.log('from Result.vue : ' + response.data);
    //     this.fundraisings = response.data;
    //   })
    //   .catch(error => {
    //     console.log("There was an error:", error.response);
    //   });
    // EventService.getChart()
    //   .then(response => {
    //     this.chartData = response.data;
    //     this.options[0].xAxis.categories = response.data.bar;
    //     this.options[0].series = response.data.fundraisings;
    //   })
    //   .catch(error => {
    //     console.log("There was an error:", error.response);
    //   });
    // EventService.getPoints()
    //   .then(response => {
    //     this.points = response.data;
    //   })
    //   .catch(error => {
    //     console.log("There was an error:", error.response);
    //   });
    // EventService.getRates()
    //   .then(response => {
    //     this.rates = response.data;
    //   })
    //   .catch(error => {
    //     console.log("There was an error:", error.response);
    //   });

};
exportingInit(Highcharts);
//圖表
var chartOption = {
  chart: {
    type: "column",
    height: (9 / 16) * 100 + "%"
  },
  title: {
    useHTML: true,
    text: "<div style=height:30px></div>"
  },
  xAxis: {
    //x軸種類
    categories: null,
    title: {
      text: "回饋方案金額(元)"
    }
  },
  yAxis: {
    min: 0,
    title: {
      text: "選擇人數(人)",
      align: "high",
      offset: -30,
      rotation: 0,
      y: -30
    },
    //總數
    stackLabels: {
      enabled: true,
      style: {
        fontWeight: "bold",
        color:
          // theme
          (Highcharts.defaultOptions.title.style &&
            Highcharts.defaultOptions.title.style.color) ||
          "gray"
      }
    }
  },
  tooltip: {
    useHTML: true,
    formatter: function() {
      //重新生成
      var content =
        '<div style="font-family: "微軟正黑體";letter-spacing: 1.5px;line-height: 25px;color: #41404b;">' +
        this.series.name +
        "<br/>" +
        "選擇人數：" +
        this.point.y +
        "</div>";
      return content;
    }
  },
  plotOptions: {
    series: {
      //不顯示Legend
      showInLegend: false,
      stacking: "normal"
    }
  },
  series: null,
  //highchart logo
  credits: {
    enabled: false
  },
  //輸出圖示
  exporting: {
    enabled: false
  }
};
</script>
