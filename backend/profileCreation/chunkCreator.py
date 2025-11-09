from aiDelegate import run_helper

def createTranscriptChunks(transcripts):
    allChunks = []

    for transcript in transcripts:
        prompt = (
            f"Divide the following text into smaller chunks based on complete thoughts or topic changes. "
            f"Each chunk should capture one clear idea and stay under 250 words. "
            f"Return the chunks as plain text separated by a line break.\n\n"
            f"Text:\n{transcript}"
        )

        response = run_helper(prompt)
        splitChunks = [c.strip() for c in response.split("\n") if c.strip()]
        allChunks.extend(splitChunks)

    return allChunks


def cleanChunks(chunks):
    cleaned = []
    for chunk in chunks:
        chunk = chunk.replace("\n", " ").strip()
        chunk = " ".join(chunk.split())  
        cleaned.append(chunk)
    return cleaned
