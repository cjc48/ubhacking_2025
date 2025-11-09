import asyncio
from ..aiDelegate import messageStyleAI
from ..FireBase import getTranscripts

async def transform_stylistic_response(mentor_id, llm_response):
    transcripts = getTranscripts(mentor_id)
    if not transcripts:
        return llm_response

    combined_samples = "\n".join(t.get("content", "") for t in transcripts)

    prompt = (
        "You are tasked with performing an advanced stylistic immitation. "
        "You will rewrite the following AI-generated response so that it sounds EXACTLY like the person whose writing and speaking style is demonstrated below.\n\n"
        "You must precisely emulate:\n"
        "- The mentor’s rhythm, tone, and sentence flow.\n"
        "- Typical phrasing patterns, connectors, and transition words.\n"
        "- Variations in pacing: long reflective explanations vs. short decisive statements.\n"
        "- Consistency with mentor-level confidence and mannerisms (avoid general politeness).\n\n"
        "Mentor reference data (analyzed samples from their transcripts):\n"
        "<<<\n"
        f"{combined_samples[:12000]}\n"
        ">>>\n\n"
        "AI-generated response to restyle:\n"
        "<<<\n"
        f"{llm_response}\n"
        ">>>\n\n"
        "Your task:\n"
        "- Rewrite the text so that it could plausibly have been said or written by the person above.\n"
        "- You are not allowed to add or remove factual information — only adjust tone, rhythm, and expression.\n"
        "- Keep every detail semantically intact but alter *how* it’s said to perfectly match the persons voice. (if neccesary)\n"
        "- The final text should feel *authentically human*, with micro-hesitations, confidence markers, or expressive phrasing consistent with the mentor.\n"
        "- Never mention that you are restyling or referencing transcripts.\n"
        "- Do not include explanations or labels; output only the final restyled response.\n\n"
        "Produce the final rewritten response below."
    )

    response = await asyncio.to_thread(messageStyleAI, prompt)
    return response
