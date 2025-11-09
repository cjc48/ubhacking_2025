import React from 'react';
import { TextField, Box, Typography, Grid, ListItemText } from '@mui/material';
import Button from "@mui/material/Button";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";

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
    const [transcriptFiles, setTranscriptFiles] = React.useState<File[]>([]);
    const [background, setBackground] = React.useState(backgroundPrompt);
    const [rules, setRules] = React.useState('');

    const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        if (event.target.files) {
            setTranscriptFiles(Array.from(event.target.files));
        }
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
            <Box>
                <Typography variant="h6" gutterBottom>
                    Transcripts
                </Typography>
                <Typography variant="body1" paragraph>
                    Please provide field-relevant transcripts here. For now, provide only in .txt (plaintext) format.
                </Typography>
                <Button variant="contained" component="label">
                    Upload Files
                    <input
                        type="file"
                        hidden
                        multiple
                        accept="text/plain"
                        onChange={handleFileChange}
                    />
                </Button>
                <Box sx={{ mt: 2 }}>
                    <Typography variant="subtitle1" gutterBottom>
                        Selected Files:
                    </Typography>
                    <List>
                        {transcriptFiles.length > 0 ? (
                            transcriptFiles.map((file, index) => (
                                <ListItem key={index}>
                                    <ListItemText primary={file.name} />
                                </ListItem>
                            ))
                        ) : (
                            <ListItem>
                                <ListItemText primary="No files selected." />
                            </ListItem>
                        )}
                    </List>
                </Box>
            </Box>
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
            <Typography variant="body1" paragraph>
                Please provide any rules the LLM should follow here.
            </Typography>
            <TextField
                label="Rules"
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
