import { useState } from "react";
import { useNavigate } from "react-router-dom";
import API from "../api";

function Login() {

  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async (e) => {

    e.preventDefault();

    console.log("Login clicked");

    try {

      const response = await API.post(
        "/auth/login",
        {
          email,
          password,
        }
      );

      console.log(response.data);

      localStorage.setItem(
        "token",
        response.data.token
      );

      alert("Login Successful 🚀");

      navigate("/dashboard");

    } catch (error) {

      console.log(error);

      alert("Login Failed ❌");
    }
  };

  return (
    <div
      style={{
        height: "100vh",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        background:
          "linear-gradient(to right, #0f172a, #1e293b)",
      }}
    >
      <div
        style={{
          background: "#111827",
          padding: "40px",
          width: "350px",
          borderRadius: "15px",
          boxShadow: "0 0 20px rgba(0,0,0,0.3)",
          color: "white",
        }}
      >
        <h1
          style={{
            textAlign: "center",
            marginBottom: "30px",
            fontSize: "32px",
          }}
        >
          GeoIndia Login 🚀
        </h1>

        <input
          type="email"
          placeholder="Enter Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          style={{
            width: "100%",
            padding: "12px",
            marginBottom: "15px",
            borderRadius: "8px",
            border: "1px solid #374151",
            background: "#1f2937",
            color: "white",
            outline: "none",
            boxSizing: "border-box",
          }}
        />

        <input
          type="password"
          placeholder="Enter Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          style={{
            width: "100%",
            padding: "12px",
            marginBottom: "20px",
            borderRadius: "8px",
            border: "1px solid #374151",
            background: "#1f2937",
            color: "white",
            outline: "none",
            boxSizing: "border-box",
          }}
        />

        <button
          type="button"
          onClick={handleLogin}
          style={{
            width: "100%",
            padding: "12px",
            background: "#2563eb",
            color: "white",
            border: "none",
            borderRadius: "8px",
            cursor: "pointer",
            fontSize: "16px",
            fontWeight: "bold",
          }}
        >
          Login
        </button>
      </div>
    </div>
  );
}

export default Login;