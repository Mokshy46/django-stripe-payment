import { useEffect } from "react";
import { useSearchParams, useNavigate } from "react-router-dom";
import { loadStripe } from "@stripe/stripe-js";
import "./PaymentPage.css";

const stripePromise = loadStripe(
  "pk_test_51SMNspHZMGfpni4JAeIzpk0Ima8cE9PdCmwVkvVysGoJDFjj96WkMxq938GCxkLsy3xVkm5us4IaAcnwUxoJTA9A00HHHpStu3"
);

export default function PaymentPage() {
  const [params] = useSearchParams();
  const navigate = useNavigate();

  useEffect(() => {
    const clientSecret = params.get("secret");

    async function pay() {
      const stripe = await stripePromise;
      const result = await stripe.confirmCardPayment(clientSecret);

      if (result.paymentIntent?.status === "succeeded") {
        navigate("/success");
      } else {
        navigate("/cancel");
      }
    }

    pay();
  }, []);

  return (
    <div className="payment-wrapper">
      <div className="payment-box">
        <div className="payment-loader"></div>
        <p className="payment-text">Processing your payment...</p>
      </div>
    </div>
  );
}
