import { useState, useEffect } from 'react';
import axios from 'axios';

export default function App() {
  const [view, setView] = useState('courses'); // 'courses', 'topics', or 'quiz'
  const [modules, setModules] = useState([]);
  const [selectedCourse, setSelectedCourse] = useState(null);
  const [selectedTopic, setSelectedTopic] = useState(null);
  const [completedTopics, setCompletedTopics] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/api/modules')
      .then(res => setModules(res.data.data));
  }, []);

  // --- VIEW 1: COURSE SELECTION (Your 1st Image) ---
  const CourseLanding = () => {
    const uniqueCourses = [...new Set(modules.map(m => m.course))];
    return (
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-10">
        {uniqueCourses.map(courseName => (
          <div 
            key={courseName}
            onClick={() => { setSelectedCourse(courseName); setView('topics'); }}
            className="h-48 border-4 border-blue-500 rounded-xl flex items-center justify-center text-3xl font-bold text-blue-600 cursor-pointer hover:bg-blue-50 transition-all"
          >
            {courseName}
          </div>
        ))}
      </div>
    );
  };

  // --- VIEW 2: TOPIC SELECTION (Your 2nd Image) ---
  const TopicList = () => {
    const filteredTopics = modules.filter(m => m.course === selectedCourse);
    return (
      <div className="mt-10">
        <button onClick={() => setView('courses')} className="mb-4 text-blue-600 font-bold">← Back to Courses</button>
        <h2 className="text-4xl font-bold mb-8">{selectedCourse} Modules</h2>
        <div className="flex flex-wrap gap-4">
          {filteredTopics.map(topic => (
            <div 
              key={topic.topic_id}
              onClick={() => { setSelectedTopic(topic); setView('quiz'); }}
              className="p-8 border-2 border-slate-800 rounded-lg min-w-[200px] text-center cursor-pointer hover:shadow-xl transition-all"
            >
              <h3 className="text-xl font-bold">{topic.name}</h3>
              <p className="text-xs text-slate-500 mt-2">Prereqs: {topic.prerequisites.length || 'None'}</p>
            </div>
          ))}
        </div>
      </div>
    );
  };

  // --- VIEW 3: KNOWLEDGE CHECK (The Logic Gateway) ---
  const KnowledgeCheck = () => (
    <div className="max-w-2xl mx-auto mt-20 p-10 bg-white shadow-2xl rounded-3xl border-2 border-slate-100">
      <h2 className="text-2xl font-bold mb-4">Knowledge Check: {selectedTopic.name}</h2>
      <p className="text-slate-600 mb-8">Before we start, let's see what you already know about this topic.</p>
      
      {/* This is where we will build the MCQ component next */}
      <div className="space-y-4">
        <div className="p-4 border rounded-lg hover:bg-slate-50 cursor-pointer">Question 1: Sample Placeholder?</div>
        <button 
          onClick={() => setView('topics')}
          className="w-full py-4 bg-slate-900 text-white rounded-xl font-bold"
        >
          Submit Answers
        </button>
      </div>
    </div>
  );

  return (
    <div className="min-h-screen bg-slate-50 p-8">
      <nav className="flex justify-between items-center mb-10">
        <h1 className="text-2xl font-black italic text-blue-600">EduStreamAI</h1>
        <div className="px-4 py-2 bg-white rounded-full shadow-sm text-sm font-bold">User: Shashwat</div>
      </nav>

      {view === 'courses' && <CourseLanding />}
      {view === 'topics' && <TopicList />}
      {view === 'quiz' && <KnowledgeCheck />}
    </div>
  );
}