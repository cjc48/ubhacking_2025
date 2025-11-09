import firebase_admin
from firebase_admin import credentials, firestore
import datetime

# Initializer

def initializeFirebase():
    cred = credentials.Certificate("serviceAccountKey.json")
    try:
        firebase_admin.get_app()
    except ValueError:
        firebase_admin.initialize_app(cred)
    return firestore.client()

db = initializeFirebase()

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

