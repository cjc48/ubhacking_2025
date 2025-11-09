import './App.css';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import { Route, Routes, Navigate } from "react-router-dom";
import Settings from "./Pages/Settings.tsx";
import MyDoppel from "./Pages/MyDoppel.tsx";
import ChatPage from './Pages/ChatPage.tsx';
import Root from "./Root.tsx";

const theme = createTheme({
    palette: {
        primary: {
            main: '#1976d2',
        },
        secondary: {
            main: '#dc004e',
        },
    },
});

function App() {
    return (
        <ThemeProvider theme={theme}>
            <CssBaseline />
            <Routes>
                <Route path="/" element={<Root />}>
                    {/* 1. Update the redirect to point to the new default mentor route */}
                    <Route index element={<Navigate to="/mydoppel" replace />} />
                    <Route path="settings" element={<Settings />} />
                    <Route path="mydoppel" element={<MyDoppel />} />
                    {/* 2. Create a new 'mentor' path that contains the dynamic chat page */}
                    <Route path="mentor">
                        <Route path=":mentorId" element={<ChatPage />} />
                    </Route>
                </Route>
            </Routes>
        </ThemeProvider>
    );
}

export default App;