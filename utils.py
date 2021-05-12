def tokenize(text: str, width: int = 100):
    sentences = text.split("。")
    current = []
    size = 0
    for sentence in sentences:
        if size + (length := len(sentence)) <= width:
            current.append(sentence)
            size += length
        else:
            yield "。".join(current)
            current = [sentence]
            size = length
    if current:
        yield "".join(current)
