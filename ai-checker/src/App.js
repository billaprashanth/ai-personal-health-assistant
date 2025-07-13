import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import SymptomChecker from './components/SymptomChecker';
import Chatbot from './components/Chatbot';
import FAQAdder from './components/FAQAdder';
import FAQAdmin from './components/FAQAdmin';
import Home from './components/Home';
import NotFound from './components/NotFound';
import ReminderSystem from './components/ReminderSystem';
import { ToastContainer } from "react-toastify";
import ReminderViewer from "./components/ReminderViewer";
import "react-toastify/dist/ReactToastify.css";


function App() {
  return (
    <>
    <Router>
      <Routes>
        
        <Route path="/" element={<Home />} />
        <Route path="/symptom-checker" element={<SymptomChecker />} />
        <Route path="/chatbot" element={<Chatbot />} />
        <Route path='/faq-all' element={<FAQAdmin />} />
        <Route path="/add-faq" element={<FAQAdder />} />
        <Route path='/reminder-set' element={<ReminderSystem />} />
        <Route path="/view-reminders" element={<ReminderViewer />} />
        <Route path="*" element={<NotFound />} />

      </Routes>
    </Router>
    <ToastContainer position="top-right" autoClose={3000} />
    </>
  );
}

export default App;
