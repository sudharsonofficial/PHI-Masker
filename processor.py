import math
import re
from simpletransformers.ner import NERModel
import nltk

class Processor:
    """
    A class that processes text and extracts important information from it.

    Attributes:
        labels (list): A list of labels that the NER model can identify.
        model (NERModel): A NER model that is used to identify entities in text.

    Methods:
        predict(text:str) -> list: Predicts the entities in a piece of text.
        strip(text:str) -> str: Strips the text of non-alpha-numeric characters.
        mask(text:str, prediction:list) -> str: Masks the entities in the text with their corresponding labels.
        delete_repeated(text:str) -> str: Deletes repeated entities from the text.
        process(text:str) -> str: Processes the text and returns a string with the extracted information.
    """
    
    def __init__(self) -> None:
        """
        Initializes the Processor class.
        """
        self.labels = ['PERSON', 'OTHER', 'DATE', 'ADDRESS', 'MEDICAL', 'PHONE-NUMBER', 'AGE']


        self.model = NERModel('bert', 'saved_model', labels = self.labels, use_cuda = False)

        

    def __predict(self, text:str) -> list:
        """
        Predicts the entities in a piece of text.

        Args:
            text (str): The text to be processed.

        Returns:
            list: A list of entities in the text.
        """
        prediction, _ = self.model.predict([text])

        return prediction
    

    def __strip(self, text:str) -> str:
        """
        Strips the text of non-alpha-numeric characters.

        Args:
            text (str): The text to be processed.

        Returns:
            str: The stripped text.
        """
        text = text.lower()
        words = text.split()
        res = ""
        for word in words:
            pattern = r"^[^0-9a-zA-Z+]+|[^0-9a-zA-Z+]+$"
            
            word = re.sub(pattern, "", word)
            res += word + " "

        res = res.removeprefix("description")
        return res.strip()
    

    def __mask(self, text:str, prediction:list) -> str:
        """
        Masks the entities in the text with their corresponding labels.

        Args:
            text (str): The text to be processed.
            prediction (list): A list of entities in the text.

        Returns:
            str: The text with the entities masked.
        """
        find_list = []
        replace_list = []

        for i in prediction[0]:
            find = list(i.items())[0][0]
            replace = list(i.items())[0][1]

            if(replace!="OTHER" and replace!="MEDICAL"):
                find_list.append(find)
                replace_list.append(f"[{replace}]")


        text_list = text.split()

        res = ""

        for word in text_list:

            l = word.lower()

            for i in range(len(find_list)):
                if(find_list[i] in l):
                    res += l.replace(find_list[i], replace_list[i],1) + " "
                    find_list = find_list[i+1:]
                    replace_list = replace_list[i+1:]
                    break
            else:
                res += word + " "

        return res  
    
    
    

    def __delete_repeated(self, text:str) -> str:
        """
        Deletes repeated entities from the text.

        Args:
            text (str): The text to be processed.

        Returns:
            str: The text with the repeated entities deleted.
        """

        labels = [f"[{label}]" for label in self.labels]


        text_list = text.split()

        res_list = []

        for text in text_list:
            for label in labels:
                if(label in text):
                    recent = label
                    try:
                        if(recent not in res_list[-1]):
                            res_list.append(text)
                        break
                    except:
                        pass
            else:
                res_list.append(text)

        return " ".join(res_list)


    def process(self, text:str) -> str:
        """
        Processes the text and returns a string with the extracted information.

        Args:
            text (str): The text to be processed.

        Returns:
            str: The text with the extracted information.
        """

        stripped_text = self.__strip(text)

        # print(stripped_text)
        prediction = self.__predict(stripped_text)
        print(prediction[0])
 
        res = self.__mask(text, prediction)

        res = self.__delete_repeated(res)

        return res
    
if __name__ == "__main__":
    txt = """
    On June 26, 2023, at approximately 10:30 AM, a medical incident occurred involving a patient named John Doe. Mr. Doe was admitted to the hospital's emergency department with symptoms of acute abdominal pain and nausea. The incident was immediately addressed by the medical staff, including a team of doctors and nurses.

Upon assessment, it was determined that Mr. Doe's symptoms were indicative of a potential gastrointestinal issue. Diagnostic tests, including blood work and imaging, were promptly ordered to further evaluate the underlying cause. The medical team worked efficiently to provide appropriate care and comfort to the patient during this challenging time.

Throughout the incident, close monitoring of vital signs, pain management, and regular communication with Mr. Doe and his family were prioritized. The medical staff ensured a compassionate and professional environment, offering support and reassurance to alleviate any concerns.

Consultations with relevant specialists, such as gastroenterologists and surgeons, were arranged to obtain expert opinions and assist in formulating an accurate diagnosis and treatment plan. Collaborative efforts were made to ensure the best possible outcome for Mr. Doe's condition.

As the incident unfolded, detailed documentation of assessments, interventions, and medication administration was maintained in the patient's electronic health record. The interdisciplinary healthcare team worked in unison, following established protocols and guidelines to deliver comprehensive care.

The incident is currently ongoing, with further investigations and treatment interventions in progress. Regular updates will be provided to Mr. Doe and his family, ensuring transparency and involvement in the decision-making process.

The medical incident involving Mr. John Doe highlights the dedication and commitment of the healthcare professionals involved, striving to provide optimal care, accurate diagnosis, and appropriate treatment for the patient's condition.
    """

    p = Processor()

    txt_list = txt.split()

    start = 0
    end = 100

    for _ in range(math.ceil(len(txt_list)/100)):
        s = " ".join(txt_list[start:end])
        p.process(s)
        start += 100
        end += 100


    print(len(txt_list))


    # for sentence in txt:
    #     p.process(sentence)