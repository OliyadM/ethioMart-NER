import os
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForTokenClassification, TrainingArguments, Trainer
import numpy as np
from sklearn.metrics import precision_recall_fscore_support, accuracy_score

MODEL_NAME = "xlm-roberta-base"
SAVE_DIR = "./saved_models/xlmroberta_model"

def compute_metrics(p):
    predictions, labels = p
    preds = np.argmax(predictions, axis=2)
    # Remove ignored index (usually -100)
    true_labels = [[l for l in label if l != -100] for label in labels]
    true_preds = [[p for (p, l) in zip(pred, label) if l != -100] for pred, label in zip(preds, labels)]
    precision, recall, f1, _ = precision_recall_fscore_support(true_labels, true_preds, average="weighted")
    accuracy = accuracy_score(true_labels, true_preds)
    return {"precision": precision, "recall": recall, "f1": f1, "accuracy": accuracy}

def main():
    # Load dataset (adjust this to your dataset loading method)
    dataset = load_dataset("conll2003")  # Replace with your actual Amharic NER dataset

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForTokenClassification.from_pretrained(MODEL_NAME, num_labels=9)  # Adjust num_labels

    def tokenize_and_align_labels(examples):
        tokenized_inputs = tokenizer(examples['tokens'], truncation=True, is_split_into_words=True)
        labels = []
        for i, label in enumerate(examples['ner_tags']):
            word_ids = tokenized_inputs.word_ids(batch_index=i)
            previous_word_idx = None
            label_ids = []
            for word_idx in word_ids:
                if word_idx is None:
                    label_ids.append(-100)
                elif word_idx != previous_word_idx:
                    label_ids.append(label[word_idx])
                else:
                    label_ids.append(label[word_idx] if False else -100)  # Use False if not using IOB format continuation labels
                previous_word_idx = word_idx
            labels.append(label_ids)
        tokenized_inputs["labels"] = labels
        return tokenized_inputs

    tokenized_datasets = dataset.map(tokenize_and_align_labels, batched=True)

    training_args = TrainingArguments(
        output_dir=SAVE_DIR,
        evaluation_strategy="epoch",
        learning_rate=5e-5,
        per_device_train_batch_size=16,
        per_device_eval_batch_size=16,
        num_train_epochs=3,
        weight_decay=0.01,
        save_strategy="epoch",
        load_best_model_at_end=True,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_datasets["train"],
        eval_dataset=tokenized_datasets["validation"],
        tokenizer=tokenizer,
        compute_metrics=compute_metrics,
    )

    trainer.train()
    trainer.save_model(SAVE_DIR)

if __name__ == "__main__":
    main()
