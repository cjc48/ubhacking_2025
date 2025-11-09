import React from 'react';
import { Box, Typography, TextField, Button, List, ListItem, ListItemText } from '@mui/material';

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

export default function MyDoppel() {
    const [transcriptFiles, setTranscriptFiles] = React.useState<File[]>([]);
    const [background, setBackground] = React.useState(backgroundPrompt);
    const [rules, setRules] = React.useState('');
    const [loading, setLoading] = React.useState(false);

    const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        if (event.target.files) {
            setTranscriptFiles(Array.from(event.target.files));
        }
    };

    const handleSubmit = async () => {
        if (transcriptFiles.length === 0) {
            alert('Please upload at least one transcript file.');
            return;
        }

        setLoading(true);
        const formData = new FormData();
        formData.append('mentor_id', 'ash');
        formData.append('userDescription', background);
        formData.append('userRules', rules);
        transcriptFiles.forEach(file => formData.append('userFiles', file));

        try {
            const res = await fetch('http://localhost:5000/api/create_profile', {
                method: 'POST',
                body: formData,
            });

            const data = await res.json();
            console.log('Profile created:', data);
            alert('Profile uploaded successfully!');
        } catch (err) {
            console.error('Upload failed:', err);
            alert('Upload failed. Check the console for details.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <Box sx={{ p: 3 }}>
            <Typography variant="h4" gutterBottom>My Doppel</Typography>

            <Typography variant="h6" gutterBottom>Transcripts</Typography>
            <Typography variant="body1" paragraph>
                Upload your plaintext (.txt) transcripts below.
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
                <Typography variant="subtitle1" gutterBottom>Selected Files:</Typography>
                <List>
                    {transcriptFiles.length > 0 ? (
                        transcriptFiles.map((file, i) => (
                            <ListItem key={i}>
                                <ListItemText primary={file.name} />
                            </ListItem>
                        ))
                    ) : (
                        <ListItem><ListItemText primary="No files selected." /></ListItem>
                    )}
                </List>
            </Box>

            <Typography variant="h6" gutterBottom sx={{ mt: 3 }}>User Background</Typography>
            <Typography variant="body1" paragraph>
                Provide your field-related background below.
            </Typography>
            <TextField
                label="Background Information"
                multiline
                rows={12}
                fullWidth
                value={background}
                onChange={(e) => setBackground(e.target.value)}
                variant="outlined"
            />

            <Typography variant="h6" gutterBottom sx={{ mt: 3 }}>Rules</Typography>
            <Typography variant="body1" paragraph>
                Provide any rules or guidelines the AI should follow.
            </Typography>
            <TextField
                label="Rules"
                multiline
                rows={6}
                fullWidth
                value={rules}
                onChange={(e) => setRules(e.target.value)}
                variant="outlined"
            />

            <Button
                variant="contained"
                color="primary"
                sx={{ mt: 3 }}
                onClick={handleSubmit}
                disabled={loading}
            >
                {loading ? 'Uploading...' : 'Create My Doppel'}
            </Button>
        </Box>
    );
}