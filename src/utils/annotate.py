from annotated_text import annotated_text


def display_annotated_text(text, response):
   
    annotations = []
    last_idx = 0
    
    annotated_entities = [(text.find(entity['word'], last_idx), text.find(entity['word'], last_idx) + len(entity['word']), entity['word'], entity['entity_group']) for entity in response]
    
    annotated_entities.sort(key=lambda x: x[0])
    
    for start_idx, end_idx, word, label in annotated_entities:
        if start_idx > last_idx:
            annotations.append(text[last_idx:start_idx])
        
        annotations.append((word, label))
        last_idx = end_idx
    
    if last_idx < len(text):
        annotations.append(text[last_idx:])
    
    annotated_text(*annotations)