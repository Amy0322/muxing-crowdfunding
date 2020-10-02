<template>
  <div class="col-12 col-md-4">
    <div class="fundraisingCard">
      <a
        v-bind:href="fundraising.url"
        target="_blank"
        style="text-decoration:none;"
      >
        <div
          class="fundraising-imgBlock"
          v-bind:style="'background-image:url(' + fundraising.img + ')'"
        >
          <div class="no-image" v-if="fundraising.img == null">No image</div>
        </div>
        <div class="fundraising-textBlock">
          <h4 class="fundraising-title">
            {{ fundraising.title }}
          </h4>
          <p class="fundraising-author">{{ fundraising.author }}</p>
          <p class="fundraising-description">
            {{ fundraising.description }}
          </p>
<!--          <div>{{fundraising.feedbacks}}</div>-->
        </div>
      </a>
      <router-link
        class="feedback-link routerLink"
        :to="{ name: 'Feedback', params: { id: fundraising.id }, query: {feedback:JSON.stringify(fundraising)}}"

        target="_blank"
      >
        <div class="feedback_button">
          查看回饋方案
        </div>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    fundraising: Object,
  },
  methods: {
    goFeedback() {
      this.$router.push({ path: "/feedback"});
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

.fundraisingCard {
  margin: 0px 10px 50px 10px;
  border: none;
  border-radius: 15px;
  overflow: hidden;
  height: 450px;
  cursor: pointer;
  background: #fff;
  box-shadow: 0 3px 12px 0 rgba(0, 0, 0, 0.1), 0 1px 15px 0 rgba(0, 0, 0, 0.1);
}

.fundraisingCard:hover {
  transform: scale(1.03);
  box-shadow: 0 3px 12px 0 rgba(0, 0, 0, 0.1), 0 1px 15px 0 rgba(0, 0, 0, 0.1);
}

.fundraising-imgBlock {
  /* border: 1px solid black; */
  padding: 0px;
  margin-top: 10px;
  width: 100%;
  height: 40%;
  /* 圖置中 */
  background-repeat: no-repeat;
  background-size: contain;
  background-position: center center;
  background-color: #fff;
  /* 字置中 */
  display: flex;
  align-items: center;
  justify-content: center;
}

.no-image {
  color: #41404b;
}

.fundraising-textBlock {
  text-align: left;
  padding: 10px 20px 0px 20px;
  width: 100%;
  height: 50%;
}

.fundraising-title {
  font-size: 14px;
  font-weight: 500;
  /* 省略字... */
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  white-space: normal;
}

.fundraising-author {
  font-size: 8px;
  line-height: 20px;
  color: #707070;
  /* 省略字... */
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  white-space: normal;
}

.fundraising-description {
  font-size: 12px;
  line-height: 20px;
  /* 省略字... */
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  white-space: normal;
}

.feedback_button {
  padding: 5px;
  width: 100%;
  background-size: cover;
  background: #281483;
  border: 0px;
  color: white;
  font-weight: 500;
  outline: none;
  text-align: center;
  cursor: pointer;
  z-index: 66;
  transition: 0.5s;
}

.feedback_button:hover {
  background: linear-gradient(to right, #281483 0%, #be78d1 100%);
}

.feedback_button:active {
  background: linear-gradient(to right, #281483 0%, #be78d1 100%);
}

.routerLink {
  text-decoration: none;
}
</style>
