import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

def count_word_occurrences(txt_file_path, output_csv_path):
    with open(txt_file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    print("Going on...")    
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform([text])

    print("Wait ...")    
    word_counts = np.asarray(X.sum(axis=0)).flatten()
    words = vectorizer.get_feature_names_out()
    word_count_df = pd.DataFrame({'Word': words, 'Count': word_counts})
    print("Just there...")    
    top_words = word_count_df.sort_values(by='Count', ascending=False).head(30)
    top_words.to_csv(output_csv_path, index=False)
    print("coming Top words...")
    print(top_words)

txt_file_path = 'output.txt'
output_csv_path = 'top_30_words.csv'
print("Counting words...")
count_word_occurrences(txt_file_path, output_csv_path)
print("Completed...")
