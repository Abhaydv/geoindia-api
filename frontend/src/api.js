import axios from "axios";

const API = axios.create({

  baseURL: "http://127.0.0.1:8008",

});

// REQUEST INTERCEPTOR

API.interceptors.request.use(

  (config) => {

    // JWT TOKEN

    const token = localStorage.getItem(
      "token"
    );

    // API KEY

    const apiKey = localStorage.getItem(
      "api_key"
    );

    // ADD JWT

    if (token) {

      config.headers.Authorization =
        `Bearer ${token}`;
    }

    // ADD API KEY

    if (apiKey) {

      config.headers["x-api-key"] =
        apiKey;
    }

    return config;
  },

  (error) => {

    return Promise.reject(error);
  }
);

export default API;