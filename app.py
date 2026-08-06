import streamlit as st
import pickle
import pandas as pd
# Load models
with open('RandomForestRegressor.pkl', 'rb') as file:
    model = pickle.load(file)

with open('LogisticRegression.pkl', 'rb') as file:
    clf_model = pickle.load(file)


tab1, tab2 = st.tabs(["Regression Model", "Classification Model"])


# ---------------- Regression Model ----------------
with tab1:
    st.title("Revenue Prediction")
    st.write("Enter the input features to predict revenue:")

    col1,col2,col3 = st.columns(3)

    with col1:

      Company_Name = st.selectbox(
        "Company Name",
        ["select brand", "nykaa", "purplle", "tira"],
        key="reg_company"
       )

      Campaign_Type = st.selectbox(
        "Campaign Type",
        ["select campaign type", "Social Media", "Paid Ads", "Influencer", "SEO", "Email"],
        key="reg_campaign"
       )

      Target_Audience = st.selectbox(
        "Target Audience",
        ["select target audience", "College Students", "Tier 2 City Customers",
         "Youth", "Premium Shoppers", "Working Women"],
        key="reg_target"
      )

      Duration = st.number_input(
        "Duration",
        min_value=0.0,
        max_value=10000.0,
        value=0.0,
        key="reg_duration"
      )
    
      Channel_Used = st.multiselect(
        "Channel Used",
        ["Instagram", "Google", "Facebook", "Whatsapp", "Email", "YouTube"],
        key="reg_channel"
      )
    with col2:
      Impressions = st.number_input("Impressions", 0.0, 1000000.0, 0.0, key="reg_impressions")
      Clicks = st.number_input("Clicks", 0.0, 1000000.0, 0.0, key="reg_clicks")
      Leads = st.number_input("Leads", 0.0, 1000000.0, 0.0, key="reg_leads")
    
      Conversions = st.number_input("Conversions", 0.0, 1000000.0, 0.0, key="reg_conversions")
      Acquisition_Cost = st.number_input("Acquisition Cost", 0.0, 1000000.0, 0.0, key="reg_cost")
    with col3:
      Language = st.selectbox(
        "Language",
        ["select language", "English", "Hindi", "Tamil", "Bengali"],
        key="reg_language"
      )

      Engagement_Score = st.number_input(
        "Engagement Score",
        0.0,
        1000000.0,
        0.0,
        key="reg_engagement"
     )

      Customer_Segment = st.selectbox(
        "Customer Segment",
        ["select customer segment", "College Students",
         "Tier 2 City Customers", "Youth",
         "Premium Shoppers", "Working Women"],
        key="reg_segment"
     )

      ROI = st.number_input("ROI", 0.0, 100000.0, 0.0, key="reg_roi")

      Profit_Loss = st.selectbox(
        "Profit/Loss",
        ["select profit/loss", "Profit", "Loss"],
        key="reg_profit"
     )

        
    st.markdown("""
                    <style>
                    div.stButton>button{
                    background-color:#FF0000 !
                    important; /*Red*/
                       color;white ! imporant;
                      border-radius:100px ;
                    imporant; /* More Round */
                       width:250px!important;  /*Width*/
                        height:60px !important;    /*Hight*/                  
                    font-size:20px !important;  /*Text Size*/
                    font-weight:bold!important;
                    bord:none !important;
                    }
                    div.stButton>button:hover{
                    background-color:#CC0000 !
                    important; /*Dark Red on Hover*/}
                    </style>
                    """,unsafe_allow_html=True)
                
    

    if st.button("Predict Revenue", key="reg_button"):
        

        if not Channel_Used:
             st.warning("Please select at least one channel")
             st.stop()

        Channel_Used = ", ".join(Channel_Used)

        input_data = pd.DataFrame([[
            Company_Name,
            Campaign_Type,
            Target_Audience,
            Duration,
            Channel_Used,
            Impressions,
            Clicks,
            Leads,
            Conversions,
            Acquisition_Cost,
            Language,
            Engagement_Score,
            Customer_Segment,
            ROI,
            Profit_Loss
        ]],
        columns=[
            "Company_Name",
            "Campaign_Type",
            "Target_Audience",
            "Duration",
            "Channel_Used",
            "Impressions",
            "Clicks",
            "Leads",
            "Conversions",
            "Acquisition_Cost",
            "Language",
            "Engagement_Score",
            "Customer_Segment",
            "ROI",
            "Profit_Loss"
        ]
        )

        prediction = model.predict(input_data)

        st.success(f"Predicted Revenue: {prediction[0]}")


