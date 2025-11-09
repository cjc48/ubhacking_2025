from flask import Flask, jsonify, request
import firebase_admin
from firebase_admin import credentials, firestore
from flask_cors import CORS
from backend.messenger import messengerMain
from backend.profileCreation import profileMain
from backend.FireBase import db
import json

app = Flask(__name__)
CORS(app)

@app.route('/handle_chat',methods=['POST'])
async def handle_chat():
    data = request.json
    user_prompt = data.get('user_message')
    user_id = data.get('user_id')
    mentor_id = data.get('mentor_id')
    history = data.get('history',[])

    if not user_prompt or not user_id or not mentor_id:
        return jsonify({"error": "Missing required fields"}), 400

    response_data = await messengerMain.handle_chat(
        user_prompt=user_prompt,
        user_id=user_id,
        chat_history=history,
        mentorID=mentor_id
        )
    return jsonify(response_data)


@app.route('/api/create_profile', methods=['POST'])
def create_profile():
    """
    Receives mentor data and transcripts from the frontend.
    This is a multipart/form-data request.
    """
    try:
        # --- 1. Get the text data from 'request.form' ---
        mentor_id = request.form.get('mentor_id')
        description = request.form.get('description')
        rules = request.form.get('rules')

        if not mentor_id:
            return jsonify({"error": "mentor_id is required"}), 400

        # --- 2. Get the file(s) from 'request.files' ---
        uploaded_files = request.files.getlist('files')

        # --- This is the new part: Read file contents ---
        # We assume the profileMain.main function can handle the file objects directly.
        # If it expects content, you would read it here:
        # files_content = [file.read().decode('utf-8') for file in uploaded_files]

        # --- 3. Call your "brains" to do the work ---
        # Pass the list of FileStorage objects directly
        result = profileMain.main(
            uploaded_files,
            description,
            rules,
        )

        return jsonify(result)

    except Exception as e:
        print(f"Error creating profile: {e}")
        return jsonify({"error": str(e)}), 500

    
    
# CREATING A TRANSCRIPT
@app.route('/api/transcripts',methods = ['POST'])
def create_transcript():
    data = request.json

    new_transcript = {
        'mentor_id': data['mentor_id'],
        'title': data.get('title','Untitled'),
        'content': data['content']
    }

    doc_ref = db.collection('transcripts').add(new_transcript)
    return jsonify({"id": doc_ref.id, **new_transcript}),201

# READING ALL TRANSCRIPTS
@app.route('/api/transcripts', methods=['GET'])
def get_all_transcripts():
    try:
        transcripts = []
        docs = db.collection('transcripts').stream()

        for doc in docs:
            transcript_data = doc.to_dict()
            transcript_data['id'] = doc.id
            transcripts.append(transcript_data)

        return jsonify({'transcripts': transcripts})

    except Exception as e:
        return jsonify({'Error': str(e)}), 500

# READING A SINGLE TRANSCRIPT BY ID
@app.route('/api/transcripts/<string:transcript_id>',methods=['GET'])
def get_transcript(transcript_id):
    try:
        doc_ref = db.collection('transcripts').document(transcript_id)
        doc = doc_ref.get()

        if not doc.exists:
            return jsonify({'Error': 'Transcript not found'}), 404

        transcript_data = doc.to_dict()
        transcript_data['id'] = doc.id
        return jsonify(transcript_data)

    except Exception as e:
        return jsonify({'Error': str(e)}), 500

# UPDATE A TRANSCRIPT
@app.route('/api/transcripts/<string:transcript_id>',methods = ['PUT'])
def update_transcript(transcript_id):
    try:
        doc_ref = db.collection('transcripts').document(transcript_id)
        doc = doc_ref.get()

        if not doc.exists:
            return jsonify({'Error': 'Transcript not found'}),404

        data = request.json

        doc_ref.update(data)
        updated_doc = doc_ref.get()
        return_data = updated_doc.to_dict()
        return_data['id'] = updated_doc.id

        return jsonify(return_data)

    except Exception as e:
        return jsonify({'Error': str(e)}), 500


# DELETE A TRANSCRIPT BY ID

@app.route('/api/transcripts/<string:transcript_id>',methods=['DELETE'])
def delete_transcript(transcript_id):
    try:
        doc_ref = db.collection('transcripts').document(transcript_id)
        doc = doc_ref.get()

        if not doc.exists:
            return jsonify({'Error': 'Transcript not found'}), 404

        # Delete the document
        doc_ref.delete()
        return jsonify({'message': 'Transcript deleted successfully'})

    except Exception as e:
        return jsonify({'Error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
