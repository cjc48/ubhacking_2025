import asyncio
from flask import Flask, jsonify, request
from backend.messenger.typeManager import identify_response_type
from .retriever import retrieve_required_chunks
from .responseGenerator import generate_llm_response
from .stylizer import transform_stylistic_response
from ..FireBase import getProfile

app = Flask(__name__)

async def handle_chat(user_prompt, user_id, chat_history, mentor_id):
    user_profile = getProfile(mentor_id)
    if not user_prompt or not user_id:
        return {"error": "Missing prompt or userId"}

    response_type = identify_response_type(user_prompt)

    relevant_chunks = await retrieve_required_chunks(mentor_id, user_prompt, response_type)

    llm_response = await generate_llm_response(
        user_prompt,
        chat_history,
        user_profile,
        relevant_chunks,
        response_type
    )

    final_response = await transform_stylistic_response(mentor_id, llm_response)
    return {"response": final_response}
