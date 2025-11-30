import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { getProduct } from "../api/productsApi";
import { createPaymentIntent } from "../api/paymentApi";

import LoadingScreen from "../components/LoadingScreen";  // ⬅ ADD THIS
import "./ProductDetailPage.css";

export default function ProductDetailPage() {
  const { id } = useParams();
  const [product, setProduct] = useState(null);
  const [loading, setLoading] = useState(false); // ⬅ ADD THIS

  useEffect(() => {
    getProduct(id)
      .then((res) => setProduct(res.data))
      .catch(() => alert("Error loading product"));
  }, [id]);

  const handleBuyNow = async () => {
    setLoading(true); // ⬅ SHOW LOADING SCREEN IMMEDIATELY

    try {
      const res = await createPaymentIntent(product.price * 100);

      const secret =
        res?.data?.client_secret ||
        res?.client_secret ||
        res?.data?.response?.client_secret ||
        res?.data?.data?.client_secret;

      if (!secret) {
        setLoading(false);
        alert("No client secret received!");
        return;
      }

      // Smooth short delay for UX
      setTimeout(() => {
        window.location.href = `/checkout/${product.id}?secret=${secret}`;
      }, 700);

    } catch (err) {
      setLoading(false);
      alert("Payment creation failed.");
    }
  };

  if (!product) return <h2 className="loading-text">Loading…</h2>;

  return (
    <>
      {loading && <LoadingScreen />}  {/* ⬅ SHOW OVERLAY */}

      <div className="detail-container">
        <div className="product-card">
          <img src={product.image} alt="product" className="product-img" />

          <div className="product-info">
            <h1 className="product-title">{product.name}</h1>
            <p className="product-desc">{product.desc}</p>
            <h2 className="product-price">$ {product.price}</h2>

            <button className="buy-btn" onClick={handleBuyNow}>
              Buy Now
            </button>
          </div>
        </div>
      </div>
    </>
  );
}
