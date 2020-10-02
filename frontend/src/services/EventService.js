import axios from "axios";
const apiClient = axios.create({
  baseURL: `http://127.0.0.1:8000/mainapp/status/`,
  withCredentials: false,
  headers: {
    Accept: "application/json",

    "Content-Type": "application/json"
  }
});
export default {
  getFundraisings() {
    return apiClient.post("");
  },
  // getFundraising(id) {
  //   return apiClient.get("/fundraisings/" + id);
  // },
  // getChart() {
  //   return apiClient.get("/chart/");
  // },
  // getPoints() {
  //   return apiClient.get("/points/");
  // },
  // getRates() {
  //   return apiClient.get("/rates/");
  // }
};
