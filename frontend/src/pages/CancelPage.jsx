import "./CancelPage.css";

export default function CancelPage() {
  return (
    <div className="cancel-container">
      <div className="cancel-card">
        <div className="cancel-icon">✖</div>

        <h1 className="cancel-title">Payment Failed</h1>
        <p className="cancel-message">
          Unfortunately, your payment could not be processed.
          <br />Please try again.
        </p>

        <button
          className="cancel-btn"
          onClick={() => (window.location.href = "/")}
        >
          Back to Shop
        </button>
      </div>
    </div>
  );
}
