import streamlit as st
import pickle

model= pickle.load(open(r'D:\VIT\Sem 5 (3 yr)\vegatble_forcatsing\Vegatable-Price-Forecasting\models\rf1.pkl','rb'))

def run():
    
    
    ## For state
    gen_display = ('Andhra Pradesh','Chattisgarh','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu and Kashmir','Jharkhand','Karnataka','Kerala','Madhya Pradesh','Maharashtra','Nagaland','NCT of Delhi','Odisha','Punjab','Rajasthan','Telangana','Tripura','Uttar Pradesh','Uttrakhand','west Bengal')
    gen_options = list(range(len(gen_display)))
    state = st.selectbox("state",gen_options, format_func=lambda x: gen_display[x])
    
    ## For district
    gen_display = ('Andhra Pradesh','Chattisgarh','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu and Kashmir','Jharkhand','Karnataka','Kerala','Madhya Pradesh','Maharashtra','Nagaland','NCT of Delhi','Odisha','Punjab','Rajasthan','Telangana','Tripura','Uttar Pradesh','Uttrakhand','west Bengal')
    gen_options = list(range(len(gen_display)))
    district = st.selectbox("district",gen_options, format_func=lambda x: gen_display[x])

    ## For month
    mar_display = ('','January','Febuary','March','April','May','June','july','Augest','September')
    mar_options = list(range(len(mar_display)))
    month = st.selectbox("month", mar_options, format_func=lambda x: mar_display[x])

    ## day
    dep_display = ('no','One','Two','More than Two')
    dep_options = list(range(len(dep_display)))
    day = st.selectbox("Dependents",  dep_options, format_func=lambda x: dep_display[x])






    if st.button("Submit"):
    
        features = [[state, district, month, day]]
        print(features)
        prediction = model.predict(features)
        prediction= prediction/100
        st.text(prediction)

run()