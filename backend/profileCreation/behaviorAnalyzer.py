from ..aiDelegate import mainComposer, mainLLM

def analyzeBehavior(transcriptChunks):
    behaviorInsights = []
    for chunk in transcriptChunks:
        prompt = (
            "You are an expert discourse analyst and pedagogy researcher. "
            "Analyze the following single text chunk to extract the speaker's behavioral and communicative style with maximal depth and precision. "
            "Your goal is NOT to summarize the topic, but to profile HOW the person thinks, explains, and interacts.\n\n"
            "Instructions:\n"
            "- Focus strictly on behavior: tone, reasoning pattern, rhetorical moves, pacing, interaction stance, and didactic tactics.\n"
            "- Infer structure: How does the idea start, develop, and resolve? Identify micro-templates (e.g., define → motivate → example → recap; claim → evidence → implication; setup → contrast → resolution). "
            "Map this structure explicitly.\n"
            "- Tone and affect: formal vs conversational; calm vs energetic; supportive vs challenging; confidence vs humility; use of hedges or certainty markers.\n"
            "- Sentence dynamics: typical sentence length, complexity, clause chaining; prevalence of transition markers (first, now, therefore, in practice, notice that) and how they guide flow.\n"
            "- Question usage: rhetorical questions, checks-for-understanding, prompts to reflect.\n"
            "- Pedagogical moves: examples density; analogies or metaphors; stepwise scaffolding; error-first framing; misconception preemption; recaps/summaries.\n"
            "- Audience management: second-person address, inclusive pronouns, invitations to try steps, directives, or reflective prompts.\n"
            "- Handling uncertainty: when evidence is thin, do they reason forward, qualify, defer, or simulate possibilities?\n"
            "- Lexical fingerprint: recurring phrases, transitions, or signature expressions if present. If none are explicit, infer probable connective habits from the style.\n"
            "- Constraints: do NOT add external facts; do NOT judge correctness; stay within the chunk; describe behavior even if subtle.\n\n"
            "Output format:\n"
            "- One dense analytical paragraph (about 120–220 words) describing only behavioral/style traits observed in THIS chunk.\n\n"
            "Chunk:\n"
            f"{chunk}\n\n"
            "Now produce the behavioral analysis paragraph."
        )
        response = mainComposer(prompt)
        behaviorInsights.append(response.strip())
    combinedInsights = "\n".join(behaviorInsights)
    return combinedInsights

def compileBehaviorProfile(behaviorAnalysis):
    prompt = (
        "You are crafting a master behavioral blueprint for a mentor based on multiple prior behavioral observations. "
        "Your task is to synthesize a single, cohesive profile that another model can follow to emulate the mentor’s communication and reasoning. "
        "Do NOT summarize subject matter; focus entirely on HOW the mentor thinks and speaks.\n\n"
        "Source observations (multi-chunk analyses follow):\n"
        f"{behaviorAnalysis}\n\n"
        "Requirements for the final blueprint:\n"
        "- Length: at least 250 words and up to 1000 words; rich, specific, and operational.\n"
        "- Tone characterization: describe baseline affect (calm vs energetic), formality, warmth, confidence, and emotional coloration; note hedging or certainty norms.\n"
        "- Reasoning architecture: identify default global templates (e.g., introduce → analyze → example → conclude; claim → evidence → implication; definition → decomposition → application → recap). "
        "Explain when each template is likely chosen and how transitions are signaled.\n"
        "- Discourse moves: typical transitions and connective logic (therefore, in practice, notice that, to wrap up); cadence of signposting (first, next, finally); rhetorical questions; checks-for-understanding; contrast frames; error handling.\n"
        "- Pedagogical tactics: example and analogy style (abstract vs concrete), scaffolding pattern, recap frequency, guidance style (directive vs reflective), and how misconceptions are preempted or corrected.\n"
        "- Pacing and density: sentence length tendencies, pause/segmentation cues, information chunking, repetition or emphasis strategies.\n"
        "- Audience engagement: use of second-person address, inclusive pronouns, invitations to reflect or act, encouragement style, boundary-setting for scope.\n"
        "- Handling uncertainty: preferred strategy under ambiguity (enumerate possibilities, qualify claims, defer to principles, request more context), and how this is worded.\n"
        "- Lexical fingerprint: list a handful of likely recurring transitions or signature phrases IF reliably implied by the observations (do not invent brand-new catchphrases without basis; if uncertain, describe their type rather than exact wording).\n"
        "- Operational guidance: instruct a downstream generator how to implement this style (ordering of steps, where to place examples, when to recap, how to phrase directives or questions). "
        "Anylize each of the characteristics and attributes expressed with responses for each of the types: {define, explain, prove, compare, motivate, summarize, reflect, critique, instruct}. you need to go in depth to anylize how each of these responses are behaviorly expressed.\n"
        "Write as natural prose, not bullet points.\n"
        "- Prohibitions: do not include headings; do not include numbered lists; do not mention these instructions; do not summarize topic content; focus only on behavior.\n\n"
        "Deliver a single cohesive narrative profile (250–1000 words) that could be injected as a style blueprint for generation."
    )
    profileDescription = mainLLM(prompt)
    return profileDescription.strip()
