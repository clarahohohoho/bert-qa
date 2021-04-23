# Question and Answer tool with BERT

## Introduction

A Question and Answer bot that is able to answer questions based on a provided set of text.  
The trained BERT model is adopted from Huggingface's repository of models, where a large BERT model was trained on the popular question answering dataset SQuAd 2.0.
I have also developed a simple user interface (UI) with PyQt5 to access the QnA tool.

## Screenshot of Application

![Alt text](./screenshot.png?raw=true "Optional Title")

## Data Structure

```
ATLOP
 |-- main.py (main running script to call pretrained BERT model)
 |-- ui.py (script to form user interface)
 |-- requirements.txt
 |-- README.md
```

## Set up environment

``` bash
cd bert-qa
virtualenv venv
pip install -r requirements.txt
```

## Run QnA Tool
``` bash
python ui.py
```


