import os
import uuid
from .transcriber import transcribeMedia
from .chunkCreator import createTranscriptChunks
from .behaviorAnalyzer import analyzeBehavior, compileBehaviorProfile
from .critiqueFeedback import critiqueProfile
from ..FireBase import saveProfile, saveTranscript
from .tagCreator import createTaggedChunks


def main(userFiles, userDescription, userRules):
    print("MAIN HAS BEEN BECKONED!!!")
    userId = str(uuid.uuid4())
    print("USER ID GENERATED: ", userId)
    #the error is somewhere in formatUserData or below
    formattedData = formatUserData(userFiles)
    print("DATA FORMATTED")
    chunks = createTranscriptChunks(formattedData)
    profile = generateBehaviorProfile(chunks)
    if profile:
        createUserInFirebase(userId, profile, chunks, userDescription, userRules)
        print(f"User {userId} profile created and saved successfully.")
    else:
        print("Profile generation failed.")


def formatUserData(userFiles):
    transcribedData = []
    videoAudioExt = [".mp4", ".mov", ".m4a", ".mp3", ".wav", ".aac"]
    for filename in userFiles:
        with open(filename, "rb") as f:
            file = f.read()
            ext = os.path.splitext(file)[1].lower()
            if ext in videoAudioExt:
                text = transcribeMedia(file)
            else:
                text = f.read()
                transcribedData.append(text)
    return transcribedData


def generateBehaviorProfile(chunks):
    behaviorAnalysis = analyzeBehavior(chunks)
    generalProfile = compileBehaviorProfile(behaviorAnalysis)
    if critiqueProfile(generalProfile):
        return generalProfile
    else:
        return None


def createUserInFirebase(userId, profileDescription, chunks, userDescription, userRules):
    profileData = {
        "userId": userId,
        "profileDescription": profileDescription,
        "userDescription": userDescription,
        "userRules": userRules
    }
    saveProfile(profileData, userId)
    taggedChunks = createTaggedChunks(chunks)
    for index, chunk in enumerate(taggedChunks):
        transcriptName = f"chunk_{index}"
        chunkData = {
            "chunkId": transcriptName,
            "mentorId": userId,
            "content": chunk.get("content", chunk),
            "tags": chunk.get("tags", [])
        }
        saveTranscript(userId, transcriptName, chunkData)
