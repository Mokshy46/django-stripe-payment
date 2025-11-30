import api from "./axiosClient";

export const getProducts = () => api.get("/api/");
export const getProduct = (id) => api.get(`/api/${id}/`);