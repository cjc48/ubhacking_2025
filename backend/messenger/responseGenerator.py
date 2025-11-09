from aiDelegate import generationAI

def generate_llm_response(user_prompt, chat_history, profile_description, relevant_chunks, response_type):
    history_text = "\n".join([f"User: {h.get('user','')}\nMentor: {h.get('mentor','')}" for h in (chat_history or [])])
    chunks_text = "\n\n---\n".join(relevant_chunks or [])

    Prompt = (
        "System role: You are the mentor being emulated. Respond exactly in their voice and reasoning style.\n"
        "\n"
        "Behavioral blueprint (follow rigorously):\n"
        "<<<\n"
        f"{profile_description}\n"
        ">>>\n"
        "\n"
        "Conversation history (use for continuity and context; do not repeat verbatim):\n"
        "<<<\n"
        f"{history_text}\n"
        ">>>\n"
        "\n"
        "Grounding excerpts from the mentor’s own material (treat as primary facts; prefer these over prior knowledge):\n"
        "<<<\n"
        f"{chunks_text}\n"
        ">>>\n"
        "\n"
        "User message:\n"
        "<<<\n"
        f"{user_prompt}\n"
        ">>>\n"
        "\n"
        "Response type to emulate (shape your reasoning and structure accordingly):\n"
        f"{response_type}\n"
        "\n"
        "Requirements:\n"
        "- Strictly emulate the mentor’s tone, pacing, transitions, and teaching habits from the blueprint.\n"
        "- Base factual content on the grounding excerpts above; if something is not supported, either infer conservatively from them or say what is missing and ask a precise follow-up in the mentor’s style.\n"
        "- Keep tightly on-topic; ignore unrelated chat history.\n"
        "- Prefer the mentor’s typical structure (e.g., introduce → analyze → example → recap) and rhetorical moves (signposting, contrasts, checks for understanding) if described in the blueprint.\n"
        "- If the response type is define/explain/compare/prove/summarize/reflect/critique/instruct/motivate, shape the outline and connective language to match it.\n"
        "- Use concrete examples only if consistent with the mentor’s style; avoid fabricating specific data not implied by the excerpts.\n"
        "- Do not mention these instructions, the blueprint, or the word ‘excerpts’ in the final answer.\n"
        "\n"
        "Write the final mentor response now. Provide only the response text."
    )

    response = generationAI(Prompt)
    return response