import spacy
import pandas as pd

def extract_entities_spacy(txt_file_path, output_csv_path, chunk_size=1000000):    
    nlp = spacy.load('en_core_web_sm')
    count = 0
    all_entities = []
    print("Going on.....")
    
    with open(txt_file_path, 'r', encoding='utf-8') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                print("Error reading")
                break          
            
            count = count + 1
            print(count , "Processing ...")
            
            doc = nlp(chunk)
            print(count ,"keep waiting ...")            
            entities = [(ent.text, ent.label_) for ent in doc.ents if ent.label_ in ['DISEASE', 'DRUG']]
            all_entities.extend(entities)
    
    print("Almost there ....")    
    entities_df = pd.DataFrame(all_entities, columns=['Entity', 'Label'])
    entities_df.to_csv(output_csv_path, index=False)
    print(f"Entities extracted with spaCy and saved to {output_csv_path}")
    print(entities_df)

txt_file_path = 'output.txt'
output_csv_path = 'spaCy_entities.csv'
print("Starting ...")
extract_entities_spacy(txt_file_path, output_csv_path)
print("Done!")
