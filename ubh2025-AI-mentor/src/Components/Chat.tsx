
import * as React from 'react';
import { useState, useEffect } from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemText from '@mui/material/ListItemText';
import Paper from '@mui/material/Paper';
import Typography from '@mui/material/Typography';
import Send from '@mui/icons-material/Send';

// Define the shape of a message
interface Message {
    id: number;
    text: string;
    sender: 'user' | 'mentor';
}

// Define the props for the Chat component
interface ChatProps {
    mentor: string;
}

export default function Chat({ mentor }: ChatProps) {
    const [messages, setMessages] = useState<Message[]>([]);
    const [inputText, setInputText] = useState('');

    // This useEffect hook runs whenever the `mentor` prop changes
    useEffect(() => {
        // When the mentor changes, reset the chat to its initial state.
        // This simulates loading a new chat session for the selected mentor.
        setMessages([
            { id: 1, text: `Hello! I am ${mentor}. How may I help you today?`, sender: 'mentor' },
        ]);
        // Also, clear any text from the input field
        setInputText('');
    }, [mentor]); // The dependency array ensures this effect runs only when `mentor` changes

    const handleSendMessage = () => {
        if (inputText.trim() !== '') {
            const newMessage: Message = {
                id: messages.length + 1,
                text: inputText,
                sender: 'user',
            };
            setMessages([...messages, newMessage]);
            setInputText('');

            // Simulate a reply from the mentor
            setTimeout(() => {
                const mentorReply: Message = {
                    id: messages.length + 2,
                    text: `That's a great question about ${mentor}. Let me think...`,
                    sender: 'mentor',
                };
                setMessages((prevMessages) => [...prevMessages, mentorReply]);
            }, 1000);
        }
    };

    const handleKeyPress = (event: React.KeyboardEvent) => {
        if (event.key === 'Enter' && !event.shiftKey) {
            event.preventDefault();
            handleSendMessage();
        }
    };

    return (
        <Paper elevation={3} sx={{ height: '100%', display: 'flex', flexDirection: 'column' }}>
            <Box sx={{ p: 2, borderBottom: '1px solid #ddd' }}>
                <Typography variant="h6">Chat with {mentor.replace('/', '')}</Typography>
            </Box>
            <Box sx={{ flexGrow: 1, overflow: 'auto', p: 2 }}>
                <List>
                    {messages.map((message) => (
                        <ListItem key={message.id} sx={{
                            display: 'flex',
                            justifyContent: message.sender === 'user' ? 'flex-end' : 'flex-start'
                        }}>
                            <Box
                                sx={{
                                    bgcolor: message.sender === 'user' ? 'primary.main' : 'grey.300',
                                    color: message.sender === 'user' ? 'primary.contrastText' : 'black',
                                    p: '8px 12px',
                                    borderRadius: 2,
                                    maxWidth: '70%',
                                }}
                            >
                                <ListItemText primary={message.text} />
                            </Box>
                        </ListItem>
                    ))}
                </List>
            </Box>
            <Box sx={{ p: 2, borderTop: '1px solid #ddd', display: 'flex', alignItems: 'center' }}>
                <TextField
                    fullWidth
                    variant="outlined"
                    placeholder="Type your message..."
                    value={inputText}
                    onChange={(e) => setInputText(e.target.value)}
                    onKeyPress={handleKeyPress}
                    multiline
                    maxRows={4}
                />
                <Button variant="contained" sx={{paddingTop: 2, paddingBottom: 2}} color="primary" onClick={handleSendMessage} startIcon={<Send/>}>
                    Send
                </Button>
            </Box>
        </Paper>
    );
}
