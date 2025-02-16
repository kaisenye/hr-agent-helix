import api from '../config/api';
import { ChatRequest, ChatResponse, SequenceResponse, SaveSequenceRequest } from '../types/types';

export const chatApi = {
  sendMessage: async (data: ChatRequest): Promise<ChatResponse> => {
    const response = await api.post<ChatResponse>('/chat', data);
    return response.data;     
  },

  getSequence: async (userId: string): Promise<SequenceResponse> => {
    const response = await api.get<SequenceResponse>(`/sequence`, {
      params: { user_id: userId }
    });
    return response.data;
  },

  saveSequence: async (data: SaveSequenceRequest): Promise<SequenceResponse> => {
    const response = await api.post<SequenceResponse>('/sequence', data);
    return response.data;
  }
};