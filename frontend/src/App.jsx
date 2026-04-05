import { useState, useEffect } from 'react';
import axios from 'axios';

export default function App() {
  const [view, setView] = useState('courses'); 
  const [modules, setModules] = useState([]);
  const [selectedCourse, setSelectedCourse] = useState(null);
  const [selectedTopic, setSelectedTopic] = useState(null);

  useEffect(() => {
    axios.get('http://localhost:5000/api/modules')
      .then(res => setModules(res.data.data));
  }, []);

  // --- VIEW 1: COURSE SELECTION ---
  const CourseLanding = () => {
    const uniqueCourses = [...new Set(modules.map(m => m.course))];
    
    // A little helper to give different courses different accent colors
    const getAccent = (index) => {
      const accents = [
        'bg-gradient-to-br from-blue-500 to-indigo-600 shadow-blue-500/30',
        'bg-gradient-to-br from-emerald-400 to-teal-500 shadow-teal-500/30',
        'bg-gradient-to-br from-violet-500 to-purple-600 shadow-purple-500/30',
      ];
      return accents[index % accents.length];
    };

    return (
      <div className="mt-12 animate-in fade-in slide-in-from-bottom-4 duration-700">
        <div className="text-center mb-16">
          <h2 className="text-5xl font-extrabold text-slate-900 tracking-tight mb-4">
            What do you want to <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-indigo-600">master</span> today?
          </h2>
          <p className="text-lg text-slate-500 font-medium">Select a learning path to begin your intelligent journey.</p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-5xl mx-auto">
          {uniqueCourses.map((courseName, index) => (
            <div 
              key={courseName}
              onClick={() => { setSelectedCourse(courseName); setView('topics'); }}
              className={`relative h-64 rounded-[2rem] p-8 cursor-pointer group transition-all duration-300 hover:-translate-y-2 hover:shadow-2xl overflow-hidden ${getAccent(index)}`}
            >
              {/* Decorative background glow */}
              <div className="absolute -right-10 -top-10 w-40 h-40 bg-white opacity-10 rounded-full blur-2xl group-hover:scale-150 transition-transform duration-500"></div>
              
              <div className="relative h-full flex flex-col justify-between z-10">
                <div className="w-14 h-14 bg-white/20 backdrop-blur-md rounded-2xl flex items-center justify-center shadow-inner">
                  <span className="text-2xl text-white font-black">
                    {courseName.charAt(0)}
                  </span>
                </div>
                
                <div>
                  <h3 className="text-3xl font-bold text-white mb-1">{courseName}</h3>
                  <div className="flex items-center text-white/80 text-sm font-medium">
                    <span>Explore Path</span>
                    <span className="ml-2 group-hover:translate-x-1 transition-transform">→</span>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    );
  };

  // --- VIEW 2: TOPIC SELECTION ---
  const TopicList = () => {
    const filteredTopics = modules.filter(m => m.course === selectedCourse);
    return (
      <div className="mt-8 max-w-5xl mx-auto animate-in fade-in slide-in-from-right-8 duration-500">
        <button 
          onClick={() => setView('courses')} 
          className="mb-8 flex items-center text-sm font-bold text-slate-400 hover:text-slate-800 transition-colors bg-white px-4 py-2 rounded-full shadow-sm border border-slate-100 w-fit"
        >
          ← Back to Paths
        </button>
        
        <div className="mb-12">
          <h2 className="text-4xl font-black text-slate-900 tracking-tight">{selectedCourse} Curriculum</h2>
          <p className="text-slate-500 mt-2 text-lg">Select a module to begin your knowledge check.</p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredTopics.map((topic, idx) => (
            <div 
              key={topic.topic_id}
              onClick={() => { setSelectedTopic(topic); setView('quiz'); }}
              className="group p-8 bg-white/80 backdrop-blur-xl border border-slate-100 rounded-3xl cursor-pointer hover:shadow-xl hover:shadow-blue-500/5 hover:-translate-y-1 transition-all duration-300 relative overflow-hidden"
            >
              <div className="absolute top-0 left-0 w-1 h-full bg-slate-200 group-hover:bg-blue-500 transition-colors duration-300"></div>
              
              <div className="flex justify-between items-start mb-4">
                <span className="text-xs font-bold uppercase tracking-wider text-blue-600 bg-blue-50 px-3 py-1 rounded-full">
                  Module {idx + 1}
                </span>
                <span className="text-xs font-semibold text-slate-400 capitalize">{topic.difficulty}</span>
              </div>
              
              <h3 className="text-2xl font-bold text-slate-800 mb-3">{topic.name}</h3>
              
              <div className="flex items-center text-xs font-medium text-slate-500 bg-slate-50 w-fit px-3 py-1.5 rounded-lg">
                <span className="mr-2">⚡</span>
                Requires: {topic.prerequisites.length > 0 ? topic.prerequisites.length + " modules" : "None"}
              </div>
            </div>
          ))}
        </div>
      </div>
    );
  };

  // --- VIEW 3: KNOWLEDGE CHECK ---
  const KnowledgeCheck = () => {
    const [currentQ, setCurrentQ] = useState(0);
    const [answers, setAnswers] = useState({}); 
    const [showResults, setShowResults] = useState(false);

    const quizData = selectedTopic.quiz || [];

    const handleOptionSelect = (qIndex, optIndex) => {
      setAnswers({ ...answers, [qIndex]: optIndex });
    };

    if (quizData.length === 0) {
      return (
        <div className="max-w-2xl mx-auto mt-20 p-12 bg-white shadow-2xl shadow-blue-900/5 rounded-[2.5rem] border border-slate-100 text-center animate-in zoom-in-95 duration-500">
          <div className="w-20 h-20 bg-blue-50 text-blue-600 rounded-full flex items-center justify-center mx-auto mb-6 text-3xl">🚀</div>
          <h2 className="text-3xl font-black text-slate-900 mb-4">{selectedTopic.name}</h2>
          <p className="text-slate-500 mb-10 text-lg">This is a foundational module. No diagnostic check is required to begin.</p>
          
          <a href={selectedTopic.video_url} target="_blank" rel="noreferrer" className="inline-block w-full px-8 py-4 bg-slate-900 text-white font-bold rounded-2xl hover:bg-blue-600 transition-all shadow-lg hover:shadow-blue-500/30 text-lg">
            Start Lesson Now
          </a>
          
          <button onClick={() => setView('topics')} className="block mt-6 text-slate-400 mx-auto hover:text-slate-800 font-bold text-sm transition-colors">
            Cancel
          </button>
        </div>
      );
    }

    if (showResults) {
      let correctCount = 0;
      quizData.forEach((q, index) => {
        if (answers[index] === q.correct_index) correctCount++;
      });
      const scorePercentage = (correctCount / quizData.length) * 100;
      const passed = scorePercentage >= 70; 

      return (
        <div className="max-w-2xl mx-auto mt-16 p-12 bg-white shadow-2xl shadow-slate-900/5 rounded-[2.5rem] border border-slate-100 text-center animate-in zoom-in-95 duration-500">
          <div className="inline-block px-4 py-1 bg-slate-100 text-slate-600 font-bold rounded-full text-sm mb-6">
            Diagnostic Complete
          </div>
          
          <div className={`text-7xl font-black mb-8 tracking-tighter ${passed ? 'text-transparent bg-clip-text bg-gradient-to-r from-emerald-400 to-teal-500' : 'text-transparent bg-clip-text bg-gradient-to-r from-orange-400 to-red-500'}`}>
            {scorePercentage}%
          </div>

          {passed ? (
            <div className="bg-emerald-50 text-emerald-900 p-8 rounded-3xl mb-10 border border-emerald-100/50 text-left">
              <h3 className="text-2xl font-black mb-2 flex items-center"><span className="text-3xl mr-3">✨</span> Solid Foundation!</h3>
              <p className="text-emerald-700/80 font-medium">You have a great grasp of the prerequisites. You are perfectly ready to tackle <b>{selectedTopic.name}</b>.</p>
            </div>
          ) : (
            <div className="bg-orange-50 text-orange-900 p-8 rounded-3xl mb-10 border border-orange-100/50 text-left">
              <h3 className="text-2xl font-black mb-2 flex items-center"><span className="text-3xl mr-3">🧠</span> Knowledge Gap</h3>
              <p className="text-orange-800/80 font-medium">You might struggle with some concepts in <b>{selectedTopic.name}</b>. We highly recommend reviewing the prerequisites first.</p>
            </div>
          )}

          <div className="flex flex-col gap-4">
            {!passed && selectedTopic.prerequisites.length > 0 && (
              <button 
                onClick={() => setView('topics')}
                className="w-full py-4 bg-gradient-to-r from-orange-500 to-red-500 text-white font-bold rounded-2xl hover:opacity-90 transition-all shadow-lg shadow-orange-500/30 text-lg"
              >
                Review Prerequisites First
              </button>
            )}
            
            <a 
              href={selectedTopic.video_url} 
              target="_blank" 
              rel="noreferrer"
              className={`w-full py-4 font-bold rounded-2xl transition-all text-lg ${passed ? 'bg-slate-900 text-white hover:bg-blue-600 shadow-xl' : 'bg-white text-slate-500 border-2 border-slate-200 hover:border-slate-300 hover:text-slate-800'}`}
            >
              {passed ? "Start Lesson Video" : "Proceed Anyway"}
            </a>
          </div>
        </div>
      );
    }

    const q = quizData[currentQ];

    return (
      <div className="max-w-3xl mx-auto mt-12 bg-white shadow-2xl shadow-blue-900/5 rounded-[2.5rem] border border-slate-100 overflow-hidden animate-in slide-in-from-bottom-8 duration-500">
        
        {/* Sleek Progress Bar */}
        <div className="h-2 w-full bg-slate-100">
          <div className="h-full bg-gradient-to-r from-blue-500 to-indigo-500 transition-all duration-500 ease-out" style={{ width: `${((currentQ + 1) / quizData.length) * 100}%` }}></div>
        </div>
        
        <div className="p-10 md:p-14">
          <div className="flex justify-between items-center mb-10">
            <div className="px-4 py-1.5 bg-blue-50 text-blue-600 font-bold rounded-full text-xs tracking-widest uppercase">
              Question {currentQ + 1} / {quizData.length}
            </div>
            <button onClick={() => setView('topics')} className="w-10 h-10 rounded-full bg-slate-50 flex items-center justify-center text-slate-400 hover:bg-slate-100 hover:text-slate-800 transition-colors">
              ✕
            </button>
          </div>

          <h2 className="text-3xl font-black text-slate-900 mb-10 leading-tight">{q.question}</h2>
          
          <div className="space-y-4 mb-12">
            {q.options.map((opt, idx) => {
              const isSelected = answers[currentQ] === idx;
              return (
                <div 
                  key={idx}
                  onClick={() => handleOptionSelect(currentQ, idx)}
                  className={`p-6 rounded-2xl cursor-pointer transition-all duration-200 flex items-center group
                    ${isSelected 
                      ? 'bg-blue-50 border-2 border-blue-500 shadow-sm shadow-blue-500/10' 
                      : 'bg-white border-2 border-slate-100 hover:border-slate-300 hover:bg-slate-50'}`}
                >
                  <div className={`w-6 h-6 rounded-full border-2 flex items-center justify-center mr-4 transition-colors
                    ${isSelected ? 'border-blue-500 bg-blue-500' : 'border-slate-300 group-hover:border-slate-400'}`}>
                    {isSelected && <div className="w-2 h-2 bg-white rounded-full"></div>}
                  </div>
                  <span className={`text-lg font-medium ${isSelected ? 'text-blue-900' : 'text-slate-700'}`}>
                    {opt}
                  </span>
                </div>
              );
            })}
          </div>

          <div className="flex justify-between items-center pt-8 border-t border-slate-100">
            <button 
              disabled={currentQ === 0}
              onClick={() => setCurrentQ(prev => prev - 1)}
              className="px-6 py-3 text-slate-400 font-bold disabled:opacity-0 hover:text-slate-800 transition-all"
            >
              ← Previous
            </button>
            
            {currentQ === quizData.length - 1 ? (
              <button 
                disabled={answers[currentQ] === undefined}
                onClick={() => setShowResults(true)}
                className="px-10 py-4 bg-slate-900 text-white rounded-2xl font-bold disabled:opacity-50 hover:bg-blue-600 shadow-xl transition-all"
              >
                Reveal Results
              </button>
            ) : (
              <button 
                disabled={answers[currentQ] === undefined}
                onClick={() => setCurrentQ(prev => prev + 1)}
                className="px-10 py-4 bg-blue-600 text-white rounded-2xl font-bold disabled:opacity-50 hover:bg-blue-700 shadow-xl shadow-blue-500/30 transition-all"
              >
                Next Question →
              </button>
            )}
          </div>
        </div>
      </div>
    );
  };

  // --- MAIN RENDER BLOCK ---
  return (
    <div className="min-h-screen bg-[#F8FAFC] selection:bg-blue-200 font-sans pb-24">
      {/* Sleek Floating Navbar */}
      <nav className="sticky top-0 z-50 backdrop-blur-xl bg-white/70 border-b border-slate-200/50">
        <div className="max-w-6xl mx-auto px-6 py-4 flex justify-between items-center">
          <div className="flex items-center gap-2 cursor-pointer" onClick={() => setView('courses')}>
            <div className="w-8 h-8 bg-gradient-to-br from-blue-600 to-indigo-600 rounded-lg flex items-center justify-center shadow-sm">
              <div className="w-3 h-3 bg-white rounded-full"></div>
            </div>
            <h1 className="text-2xl font-black tracking-tight text-slate-900">EduStream<span className="text-blue-600">AI</span></h1>
          </div>
          <div className="flex items-center gap-3 bg-white px-3 py-1.5 rounded-full border border-slate-200 shadow-sm cursor-pointer hover:shadow-md transition-shadow">
            <div className="w-7 h-7 bg-indigo-100 text-indigo-700 rounded-full flex items-center justify-center font-bold text-sm">S</div>
            <span className="text-sm font-bold text-slate-700 pr-2">Shashwat</span>
          </div>
        </div>
      </nav>

      <main className="max-w-6xl mx-auto px-6">
        {view === 'courses' && <CourseLanding />}
        {view === 'topics' && <TopicList />}
        {view === 'quiz' && <KnowledgeCheck />}
      </main>
    </div>
  );
}