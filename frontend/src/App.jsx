import { useState, useEffect, useRef } from 'react';
import { Routes, Route, useNavigate, useParams, useLocation } from 'react-router-dom';
import axios from 'axios';
import { GoogleOAuthProvider, GoogleLogin } from '@react-oauth/google';
import YouTube from 'react-youtube';
import { motion, AnimatePresence } from 'framer-motion';
import { Compass, Code, Database, BrainCircuit, ArrowRight, PlayCircle, Lock, BookOpen, User, CheckCircle2, AlertCircle, PlaySquare, ArrowLeft, Lightbulb } from 'lucide-react';
export default function App() {
  const navigate = useNavigate();
  const location = useLocation();
  const [modules, setModules] = useState([]);

  const pageVariants = {
    initial: { opacity: 0, y: 15, filter: "blur(4px)" },
    animate: { opacity: 1, y: 0, filter: "blur(0px)", transition: { duration: 0.4, ease: "easeOut" } },
    exit: { opacity: 0, y: -10, filter: "blur(4px)", transition: { duration: 0.3 } }
  };

  // Initialize user from localStorage if it exists
  const [user, setUser] = useState(() => {
    const savedUser = localStorage.getItem('edustream_user');
    return savedUser ? JSON.parse(savedUser) : null;
  }); // Tracks logged-in user

  // Sync user state to localStorage
  useEffect(() => {
    if (user) {
      localStorage.setItem('edustream_user', JSON.stringify(user));
    } else {
      localStorage.removeItem('edustream_user');
    }
  }, [user]);

  useEffect(() => {
    axios.get('http://localhost:5000/api/modules')
      .then(res => setModules(res.data.data));
  }, []);

  const handleGoogleSuccess = async (credentialResponse) => {
    try {
      // Send the secure Google token to our Flask backend
      const res = await axios.post('http://localhost:5000/api/auth/google', {
        token: credentialResponse.credential
      });

      // Save the user data returned from MongoDB into React State
      const userData = { ...res.data.user, token: credentialResponse.credential };
      setUser(userData);
      console.log("Logged in successfully!", userData);
    } catch (error) {
      console.error("Login Failed on backend", error);
    }
  };

  const CourseLanding = () => {
    const navigate = useNavigate();
    const uniqueCourses = [...new Set(modules.map(m => m.course))];

    const getIcon = (name) => {
      if (name.includes("Programming")) return <Code className="w-6 h-6 text-white opacity-90" />;
      if (name.includes("Data")) return <Database className="w-6 h-6 text-white opacity-90" />;
      if (name.includes("AI") || name.includes("Artificial")) return <BrainCircuit className="w-6 h-6 text-white opacity-90" />;
      return <Compass className="w-6 h-6 text-white opacity-90" />;
    };

    const getAccent = (index) => {
      const accents = [
        'from-sky-400 to-indigo-500',
        'from-emerald-400 to-teal-500',
        'from-violet-400 to-purple-500',
        'from-orange-400 to-rose-500',
      ];
      return accents[index % accents.length];
    };

    return (
      <motion.div variants={pageVariants} initial="initial" animate="animate" exit="exit" className="mt-8 max-w-6xl mx-auto px-6">
        <div className="text-center mb-16">
          <h2 className="text-5xl font-extrabold text-slate-800 tracking-tight mb-4">
            Master your potential.
          </h2>
          <p className="text-lg text-slate-500 font-medium max-w-2xl mx-auto">Select a foundational path below to begin your intelligent learning journey.</p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {uniqueCourses.map((courseName, index) => (
            <div
              key={courseName}
              onClick={() => navigate(`/course/${encodeURIComponent(courseName)}`)}
              className="bg-white rounded-[1.5rem] border border-slate-200 shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 cursor-pointer overflow-hidden flex flex-col h-72 group"
            >
              {/* Top Half: Image placeholder gradient */}
              <div className={`h-1/2 w-full bg-gradient-to-br ${getAccent(index)} p-5 flex justify-end items-start relative overflow-hidden`}>
                 <div className="absolute -left-10 -bottom-10 w-40 h-40 bg-white opacity-10 rounded-full blur-2xl group-hover:scale-150 transition-transform duration-700"></div>
                 <div className="bg-white/20 backdrop-blur-md p-2 rounded-xl shadow-inner">
                   {getIcon(courseName)}
                 </div>
              </div>
              {/* Bottom Half: Content */}
              <div className="h-1/2 p-6 flex flex-col justify-between bg-white z-10">
                 <div>
                   <h3 className="text-xl font-bold text-slate-800">{courseName}</h3>
                   <p className="text-xs text-slate-500 mt-1 line-clamp-1">Master foundational concepts and theory</p>
                 </div>
                 <div className="bg-slate-100 hover:bg-slate-200 text-slate-600 text-xs font-bold py-2 px-4 rounded-full w-fit flex items-center transition-colors">
                   Explore <ArrowRight className="w-3 h-3 ml-2" />
                 </div>
              </div>
            </div>
          ))}
        </div>
      </motion.div>
    );
  };

  // --- VIEW 2: TOPIC SELECTION ---
  const TopicList = () => {
    const navigate = useNavigate();
    const { courseId } = useParams();
    const selectedCourse = decodeURIComponent(courseId);
    const filteredTopics = modules.filter(m => m.course === selectedCourse);

    const getPrereqNames = (prereqIds) => {
      if (!prereqIds || prereqIds.length === 0) return "None";
      return prereqIds.map(id => {
        const found = modules.find(m => m.skills?.includes(id));
        return found ? found.name : id;
      }).join(", ");
    };

    const getAccent = (name) => {
      if (name.includes("Programming")) return 'bg-gradient-to-r from-sky-400 to-indigo-500';
      if (name.includes("Data")) return 'bg-gradient-to-r from-emerald-400 to-teal-500';
      if (name.includes("AI") || name.includes("Artificial")) return 'bg-gradient-to-r from-violet-400 to-purple-500';
      return 'bg-gradient-to-r from-orange-400 to-rose-500';
    };

    return (
      <motion.div variants={pageVariants} initial="initial" animate="animate" exit="exit" className="w-full">
        {/* Full-width Header */}
        <div className={`w-full ${getAccent(selectedCourse)} py-16 px-6 text-white shadow-md relative overflow-hidden`}>
          <div className="max-w-4xl mx-auto relative z-10 flex flex-col md:flex-row items-center justify-between">
            <div>
              <button
                onClick={() => navigate('/')}
                className="mb-6 flex items-center text-sm font-semibold text-white hover:opacity-80 transition-all bg-white/20 backdrop-blur-md px-4 py-2 rounded-full w-fit hover:bg-white/30"
              >
                <ArrowLeft className="w-4 h-4 mr-2" /> Back to Paths
              </button>
              <h2 className="text-5xl font-black tracking-tight">{selectedCourse}</h2>
              <p className="text-white/90 mt-3 text-lg font-medium">Explore foundational concepts and Interactive lessons</p>
            </div>
            <div className="hidden md:block opacity-80">
              <BookOpen className="w-24 h-24 text-white" />
            </div>
          </div>
        </div>

        {/* List Content */}
        <div className="max-w-4xl mx-auto mt-12 px-6 pb-20">
          <div className="mb-6 flex flex-col">
            <h3 className="text-xl font-bold text-slate-800 flex items-center gap-2">
              <BookOpen className="w-5 h-5 text-slate-500" /> Select a Subtopic
            </h3>
            <p className="text-sm text-slate-500 mt-1 pl-7">Choose a subtopic to test your knowledge before proceeding to the video lesson.</p>
          </div>

          <div className="flex flex-col gap-4 pl-7">
            {filteredTopics.map((topic, idx) => {
              const isCompleted = user?.completed_topics?.includes(topic.topic_id);
              return (
                <div
                  key={topic.topic_id}
                  onClick={() => navigate(`/topic/${topic.topic_id}`)}
                  className="bg-white rounded-[1.25rem] p-6 border border-slate-200 shadow-sm hover:shadow-md transition-all duration-200 cursor-pointer flex justify-between items-center group"
                >
                  <div className="flex-1 pr-6">
                    <h4 className="text-[1.35rem] font-bold text-blue-600 mb-1">{topic.name}</h4>
                    <p className="text-[0.9rem] text-slate-500 line-clamp-1">{topic.learning_objective}</p>
                    <div className="flex items-center gap-4 mt-4">
                      {isCompleted ? (
                        <span className="text-xs font-bold text-emerald-600 bg-emerald-50 px-2 py-1 rounded flex items-center">
                          <CheckCircle2 className="w-3 h-3 mr-1" /> Completed
                        </span>
                      ) : (
                        <span className="text-xs font-semibold text-slate-400 bg-slate-50 px-2 py-1 rounded uppercase">
                          {topic.difficulty}
                        </span>
                      )}
                      {getPrereqNames(topic.prerequisites) !== "None" && (
                        <span className="text-xs text-amber-600 font-medium bg-amber-50 px-2 py-1 rounded flex items-center">
                          <AlertCircle className="w-3 h-3 mr-1" /> Req: {getPrereqNames(topic.prerequisites)}
                        </span>
                      )}
                    </div>
                  </div>
                  <div className="w-10 h-10 rounded-full bg-blue-50/50 flex items-center justify-center border border-blue-100 group-hover:bg-blue-100 group-hover:border-blue-200 transition-colors">
                    <ArrowRight className="w-4 h-4 text-blue-600" />
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </motion.div>
    );
  };

  // --- VIEW 3: KNOWLEDGE CHECK ---
  const KnowledgeCheck = () => {
    const navigate = useNavigate();
    const { topicId } = useParams();
    const selectedTopic = modules.find(m => m.topic_id === topicId);

    const [currentQ, setCurrentQ] = useState(0);
    const [answers, setAnswers] = useState({});
    const [showResults, setShowResults] = useState(false);
    const [showVideo, setShowVideo] = useState(false);
    const [useFallback, setUseFallback] = useState(false);
    const [dismissStruggling, setDismissStruggling] = useState(false);
    const [showStruggleNudge, setShowStruggleNudge] = useState(false);

    const [pauseCount, setPauseCount] = useState(0);
    const [rewindCount, setRewindCount] = useState(0);
    const playheadTimeRef = useRef(0);
    const videoPlayerRef = useRef(null);

    const MAX_PAUSES = 3;
    const MAX_REWINDS = 5;

    useEffect(() => {
      setCurrentQ(0);
      setAnswers({});
      setShowResults(false);
      setShowVideo(false);
      setUseFallback(false);
      setDismissStruggling(false);
      setShowStruggleNudge(false);
      setPauseCount(0);
      setRewindCount(0);
      playheadTimeRef.current = 0;
      videoPlayerRef.current = null;
    }, [topicId]);

    // Threshold Check
    useEffect(() => {
      if (pauseCount >= MAX_PAUSES || rewindCount >= MAX_REWINDS) {
        setShowStruggleNudge(true);
      }
    }, [pauseCount, rewindCount]);

    // Polling for rewinds
    useEffect(() => {
      let interval;
      if ((showVideo || selectedTopic?.quiz?.length === 0) && !useFallback && !dismissStruggling && selectedTopic?.fallback_video_url) {
        interval = setInterval(async () => {
          if (videoPlayerRef.current) {
             const currentTime = await videoPlayerRef.current.getCurrentTime();
             if (playheadTimeRef.current - currentTime > 3) {
                // Time went backward by more than 3 sec
                setRewindCount(prev => prev + 1);
             }
             playheadTimeRef.current = currentTime;
          }
        }, 1000);
      }
      return () => clearInterval(interval);
    }, [showVideo, useFallback, dismissStruggling, selectedTopic]);

    if (modules.length === 0) return <div className="text-center mt-20 text-slate-500 font-bold">Loading modules...</div>;
    if (!selectedTopic) return <div className="text-center mt-20 text-slate-500 font-bold">Topic not found</div>;

    const quizData = selectedTopic.quiz || [];

    const handleOptionSelect = (qIndex, optIndex) => {
      setAnswers({ ...answers, [qIndex]: optIndex });
    };

    const getVideoId = (url) => {
      if (!url) return '';
      const videoIdMatch = url.match(/(?:\?v=|\/embed\/|\.be\/)([^&\n?#]+)/);
      if (videoIdMatch && videoIdMatch[1]) {
        return videoIdMatch[1];
      }
      return url;
    };

    const handleVideoReady = (e) => {
      videoPlayerRef.current = e.target;
    };

    const handleVideoStateChange = (e) => {
      if (e.data === 2) { // 2 = PAUSED
         setPauseCount(prev => prev + 1);
      }
    };

    const markComplete = async () => {
      if (!user || !user.token) return;
      try {
        const res = await axios.post('http://localhost:5000/api/progress', {
          token: user.token,
          topic_id: selectedTopic.topic_id
        });
        setUser({ ...res.data.user, token: user.token });
        navigate(`/course/${encodeURIComponent(selectedTopic.course)}`);
      } catch (err) {
        console.error("Failed to mark complete:", err);
      }
    };

    const renderVideoSection = () => {
      const activeVideoUrl = useFallback ? selectedTopic.fallback_video_url : selectedTopic.primary_video_url;
      const ytVideoId = getVideoId(activeVideoUrl);

      return (
        <div className="max-w-4xl mx-auto mt-10 p-8 bg-white shadow-2xl shadow-blue-900/5 rounded-[2.5rem] border border-slate-100 animate-in zoom-in-95 duration-500">
          <div className="flex justify-between items-center mb-6">
            <h2 className="text-3xl font-black text-slate-900">{selectedTopic.name} Lesson</h2>
            <button onClick={() => navigate(`/course/${encodeURIComponent(selectedTopic.course)}`)} className="px-4 py-2 text-slate-400 font-bold hover:text-slate-800 transition-colors">
              ✕ Close
            </button>
          </div>

          <div className="relative aspect-video rounded-2xl overflow-hidden bg-slate-900 shadow-inner mb-8 group/video">
            <YouTube 
              videoId={ytVideoId} 
              opts={{ width: '100%', height: '100%', playerVars: { autoplay: 1 } }}
              onReady={handleVideoReady}
              onStateChange={handleVideoStateChange}
              className="absolute inset-0 w-full h-full"
            />

            {showStruggleNudge && !useFallback && !dismissStruggling && selectedTopic.fallback_video_url && (
              <div className="absolute bottom-4 right-4 w-80 backdrop-blur-xl bg-white/95 p-4 rounded-2xl shadow-2xl border border-slate-200 flex flex-col gap-2 animate-in slide-in-from-bottom-4 duration-500 z-10">
                <div className="flex justify-between items-start">
                  <span className="text-sm font-bold text-slate-800 flex items-center gap-2">
                    <span className="text-xl">💡</span> Struggling a bit?
                  </span>
                  <button onClick={() => setDismissStruggling(true)} className="text-slate-400 hover:text-slate-600 transition-colors">✕</button>
                </div>
                <p className="text-xs text-slate-500 font-medium leading-relaxed">We have an alternative explanation with a different teaching style available for this topic.</p>
                <button
                  onClick={() => setUseFallback(true)}
                  className="mt-1 w-full py-2.5 bg-gradient-to-r from-blue-500 to-indigo-600 text-white font-bold rounded-xl shadow-lg shadow-blue-500/30 hover:shadow-blue-500/50 hover:opacity-90 transition-all text-xs"
                >
                  Try Alternative Video
                </button>
              </div>
            )}
          </div>

          <div className="flex justify-between items-center bg-slate-50 p-6 rounded-2xl border border-slate-100">
            <div>
              <h4 className="font-bold text-slate-800">Done watching?</h4>
              <p className="text-xs text-slate-500 font-medium mt-1">Mark this module as complete to update your tracked progress.</p>
            </div>
            {user ? (
              <button
                onClick={markComplete}
                className="px-6 py-3 bg-emerald-500 text-white font-bold rounded-xl hover:bg-emerald-600 transition-all hover:scale-105 active:scale-95 shadow-lg shadow-emerald-500/20"
              >
                Mark Complete →
              </button>
            ) : (
              <div className="text-xs font-bold text-slate-400 bg-white px-4 py-2 rounded-lg border border-slate-200">
                Log in to save progress
              </div>
            )}
          </div>
        </div>
      );
    };

    if (showVideo || quizData.length === 0) {
      return renderVideoSection();
    }

    if (showResults) {
      let correctCount = 0;
      quizData.forEach((q, index) => {
        if (answers[index] === q.correct_index) correctCount++;
      });
      const scorePercentage = (correctCount / quizData.length) * 100;
      const passed = scorePercentage >= 70;

      return (
        <motion.div variants={pageVariants} initial="initial" animate="animate" exit="exit" className="w-full max-w-4xl mx-auto px-6 mt-8 pb-20">
          {passed ? (
            <div className="max-w-2xl mx-auto mt-8 p-12 bg-white shadow-xl shadow-emerald-900/5 rounded-[2.5rem] border border-slate-100 text-center">
              <div className="inline-block px-5 py-2 bg-emerald-50 text-emerald-600 font-bold tracking-wide rounded-full text-base mb-6">
                Diagnostic Passed
              </div>
              <div className="text-6xl font-black mb-8 tracking-tighter text-transparent bg-clip-text bg-gradient-to-r from-emerald-400 to-teal-500">
                {scorePercentage}%
              </div>
              <h3 className="text-2xl font-black text-slate-800 mb-2">Solid Foundation!</h3>
              <p className="text-slate-500 font-medium mb-10">You have a great grasp of the prerequisites. You are perfectly ready to tackle this lesson.</p>
              
              <button
                onClick={() => setShowVideo(true)}
                className="w-full py-4 font-bold rounded-2xl transition-all text-lg bg-emerald-500 text-white hover:bg-emerald-600 shadow-lg shadow-emerald-500/20"
              >
                Start Lesson Video
              </button>
            </div>
          ) : (
            <div className="flex flex-col items-center">
               <h2 className="text-4xl font-black text-slate-900 mb-4 tracking-tight">Let's Build Your Foundation</h2>
               <p className="text-lg text-slate-500 mb-10 text-center max-w-xl">No worries! We've curated the perfect learning path to help you master these concepts.</p>
               
               <div className="w-full bg-amber-50/40 border border-orange-100/60 rounded-[2rem] p-8 md:p-10 text-left relative overflow-hidden">
                  <div className="flex items-center text-xs font-semibold text-orange-600 mb-2">
                     <span className="w-2 h-2 rounded-full bg-orange-500 mr-2"></span>
                     {selectedTopic.course}
                  </div>
                  <h3 className="text-3xl font-bold text-slate-900 mb-2">{selectedTopic.name}</h3>
                  <p className="text-slate-500 text-sm mb-12">{selectedTopic.learning_objective}</p>

                  <div className="flex items-center gap-2 mb-4 text-orange-800 font-bold">
                     <BookOpen className="w-5 h-5" /> Recommended Learning Path
                  </div>
                  <p className="text-slate-500 text-sm mb-8 leading-relaxed">We've selected a foundational module that covers the essential prerequisites. This will give you the knowledge you need to succeed.</p>

                  {selectedTopic.prerequisites.length > 0 && selectedTopic.prerequisites.map(prereqId => {
                      const prereqModule = modules.find(m => m.skills?.includes(prereqId));
                      if (!prereqModule) return null;
                      return (
                        <div key={prereqId} className="w-full bg-gradient-to-r from-orange-500 to-amber-500 rounded-[2rem] p-8 text-white shadow-xl shadow-orange-500/20 relative overflow-hidden group">
                           <div className="absolute -right-10 -bottom-10 w-48 h-48 bg-white/10 rounded-full blur-2xl group-hover:scale-150 transition-transform duration-700"></div>
                           <div className="flex flex-col md:flex-row gap-6 items-start md:items-center relative z-10">
                              <div className="w-16 h-16 rounded-2xl bg-white/20 backdrop-blur-sm flex items-center justify-center flex-shrink-0 border border-white/20">
                                 <PlaySquare className="w-8 h-8 text-white" />
                              </div>
                              <div className="flex-1">
                                 <h4 className="text-2xl font-bold mb-1">{prereqModule.name}</h4>
                                 <p className="text-white/90 text-sm mb-4 line-clamp-1">{prereqModule.learning_objective}</p>
                                 <div className="flex gap-2">
                                     <span className="text-[0.7rem] font-bold tracking-wide uppercase bg-white/20 px-3 py-1 rounded-full backdrop-blur-sm">Beginner Friendly</span>
                                     <span className="text-[0.7rem] font-bold tracking-wide uppercase bg-white/20 px-3 py-1 rounded-full backdrop-blur-sm">{prereqModule.difficulty}</span>
                                 </div>
                              </div>
                           </div>
                           <button onClick={() => navigate(`/topic/${prereqModule.topic_id}`)} className="mt-8 w-full bg-white text-orange-600 font-bold py-4 rounded-xl hover:bg-slate-50 transition-colors shadow-lg relative z-10 hover:scale-[1.01] active:scale-[0.99] duration-200">
                              Start Learning
                           </button>
                        </div>
                      )
                  })}
               </div>
               
               <div className="flex flex-col md:flex-row gap-4 w-full mt-6">
                  <button onClick={() => { setCurrentQ(0); setAnswers({}); setShowResults(false); }} className="flex-1 py-4 bg-white border border-slate-200 text-slate-600 rounded-xl font-bold shadow-sm hover:bg-slate-50 transition-colors flex justify-center items-center">
                     <span className="mr-2">↺</span> Retry Question
                  </button>
                  <button onClick={() => navigate(`/course/${encodeURIComponent(selectedTopic.course)}`)} className="flex-1 py-4 bg-white border border-slate-200 text-slate-600 rounded-xl font-bold shadow-sm hover:bg-slate-50 transition-colors">
                     Choose Another Topic
                  </button>
               </div>

               <button onClick={() => setShowVideo(true)} className="mt-12 text-slate-400 font-medium hover:text-slate-600 text-sm underline decoration-slate-300 underline-offset-4 transition-colors">
                  or proceed to video anyway (not recommended)
               </button>
            </div>
          )}
        </motion.div>
      );
    }

    const q = quizData[currentQ];

      return (
      <motion.div variants={pageVariants} initial="initial" animate="animate" exit="exit" className="w-full max-w-4xl mx-auto px-6 mt-8 pb-20">
        
        {/* Top Navigation */}
        <button
          onClick={() => navigate(`/course/${encodeURIComponent(selectedTopic.course)}`)}
          className="mb-8 flex items-center text-sm font-bold text-slate-500 hover:text-slate-800 transition-colors w-fit"
        >
          <ArrowLeft className="w-4 h-4 mr-2" /> Back to Subtopics
        </button>

        <div className="bg-white shadow-xl shadow-slate-200/50 rounded-[2rem] border border-slate-100 overflow-hidden">
          <div className="p-10 md:p-14">
            
            {/* Breadcrumb Header */}
            <div className="flex items-center text-xs font-semibold text-slate-400 mb-2">
               <span className="w-2 h-2 rounded-full bg-orange-500 mr-2"></span>
               {selectedTopic.course} <span className="mx-2">•</span> {selectedTopic.name}
            </div>
            <h2 className="text-3xl font-bold text-slate-800 mb-10">Knowledge Check</h2>

            {/* Question */}
            <div className="flex items-start gap-4 mb-8">
              <div className="w-10 h-10 rounded-full bg-violet-500 flex-shrink-0 flex items-center justify-center shadow-inner mt-1">
                 <Lightbulb className="w-5 h-5 text-white" />
              </div>
              <div>
                 <h3 className="text-[1.35rem] font-bold text-slate-800 leading-tight">
                   {q.question}
                 </h3>
                 <p className="text-xs text-slate-400 font-bold tracking-widest uppercase mt-3">Question {currentQ + 1} of {quizData.length}</p>
              </div>
            </div>

            {/* Options */}
            <div className="space-y-3 mb-10 pl-14">
              {q.options.map((opt, idx) => {
                const isSelected = answers[currentQ] === idx;
                return (
                  <div
                    key={idx}
                    onClick={() => handleOptionSelect(currentQ, idx)}
                    className={`p-4 rounded-xl cursor-pointer transition-all duration-200 flex items-center group
                      ${isSelected
                        ? 'border-2 border-violet-400 bg-violet-50/30'
                        : 'border border-slate-200 hover:border-slate-300 hover:bg-slate-50'}`}
                  >
                    <span className={`text-[1rem] font-medium ${isSelected ? 'text-violet-900' : 'text-slate-700'}`}>
                      {opt}
                    </span>
                  </div>
                );
              })}
            </div>

            {/* Actions */}
            <div className="pl-14 pt-6 border-t border-slate-100 flex gap-4">
              {currentQ > 0 && (
                <button
                  onClick={() => setCurrentQ(prev => prev - 1)}
                  className="px-6 py-4 bg-slate-100 text-slate-600 font-bold rounded-xl hover:bg-slate-200 transition-all text-sm"
                >
                  Previous
                </button>
              )}
              {currentQ === quizData.length - 1 ? (
                <button
                  disabled={answers[currentQ] === undefined}
                  onClick={() => setShowResults(true)}
                  className="flex-1 py-4 bg-slate-200 text-slate-500 rounded-xl font-bold disabled:opacity-50 hover:bg-slate-800 hover:text-white transition-all text-sm"
                >
                  Submit Answer
                </button>
              ) : (
                <button
                  disabled={answers[currentQ] === undefined}
                  onClick={() => setCurrentQ(prev => prev + 1)}
                  className="flex-1 py-4 bg-violet-500 text-white rounded-xl font-bold disabled:opacity-50 hover:bg-violet-600 shadow-md shadow-violet-500/20 transition-all text-sm"
                >
                  Next Question
                </button>
              )}
            </div>
          </div>
        </div>
      </motion.div>
    );
  };

  // --- MAIN RENDER BLOCK ---
  return (
    <GoogleOAuthProvider clientId={import.meta.env.VITE_GOOGLE_CLIENT_ID}>
      <div className="min-h-screen bg-[#F8FAFC] selection:bg-blue-200 font-sans pb-24">
        {/* Sleek Floating Navbar */}
        <nav className="sticky top-0 z-50 backdrop-blur-xl bg-white/70 border-b border-slate-200/50">
          <div className="max-w-6xl mx-auto px-6 py-4 flex justify-between items-center">
            <div className="flex items-center gap-2 cursor-pointer"
              onClick={() => navigate('/')}>
              <div className="w-8 h-8 bg-gradient-to-br from-blue-600 to-indigo-600 rounded-lg flex items-center justify-center shadow-sm">
                <div className="w-3 h-3 bg-white rounded-full"></div>
              </div>
              <h1 className="text-2xl font-black tracking-tight text-slate-900">EduStream<span className="text-blue-600">AI</span></h1>
            </div>

            {/* AUTHENTICATION UI */}
            <div>
              {user ? (
                <div className="flex items-center gap-3 bg-white px-3 py-1.5 rounded-full border border-slate-200 shadow-sm">
                  <img src={user.picture} alt="Profile" className="w-7 h-7 rounded-full" />
                  <span className="text-sm font-bold text-slate-700 pr-2">{user.name}</span>
                  {/* Basic Logout: just clear the state */}
                  <button onClick={() => setUser(null)} className="text-xs text-slate-400 hover:text-red-500 font-bold ml-2">Logout</button>
                </div>
              ) : (
                <GoogleLogin
                  onSuccess={handleGoogleSuccess}
                  onError={() => console.log('Google Login Failed')}
                  theme="outline"
                  shape="pill"
                />
              )}
            </div>

          </div>
        </nav>

        <main className="w-full">
          <AnimatePresence mode="wait">
            <Routes location={location} key={location.pathname}>
              <Route path="/" element={<CourseLanding />} />
              <Route path="/course/:courseId" element={<TopicList />} />
              <Route path="/topic/:topicId" element={<KnowledgeCheck />} />
            </Routes>
          </AnimatePresence>
        </main>
      </div>
    </GoogleOAuthProvider>
  );
}