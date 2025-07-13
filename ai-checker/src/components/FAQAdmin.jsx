import React, { useEffect, useState } from "react";
import axios from "axios";
const truncateAnswer = (text, wordLimit = 70) => {
  const words = text.split(" ");
  return words.length > wordLimit
    ? words.slice(0, wordLimit).join(" ") + "..."
    : text;
};

const shuffleArray = (array) => {
  return array
    .map((item) => ({ item, sort: Math.random() }))
    .sort((a, b) => a.sort - b.sort)
    .map(({ item }) => item);
};

const FAQViewer = () => {
  const [faqs, setFaqs] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchFaqs = async () => {
      try {
        const res = await axios.get("https://ai-personal-health-assistant.onrender.com/faq/all");
        const shuffled = shuffleArray(res.data.faqs);
        setFaqs(shuffled.slice(0, 5)); // random 5
      } catch (err) {
        setError("Failed to load FAQs.");
        console.error(err);
      }
    };

    fetchFaqs();
  }, []);

  return (
    <div className="max-w-4xl mx-auto px-6 py-10">
      <h2 className="text-3xl font-bold mb-6 text-blue-700">Frequently Asked Questions</h2>
      {error && <p className="text-red-600">{error}</p>}

      <div className="space-y-4">
        {faqs.map((faq, index) => (
          <div key={index} className="p-4 border rounded-lg shadow-md bg-white">
            <h3 className="font-semibold text-lg text-blue-600">{faq.question}</h3>
            <p className="text-gray-800 mt-2">{truncateAnswer(faq.answer, 70)}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default FAQViewer;
