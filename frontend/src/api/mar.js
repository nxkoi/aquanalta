import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:8000", // ou o endereço da API do mar
});

export const updateBarco = (barco) => API.post("/update", barco);
export const getVizinhos = (id) => API.get("/nearby", { params: { id } });
