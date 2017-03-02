def decrypt_story():
    storyString = get_story_string()
    f = CiphertextMessage(storyString)
    return f.decrypt_message()