from aiDelegate import mainHelper


def generateTag(chunk): 
    prompt = (
        f"Generate 3 to 6 concise, relevant tags for the following text to categorize its content. "
        f"Return the tags as a comma-separated list without numbering or extra words.\n\n"
        f"Text:\n{chunk}"
    )

    response = mainHelper(prompt)
    tags = [tag.strip() for tag in response.split(',') if tag.strip()]
    return tags

def createTaggedChunks(chunks):
    taggedChunks = []
    for i, chunk in enumerate(chunks):
        tags = generateTag(chunk)
        taggedChunks.append({
            "chunkId": f"chunk_{i}",
            "content": chunk,
            "tags": tags
        })
    return taggedChunks
