# main.py

import pandas as pd
from data_processing import load_genomic_data, preprocess_data
from ner_model import train_ner_model, identify_genetic_entities
from summarization import summarize_genetic_info
from personalization import personalize_risk_explanation

def main():
    # Step 1: Load and preprocess genomic data
    print("Loading and preprocessing genomic data...")
    file_path = 'path_to_your_genomic_data.csv'  # Replace with your actual file path
    data = load_genomic_data(file_path)
    processed_data = preprocess_data(data)
    print("Data processed. Sample:")
    print(processed_data.head())
    print("\n")

    # Step 2: Train NER model and identify entities
    print("Training NER model and identifying entities...")
    nlp_model = train_ner_model()
    sample_text = "Patients with BRCA1 mutations have an increased risk of breast cancer."
    entities = identify_genetic_entities(sample_text, nlp_model)
    print(f"Identified entities: {entities}")
    print("\n")

    # Step 3: Summarize genetic information
    print("Summarizing genetic information...")
    genetic_info = """
    The BRCA1 and BRCA2 genes are tumor suppressor genes that help repair damaged DNA. 
    When these genes have certain mutations, they can't function properly, which increases the risk of breast and ovarian cancer. 
    People with BRCA1 mutations have a 55-65% chance of developing breast cancer before age 70. 
    BRCA2 mutations are associated with a 45% chance of breast cancer by age 70. 
    These mutations can be inherited from either parent and can affect both men and women.
    """
    summary = summarize_genetic_info(genetic_info)
    print("Summary of genetic information:")
    print(summary)
    print("\n")

    # Step 4: Personalize risk explanation
    print("Generating personalized risk explanation...")
    # Assuming we're using the first row of our processed data
    sample_data = processed_data.iloc[0]
    variant = sample_data['variant']
    risk_score = sample_data['risk_score']
    age = 45  # Example age
    family_history = True  # Example family history

    explanation = personalize_risk_explanation(variant, risk_score, age, family_history)
    print("Personalized risk explanation:")
    print(explanation)

if __name__ == "__main__":
    main()
