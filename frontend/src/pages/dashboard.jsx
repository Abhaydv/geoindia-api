import { useNavigate } from "react-router-dom";
import { useState } from "react";
import API from "../api";

function Dashboard() {

  const navigate = useNavigate();

  const token = localStorage.getItem("token");

  const [apiKey, setApiKey] = useState("");

  const handleLogout = () => {

    localStorage.removeItem("token");

    alert("Logged Out 🚀");

    navigate("/");
  };

  const generateApiKey = async () => {

    try {

      const response = await API.post(
        "/api-keys/generate?user_id=1"
      );

      console.log(response.data);

      setApiKey(response.data.api_key);

      alert("API Key Generated 🚀");

    } catch (error) {

      console.log(error);

      alert("Failed To Generate API Key ❌");
    }
  };

  const copyApiKey = () => {

    navigator.clipboard.writeText(apiKey);

    alert("API Key Copied 🚀");
  };

  return (

    <div className="min-h-screen bg-slate-900 text-white p-8">

      {/* TOP BAR */}

      <div className="flex justify-between items-center">

        <h1 className="text-4xl font-bold">
          GeoIndia Dashboard 🚀
        </h1>

        <button
          onClick={handleLogout}
          className="bg-red-500 hover:bg-red-600 px-5 py-2 rounded-lg"
        >
          Logout
        </button>

      </div>

      {/* AUTH STATUS */}

      <div className="mt-10 bg-slate-800 p-6 rounded-xl shadow-lg">

        <h2 className="text-2xl font-semibold mb-4">
          Authentication Status ✅
        </h2>

        <p className="text-slate-300">
          JWT Token Stored Successfully 🔐
        </p>

        <p className="text-slate-400 mt-4 text-sm">
          Token Preview:
        </p>

        <code className="text-sky-400">
          {token?.slice(0, 40)}...
        </code>

      </div>

      {/* STATS CARDS */}

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-10">

        {/* CARD 1 */}

        <div className="bg-slate-800 p-6 rounded-xl shadow-lg">

          <h2 className="text-xl font-semibold">
            API Keys 🔑
          </h2>

          <p className="text-4xl font-bold mt-4 text-blue-400">
            1
          </p>

        </div>

        {/* CARD 2 */}

        <div className="bg-slate-800 p-6 rounded-xl shadow-lg">

          <h2 className="text-xl font-semibold">
            Requests 📡
          </h2>

          <p className="text-4xl font-bold mt-4 text-green-400">
            125
          </p>

        </div>

        {/* CARD 3 */}

        <div className="bg-slate-800 p-6 rounded-xl shadow-lg">

          <h2 className="text-xl font-semibold">
            Status 🚀
          </h2>

          <p className="text-2xl font-bold mt-4 text-purple-400">
            Active
          </p>

        </div>

      </div>

      {/* API KEY SECTION */}

      <div className="mt-10">

        <button
          onClick={generateApiKey}
          className="bg-blue-600 hover:bg-blue-700 px-6 py-3 rounded-xl text-lg"
        >
          Generate API Key
        </button>

        {
          apiKey && (

            <div className="bg-slate-800 p-6 rounded-xl mt-6 shadow-lg">

              <h3 className="text-2xl font-semibold mb-4">
                Your API Key 🔑
              </h3>

              <div className="flex items-center gap-4 mt-4">

                <p className="text-green-400 break-all">
                  {apiKey}
                </p>

                <button
                  onClick={copyApiKey}
                  className="bg-green-600 hover:bg-green-700 px-4 py-2 rounded-lg"
                >
                  Copy
                </button>

              </div>

            </div>
          )
        }

      </div>

    </div>
  );
}

export default Dashboard;