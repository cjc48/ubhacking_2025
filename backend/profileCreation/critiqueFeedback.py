from ..aiDelegate import critiqueAI, generateAI, mainLLM


def critiqueProfile(generalProfile):
    count = 0
    while True:
        simulatedResponse = simulateProfileResponse(generalProfile)
        accuracyReport = evaluateProfileAccuracy(simulatedResponse, generalProfile)
        if accuracyReport.strip().lower() == 'true' or count >= 3:
            return True
        else:
            generalProfile = refineProfileDescription(generalProfile, accuracyReport)
            count += 1


def simulateProfileResponse(generalProfile):
    prompt = (
        f"Based on the following mentor profile description, generate a simulated response to a mentee's question.\n\n"
        f"Profile Description:\n{generalProfile}\n\n"
        f"Come up with an applicable question a user would ask this profile'\n\n"
        f"respond in the following format:\n"
        f"Question: <the question you come up with>\n"
        f"Response: <the simulated response from the Profile Description>\n"
    )
    simulatedResponse = generateAI(prompt)

    return simulatedResponse


def evaluateProfileAccuracy(simulatedResponse, generalProfile):
    prompt = (
        f"The following is a mentor profile description and a simulated response generated from it.\n\n"
        f"Profile Description:\n{generalProfile}\n\n"
        f"Simulated Response:\n{simulatedResponse}\n\n"
        f"Determine if the simulated response accurately reflects the behavior, tone, and reasoning style described in the profile. "
        f"If it does, respond with only 'True'. If it does not, write an in depth description on what needs to be improved in the description to get the desired output."
    )
    response = critiqueAI(prompt)
    return response


    

def refineProfileDescription(generalProfile, accuracyReport):
    prompt = (
        f"The following is a mentor profile description that needs refinement based on feedback.\n\n"
        f"Profile Description:\n{generalProfile}\n\n"
        f"Feedback on Inaccuracies:\n{accuracyReport}\n\n"
        f"Refine and improve the profile description to better align with the desired behavior, tone, and reasoning style indicated in the feedback. "
        f"Provide only the refined profile description without any additional commentary."
    )

    response = mainLLM(prompt)

    return response
