import { useState } from "react";
import axios from "axios";
const SymptomChecker = () => {
  const [symptoms, setSymptoms] = useState("");
  const [result, setResult] = useState("");

  const handleCheck = async () => {
    try {
      const res = await axios.post("https://ai-personal-health-assistant.onrender.com/predict/", { // "http://localhost:8000/predict/"
        symptoms: symptoms.split(","),
      });
      setResult(res.data.predicted_disease);
    } catch (error) {
      setResult("An error occurred. Please try again.");
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-100 to-white flex items-center justify-center px-4">
      <div className="bg-white p-8 rounded-3xl shadow-2xl w-full max-w-2xl">
        <h2 className="text-3xl font-bold text-blue-700 mb-6 text-center">
          Symptom Checker
        </h2>
        <input
          type="text"
          className="w-full p-4 border border-gray-300 rounded-xl mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500 shadow-sm"
          placeholder="e.g., fever, headache, fatigue"
          value={symptoms}
          onChange={(e) => setSymptoms(e.target.value)}
        />
        <button
          onClick={handleCheck}
          className="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 rounded-xl transition duration-300 shadow-md"
        >
          Check Disease
        </button>
        {result && (
          <div className="mt-6 bg-green-50 border border-green-400 text-green-800 p-4 rounded-xl shadow-sm text-center">
            <strong>Predicted Disease:</strong> {result}
          </div>
        )}
      </div>
    </div>
  );
};

export default SymptomChecker;
