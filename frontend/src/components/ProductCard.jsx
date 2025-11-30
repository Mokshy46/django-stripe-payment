import { Link } from "react-router-dom";
import "./ProductCard.css";

export default function ProductCard({ product }) {
  return (
    <div className="card">
      <img 
        src={product.image} 
        alt={product.name} 
        className="card-img"
      />

      <h3 className="card-title">{product.name}</h3>
      <p className="card-price">$ {product.price}</p>

      <Link to={`/product/${product.id}`} className="card-btn-link">
        <button className="card-btn">View Product</button>
      </Link>
    </div>
  );
}
