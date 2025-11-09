import os
import firebase_admin
from firebase_admin import credentials, firestore
import datetime
import json

# Initializer

if not firebase_admin._apps:
    try:
        key_path = os.path.join(os.path.dirname(__file__), "../serviceAccountKey.json")
        with open(key_path, 'r') as f:
            cert_dict = json.load(f)

        cred = credentials.Certificate(cert_dict)
        firebase_admin.initialize_app(cred)
    except Exception as e:
        print(f"Error initializing Firebase: {e}")
        # Re-raise the exception to see the full traceback
        raise


# Firestore client
db = firestore.client()

#Profile Manager

def saveProfile(profileData, mentorId):
    docRef = db.collection("mentorProfiles").document(mentorId)
    docRef.set(profileData)

def getProfile(mentorId):
    doc = db.collection("mentorProfiles").document(mentorId).get()
    if doc.exists:
        return doc.to_dict()
    else:
        print("Profile not found.")
        return None

def updateProfile(mentorId, updatedData):
    docRef = db.collection("mentorProfiles").document(mentorId)
    docRef.update(updatedData)

def deleteProfile(mentorId):
    db.collection("mentorProfiles").document(mentorId).delete()


# Transcript Storage

def saveTranscript(mentorId, transcriptName, transcriptData):
    docRef = db.collection("mentorTranscripts").document(f"{mentorId}_{transcriptName}")
    data = {
        "mentorId": mentorId,
        "transcriptName": transcriptName,
        "content": transcriptData,
        "createdAt": datetime.datetime.utcnow()
    }
    docRef.set(data)

def getTranscripts(mentorId):
    transcripts = db.collection("mentorTranscripts").where("mentorId", "==", mentorId).stream()
    return [t.to_dict() for t in transcripts]

