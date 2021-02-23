import streamlit as st

###### just for coding purposes, ignore
sex=0
allod=0
b_phq=0


siteHeader = st.beta_container()
dataExploration = st.beta_container()
newFeatures = st.beta_container()
modelTraining = st.beta_container()

with siteHeader:
	st.title(' Calulate probability of improvement in headache after taking ANY OTC')

with dataExploration:
	st.header("**_Patient Parameters_**.")
	#st.text(')

with newFeatures:
	st.markdown('Note. _We do not record any information._')

age = st.number_input('Age in years (18-80)',min_value=18,max_value=80)

gender = st.radio("Gender: ", ('Male', 'Female'))
if(gender == 'Male'):
	sex=1
if (gender == 'Female'):
	sex=0

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
				('Yes','No'))

if(allo == 'Yes'):
	allod=1
if (allo == 'No'):
	allod=0

MSSS = st.number_input('Migraine Symptom Severity Score (MSSS; range:0-21)',min_value=0,max_value=21)

phq = st.number_input('PHQ-9 score (range: 0-27)',min_value=0,max_value=27)
#allo = st.selectbox\
#	('Is there Cutaneous Allodynia?',
 #   options=[1,2],
  #  index=1)

#st.button("Calculate")

if(st.button('Calculate')):

	# MODEL's FORMULA HERE
	e=2.71828

	###### FORMULA FOR 2 HOURs PAIN RELIEF
	intercept=1.78
	b_age=0
	b_sex=0
	b_pain=-0.18
	b_mhd=0
	b_allod=-0.30
	b_MSSS=-0.07
	#Categorical variables with more that 2 categories
	# PHQ
	b_phq1=-0.28
	b_phq2 = -0.36
	b_phq3 = -0.58
	b_phq4 = -0.85

	###### FORMULA FOR 24 HOURs PAIN RELIEF

	intercept_24 = 1.66
	b_age_24 = 0
	b_sex_24 = 0
	b_pain_24 = -0.15
	b_mhd_24 = -0.08
	b_allod_24 = -0.46
	b_MSSS_24 = 0
	# Categorical variables with more that 2 categories
	# PHQ
	b_phq1_24 = -0.14
	b_phq2_24 = -0.55
	b_phq3_24 = -0.64
	b_phq4_24 = -0.80

	# Defining Categories of categorical input
	# PHQ
	phqcat = 0
	if phq<=4:
		phqcat=0
		b_phq=0
	if 5<=phq<=9:
		phqcat=1
		b_phq=b_phq1
	if 10 <= phq <= 14:
		phqcat=2
		b_phq=b_phq2
	if 15 <= phq <= 19:
		phqcat=3
		b_phq=b_phq3
	if 20 <= phq <= 27:
		phqcat=4
		b_phq=b_phq4

	out1=intercept+age*b_age+ sex*b_sex+ pain*b_pain + mhd*b_mhd + allod*b_allod + MSSS*b_MSSS+ phqcat*b_phq
	out2 = intercept + age * b_age_24 + sex * b_sex_24 + pain * b_pain_24 + mhd * b_mhd_24 + allod * b_allod_24 + MSSS * b_MSSS_24 + phqcat * b_phq


	TwoHpf = round(((e**out1)/(1+e**(out1)))*100)
	TwentyTwoHpf=round(((e**out2)/(1+e**(out2)))*100)

	#left, right = st.beta_columns(2)
	st.info("**Probability of pain freedom in _2 hours_ is   _{}".format(TwoHpf) +"%_**")
	st.success("**Probability of pain freedom in _24 hours_ is   _{}".format(TwentyTwoHpf) + "%_**")







