import { useState } from "react";
import API from "../api";

function Register() {

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleRegister = async () => {

    try {

      const response = await API.post(
        "/auth/register",
        {
          email,
          password,
        }
      );

      alert("User Registered Successfully 🚀");

      console.log(response.data);

    } catch (error) {

      console.log(error);

      alert("Registration Failed ❌");
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
          GeoIndia Register 🚀
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
          onClick={handleRegister}
          style={{
            width: "100%",
            padding: "12px",
            background: "#16a34a",
            color: "white",
            border: "none",
            borderRadius: "8px",
            cursor: "pointer",
            fontSize: "16px",
            fontWeight: "bold",
          }}
        >
          Register
        </button>
      </div>
    </div>
  );
}

export default Register;