###### App to calculate PHQ9 score


import streamlit as st
import streamlit.components.v1 as components
st.subheader('Ask the patient: how often have they been bothered by the following over the past 2 weeks?')

q1 = st.radio("Little interest or pleasure in doing things?",
				('Not at all','Several days', 'More than half the days', 'Nearly every day'))

if(q1 == 'Not at all'):
	q1s=0
if(q1 == 'Several days'):
	q1s=1
if(q1 == 'More than half the days'):
	q1s=2
if(q1 == 'Nearly every day'):
	q1s=3

q2 = st.radio("Feeling down, depressed, or hopeless?",
				('Not at all','Several days', 'More than half the days', 'Nearly every day'))

if(q2 == 'Not at all'):
	q2s=0
if(q2 == 'Several days'):
	q2s=1
if(q2 == 'More than half the days'):
	q2s=2
if(q2 == 'Nearly every day'):
	q2s=3


q3 = st.radio("Trouble falling or staying asleep, or sleeping too much?",
				('Not at all','Several days', 'More than half the days', 'Nearly every day'))

if(q3 == 'Not at all'):
	q3s=0
if(q3 == 'Several days'):
	q3s=1
if(q3 == 'More than half the days'):
	q3s=2
if(q3 == 'Nearly every day'):
	q3s=3

q4 = st.radio("Feeling tired or having little energy?",
				('Not at all','Several days', 'More than half the days', 'Nearly every day'))

if(q4 == 'Not at all'):
	q4s=0
if(q4 == 'Several days'):
	q4s=1
if(q4 == 'More than half the days'):
	q4s=2
if(q4 == 'Nearly every day'):
	q4s=3


q5 = st.radio("Poor appetite or overeating?",
				('Not at all','Several days', 'More than half the days', 'Nearly every day'))

if(q5 == 'Not at all'):
	q5s=0
if(q5 == 'Several days'):
	q5s=1
if(q5 == 'More than half the days'):
	q5s=2
if(q5 == 'Nearly every day'):
	q5s=3

q6 = st.radio("Feeling bad about yourself — or that you are a failure or have let yourself or your family down?",
				('Not at all','Several days', 'More than half the days', 'Nearly every day'))

if(q6 == 'Not at all'):
	q6s=0
if(q6 == 'Several days'):
	q6s=1
if(q6 == 'More than half the days'):
	q6s=2
if(q6 == 'Nearly every day'):
	q6s=3

q7 = st.radio("Trouble concentrating on things, such as reading the newspaper or watching television?",
				('Not at all','Several days', 'More than half the days', 'Nearly every day'))

if(q7 == 'Not at all'):
	q7s=0
if(q7 == 'Several days'):
	q7s=1
if(q7 == 'More than half the days'):
	q7s=2
if(q7 == 'Nearly every day'):
	q7s=3

q8 = st.radio("Moving or speaking so slowly that other people could have noticed? Or so fidgety or restless that you have been moving a lot more than usual?",
				('Not at all','Several days', 'More than half the days', 'Nearly every day'))

if(q8 == 'Not at all'):
	q8s=0
if(q8 == 'Several days'):
	q8s=1
if(q8 == 'More than half the days'):
	q8s=2
if(q8 == 'Nearly every day'):
	q8s=3

q9 = st.radio("Thoughts that you would be better off dead, or thoughts of hurting yourself in some way?",
				('Not at all','Several days', 'More than half the days', 'Nearly every day'))

if(q9 == 'Not at all'):
	q9s=0
if(q9 == 'Several days'):
	q9s=1
if(q9 == 'More than half the days'):
	q9s=2
if(q9 == 'Nearly every day'):
	q9s=3



phq9tot=q1s+q2s+q3s+q4s+q5s+q6s+q7s+q8s+q9s

st.info("**PHQ 9 score:    _{}".format(phq9tot) +"_**")
# st.success("**MIDAS Grade:    _{}".format(midasgrade) + "_**")
if q9s>0:
	st.error("**Warning**:    _This patient is having thoughts concerning for suicidal ideation or self-harm. "
			 "Patient needs immidiate psychiatric evaluation and should be probed further, referred, "
			 "or transferred for emergency psychiatric evaluation as clinically appropriate and depending on clinician overall risk assessment._")











