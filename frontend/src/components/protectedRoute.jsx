import { Navigate } from "react-router-dom";

function ProtectedRoute({ children }) {

  const token = localStorage.getItem("token");

  // TOKEN CHECK

  if (!token) {

    return <Navigate to="/" />;
  }

  // VALID USER

  return children;
}

export default ProtectedRoute;