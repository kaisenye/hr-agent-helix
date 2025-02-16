import { useState } from "react";
import "./App.css";
import ChatBar from './components/ChatBar';
import { ChatMessage } from './types/types';
import { chatApi } from './services/api';

const fakeSequence = [
  "Hi {{first_name}}! - I've been keeping up with the news in LA. I hope you and your family are safe. Let us know if we can help in any way.",
  "I work at Trajillo Tech - we release a new government aid program for homeowners affected by the wildfires. Up to $2mil in aid. Let me know if you'd like to learn more.",
  "Also.. it's a fully government-supported program. No cost or burden to you whatsoever. Let me know!"
];

const App = () => {
  const [chatHistory, setChatHistory] = useState<ChatMessage[]>([{
    role: "assistant",
    content: "Hello! I'm here to help you with the sequence. How can I assist you today?"
  }]);
  const [loading, setLoading] = useState(false);

  const handleSendMessage = async (message: string) => {
    // Add user message to chat
    setChatHistory(prev => [...prev, {  
      role: "user", 
      content: message, 
    }]);

    setLoading(true);
    
    try {
      const data = await chatApi.sendMessage({
        message: message,
        history: chatHistory.map(msg => ({
          role: msg.role,
          content: msg.content
        }))
      });

      setChatHistory(prev => [...prev, {
        role: "assistant",
        content: data.response,
      }]);
    } catch (error) {
      console.error("Error:", error);
      setChatHistory(prev => [...prev, {
        role: "assistant",
        content: "Sorry, I encountered an error. Please try again.",
      }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      <ChatBar 
        chatHistory={chatHistory}
        loading={loading}
        onSendMessage={handleSendMessage}
      />
      
      {/* Workspace */}
      <div className="workspace">
        <h2>Workspace</h2>
        <div className="sequence-box">
          {fakeSequence.length > 0 ? (
            fakeSequence.map((step, index) => (
              <div key={index} className="sequence-step">
                Step {index + 1}: {step}
              </div>
            ))
          ) : (
            <p>No sequence generated.</p>
          )}
        </div>
      </div>
    </div>
  );
};

export default App;
