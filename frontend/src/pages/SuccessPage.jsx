import "./SuccessPage.css";

export default function SuccessPage() {
  return (
    <div className="success-container">
      <div className="success-card">
        <div className="success-icon">✔</div>

        <h1 className="success-title">Payment Successful</h1>
        <p className="success-message">
          Your payment has been processed securely.
        </p>

        <button 
          className="success-btn"
          onClick={() => window.location.href = "/"}
        >
          Back to Shop
        </button>
      </div>
    </div>
  );
}
