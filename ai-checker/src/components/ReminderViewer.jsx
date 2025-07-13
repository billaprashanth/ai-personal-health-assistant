import React, { useEffect, useState } from "react";
import axios from "axios";
import { toast } from "react-toastify";
toast.success("Reminder added successfully!");
toast.error("Failed to load data!");

const ReminderViewer = () => {
  const [reminders, setReminders] = useState([]);
  const [editingIndex, setEditingIndex] = useState(null);
  const [editData, setEditData] = useState({ medicine_name: "", time: "" });

  const fetchReminders = async () => {
    try {
      const res = await axios.get("http://localhost:8000/get/reminder");
      setReminders(res.data);
    } catch (err) {
      console.error("Fetch error", err);
    }
  };

  useEffect(() => {
    fetchReminders();
  }, []);

  const handleDelete = async (name, time) => {
    try {
      await axios.delete(`http://localhost:8000/reminders/${name}/${time}`);
      fetchReminders();
    } catch (err) {
      console.error("Delete error", err);
    }
  };

  const startEdit = (index) => {
    setEditingIndex(index);
    setEditData(reminders[index]);
  };

  const handleUpdate = async () => {
    try {
      const { medicine_name, time } = reminders[editingIndex];
      await axios.patch(
        `http://localhost:8000/reminders/${medicine_name}/${time}`,
        editData
      );
      setEditingIndex(null);
      setEditData({ medicine_name: "", time: "" });
      fetchReminders();
    } catch (err) {
      console.error("Update error", err);
    }
  };

  return (
    <div className="max-w-3xl mx-auto p-6 mt-10 bg-white rounded-xl shadow-lg">
      <h2 className="text-2xl font-bold text-blue-700 mb-6 text-center">
        Your Medication Reminders
      </h2>

      {reminders.length === 0 ? (
        <p className="text-center text-gray-500">No reminders yet.</p>
      ) : (
        reminders.map((reminder, index) => (
          <div
            key={index}
            className="p-4 border rounded-lg mb-4 shadow-md bg-gray-50 flex justify-between items-center"
          >
            {editingIndex === index ? (
              <div className="flex flex-col w-full gap-2">
                <input
                  type="text"
                  value={editData.medicine_name}
                  onChange={(e) =>
                    setEditData({ ...editData, medicine_name: e.target.value })
                  }
                  className="border px-2 py-1 rounded"
                />
                <input
                  type="time"
                  value={editData.time}
                  onChange={(e) =>
                    setEditData({ ...editData, time: e.target.value })
                  }
                  className="border px-2 py-1 rounded"
                />
                <button
                  onClick={handleUpdate}
                  className="bg-green-600 text-white py-1 px-3 rounded mt-1"
                >
                  Save
                </button>
              </div>
            ) : (
              <>
                <div>
                  <p className="text-lg font-medium">{reminder.medicine_name}</p>
                  <p className="text-gray-600">Time: {reminder.time}</p>
                </div>
                <div className="flex gap-2">
                  <button
                    onClick={() => startEdit(index)}
                    className="bg-yellow-400 px-3 py-1 rounded text-white"
                  >
                    Edit
                  </button>
                  <button
                    onClick={() =>
                      handleDelete(reminder.medicine_name, reminder.time)
                    }
                    className="bg-red-500 px-3 py-1 rounded text-white"
                  >
                    Delete
                  </button>
                </div>
              </>
            )}
          </div>
        ))
      )}
    </div>
  );
};

export default ReminderViewer;
