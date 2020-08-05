<template>
  <div class="feedbackCard row row-cols-1">
    <div class="row">
      <h4 class="fundraising-title">
        {{ fundraising.title }}
      </h4>
    </div>
    <div class="col-12 col-md-4 ">
      <div
        class="feedback-imgBlock"
        v-bind:style="'background-image:url(' + fundraising.feedback.img + ')'"
      ></div>
    </div>
    <div class="col-12 col-md-4 ">
      <div class="feedback-textBlock">
        <h4 class="feedback-content">
          {{ fundraising.feedback.content }}
        </h4>
        <!-- 遮 -->
        <!-- <div id="page-wrapper"> -->
        <!-- <button id="myBtn" @click="toggleModal()">Open Modal</button> -->
        <!--Modal-->
        <!-- <div class="modal modal_animation"> -->
        <!--Modal content-->
        <!-- <div class="modal_content">
              <div class="modal_content__header">
                <span class="modal_close" @click="toggleModal()">&times;</span>
                <div>{{ fundraising.feedback.content }}</div>
              </div>
            </div>
          </div>
        </div> -->
        <!-- 遮 -->
      </div>
    </div>
    <div class="col-12 col-md-4 row row-cols-2 dataBlock">
      <div class="col-12 col-md-6">
        <div class="feedback-dataBlock">
          <p class="feedback-pricing data-title">
            定價
          </p>
          <p class="feedback-pricing data-data">
            ${{ fundraising.feedback.pricing }}
          </p>
          <p class="feedback-donator data-title">
            選擇人數
          </p>
          <p class="feedback-donator data-data">
            {{ fundraising.feedback.donator }}
          </p>
        </div>
      </div>
      <div class="col-12 col-md-6">
        <div class="feedback-dataBlock">
          <p class="feedback-amountRaised data-title">
            募得金額
          </p>
          <p class="feedback-amountRaised data-data">
            ${{ fundraising.feedback.amountRaised }}
          </p>
          <p class="feedback-amountReached data-title">
            達標金額
          </p>
          <p class="feedback-amountReached data-data">
            ${{ fundraising.feedback.amountReached }}
          </p>
        </div>
      </div>
      <div class="col-12 col-md-12">
        <div class="line"></div>
        <p class="feedback-proportion data-title">
          募得金額占達標金額比例
        </p>
        <p class="feedback-proportion proportion-data">
          {{ fundraising.feedback.proportion }}%
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    fundraising: Object
  }
  // methods: {
  //   toggleModal() {
  //     const modal = document.querySelector(".modal");
  //     if (modal.style.display === "block") {
  //       modal.style.display = "none";
  //     } else {
  //       modal.style.display = "block";
  //     }
  //   }
  // }
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

.feedbackCard {
  margin: 0px 10px 50px 10px;
  border: none;
  border-radius: 15px;
  overflow: hidden;
  min-height: 250px;
  /* cursor: pointer; */
  background: #fff;
}

.feedbackCard:hover {
  transform: scale(1.01);
  box-shadow: 0 3px 12px 0 rgba(0, 0, 0, 0.2), 0 1px 15px 0 rgba(0, 0, 0, 0.19);
}

.fundraising-title {
  width: 100%;
  font-size: 14px;
  font-weight: 550;
  text-align: left;
  margin: 10px 20px 10px 35px;
  /* 省略字... */
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
  white-space: normal;
}

.feedback-imgBlock {
  width: 95%;
  height: 210px;
  background-size: cover;
  border-radius: 15px;
  margin: auto;
  margin-bottom: 20px;
}

.feedback-textBlock {
  background-color: #f5f5f5;
  border-radius: 15px;
  width: 100%;
  height: 210px;
  font-size: 14px;
  text-align: left;
  /* margin: auto; */
  margin-bottom: 20px;
  padding: 20px;
  /* box-shadow: 0 3px 12px 0 rgba(100, 100, 100, 0.2), 0 1px 15px 0 rgba(100, 100, 100, 0.19); */
}

/* .feedback-textBlock > p {
  margin: 5px 0px;
} */

.feedback-content {
  height: 175px;
  font-size: 14px;
  /* font-weight: 550; */
  /* padding-bottom: 20px; */
  /* 省略字... */
  overflow: auto;
  /* white-space: nowrap;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 5;
  -webkit-box-orient: vertical;
  white-space: normal; */
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
  padding-left: 20px;
}

.data-title {
  font-size: 12px;
  margin: 0px;
}

.data-data {
  font-size: 16px;
  font-weight: 550;
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
  font-weight: 550;
  margin: 5px 0px 20px 0px;
}

/* #myBtn {
  display: block;
  margin: 0 auto;
  padding: 1rem 1.25rem;
  background-color: #34b878;
  color: #fff;
  font-size: 1rem;
  font-weight: bold;
  border: none;
  border-radius: 5px;
  box-shadow: 0px 4px 0px 0px rgba(16, 113, 65, 1);
}

#myBtn:hover,
#myBtn:active {
  cursor: pointer;
  box-shadow: none;
  transition: box-shadow 0.5s ease;
} */

/*Modal*/
/* .modal {
  display: none;
  width: 100%;
  height: 100%;
  z-index: 1;
  position: fixed;
  top: 0;
  left: 0;
  overflow: auto;
  background-color: rgba(0, 0, 0, 0.4);
}

.modal_content {
  width: 60%;
  height: 60%;
  top: 20%;
  margin: auto;
  border-radius: 5px;
  background-color: #fff;
}

.modal_close {
  color: #34b878;
  font-size: 2rem;
  font-weight: bold;
  float: right;
  margin-right: 0.5rem;
}

.modal_close:hover {
  cursor: pointer;
  color: #cacafc;
}

/*animate modal transition*/
/* .modal_animation {
  animation: fadeIn 1s 1;
}  */

.feedback-content {
  white-space: pre-line;
}
</style>
