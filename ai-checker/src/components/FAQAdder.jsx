import React, { useState } from "react";
import axios from "axios";
import { toast } from "react-toastify";

const FAQAdder = () => {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [message, setMessage] = useState("");

  const handleAddFaq = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post("https://ai-personal-health-assistant.onrender.com/faq/add", {
        question,
        answer,
      });
      toast.success("Reminder added successfully!");
      setMessage(res.data.message);
      setQuestion("");
      setAnswer("");
    } catch (err) {
      // toast.error("Failed to load data!");
      setMessage("Failed to add FAQ.");
      console.error(err);
    }
  };

  return (
    <div className="max-w-2xl mx-auto px-6 py-10">
      <h2 className="text-2xl font-bold mb-4 text-blue-700">Add New FAQ</h2>
      <form onSubmit={handleAddFaq} className="space-y-4">
        <input
          type="text"
          placeholder="Enter your question"
          className="w-full p-3 border rounded-md"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          required
        />
        <textarea
          rows="4"
          placeholder="Enter the answer"
          className="w-full p-3 border rounded-md"
          value={answer}
          onChange={(e) => setAnswer(e.target.value)}
          required
        ></textarea>
        <button
          type="submit"
          className="bg-blue-600 text-white px-6 py-2 rounded-md hover:bg-blue-700 transition"
        >
          Submit FAQ
        </button>
      </form>
      {message && <p className="mt-4 text-green-700 font-medium">{message}</p>}
    </div>
  );
};

export default FAQAdder;
