import { io } from "socket.io-client";

const SOCKET_URL = "http://localhost:5000"; // Adjust if backend runs elsewhere
export const socket = io(SOCKET_URL);
