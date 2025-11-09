import asyncio
from flask import Flask, request, jsonify

from typeManager import identify_response_type
from retriever import retrieve_required_chunks
from responseGenerator import generate_llm_response
from stylizer import transform_stylistic_response
from FireBase import getUserProfile


# ===============================
# MAIN CHAT HANDLER
# ===============================

async def handle_chat(user_prompt, user_id, chat_history, mentorID):
    user_profile = getUserProfile(mentorID)

    if not user_prompt or not user_id:
        return jsonify({"error": "Missing prompt or userId"}), 400

    response_type = await identify_response_type(user_prompt)


    relevant_chunks = await retrieve_required_chunks(user_id, user_prompt, response_type)

    llm_response = await generate_llm_response(user_prompt, chat_history, user_profile, relevant_chunks, response_type)

    final_response = await transform_stylistic_response(llm_response)

    return  final_response
