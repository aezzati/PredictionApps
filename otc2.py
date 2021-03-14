import streamlit as st
import streamlit.components.v1 as components





###### just for coding purposes, can ignore
sex=0
allod=0
b_phq=0

# ADD LOGO OF OUR PAGE TO THE SIDEBAR
# st.sidebar.image('./logo.png')

# with siteHeader:
#st.sidebar.title(' OTC FOR MIGRAINE')

# with dataExploration:
st.header("**_Patient Parameters_**.")
	#st.text(')

# with newFeatures:
# st.sidebar.markdown("**_When to use?_** Can be used to estimate if _Over The Counter_ meds can improve patient's headache")
# st.sidebar.markdown('**_Limitations:_** Models are developed only for patients with diagnosis of _Episodic Migraine_.')
#st.sidebar.markdown('**_Note._** This app  does not record any information entered by users.')

#st.sidebar.error(
#	"""
#	[Disclaimer](https://www.neurodiction.com/disclaimer)
#	"""
#)

# age = st.number_input('Age in years (18-80)',min_value=18,max_value=80)

# gender = st.radio("Gender: ", ('Male', 'Female'))
# if(gender == 'Male'):
#	sex=1
# if (gender == 'Female'):
#	sex=0

pain = st.slider\
	('On Average how bad is the pain intensity? (1-10)',
	min_value=1, max_value=10,
    value=1,
    step=1)

mhd = st.slider\
	('Number of days with headache per month (1-15)',
	min_value=1, max_value=15,
    value=1,
    step=1)

allo = st.radio('Does patient have Cutaneous Allodynia?',
				('No','Yes'))

if(allo == 'Yes'):
	allod=1
if (allo == 'No'):
	allod=0

MSSS = st.number_input('Migraine Symptom Severity Score (MSSS; range:0-21)',min_value=0,max_value=21)

phq = st.number_input('PHQ-9 score (range: 0-27)',min_value=0,max_value=27)

medclass = st.radio('Which medication do you want to use?',
				('Acetaminophen (Tylenol, Midrin)'
				 ,'Aspirin'
				 ,'NSAIDs (naproxen [Aleve], ibuprofen [Motrin, Advil], ketorolac tromethamine [Toradol])'
				 , 'Caffeine Combination products (Excedrin, Excedrin Migrain)'))
med=0
if(medclass == 'Acetaminophen (e.g., Tylenol, Midrin)'):
	med= 0
if (medclass == 'Aspirin'):
	med= 1
if (medclass == 'NSAIDs (naproxen [Aleve], ibuprofen [Motrin, Advil], ketorolac tromethamine [Toradol])'):
	med = 2
if (medclass == 'Caffeine Combination products (Excedrin, Excedrin Migrain)'):
	med = 3

#allo = st.selectbox\

# st.button("Calculate")
#st.balloons()

if(st.button('CALCULATE')):
	#st.balloons()
	# MODEL's FORMULA HERE
	e=2.71828
########
	###### FORMULA FOR #############    2    ###########HOURs PAIN RELIEF


	intercept=2.7
	#b_age=0
	#b_sex=0
	b_pain=-0.16
	b_mhd=0
	b_allod=-0.30
	b_MSSS=-0.07
	#Categorical variables with more that 2 categories
	# PHQ
	b_phq1=-0.33
	b_phq2 = -0.36
	b_phq3 = -0.43
	b_phq4 = -0.83
	# med
	b_med=0
	if med == 0:
		b_med=0
	if med == 1:
		b_med=-0.12
	if med == 2:
		b_med=0.15
	if med == 3:
		b_med=0.44


	###### FORMULA FOR #############    24    ###########HOURs PAIN RELIEF

	intercept_24 = 1.95
	# b_age_24 = 0
	# b_sex_24 = 0
	b_pain_24 = -0.13
	b_mhd_24 = -0.09
	b_allod_24 = -0.41
	b_MSSS_24 = -0.035
	# Categorical variables with more that 2 categories
	# PHQ
	b_phq1_24 = -0.003
	b_phq2_24 = -0.61
	b_phq3_24 = -0.43
	b_phq4_24 = -0.7
	b_med_24=0
	if med == 0:
		b_med_24=0
	if med == 1:
		b_med_24=0.012
	if med == 2:
		b_med_24=0.13
	if med == 3:
		b_med_24=0.40


	# Defining Categories of categorical input
	# PHQ
	b_phq = 0
	b_phq_24 = 0
	if phq<=4:
		b_phq=0
		b_phq_24 = 0
	if 5<=phq<=9:
		b_phq=b_phq1
		b_phq_24 = b_phq1_24
	if 10 <= phq <= 14:
		b_phq=b_phq2
		b_phq_24 = b_phq2_24
	if 15 <= phq <= 19:
		b_phq=b_phq3
		b_phq_24 = b_phq3_24
	if 20 <= phq <= 27:
		b_phq=b_phq4
		b_phq_24 = b_phq4_24




	out1=intercept + pain*b_pain + mhd*b_mhd + allod*b_allod + MSSS*b_MSSS + b_phq + b_med
	out2 = intercept + pain * b_pain_24 + mhd * b_mhd_24 + allod * b_allod_24 + MSSS * b_MSSS_24 +  b_phq_24 + b_med_24


	TwoHpf = round(((e**out1)/(1+e**(out1)))*100)
	TwentyTwoHpf=round(((e**out2)/(1+e**(out2)))*100)

	#left, right = st.beta_columns(2)
	st.info("**Probability of pain freedom in _2 hours_ is   _{}".format(TwoHpf) +"%_**")
	st.success("**Probability of sustained pain relief in _24 hours_ is   _{}".format(TwentyTwoHpf) + "%_**")

	left, right = st.beta_columns(2)
	with left:
		st.error(
			"""
			[Disclaimer](https://www.neurodiction.com/disclaimer) 
			"""
		)

	#with right:
	#	right.subheader('Evidence')
	#	st.markdown('This app is developed based on results of studies by our team at NEURODICTION on AMPP dataset. '
	#				'The mansucript is currently under review. Please [contact us](https://www.neurodiction.com/contact) '
	#				'if you have questions or need a copy of the manuscript.')











