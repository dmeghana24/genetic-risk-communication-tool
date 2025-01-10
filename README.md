# genetic-risk-communication-tool
Personalized Genetic Risk Communication Tool for Electronic Health Records

---

# Personalized Genetic Risk Communication Tool for Electronic Health Records

## Project Overview

This project focuses on developing a natural language processing (NLP) tool to automatically generate personalized, easy-to-understand summaries of genetic risk information from patients' genomic data. The generated summaries are designed to integrate seamlessly into electronic health records (EHRs). 

The task is particularly challenging due to the complexity of genomic data, the need for personalization based on patient demographics and health literacy, and the ethical considerations of presenting sensitive genetic risk information. The tool aims to bridge the gap between complex genomic findings and actionable clinical insights for both patients and healthcare providers.

## Goals

The primary goal of this project is to classify and summarize genetic risk information into personalized reports that can be integrated into EHRs. The task involves:
1. **Data Integration**: Linking genetic variants to associated health risks using publicly available genomic datasets and simulated EHR data.
2. **NLP Techniques**: Applying named entity recognition (NER) to identify genetic variants and associated conditions, summarizing complex genetic information, and ensuring neutral language through sentiment analysis.
3. **Personalization**: Tailoring risk explanations based on patient demographics, family history, and health literacy levels.
4. **Readability Optimization**: Ensuring summaries are accessible to a general audience using readability metrics such as Flesch-Kincaid scores.
5. **EHR Integration**: Designing a prototype interface for clinicians to interact with generated summaries.

## Classification Task

This project involves a three-way classification task where the target classes are:
1. **Self-Reports**: Genetic risk information directly related to the patient.
2. **Non-Personal Reports**: Risk information related to others (e.g., family or caregivers).
3. **Literature/News Mentions**: General references or scientific discourse unrelated to specific individuals.

## Contributor:
   Meghana 

## Methodology

### Data Integration
- Publicly available datasets such as the 1000 Genomes Project were used.
- Simulated EHR data was created for testing purposes.
- A mapping system was implemented to link genetic variants with associated health risks.

### NLP Techniques
- Named Entity Recognition (NER) was applied to identify genetic variants and conditions.
- Text summarization techniques were used to condense complex genetic data into concise summaries.
- Sentiment analysis ensured that generated summaries used neutral, non-alarming language.

### Personalization
- An algorithm was developed to tailor summaries based on patient characteristics such as age, family history, and health literacy levels.

### Evaluation
- The tool's performance was evaluated through comparisons between automatically generated summaries and manually written ones.
- A small-scale user study with medical students or clinicians assessed the tool's usefulness and accuracy.

## Deliverables

1. **Software Package**: A Python-based tool implementing the classification and summarization system.
2. **Demo**: A functional prototype showcasing how generated summaries appear within an EHR interface.
3. **Technical Report**: Comprehensive documentation of the project's methodology, results, and future directions.

## How to Use

### Requirements
Install the required Python libraries:
```bash
pip install pandas numpy spacy nltk
```

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/genetic-risk-tool.git
   cd genetic-risk-tool
   ```
2. Prepare your genomic dataset in CSV format and place it in the `data/` folder.
3. Run `main.py`:
   ```bash
   python src/main.py
   ```

### Outputs
The tool will produce:
1. Preprocessed genomic data linked with EHR data.
2. Summarized genetic risk reports tailored for individual patients.

## Challenges and Considerations

1. **Data Complexity**: Genomic data is inherently complex, requiring effective preprocessing and integration techniques.
2. **Ethical Concerns**: Presenting sensitive health information requires careful attention to neutrality in language.
3. **Evaluation Limitations**: User studies were conducted on a small scale due to resource constraints.

## Future Work

1. Expanding the dataset with real-world genomic and EHR data.
2. Improving NLP models using pre-trained transformers like BERT for better accuracy in NER tasks.
3. Conducting larger-scale evaluations with healthcare professionals.


Citations:
[1] https://ceur-ws.org/Vol-3395/T5-4.pdf
[2] https://pmc.ncbi.nlm.nih.gov/articles/PMC10365612/
[3] https://www.nature.com/articles/s41598-024-69687-8
[4] https://pmc.ncbi.nlm.nih.gov/articles/PMC7834613/
[5] https://aclanthology.org/2021.smm4h-1.19
[6] https://www.biorxiv.org/content/10.1101/2021.12.15.472745v1.full-text
[7] https://www.cell.com/heliyon/fulltext/S2405-8440(24)10134-X
[8] https://openreview.net/pdf?id=xyGSIttHYO
