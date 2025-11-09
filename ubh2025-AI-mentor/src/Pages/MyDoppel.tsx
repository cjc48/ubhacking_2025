import { Typography, Paper } from '@mui/material';

export default function MyDoppel() {
    return (
        <Paper sx={{ m: 4, p: 4, backgroundColor: '#282c34' }}>
            <Typography variant="h4" color="white">My Doppel</Typography>
            <Typography color="white">
                This is where you can configure your digital doppelgänger.
            </Typography>
        </Paper>
    );
}
