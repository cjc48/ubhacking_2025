
import asyncio
from aiDelegate import retrievalAI
from FireBase import getTranscripts

async def retrieve_required_chunks(user_id, user_prompt, response_type):
    transcripts = getTranscripts(user_id)
    if not transcripts:
        return []

    matching_chunks = []
    query_terms = set(user_prompt.lower().split() + [response_type.lower()])

    for t in transcripts:
        tags = [tag.lower() for tag in t.get("tags", [])]
        if any(tag in query_terms for tag in tags):
            matching_chunks.append(t["content"])

    if len(matching_chunks) < 3:
        combined_text = "\n".join(t["content"] for t in transcripts)
        retrieval_prompt = (
            f"From the following mentor data, extract the 3–5 most relevant excerpts "
            f"that relate to the user's message.\n\n"
            f"User message: {user_prompt}\nResponse type: {response_type}\n\n"
            f"Mentor data:\n{combined_text[:7000]}"
        )
        semantic_result = await asyncio.to_thread(retrievalAI, retrieval_prompt)
        semantic_chunks = [chunk.strip() for chunk in semantic_result.split("\n") if len(chunk.strip()) > 50]
        matching_chunks.extend(semantic_chunks)

    seen = set()
    final_chunks = []
    for c in matching_chunks:
        if c not in seen:
            seen.add(c)
            final_chunks.append(c)
    return final_chunks[:5]
