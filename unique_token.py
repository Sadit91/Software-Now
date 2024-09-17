from transformers import AutoTokenizer
from collections import Counter
import pandas as pd

def count_unique_tokens(txt_file_path, output_csv_path, chunk_size=1000): 
    tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
    token_counts = Counter()
    with open(txt_file_path, 'r', encoding='utf-8') as file:
        while True:            
            chunk = file.read(chunk_size)
            if not chunk:
                break            
            
            tokens = tokenizer.tokenize(chunk)            
            max_length = tokenizer.model_max_length  
            for i in range(0, len(tokens), max_length):
                token_chunk = tokens[i:i + max_length]
                token_counts.update(token_chunk)
    

    top_tokens = token_counts.most_common(30)  
    top_tokens_df = pd.DataFrame(top_tokens, columns=['Token', 'Count'])
    top_tokens_df.to_csv(output_csv_path, index=False)

    print("Token counts saved to:", output_csv_path)
    print(top_tokens_df)

txt_file_path = 'output.txt'
output_csv_path = 'top_30_tokens.csv'
print("Starting...")
count_unique_tokens(txt_file_path, output_csv_path)
print("Done.")
