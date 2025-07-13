import { Link } from "react-router-dom";

const Home = () => {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-white py-10 px-6 ">
      {/* Hero Section */}
      <div className="text-center max-w-3xl mx-auto mb-10">
        <h1 className="text-4xl md:text-5xl font-bold text-blue-700 mb-4">
          Welcome to Your AI Health Assistant
        </h1>
        <p className="text-lg text-gray-700">
          Get instant health advice, manage your symptoms, set reminders, and access FAQs—all in one place.
        </p>
      </div>

      {/* Feature Cards */}
      <div className="grid gap-6 grid-cols-1 sm:grid-cols-2 md:grid-cols-3 max-w-6xl mx-auto">
        <Link to="/symptom-checker" className="bg-white rounded-2xl shadow-md p-6 hover:shadow-xl transition border border-blue-200">
          <h2 className="text-xl font-semibold text-blue-600 mb-2">Symptom Checker</h2>
          <p className="text-gray-700">Input your symptoms and receive AI-powered suggestions instantly.</p>
        </Link>

        <Link to="/reminder-set" className="bg-white rounded-2xl shadow-md p-6 hover:shadow-xl transition border border-blue-200">
          <h2 className="text-xl font-semibold text-blue-600 mb-2">Medication Reminder</h2>
          <p className="text-gray-700">Set reminders for taking medicines or other health-related tasks.</p>
        </Link>

        <Link to="/chatbot" className="bg-white rounded-2xl shadow-md p-6 hover:shadow-xl transition border border-blue-200">
          <h2 className="text-xl font-semibold text-blue-600 mb-2">AI Chatbot</h2>
          <p className="text-gray-700">Chat with your personal health assistant about common conditions.</p>
        </Link>

        <Link to="/add-faq" className="bg-white rounded-2xl shadow-md p-6 hover:shadow-xl transition border border-blue-200">
          <h2 className="text-xl font-semibold text-blue-600 mb-2">Add FAQ</h2>
          <p className="text-gray-700">Add new frequently asked questions and answers dynamically.</p>
        </Link>

        <Link to="/view-reminders" className="bg-white rounded-2xl shadow-md p-6 hover:shadow-xl transition border border-blue-200">
          <h2 className="text-xl font-semibold text-blue-600 mb-2">View Reminders</h2>
          <p className="text-gray-700">View Reminders of Your's that are frequently set reminders</p>
        </Link>

        <Link to="/faq-all" className="bg-white rounded-2xl shadow-md p-6 hover:shadow-xl transition border border-blue-200">
          <h2 className="text-xl font-semibold text-blue-600 mb-2">FAQs</h2>
          <p className="text-gray-700">Browse answers to frequently asked health-related questions.</p>
        </Link>

      </div>
    </div>
  );
};

export default Home;
