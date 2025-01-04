##Personalization Algorithm
#In personalization_algorithm.py, create functions to:
#Tailor risk explanations based on patient data
#Incorporate readability metrics
#Implement controlled vocabulary


# file: personalization.py

def personalize_risk_explanation(variant, risk_score, age, family_history):
    base_explanation = f"Your genetic test shows a variant in the {variant} gene."
    
    risk_level = "low" if risk_score < 0.3 else "moderate" if risk_score < 0.7 else "high"
    risk_explanation = f"This variant is associated with a {risk_level} risk of developing certain conditions."
    
    age_factor = "Your current age is a factor in assessing this risk." if age > 40 else ""
    
    family_factor = "Your family history may also contribute to your overall risk." if family_history else ""
    
    personalized_explanation = f"{base_explanation} {risk_explanation} {age_factor} {family_factor}"
    
    return personalized_explanation

# Usage
variant = "BRCA1"
risk_score = 0.75
age = 45
family_history = True

explanation = personalize_risk_explanation(variant, risk_score, age, family_history)
print(explanation)
