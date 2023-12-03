# PHI-Masker

Protected health information (PHI) is any information about an individual's past, present, or future health condition, the provision of healthcare to the individual, or payment for the provision of healthcare to the individual. PHI can include demographic information, medical histories, test results, insurance information, and other data that could be used to identify an individual.

The Health Insurance Portability and Accountability Act (HIPAA) of 1996 is a federal law that protects the privacy and security of PHI. HIPAA requires healthcare organizations to take steps to protect PHI, including masking PHI when it is not necessary to be disclosed.

There are several reasons why it is important to mask PHI. First, masking PHI helps to protect patient privacy. By masking PHI, it is more difficult for unauthorized individuals to access and use this information. Second, masking PHI helps organizations to comply with HIPAA regulations. HIPAA requires organizations to take reasonable steps to protect PHI, and masking PHI is one way to do this. Third, masking PHI can make PHI more anonymous for research purposes. This can help to protect the privacy of research participants and to ensure that the results of research are not biased. Finally, masking PHI can improve the quality of care. By masking PHI, organizations can reduce the risk of medical errors and improve the accuracy of patient records.

Healthcare organizations should take steps to mask PHI whenever possible. This can be done by removing or obscuring certain information, such as names, dates of birth, and Social Security numbers. Organizations should also have policies and procedures in place for masking PHI and should train their staff on how to do this effectively.


# What does PHI Masker do?

PHI Masker is an AI-based tool that masks protected health information (PHI) in medical text. PHI is any information about an individual's past, present, or future health condition. PHI can include demographic information, medical histories, test results, and other data that could be used to identify an individual.

PHI Masker works by replacing PHI with masked values. The masked values are general placeholders and are not linked to any individual. This makes it difficult for unauthorized individuals to access and use PHI.

To use PHI Masker, you can simply provide it with a medical text that contains PHI. PHI Masker will then mask the PHI in the text and return the masked text.


# How does PHI Masker work?

PHI Masker works by first identifying the PHI in the text using a fine-tuned transformer-based named entity recognition (NER) model. The NER model is trained on a dataset of medical text that contains PHI. Once the PHI has been identified, it is then replaced with masked values. The masked values are general placeholders that represents the context of the text that it contains.

# Examples

**Input**
```txt
The medical record of Michael Davis (born on 09/22/1965), a 58-year-old resident of 789 Oak Lane, Village, shows symptoms of chest pain and shortness of breath.
Immediate intervention was provided to stabilize his condition and prevent further complications.
For any queries, please contact Michael Davis at +1 (555) 789-0123.
```
**Output**
```txt
The medical record of [PERSON] (born on [DATE]), a [AGE] resident of [ADDRESS] shows symptoms of chest pain and shortness of breath.
Immediate intervention was provided to stabilize his condition and prevent further complications.
For any queries, please contact [PERSON] at [PHONE-NUMBER]
```

# Usage
**To Install the required packages, execute the command:**
```cmd
pip install -r requirements.txt
```

**To run the code use the command:**
```cmd
python app.py
```
