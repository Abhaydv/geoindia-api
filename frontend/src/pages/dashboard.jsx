import { useNavigate } from "react-router-dom";
import { useState, useEffect } from "react";
import API from "../api";

function Dashboard() {

  const navigate = useNavigate();

  const token = localStorage.getItem("token");

  const [apiKey, setApiKey] = useState("");

  const [states, setStates] = useState([]);

  const [districts, setDistricts] = useState([]);

  const [villages, setVillages] = useState([]);

  const [usageCount, setUsageCount] =
    useState(0);

  const [search, setSearch] = useState("");

  const [searchResults, setSearchResults] =
    useState([]);

  const [selectedState, setSelectedState] =
    useState("");

  const [selectedDistrict, setSelectedDistrict] =
    useState("");

  // LOGOUT

  const handleLogout = () => {

    localStorage.removeItem("token");

    localStorage.removeItem("api_key");

    navigate("/");
  };

  // GENERATE API KEY

  const generateApiKey = async () => {

    try {

      const response = await API.post(
        "/api-keys/generate?user_id=1"
      );

      setApiKey(response.data.api_key);

      localStorage.setItem(
        "api_key",
        response.data.api_key
      );

      alert("API Key Generated 🚀");

    } catch (error) {

      console.log(error);

      alert("Failed ❌");
    }
  };

  // FETCH STATES

  const fetchStates = async () => {

    try {

      const response = await API.get(
        "/location/states"
      );

      setStates(response.data);

      fetchUsageCount();

    } catch (error) {

      console.log(error);
    }
  };

  // FETCH DISTRICTS

  const fetchDistricts = async () => {

    try {

      const response = await API.get(
        `/location/districts/${selectedState}`
      );

      setDistricts(response.data);

      fetchUsageCount();

    } catch (error) {

      console.log(error);
    }
  };

  // FETCH VILLAGES

  const fetchVillages = async () => {

    try {

      const response = await API.get(
        `/location/villages/${selectedDistrict}`
      );

      setVillages(response.data);

      fetchUsageCount();

    } catch (error) {

      console.log(error);
    }
  };

  // SEARCH

  const searchVillages = async () => {

    try {

      const response = await API.get(
        `/location/search?q=${search}`
      );

      setSearchResults(response.data);

      fetchUsageCount();

    } catch (error) {

      console.log(error);
    }
  };

  // USAGE

  const fetchUsageCount = async () => {

    try {

      const response = await API.get(
        "/location/usage-count"
      );

      setUsageCount(
        response.data.total_requests
      );

    } catch (error) {

      console.log(error);
    }
  };

  useEffect(() => {

    fetchUsageCount();

  }, []);

  return (

    <div className="flex min-h-screen bg-slate-900 text-white">

      {/* SIDEBAR */}

      <div className="w-64 bg-slate-950 p-6 hidden md:block">

        <h1 className="text-3xl font-bold mb-10">
          GeoIndia 🚀
        </h1>

        <div className="space-y-4">

          <button className="w-full text-left bg-slate-800 p-3 rounded-lg">
            Dashboard
          </button>

          <button
            onClick={handleLogout}
            className="w-full text-left bg-red-600 p-3 rounded-lg"
          >
            Logout
          </button>

        </div>

      </div>

      {/* MAIN */}

      <div className="flex-1 p-8">

        <h1 className="text-4xl font-bold">
          GeoIndia Dashboard 🚀
        </h1>

        {/* TOKEN */}

        <div className="mt-8 bg-slate-800 p-6 rounded-xl">

          <h2 className="text-2xl font-semibold">
            Authentication Status ✅
          </h2>

          <p className="mt-4">
            JWT Stored Successfully 🔐
          </p>

          <code className="text-sky-400 break-all">
            {token?.slice(0, 40)}...
          </code>

        </div>

        {/* STATS */}

        <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mt-10">

          <div className="bg-slate-800 p-6 rounded-xl">
            <h2>States 🌍</h2>
            <p className="text-4xl mt-4">
              {states.length}
            </p>
          </div>

          <div className="bg-slate-800 p-6 rounded-xl">
            <h2>Districts 🏙️</h2>
            <p className="text-4xl mt-4">
              {districts.length}
            </p>
          </div>

          <div className="bg-slate-800 p-6 rounded-xl">
            <h2>Villages 🏘️</h2>
            <p className="text-4xl mt-4">
              {villages.length}
            </p>
          </div>

          <div className="bg-slate-800 p-6 rounded-xl">
            <h2>Requests 📡</h2>
            <p className="text-4xl mt-4">
              {usageCount}
            </p>
          </div>

        </div>

        {/* API KEY */}

        <div className="mt-10">

          <button
            onClick={generateApiKey}
            className="bg-blue-600 px-6 py-3 rounded-xl"
          >
            Generate API Key
          </button>

          {
            apiKey && (

              <div className="bg-slate-800 p-6 rounded-xl mt-6">

                <p className="break-all text-green-400">
                  {apiKey}
                </p>

              </div>
            )
          }

        </div>

        {/* SEARCH */}

        <div className="mt-10 bg-slate-800 p-6 rounded-xl">

          <h2 className="text-2xl mb-4">
            Search Villages 🔍
          </h2>

          <div className="flex gap-4">

            <input
              type="text"
              placeholder="Village name"
              value={search}
              onChange={(e) =>
                setSearch(e.target.value)
              }
              className="flex-1 bg-slate-700 p-3 rounded-lg"
            />

            <button
              onClick={searchVillages}
              className="bg-yellow-500 px-6 py-3 rounded-xl"
            >
              Search
            </button>

          </div>

          {
            searchResults.length > 0 && (

              <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mt-6">

                {
                  searchResults.map((item, index) => (

                    <div
                      key={index}
                      className="bg-slate-700 p-3 rounded-lg"
                    >
                      {item.name}
                    </div>
                  ))
                }

              </div>
            )
          }

        </div>

        {/* STATES */}

        <div className="mt-10">

          <button
            onClick={fetchStates}
            className="bg-purple-600 px-6 py-3 rounded-xl"
          >
            Fetch States 🌍
          </button>

        </div>

        {/* DISTRICTS */}

        <div className="mt-10 bg-slate-800 p-6 rounded-xl">

          <select
            value={selectedState}
            onChange={(e) =>
              setSelectedState(e.target.value)
            }
            className="bg-slate-700 p-3 rounded-lg w-full"
          >

            <option value="">
              Select State
            </option>

            {
              states.map((state) => (

                <option
                  key={state.id}
                  value={state.id}
                >
                  {state.name}
                </option>
              ))
            }

          </select>

          <button
            onClick={fetchDistricts}
            className="bg-indigo-600 px-6 py-3 rounded-xl mt-4"
          >
            Fetch Districts
          </button>

        </div>

        {/* VILLAGES */}

        <div className="mt-10 bg-slate-800 p-6 rounded-xl">

          <select
            value={selectedDistrict}
            onChange={(e) =>
              setSelectedDistrict(e.target.value)
            }
            className="bg-slate-700 p-3 rounded-lg w-full"
          >

            <option value="">
              Select District
            </option>

            {
              districts.map((district) => (

                <option
                  key={district.id}
                  value={district.id}
                >
                  {district.name}
                </option>
              ))
            }

          </select>

          <button
            onClick={fetchVillages}
            className="bg-pink-600 px-6 py-3 rounded-xl mt-4"
          >
            Fetch Villages
          </button>

        </div>

      </div>

    </div>
  );
}

export default Dashboard;