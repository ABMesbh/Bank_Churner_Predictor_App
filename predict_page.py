import streamlit as st
import numpy as np
from joblib import load
from sklearn.ensemble import RandomForestClassifier



model = load("ML_model.joblib")
Education = "College,Doctorate,Graduate,High School,Post-Graduate,Uneducated,Unknown_Edu_Level".split(",")
Marital_status = "Divorced,Married,Single,Unknown_Mar_Status".split(",")
card = "Blue,Gold,Platinum,Silver".split(",")
income = "$120K +,$40K - $60K,$60K - $80K,$80K - $120K,Less than $40K,Unknown_Income".split(",")
sex = ["M","F"]

def show_predict_page():
    st.title("Bank churner Predictor app")

    st.write("""### We need some information to start predicting""")
    Months_on_book= st.sidebar.slider('How long customer has been on the books', 13, 56, step=1)
    Total_Relationship_Count= st.sidebar.slider('Total number of relationships customer has with the credit card provider', 1, 6, step=1)
    Months_Inactive_12_mon = st.sidebar.slider('Number of months customer has been inactive in the last twelve months', 0, 6, step=1)
    Contacts_Count_12_mon = st.sidebar.slider('Number of contacts customer has had in the last twelve months',  0, 6, step=1)
    Credit_Limit = st.sidebar.slider('Credit limit of customer', 0.0, 35000.0, step=0.1)
    Total_Revolving_Bal = st.sidebar.slider('Total revolving balance of customer', 0.0, 1500.0, step=0.1)
    Avg_Open_To_Buy = st.sidebar.slider('Average open to buy ratio of customer', 0.0, 35000.0, step=0.1)
    Total_Amt_Chng_Q4_Q1 = st.sidebar.slider('Total amount changed from quarter 4 to quarter 1', 0.0, 4.0, step=0.1)
    Total_Trans_Amt = st.sidebar.slider('Total transaction amount', 500.0, 19000.0, step=0.1)
    Total_Trans_Ct  = st.sidebar.slider('Total transaction count', 10.0, 140.0, step=0.1)
    Total_Ct_Chng_Q4_Q1 = st.sidebar.slider('Total count changed from quarter 4 to quarter 1', 0.0, 4.0, step=0.1)
    Avg_Utilization_Ratio = st.sidebar.slider('Average utilization ratio of customer', 0.0, 1.0, step=0.1)

    

    Edu_select = st.selectbox("Education Level", Education)
    Status_select = st.selectbox("Marital status", Marital_status)
    card_select = st.selectbox("Card type", card)
    income_select = st.selectbox("Income", income)
    sex_select = st.selectbox("Gender", sex )
    age = st.slider("Age", 26, 70 , 1)
    dependent_count  = st.slider("Number of dependents", 0,5,1)

    # a = [35.928409,3.812580,	2.341167,	2.455317,	8631.953698,	1162.814061,	7469.139637,	0.759941,	4404.086304,	64.858695,  0.712222,   0.274894]
    # b = [49,	2,	3,	3,	1438.3,	0,	1438.3,	1.047,	692,	16,	0.6,	0]


    ok = st.button("Start predicting")
    if ok:
        edu = [ 1 if Edu_select == Education[i] else 0 for i in range(7)   ]
        M_s = [1 if Status_select == Marital_status[i] else 0 for i in range(4) ]
        c_t = [1 if  card_select == card[i] else 0 for i in range(4) ]
        inco = [1  if income_select == income[i] else 0 for i in range(6)]
        gen = [1 if sex_select == sex[i] else 0 for i in range(2) ]
        input = [age,dependent_count,Months_on_book,Total_Relationship_Count,Months_Inactive_12_mon,Contacts_Count_12_mon,Credit_Limit,Total_Revolving_Bal,Avg_Open_To_Buy,Total_Amt_Chng_Q4_Q1,Total_Trans_Amt,Total_Trans_Ct,Total_Ct_Chng_Q4_Q1,Avg_Utilization_Ratio] + edu + M_s + c_t + inco + gen
        #Attrited Customer	62	F	0	Graduate	Married	Less than $40K	Blue	


        X = np.array(input).reshape(1, -1)
        if model.predict(X) == 0:
            st.write("the client is not going to churn " )
        else :  
            st.write("the client will churn " )



