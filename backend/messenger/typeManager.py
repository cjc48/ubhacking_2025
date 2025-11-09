from FireBase import intent_detectionAI, response_typeAI


def identify_response_type(user_prompt):
    intent = identify_intent(user_prompt)
    prompt = f"""
    You are an AI assistant that determines the appropriate response type based on the user's intent and prompt.
    Given the intent: "{intent}" and the user prompt: "{user_prompt}", classify the response type into one of the following categories:
    (question, reflection, advice, social, off-topic)
    """
    response = response_typeAI(f"Intent: {intent}\nUser Prompt: {user_prompt}")
    return response



def identify_intent(user_prompt):
    prompt = f"""
    You are an AI assistant that identifies the intent behind user prompts.
    Classify the intent into one of the following categories:
    1. Information Request
    2. Task Execution
    3. Casual Conversation
    4. Feedback/Complaint
    5. Other

    User Prompt: "{user_prompt}"

    Provide only the category name as the output.
    """
    response = intent_detectionAI(prompt)
    return response.strip()