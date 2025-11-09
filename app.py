from flask import Flask, jsonify, request
import firebase_admin
from firebase_admin import credentials, firestore
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

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
