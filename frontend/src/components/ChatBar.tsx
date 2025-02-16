import { useState } from "react";
import { ChatMessage } from "../types/types";

interface ChatBarProps {
  chatHistory: ChatMessage[];
  loading: boolean;
  onSendMessage: (message: string) => void;
}

const ChatBar = ({ chatHistory, loading, onSendMessage }: ChatBarProps) => {
  const [userInput, setUserInput] = useState("");

  const handleSend = () => {
    if (!userInput.trim()) return;
    onSendMessage(userInput);
    setUserInput("");
  };

  return (
    <div className="chatbar">
      <h2>Chat</h2>
      <div className="chat-history" style={{ display: 'flex', flexDirection: 'column' }}>
        {chatHistory.map((msg, index) => (
          <div 
            key={index} 
            className={`message ${msg.role}`}
            style={{
              alignItems: msg.role === "user" ? "flex-end" : "flex-start",
              backgroundColor: msg.role === "user" ? "#524E4EFF" : "#E3E3E3FF",
              color: msg.role === "user" ? "white" : "black",
            }}
          >
            {msg.content}
          </div>
        ))}
        {loading && (
          <div className="ai-message" style={{
            alignSelf: "flex-start",
            backgroundColor: "#f0f0f0",
            color: "black",
            borderRadius: "1rem",
            margin: "0.5rem",
            fontStyle: "italic"
          }}>
            Thinking...
          </div>
        )}
      </div>
      <div className="chat-input">
        <input
          type="text"
          value={userInput}
          onChange={(e) => setUserInput(e.target.value)}
          placeholder="Type a message..."
          onKeyPress={(e) => e.key === 'Enter' && handleSend()}
        />
        <button onClick={handleSend}>Send</button>
      </div>
    </div>
  );
};

export default ChatBar;
