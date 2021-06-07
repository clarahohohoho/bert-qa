# Question and Answer tool with BERT
A Question Answering application that is able to answer questions based on a provided set of text.  
The trained BERT model is adopted from Huggingface's repository of models, where a large BERT model was trained on the popular question answering dataset SQuAd 2.0.
I have also developed a simple user interface (UI) with PyQt5 to access the Question Answering tool.

## Screenshot of Application

![Alt text](./screenshot.png?raw=true "Optional Title")

## Data Structure

```
bert-qna
 |-- main.py (main running script to call pretrained BERT model)
 |-- ui.py (script to form user interface)
 |-- requirements.txt
 |-- README.md
```

## Set up environment

``` bash
cd bert-qa
virtualenv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

## Run QnA Tool
``` bash
source ./venv/bin/activate
python ui.py
```


