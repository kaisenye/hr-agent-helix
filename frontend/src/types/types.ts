export interface ChatMessage {
  role: 'user' | 'assistant';
  content: string;
}

export interface ChatResponse {
  response: string;
  history: Array<{
    role: string;
    content: string;
  }>;
}

export interface SequenceResponse {
  sequence: string;
}

export interface SaveSequenceRequest {
  user_id: string;
  sequence: string;
}

export interface ChatRequest {
  message: string;
  history: ChatMessage[];
}
