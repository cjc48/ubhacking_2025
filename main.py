import asyncio
from flask import Flask, request, jsonify

app = Flask(__name__)

# TRIGGERED BY "SEND BUTTON PRESSED"
@app.route('/handle_chat',methods=['POST'])
async def handle_chat():
    data = request.json
    user_prompt = data.get('prompt')
    chat_history = data.get('history',[])

    # IDENTIFY INTENT
    intent = await identify_intent(user_prompt)

    # IDENTIFY RESPONSE TYPE
    response_type = await identify_response_type(user_prompt)

    # RETRIEVE REQUIRED CHUNKS
    relevant_chunks = await retrieve_required_chunks(intent, response_type)

    # SCRAPE IMPORTANT SENTENCES FROM CHUNKS
    context = scrape_important_sentences(relevant_chunks)

    # TRANSFORM/STYLISTIC PROCESS RESPONSE
    final_response = await transform_stylistic_response(llm_response)

    #SEND TO USER
    return jsonify({"Response": final_response})
