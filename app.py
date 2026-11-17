import streamlit as st
import pickle
import nltk
import re

nltk.download('punkt')
nltk.download('stopwords')

model = pickle.load(open('resume_model.pkl', 'rb'))

def CleanResume(txt):
    CleanText=re.sub('http\S+\s','',txt)
    CleanText=re.sub('#\S+\s', '',CleanText)
    CleanText=re.sub('@\S+','', CleanText)
    CleanText=re.sub('RT|cc', '', CleanText)
    #CleanText=re.sub('[%s]' % re.escape("""~!@#$%^&*()_+{|}[\]:;./''<>?+=-"""),'',CleanText)
    CleanText=re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""),'',CleanText)
    CleanText=re.sub(r'[^\x00-\x7f]' ,'', CleanText)
    CleanText=re.sub('\s+',' ',CleanText)

    return CleanText


# Web App
def main():

    st.title('Resume Screening App')

    uploade_file = st.file_uploader('Upload Resume',type=['txt','pdf'])

    if uploade_file is not None:

        try:
            resume_bytes = uploade_file.read()
            resume_text = resume_bytes.decode('utf-8')
        
        except UnicodeDecodeError:
            # when file is uploaded then some reasons the file is failed utf-8 then
            
            resume_text = resume_bytes.decode('latin-1')


            cleaned_Resume = CleanResume(resume_text)
            prediction_id = model.predict([cleaned_Resume])[0]
        #st.write(prediction_id)

        Category_mapping = {
            6: 'Data Science',
            12: 'HR',
            0: 'Advocate',
            1: 'Arts',
            24: 'Web Designing',
            16: 'Mechanical Engineer',
            22: 'Sales',
            14: 'Health And Fitness',
            5: 'Civil Engineer',
            15: 'Java Developer',
            4: 'Business Analyst',
            21: 'SAP Developer',
            2: 'Automation Testing',
            11: 'Electrical Engineer',
            18: 'Operation Manager',
            20: 'Python Developer',
            8: 'DevOps',
            17: 'Network Security',
            19: 'PMO',
            7: 'Database',
            13: 'Hadoop',
            10: 'ETL Developer',
            9: 'Dot Net Developer',
            3: 'BlockChain',
            23: 'Testing'
             
              }        
        Category_name = Category_mapping.get(prediction_id,'Unknown')
        st.write('Resume is :-',Category_name)
#python main

if __name__ == '__main__':
    main()
