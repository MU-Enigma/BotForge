# Phishing Catcher Model

## Overview

This repository contains the model and the code for fine-tuning a text classification mdel to detect phishing websited based on their URLs. It leverages a pre-trained transformer model and eploys LoRA (Low-Rank Adaptation) for efficient fine-tuning.

You can find the code for the fine-tuning performed in the `PhishingCatcherModel.ipynb` file above. \
Model files are also available under `PranavReddyy/PhishingCatcher-FineTunedModel/`.

## 1 Datset

Source : [xinxingwu/phishing-site-classification](https://huggingface.co/datasets/xinxingwu/phishing-site-classification?row=1)

The dataset contains URLs labeled as either phishing (malicious) or legitimate. Phishing labeled as 0, legitimate as 1.

## 2 Model

Model Used : [distilbert-base-uncased](https://huggingface.co/distilbert/distilbert-base-uncased)

Getting a classification model from the model being used :

```python
model_checkpoint = 'distilbert-base-uncased'

# define label maps
id2label = {0: "Negative", 1: "Positive"}
label2id = {"Negative":0, "Positive":1}

# generate classification model from model_checkpoint
model = AutoModelForSequenceClassification.from_pretrained(
    model_checkpoint, num_labels=2, id2label=id2label, label2id=label2id)
```

## 3 Fine Tuning Process

### 3.1 Load and Tokenize the dataset

We create a tokenizer from the pre-trained mode. It will convert the text into a format suitable for the model.

```python
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint, add_prefix_space=True)
```

If tokenizer doesn't have a padding token, we add one, it ensures that all sequences in a batch have the same length, helps in efficient batch processing during training.

```python
if tokenizer.pad_token is None:
    tokenizer.add_special_tokens({'pad_token': '[PAD]'})
    model.resize_token_embeddings(len(tokenizer))
```

Function responsible for tokenizing the dataset :

```python
# create tokenize function
def tokenize_function(examples):
    # extract text
    text = examples["text"]

    # tokenize and truncate text
    # if text exceeds 512 tokens, it will be truncated from the left side
    tokenizer.truncation_side = "left"
    tokenized_inputs = tokenizer(
        text,
        return_tensors="np",
        truncation=True,
        max_length=512
    )

    return tokenized_inputs
```

Preparing our tokenized dataset :

```python
tokenized_dataset = dataset.map(tokenize_function, batched=True)
```

To handle the padding for the input sequences :
Ensures that all the sequences in a batch are padded to the same length dynamically, making input sequences with consistent lengths.

```python
data_collator = DataCollatorWithPadding(tokenizer=tokenizer)
```

### 3.2 LoRA Hyperparameters

```python
peft_config = LoraConfig(task_type="SEQ_CLS", # Sequence Classification
                        r=4, # Rank of LoRA
                        lora_alpha=32, # Scaling Factor
                        lora_dropout=0.01, # Prevents overfitting during training
                        target_modules = ['q_lin']) # Linear layers associated with the query will use LoRA
```

### 3.3 Model Initialisation

```python
model = get_peft_model(mode, peft_config)
```

### 3.4 Training Hyperparameters

```python
lr = 1e-3 # Learning Rate : Step size for the optimization during training
batch_size = 4 # No. of samples processed at once
num_epochs = 10 # No. of complete passes through the training dataset
```

### 3.5 Training Arguments

```python
training_args = TrainingArguments(
    output_dir= model_checkpoint + "-lora-text-classification", # Specifies the directory wehere the model checkpoints are saved
    learning_rate=lr, # Learning rate for the optimizer
    per_device_train_batch_size=batch_size, # Batch size for training
    per_device_eval_batch_size=batch_size, # Batch size for evaluation
    num_train_epochs=num_epochs, # Epochs to train the model
    weight_decay=0.01, # Prevents overfitting
    evaluation_strategy="epoch", # When to evaluate the model (End of each epoch)
    save_strategy="epoch", # When to save the model checkpoints (End of each epoch)
    load_best_model_at_end=True, # Best model is loaded after training (using evaluation metrics)
)
```

### 3.6 Trainer Object

```python
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],
    eval_dataset=tokenized_dataset["validation"],
    tokenizer=tokenizer,
    data_collator=data_collator, # this will dynamically pad examples in each batch to be equal length
    compute_metrics=compute_metrics,
)
```

### 3.7 Training the model

```python
trainer.train()
```

## 4 Challenges and Solutions

1. Challenge: High memory usage during fine-tuning due to large model size and long sequences.

   > Solution: LoRA fine-tuning was applied to limit the number of parameters needing updates, reducing memory requirements.

2. Challenge: Model compatibility issues when moving between different hardware (CPU, GPU, MPS).
   > Explicitly specified the device (.to('cpu')) to avoid hardware conflicts and ensure consistent results.
