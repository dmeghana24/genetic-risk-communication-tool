##In ner_module.py, implement Named Entity Recognition:

# file: ner_model.py
import spacy

def train_ner_model():
    nlp = spacy.blank("en")
    ner = nlp.add_pipe("ner")
    ner.add_label("GENE")
    ner.add_label("VARIANT")

    # Training data
    TRAIN_DATA = [
        ("The BRCA1 gene mutation increases cancer risk.", {"entities": [(4, 9, "GENE")]}),
        ("Patients with the APOE4 variant have higher Alzheimer's risk.", {"entities": [(21, 26, "VARIANT")]}),
    ]

    # Train the model
    optimizer = nlp.begin_training()
    for _ in range(20):
        for text, annotations in TRAIN_DATA:
            nlp.update([text], [annotations], sgd=optimizer)
    
    return nlp

def identify_genetic_entities(text, model):
    doc = model(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

# Usage
nlp_model = train_ner_model()
text = "Patients with BRCA1 mutations have an increased risk of breast cancer."
entities = identify_genetic_entities(text, nlp_model)
print(entities)

