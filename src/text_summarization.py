#In text_summarization.py, implement text summarization:

# file: summarization.py
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
import nltk

nltk.download('punkt')
nltk.download('stopwords')

def summarize_genetic_info(text, num_sentences=3):
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    word_frequencies = FreqDist(word for word in words if word not in stop_words)
    
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_frequencies.keys():
                if sentence not in sentence_scores.keys():
                    sentence_scores[sentence] = word_frequencies[word]
                else:
                    sentence_scores[sentence] += word_frequencies[word]
    
    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    summary = ' '.join(summary_sentences)
    return summary

# Usage
genetic_info = """
The BRCA1 and BRCA2 genes are tumor suppressor genes that help repair damaged DNA. 
When these genes have certain mutations, they can't function properly, which increases the risk of breast and ovarian cancer. 
People with BRCA1 mutations have a 55-65% chance of developing breast cancer before age 70. 
BRCA2 mutations are associated with a 45% chance of breast cancer by age 70. 
These mutations can be inherited from either parent and can affect both men and women.
"""

summary = summarize_genetic_info(genetic_info)
print(summary)
