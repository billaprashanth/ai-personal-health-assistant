import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <nav className="bg-blue-600 text-white p-4 shadow-md">
      <div className="max-w-7xl mx-auto flex justify-between items-center">
        <h1 className="font-bold text-xl">AI Health Assistant</h1>
        <div className="space-x-4">
          <Link to="/" className="hover:underline">Home</Link>
          <Link to="/symptom-checker" className="hover:underline">Checker</Link>
          <Link to="/chatbot" className="hover:underline">Chatbot</Link>
          <Link to="/faq-all" className="hover:underline">FAQ</Link>
          <Link to="/add-faq" className="hover:underline">Add FAQ</Link>
          <Link to="/reminder-set" className="hover:underline">Reminder</Link>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
