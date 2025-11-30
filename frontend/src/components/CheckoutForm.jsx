import { useStripe, useElements, CardElement } from "@stripe/react-stripe-js";
import { useState } from "react";
import "./CheckoutForm.css";
import "../components/Spinner.css";

export default function CheckoutForm({ clientSecret }) {
  const stripe = useStripe();
  const elements = useElements();
  const [loading, setLoading] = useState(false);

  const handlePayment = async (e) => {
    e.preventDefault();
    if (!stripe || !elements) return;

    setLoading(true);

    const card = elements.getElement(CardElement);

    const { error, paymentIntent } = await stripe.confirmCardPayment(clientSecret, {
      payment_method: { card },
    });

    setLoading(false);

    if (error) {
      window.location.href = "/cancel";
      return;
    }

    if (paymentIntent?.status === "succeeded") {
      window.location.href = "/success";
    } else {
      window.location.href = "/cancel";
    }
  };

  return (
    <>
      {loading && (
        <div className="spinner-overlay">
          <div className="gradient-loader"></div>
        </div>
      )}

      <form className="checkout-form" onSubmit={handlePayment}>
        <h2 className="checkout-title">Complete Payment</h2>

        <div className="card-element-box">
          <CardElement
            options={{
              style: {
                base: {
                  color: "#f5f5f5",
                  fontSize: "17px",
                  "::placeholder": { color: "#888" },
                },
                invalid: { color: "#ff4d4d" },
              },
            }}
          />
        </div>

        <button className="checkout-btn" disabled={!stripe || loading}>
          {loading ? "Processing…" : "Pay Now"}
        </button>
      </form>
    </>
  );
}
