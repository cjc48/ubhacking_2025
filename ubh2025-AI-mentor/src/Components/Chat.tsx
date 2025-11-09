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

interface Message {
    id: number;
    text: string;
    sender: 'user' | 'mentor';
}

interface ChatProps {
    mentor: string;
}

export default function Chat({ mentor }: ChatProps) {
    const [messages, setMessages] = useState<Message[]>([]);
    const [inputText, setInputText] = useState('');

    useEffect(() => {
        setMessages([
            { id: 1, text: `Hello! I am ${mentor}. How may I help you today?`, sender: 'mentor' },
        ]);
        setInputText('');
    }, [mentor]);

    const handleSendMessage = async () => {
        if (!inputText.trim()) return;

        const newMessage: Message = {
            id: Date.now(),
            text: inputText,
            sender: 'user',
        };
        setMessages(prev => [...prev, newMessage]);
        setInputText('');

        try {
            const res = await fetch('http://localhost:5000/handle_chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    user_message: inputText,
                    user_id: 'testUser123',
                    mentor_id: mentor,
                    history: messages.map(m => ({ text: m.text, sender: m.sender })),
                }),
            });

            const data = await res.json();

            const mentorReply: Message = {
                id: Date.now() + 1,
                text: data.reply || "I'm thinking...",
                sender: 'mentor',
            };

            setMessages(prev => [...prev, mentorReply]);
        } catch (err) {
            console.error('Error:', err);
            const errorReply: Message = {
                id: Date.now() + 2,
                text: "Sorry, I couldn't reach the server.",
                sender: 'mentor',
            };
            setMessages(prev => [...prev, errorReply]);
        }
    };

    const handleKeyPress = (e: React.KeyboardEvent) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            handleSendMessage();
        }
    };

    return (
        <Paper elevation={3} sx={{ height: '100%', display: 'flex', flexDirection: 'column' }}>
            <Box sx={{ p: 2, borderBottom: '1px solid #ddd' }}>
                <Typography variant="h6">Chat with {mentor}</Typography>
            </Box>
            <Box sx={{ flexGrow: 1, overflow: 'auto', p: 2 }}>
                <List>
                    {messages.map((m) => (
                        <ListItem
                            key={m.id}
                            sx={{ justifyContent: m.sender === 'user' ? 'flex-end' : 'flex-start' }}
                        >
                            <Box
                                sx={{
                                    bgcolor: m.sender === 'user' ? 'primary.main' : 'grey.300',
                                    color: m.sender === 'user' ? 'white' : 'black',
                                    p: '8px 12px',
                                    borderRadius: 2,
                                    maxWidth: '70%',
                                }}
                            >
                                <ListItemText primary={m.text} />
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
                <Button
                    variant="contained"
                    color="primary"
                    sx={{ ml: 2, py: 1.5 }}
                    startIcon={<Send />}
                    onClick={handleSendMessage}
                >
                    Send
                </Button>
            </Box>
        </Paper>
    );
}