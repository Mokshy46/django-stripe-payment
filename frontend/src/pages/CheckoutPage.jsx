import { useSearchParams, useParams } from "react-router-dom";
import { Elements } from "@stripe/react-stripe-js";
import { loadStripe } from "@stripe/stripe-js";
import CheckoutForm from "../components/CheckoutForm";
import "./CheckoutPage.css";

const stripePromise = loadStripe(
  "pk_test_51SMNspHZMGfpni4JAeIzpk0Ima8cE9PdCmwVkvVysGoJDFjj96WkMxq938GCxkLsy3xVkm5us4IaAcnwUxoJTA9A00HHHpStu3"
);

export default function CheckoutPage() {
  const { id } = useParams();
  const [params] = useSearchParams();
  const clientSecret = params.get("secret");

  if (!clientSecret)
    return (
      <div className="checkout-wrapper">
        <h2 className="checkout-error">No payment session found.</h2>
      </div>
    );

  return (
    <div className="checkout-wrapper">
      <h1 className="checkout-heading">Checkout</h1>

      <Elements stripe={stripePromise} options={{ clientSecret }}>
        <CheckoutForm clientSecret={clientSecret} />
      </Elements>
    </div>
  );
}
