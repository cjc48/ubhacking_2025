import os
import uuid
from transcriber import transcribeMedia
from chunkCreator import createTranscriptChunks
from behaviorAnalyzer import analyzeBehavior, compileBehaviorProfile
from critiqueFeedback import critiqueProfile
from FireBase import saveProfile, updateProfile, saveTranscript
from tagCreator import createTaggedChunks


def main(userFiles, userDescription, userRules):
    userId = str(uuid.uuid4())
    formattedData = formatUserData(userFiles)
    profile = generateBehaviorProfile(formattedData)
    if profile:
        createUserInFirebase(userId, profile, formattedData, userDescription, userRules)
        print(f"User {userId} profile created and saved successfully.")
    else:
        print("Profile generation failed.")


def formatUserData(userFiles):
    transcribedData = []
    videoAudioExt = [".mp4", ".mov", ".m4a", ".mp3", ".wav", ".aac"]
    for file in userFiles:
        ext = os.path.splitext(file)[1].lower()
        if ext in videoAudioExt:
            text = transcribeMedia(file)
        else:
            with open(file, "r", encoding="utf-8") as f:
                text = f.read()
        transcribedData.append(text)
    return transcribedData


def generateBehaviorProfile(interactionData):
    chunks = createTranscriptChunks(interactionData)
    behaviorAnalysis = analyzeBehavior(chunks)
    generalProfile = compileBehaviorProfile(behaviorAnalysis)
    if critiqueProfile(generalProfile):
        saveProfile({"profileDescription": generalProfile}, "temporaryProfile")
        return generalProfile
    else:
        updateProfile("unverifiedProfile", {"profileDescription": generalProfile})
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