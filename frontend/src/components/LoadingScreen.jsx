import "./LoadingScreen.css";

export default function LoadingScreen() {
  return (
    <div className="loading-overlay">
      <div className="loading-spinner"></div>
      <p className="loading-text">Preparing checkout…</p>
    </div>
  );
}
