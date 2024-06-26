import streamlit as st
import pandas as pd
import plotly.express as px
import base64 
import csv
import matplotlib.pyplot as plt
from io import StringIO, BytesIO
import math
import os
from itertools import zip_longest

hide_st_style="""
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden}
</style>
"""
st.markdown(hide_st_style,unsafe_allow_html=True)


st.title('Culturals📈')
st.subheader('Feed me with your Excel file')
st.write("ST.JOSEPH'S COLLEGE(AUTONOMOUS)")

#file upload
uploaded_file = st.file_uploader('Choose a CSV file', type='CSV')
if uploaded_file:
  st.markdown("---")
  df=pd.read_csv(uploaded_file)
  st.dataframe(df)
  #title
  title = st.text_input(
        "Enter Folder Name 👇" )
  st.write('Your folder Name is:',title)
  a=[]
  for i in df.head(0):
    if(i.title()!='Sno' and i.title()!='Name' and i.title()!='Dno' and i.title()!='Department' and i.title()!='Class'):
         a.append(i)
  groupby_column=st.selectbox('what would you like to analyse?',a)


  #post
  df=df.dropna(subset=[groupby_column])
  a = df["Name"].dropna().tolist()
  b= df["Dno"].dropna().tolist()
  c= df["Department"].dropna().tolist()
  d = df["Class"].dropna().tolist()
  e = df[groupby_column].dropna().tolist()

  #write 
  folder_input = 'D:/streamlit/Culturals/Backup/'
  file_input =title+'.csv'
  f=[a,b,c,d,e] 
  export_data = zip_longest(*f, fillvalue = '')
  with open( os.path.join(folder_input, file_input), 'w', encoding="ISO-8859-1", newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(('Name', 'Dno','Department','Class','Event'))
      wr.writerows(export_data)
  myfile.close()
  
  #sumbit
  if st.button("Submit"): 
    def main():
    #display
       col1, col2= st.columns([2,3])
       with col1:
         st.subheader('Data')
         data=pd.read_csv(r'D:/streamlit/Culturals/Backup/'+title+'.csv')
         st.dataframe(data, width = 400,height=300)
         def generate_csv():
            df = pd.DataFrame(data)
            return df
         df = generate_csv()
         csv_data = df.to_csv(index=False)
         st.download_button(label="Download CSV", data=csv_data, file_name=title+'.csv', mime='text/csv')
    if _name_ == '_main_':
main()