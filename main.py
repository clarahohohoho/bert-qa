from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline


def main(context, question):
    
    model_name = "./bert-large-uncased-whole-word-masking-squad2_model"
    tok_name = "./bert-large-uncased-whole-word-masking-squad2_tokenizer"
    model = AutoModelForQuestionAnswering.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(tok_name)

    # a) Get predictions
    nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)
    QA_input = {
        'question': question,
        'context': context
    }
    res = nlp(QA_input)

    return res['answer']

