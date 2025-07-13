import React, { useState } from "react";
import axios from "axios";
import { toast } from "react-toastify";

const ReminderSystem = () => {
  const [medicineName, setMedicineName] = useState("");
  const [datetime, setDatetime] = useState("");
  const [message, setMessage] = useState("");

  const handleSetReminder = async () => {
    if (!medicineName || !datetime) {
      setMessage("Please fill in all fields.");
      return;
    }

    const time = new Date(datetime).toTimeString().slice(0, 5); // "HH:MM"

    try {
      const res = await axios.post("http://127.0.0.1:8000/reminders", {
        medicine_name: medicineName,
        time: time,
      });
      setMessage(res.data.message || "Reminder set successfully!");
      toast.success("Reminder added successfully!");
      setMedicineName("");
      setDatetime("");
    } catch (err) {
      console.error(err);
      setMessage("Failed to set reminder.");
    }
  };

  return (
    <div className="max-w-lg mx-auto p-6 mt-10 bg-white rounded-xl shadow-md border border-blue-200">
      <h2 className="text-2xl font-bold text-blue-700 mb-4">Set Reminder</h2>

      <input
        type="text"
        placeholder="Reminder (e.g., Take medicine)"
        className="w-full p-3 border border-gray-300 rounded-lg mb-4 focus:outline-none focus:ring-2 focus:ring-blue-400"
        value={medicineName}
        onChange={(e) => setMedicineName(e.target.value)}
      />

      <input
        type="datetime-local"
        className="w-full p-3 border border-gray-300 rounded-lg mb-4 focus:outline-none focus:ring-2 focus:ring-blue-400"
        value={datetime}
        onChange={(e) => setDatetime(e.target.value)}
      />

      <button
        onClick={handleSetReminder}
        className="w-full bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700 transition duration-300"
      >
        Set Reminder
      </button>

      {message && (
        <p className="mt-4 text-center text-sm text-blue-700 font-medium">{message}</p>
      )}
    </div>
  );
};

export default ReminderSystem;
