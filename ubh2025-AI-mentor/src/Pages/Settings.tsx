import { Typography, Paper } from '@mui/material';

export default function Settings() {
    return (
        <Paper sx={{ m: 4, p: 4, backgroundColor: '#282c34' }}>
            <Typography variant="h4" color="white">Settings</Typography>
            <Typography color="white">
                Manage your application settings here.
            </Typography>
        </Paper>
    );
}
