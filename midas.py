###### App to calculate midas score


import streamlit as st
import streamlit.components.v1 as components



q1 = st.number_input('1. On how many days in the last 3 months did you miss work or school because of your headaches? (0-90)',min_value=0,max_value=90)
q2 = st.number_input('2. How many days in the last 3 months was your productivity at work or school reduced by half or more because of your headaches? (0-90)',min_value=0,max_value=90)
q3 = st.number_input('3. On how many days in the last 3 months did you not do household work (such as housework, home repairs and maintenance, shopping, caring for children and relatives) because of your headaches? (0-90)',min_value=0,max_value=90)
q4 = st.number_input('4. How many days in the last 3 months was your productivity in household work reduced by half of more because of your headaches? (0-90)',min_value=0,max_value=90)
q5 = st.number_input('5. On how many days in the last 3 months did you miss family, social or leisure activities because of your headaches? (0-90)',min_value=0,max_value=90)

midastotal=q1+q2+q3+q4+q5
midasgrade=0
midasdis='none'
if midastotal<6:
	midasgrade=1
	midasdis='Little or No Disability'
if  6<= midastotal <=10:
	midasgrade = 2
	midasdis='Mild Disability'
if  11<= midastotal <=20:
	midasgrade = 3
	midasdis='Moderate Disability'
if midastotal > 20:
	midasgrade = 4
	midasdis='Severe Disability'



st.info("**MIDAS Score:    _{}".format(midastotal) +"_**")
st.success("**MIDAS Grade:    _{}".format(midasgrade) + "_**")
st.error("**Level of Disability:    _{}".format(midasdis) + "_**")









