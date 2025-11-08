import './App.css'
import Dashboard from './Components/Dashboard'
import { createTheme, ThemeProvider } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';

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
            {/* CssBaseline kickstarts an elegant, consistent, and simple baseline to build upon. */}
            <CssBaseline />
            <Dashboard/>
        </ThemeProvider>
    )
}


export default App