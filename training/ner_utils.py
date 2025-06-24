from typing import List

def read_conll(file_path: str):
    sentences = []
    labels = []
    with open(file_path, encoding="utf-8") as f:
        sentence = []
        label = []
        for line in f:
            if line.strip() == "":
                if sentence:
                    sentences.append(sentence)
                    labels.append(label)
                    sentence = []
                    label = []
            else:
                splits = line.strip().split()
                if len(splits) == 2:
                    token, tag = splits
                    sentence.append(token)
                    label.append(tag)
        if sentence:
            sentences.append(sentence)
            labels.append(label)
    return sentences, labels
