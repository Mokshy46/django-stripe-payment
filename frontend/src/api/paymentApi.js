import api from "./axiosClient";
import { loadStripe } from "@stripe/stripe-js";

const stripePromise = loadStripe(import.meta.env.VITE_STRIPE_PUBLIC_KEY);

export const fetchProducts = () => api.get("/api/");
export const fetchProduct = (id) => api.get(`/api/${id}/`);

export const createPaymentIntent = async (amount) => {
  const res = await api.post("/api/payment/create-intent/", { amount });
  return res.data;
};

export const redirectToStripe = async (clientSecret) => {
  const stripe = await stripePromise;
  await stripe.confirmCardPayment(clientSecret);
};
