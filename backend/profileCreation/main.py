import os
from transcriber import transcribeMedia
from chunkCreator import createTranscriptChunks
from behaviorAnalyzer import analyzeBehavior, compileBehaviorProfile
from critiqueFeedback import critiqueProfile
from FireBase import saveProfile, updateProfile, saveTranscript
from tagCreator import createTaggedChunks


def main(userFiles, userDescription, userRules):
    formattedData = formatUserData(userFiles)
    profile = generateBehaviorProfile(formattedData)
    if profile:
        print(" saved successfully.")
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
        saveProfile(generalProfile)
        return generalProfile
    else:
        print("Profile did not pass critique and was not saved.")
        updateProfile("unverifiedProfile", generalProfile)
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
    for chunk in taggedChunks:
        transcriptName = chunk["chunkId"]
        saveTranscript(userId, transcriptName, chunk)
