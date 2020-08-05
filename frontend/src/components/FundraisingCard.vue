<template>
  <div class="col-12 col-md-4 ">
    <a
      v-bind:href="fundraising.url"
      target="_blank"
      style="text-decoration:none;"
    >
      <div class="fundraisingCard">
        <div
          class="fundraising-imgBlock"
          v-bind:style="'background-image:url(' + fundraising.img + ')'"
        ></div>
        <div class="fundraising-textBlock">
          <h4 class="fundraising-title">
            {{ fundraising.title }}
          </h4>
          <p class="fundraising-author">{{ fundraising.author }}</p>
          <p class="fundraising-description">
            {{ fundraising.description }}
          </p>
        </div>
      </div>
    </a>
  </div>
</template>

<script>
export default {
  props: {
    fundraising: Object
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
}

.fundraisingCard:hover {
  transform: scale(1.01);
  box-shadow: 0 3px 12px 0 rgba(0, 0, 0, 0.2), 0 1px 15px 0 rgba(0, 0, 0, 0.19);
}

.fundraising-imgBlock {
  padding: 0px;
  width: 100%;
  height: 50%;
  background-size: cover;
}

.fundraising-textBlock {
  text-align: left;
  padding: 10px 20px 0px 20px;
}

.fundraising-title {
  font-size: 14px;
  font-weight: 550;
  /* 省略字... */
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  white-space: normal;
}

.fundraising-author {
  font-size: 8px;
  line-height: 10px;
  color: #707070;
}

.fundraising-description {
  font-size: 14px;
  /* 省略字... */
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 5;
  -webkit-box-orient: vertical;
  white-space: normal;
}
</style>
