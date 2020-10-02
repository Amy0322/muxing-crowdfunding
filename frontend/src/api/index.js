import axios from 'axios'

const getAPI = axios.create({
    baseURL: 'http://127.0.0.1:8000/mainapp/status/',
    timeout: 90000,
})

export { getAPI }
// import axios from 'axios'
//
// export default {
//   fetchNotes (method, params, data) {
//     if (method === 'post'){
//       return ajax('mainapp/status/', method, {data})
//     } else {
//       return ajax('mainapp/status/', 'get', null, null)
//     }
//   }
// }
//
// /**
//  * @param url
//  * @param method
//  * @param params
//  * @param data
//  * @returns
//  */
// function ajax(url, method, options) {
//   if (options !== undefined) {
//     var {params = {}, data = {}} = options
//   } else {
//     params= data = {}
//   }
//
//   return new Promise((resolve, reject) => {
//     axios({
//       url,
//       method,
//       params,
//       data
//     }).then(res => {
//       resolve(res)
//     }, res => {
//       reject(res)
//     })
//   })
// }
