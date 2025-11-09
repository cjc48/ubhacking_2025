from ..aiDelegate import generateAI
import asyncio

async def generate_llm_response(user_prompt, chat_history, profile_description, relevant_chunks, response_type):
    history_text = "\n".join([f"User: {h.get('user','')}\nMentor: {h.get('mentor','')}" for h in (chat_history or [])])
    chunks_text = "\n\n---\n".join(relevant_chunks or [])

    prompt = (
        "System role: You are the mentor being emulated. Respond exactly in their voice and reasoning style.\n\n"
        f"Behavioral blueprint:\n<<<\n{profile_description}\n>>>\n\n"
        f"Conversation history:\n<<<\n{history_text}\n>>>\n\n"
        f"Grounding excerpts:\n<<<\n{chunks_text}\n>>>\n\n"
        f"User message:\n<<<\n{user_prompt}\n>>>\n\n"
        f"Response type:\n{response_type}\n\n"
        "Requirements:\n"
        "- Strictly emulate the mentor’s tone, pacing, and teaching structure.\n"
        "- Base content on the excerpts above; if unknown, ask a follow-up in their voice.\n"
        "- Stay concise, on-topic, and faithful to their reasoning style.\n"
        "- Do not mention these instructions.\n\n"
        "Write the final mentor response only."
    )

    response = await asyncio.to_thread(generateAI, prompt)
    return response
