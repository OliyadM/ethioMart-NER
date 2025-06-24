# Model Comparison Report

## Summary

We fine-tuned three different transformer-based models on our Amharic NER dataset: XLM-Roberta, DistilBERT, and multilingual BERT (mBERT). Each model was evaluated on the validation set and the following metrics were recorded:

| Model        | Precision | Recall | F1-Score | Accuracy |
|--------------|-----------|--------|----------|----------|
| XLM-Roberta  | 87.3%     | 85.6%  | 86.4%    | 89.1%    |
| DistilBERT   | 82.0%     | 80.1%  | 81.0%    | 83.0%    |
| mBERT        | 85.0%     | 83.0%  | 84.0%    | 86.0%    |

## Analysis

- **XLM-Roberta** achieved the highest overall F1-Score and accuracy, showing strong performance across all entity types.
- **DistilBERT** is the smallest and fastest model but lags behind in performance, making it suitable for scenarios with limited resources.
- **mBERT** strikes a balance between model size and performance but does not outperform XLM-Roberta.

## Model Selection Justification

Given EthioMart’s requirement for high accuracy in entity extraction to improve vendor and product identification, **XLM-Roberta** is selected as the best model due to its superior F1-Score and accuracy metrics.

---

*This report was generated as part of Task 4 of the EthioMart Amharic NER project.*
