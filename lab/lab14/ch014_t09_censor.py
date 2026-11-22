def censor(text: str, word: str) -> str:
    words = text.split()
    censored = []
    for w in words:
        if w == word:
            censored.append("*" * len(word))
        else:
            censored.append(w)
    return " ".join(censored
