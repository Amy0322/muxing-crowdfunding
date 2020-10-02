<template>
  <div>
    <body id="app">
      <section
        class="feedback-area"
        style="margin: 0px; padding-bottom: 0px; padding: 100px 0px 30px 0px;"
      >
        <div class="container">
          <div class="fundraising-name-block">
            <div>募資方案名稱：</div>
            <div class="fundraising-name">
              {{ fundraising.title }}
            </div>
          </div>
          <div class="functionTitle">
            <h3>回饋方案數據統計</h3>
          </div>
          <FeedbackCard2
            v-for="feedback in allFeedbacks"
            :key="feedback.id"
            :feedback="feedback"
          />
        </div>
      </section>
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

.fundraising-name-block {
  text-align: left;
  font-weight: 500;
  margin: 0px 10px 50px 10px;
  padding: 10px 20px;
  border: none;
  border-radius: 15px;
  overflow: hidden;
  background: #fff;
  box-shadow: 0 3px 12px 0 rgba(0, 0, 0, 0.1), 0 1px 15px 0 rgba(0, 0, 0, 0.1);
}

.functionTitle > h3 {
  font-weight: 500;
  padding: 10px 0px 60px 0px;
}
</style>

<script>
import FeedbackCard2 from "../components/FeedbackCard2.vue";
import EventService from "../services/EventService.js";

export default {
  components: {
    FeedbackCard2
  },
  methods: {
    goForm() {
      this.$router.push({ path: "/form" });
    }
  },
  props: ["id"],
  data() {
    return {
      fundraising: [],
      allFeedbacks:[]
    };
  },
  created() {
    // EventService.getFundraising(this.id)
    //   .then(response => {
        this.fundraising = JSON.parse(this.$route.query.feedback);
        this.allFeedbacks = this.fundraising.feedbacks;
        // this.fundraising = this.allFundraising.filter(proj => proj.id === this.id);
      // })
      // .catch(error => {
      //   console.log("There was an error:", error.response);
      // });
  }
};
</script>
