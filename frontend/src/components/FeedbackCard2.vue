<template>
  <div class="feedbackCard row row-cols-1">
    <div class="col-12 col-md-4 ">
      <div
        class="feedback-imgBlock"
        v-bind:style="'background-image:url(' + feedback.campaign_img + ')'"
      >
        <div class="no-image" v-if="feedback.campaign_img == null">No image</div>
      </div>
    </div>
    <div class="col-12 col-md-4 ">
      <div class="feedback-textBlock">
        <h4 class="feedback-content">
          {{ feedback.campaign_content }}
        </h4>
      </div>
    </div>
    <div class="col-12 col-md-4 row row-cols-2 dataBlock">
      <div class="col-12 col-md-6">
        <div class="feedback-dataBlock">
          <p class="feedback-pricing data-title">
            定價
          </p>
          <p class="feedback-pricing data-data" v-format="'$#,###'">
            {{ feedback.campaign_price | point }}
          </p>
          <p class="feedback-donator data-title">
            選擇人數
          </p>
          <p class="feedback-donator data-data">
            {{ feedback.campaign_people }}
          </p>
        </div>
      </div>
      <div class="col-12 col-md-6">
        <div class="feedback-dataBlock">
          <p class="feedback-amountRaised data-title">
            募得金額
          </p>
          <p class="feedback-amountRaised data-data" v-format="'$#,###'">
            {{ feedback.funding_price | point }}
          </p>
          <p class="feedback-amountReached data-title">
            募得總金額
          </p>
          <p class="feedback-amountReached data-data" v-format="'$#,###'">
            {{ feedback.total_price | point }}
          </p>
        </div>
      </div>
      <div class="col-12 col-md-12">
        <div class="line"></div>
        <p class="feedback-proportion data-title">
          募得金額占募得總金額比例
        </p>
        <p class="feedback-proportion proportion-data">
          {{ feedback.ratio }}%
        </p>
      </div>
    </div>
  </div>
</template>

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

.feedbackCard {
  margin: 0px 10px 50px 10px;
  border: none;
  border-radius: 15px;
  overflow: hidden;
  background: #fff;
  box-shadow: 0 3px 12px 0 rgba(0, 0, 0, 0.1), 0 1px 15px 0 rgba(0, 0, 0, 0.1);
}

.feedbackCard:hover {
  transform: scale(1.03);
  box-shadow: 0 3px 12px 0 rgba(0, 0, 0, 0.1), 0 1px 15px 0 rgba(0, 0, 0, 0.1);
}

.feedback-imgBlock {
  border-radius: 15px;
  margin: auto;
  margin-bottom: 20px;
  width: 95%;
  height: 210px;
  /* 圖置中 */
  background-repeat: no-repeat;
  background-size: contain;
  background-position: center center;
  background-color: #fff;
  /* 字置中 */
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 15px;
  margin: auto;
  margin: 20px 0px;
}

.no-image {
  color: #41404b;
}

.feedback-textBlock {
  background-color: #f5f5f5;
  border-radius: 15px;
  width: 100%;
  height: 210px;
  font-size: 14px;
  text-align: left;
  margin: 20px 0px;
  padding: 20px;
}

.feedback-content {
  height: 175px;
  font-size: 14px;
  overflow: auto;
}
/* 整個捲軸 */
::-webkit-scrollbar {
  width: 7px;
  margin-left: 10px;
}
/* 捲軸的軌道 */
::-webkit-scrollbar-track {
  border-radius: 10px;
}
/*捲軸尚未滑到的軌道*/
::-webkit-scrollbar-track-piece {
  background: #f5f5f5;
}
/* 滑動的區塊 */
::-webkit-scrollbar-thumb {
  background: rgb(197, 197, 197);
  border-radius: 10px;
}
/* 滑鼠移到滑動的區塊上 */
::-webkit-scrollbar-thumb:hover {
  background: rgb(194, 193, 193);
}

.dataBlock {
  text-align: center;
  margin: 20px 0px;
}

.data-title {
  font-size: 14px;
  color: #505058;
  margin: 0px;
}

.data-data {
  font-size: 16px;
  font-weight: 500;
  margin-bottom: 10px;
}

.line {
  height: 6px;
  background: linear-gradient(to right, #281483 0%, #be78d1 100%);
  border-radius: 30px;
  margin-bottom: 10px;
}

.proportion-data {
  font-size: 24px;
  font-weight: 500;
  margin: 10px 0px 0px 0px;
}

.feedback-content {
  white-space: pre-line;
}
</style>

<script>
export default {
  props: {
    feedback: Object
  }
};
</script>
