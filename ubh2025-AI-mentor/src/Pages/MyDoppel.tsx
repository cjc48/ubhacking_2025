import React from 'react';
import { TextField, Box, Typography, Grid } from '@mui/material';

const backgroundPrompt = `- Education:
  - Degrees, institutions, and years of graduation.

- Work Experience:
  - Job titles, companies, and key responsibilities.

- Projects:
  - Personal or professional projects, with brief descriptions.

- Research Fields:
  - Areas of academic or professional research.

- Skills and Expertise:
  - Programming languages, technologies, and other relevant skills.
`;


function MyDoppel() {
    const [transcript, setTranscript] = React.useState('');
    const [background, setBackground] = React.useState(backgroundPrompt);
    const [rules, setRules] = React.useState('');


    const handleTranscriptChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setTranscript(event.target.value);
    };

    const handleBackgroundChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setBackground(event.target.value);
    };

    const handleRulesChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setRules(event.target.value);
    };

    return (
        <Box sx={{ p: 3 }}>
            <Typography variant="h4" gutterBottom>
                My Doppel
            </Typography>
            <Typography variant="h6" gutterBottom>
                Transcripts
            </Typography>
            <Typography variant="body1" paragraph>
                Paste your transcripts so we can get a feel for your mentoring style.
            <TextField
                label="Paste Transcript"
                multiline
                rows={15}
                fullWidth
                variant="outlined"
                value={transcript}
                onChange={handleTranscriptChange}
                placeholder="Paste your conversation transcripts here..."
                sx={{
                    '& .MuiOutlinedInput-root': {
                        height: 'auto',
                    },
                }}
            />
            </Typography>
            <Typography variant="h6" gutterBottom>
                User Background
            </Typography>
            <>
            <Typography variant="body1" paragraph>
                Please provide your field-oriented background here. Include details such as those listed below.
            </Typography></>
            <TextField
                label="Background Information"
                multiline
                rows={15}
                fullWidth
                variant="outlined"
                value={background}
                onChange={handleBackgroundChange}
                sx={{
                    '& .MuiOutlinedInput-root': {
                        height: 'auto',
                        width: '100%',
                    },
                }}
            />
            <Typography variant="h6" gutterBottom>
                Rules
            </Typography>
            <TextField
                label="LLM Rules"
                multiline
                rows={8}
                fullWidth
                variant="outlined"
                value={rules}
                onChange={handleRulesChange}
                placeholder="Enter any rules the LLM should follow..."
                sx={{
                    '& .MuiOutlinedInput-root': {
                        height: 'auto',
                    },
                }}
            />

        </Box>
    );
}

export default MyDoppel;
