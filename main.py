import pandas as pd

def extract_text_from_csv(csv_file_names, output_txt_path):
    with open(output_txt_path, 'w', encoding='utf-8') as output_file:
        for file_name, text_column_name in csv_file_names.items():
            df = pd.read_csv(file_name)
            texts = df[text_column_name].dropna()
            output_file.write("\n".join(texts) + "\n")

csv_file_names = {
    'CSV1.csv': 'SHORT-TEXT',  
    'CSV2.csv': 'TEXT',
    'CSV3.csv': 'TEXT',
    'CSV4.csv': 'TEXT'
}
output_txt_path = 'output.txt'
extract_text_from_csv(csv_file_names, output_txt_path)
