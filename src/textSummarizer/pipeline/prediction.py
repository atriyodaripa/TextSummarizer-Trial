from textSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline
import torch


class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()


    
    def predict(self, text, min_text, max_text):
        print(torch.cuda.is_available())
        device = 0 if torch.cuda.is_available() else -1
        print(device)
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": max_text, "min_length":min_text}
        print(gen_kwargs)
        # gen_kwargs = kwargs

        pipe = pipeline("summarization", model=self.config.model_path, tokenizer=tokenizer, device=device)

        print("Dialogue:")
        print(text)

        output = pipe(text, **gen_kwargs)[0]["summary_text"]
        print("\nModel Summary:")
        print(output)

        return output