# ---------------- Classification Model ----------------
with tab2:

    st.title("Customer Segment Classification")
    st.write("Enter the input features to classify customer segment:")

    col1,col2,col3 =st.columns(3)

    with col1:
      Company_Name = st.selectbox(
        "Company Name",
        ["select brand", "nykaa", "purplle", "tira"],
        key="clf_company"
       )

      Campaign_Type = st.selectbox(
        "Campaign Type",
        ["select campaign type", "Social Media", "Paid Ads", "Influencer", "SEO", "Email"],
        key="clf_campaign"
      )

      Target_Audience = st.selectbox(
        "Target Audience",
        ["select target audience", "College Students",
         "Tier 2 City Customers", "Youth",
         "Premium Shoppers", "Working Women"],
        key="clf_target"
      )

 
      Duration = st.number_input(
        "Duration",
        0.0,
        10000.0,
        0.0,
        key="clf_duration"
     )

    
      Channel_Used = st.multiselect(
        "Channel Used",
        ["Instagram", "Google", "Facebook", "Whatsapp", "Email", "YouTube"],
        key="clf_channel"
     )

    with col2:
      Impressions = st.number_input("Impressions",0.0,1000000.0,0.0,key="clf_impressions")
      Clicks = st.number_input("Clicks",0.0,1000000.0,0.0,key="clf_clicks")
      Leads = st.number_input("Leads",0.0,1000000.0,0.0,key="clf_leads")
      Conversions = st.number_input("Conversions",0.0,1000000.0,0.0,key="clf_conversions")
      Acquisition_Cost = st.number_input("Acquisition Cost",0.0,1000000.0,0.0,key="clf_cost")
    with col3:
      Revenue = st.number_input(
        "Revenue",
        0.0,
        1000000000.0,
        0.0,
        key="clf_revenue"
     )


      Language = st.selectbox(
        "Language",
        ["select language", "English", "Hindi", "Tamil", "Bengali"],
        key="clf_language"
     )


      Engagement_Score = st.number_input(
        "Engagement Score",
        0.0,
        1000000.0,
        0.0,
        key="clf_engagement"
     )


      Customer_Segment = st.selectbox(
        "Customer Segment",
        ["select customer segment",
         "College Students",
         "Tier 2 City Customers",
         "Youth",
         "Premium Shoppers",
         "Working Women"],
        key="clf_segment"
      )
 

      ROI = st.number_input(
        "ROI",
        0.0,
        1000000.0,
        0.0,
        key="clf_roi"
     )
    st.markdown("""
                  <style>
                  div.stButton>button{
                  background-color:#FF0000 !
                  important; /*Red*/
                     color;white ! imporant;
                    border-radius:100px ;
                  imporant; /* More Round */
                     width:250px!important;  /*Width*/
                      height:60px !important;    /*Hight*/                  
                  font-size:20px !important;  /*Text Size*/
                  font-weight:bold!important;
                  bord:none !important;
                  }
                  div.stButton>button:hover{
                  background-color:#CC0000 !
                  important; /*Dark Red on Hover*/}
                  </style>
                  """,unsafe_allow_html=True)
              

    if st.button("Predict Profit/Loss", key="clf_button"):

        if not Channel_Used:
             st.warning("Please select at least one channel")
             st.stop()

        Channel_Used = ", ".join(Channel_Used)

        input_data = pd.DataFrame([[
            Company_Name,
            Campaign_Type,
            Target_Audience,
            Duration,
            Channel_Used,
            Impressions,
            Clicks,
            Leads,
            Conversions,
            Acquisition_Cost,
            Language,
            Engagement_Score,
            Customer_Segment,
            ROI,
            Revenue
        ]],
        columns=[
            "Company_Name",
            "Campaign_Type",
            "Target_Audience",
            "Duration",
            "Channel_Used",
            "Impressions",
            "Clicks",
            "Leads",
            "Conversions",
            "Acquisition_Cost",
            "Language",
            "Engagement_Score",
            "Customer_Segment",
            "ROI",
            "Revenue"
        ]
        )


        prediction = clf_model.predict(input_data)
        st.success(f"Profit/Loss Prediction: {prediction[0]}")