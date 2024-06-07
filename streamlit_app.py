import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

# Page title
st.set_page_config(page_title='Loan Application Risk', page_icon='📊')
st.title('🎟️🎯 Loan Application Risk Model')

with st.expander('About this app'):
  st.markdown('**What can this app do?**')
  st.info('This app is intended to use a trained Machine Learning Model to determine the Risk Status of a Loan Application.')
  st.markdown('**How to use the app?**')
  st.warning('To engage with the app, 1. Use the drop-downs to enter data about a particular loan applicant. ')
  
st.subheader('Risky or Not?')

# Load data
#df = pd.read_csv('data/movies_genres_summary.csv')
#df.year = df.year.astype('int')

# Input widgets
## Marital Status selection
marital_selection = st.multiselect('Marital Status', ['Single','Married'])

## House_Ownership selection
house_ownership = st.multiselect('Select house ownership category', ['neither rent nor own', 'owned', 'rented'])

## House_yrs selection
house_yrs = st.slider('Select years in your current home', 2, 70,(2,70))

## Car_Ownership selection
car_ownership = st.multiselect('Select car ownership category', ['no', 'yes'])

## Age selection
age = st.slider('Select age', 22, 70, (22, 70))

## Income selection
income = st.number_input('Enter the annual income')

profession_list = ['Engineer','Physician', 'Statistician', 'Web_designer', 'Psychologist', 
                  'Computer_hardware_engineer', 'Drafter', 'Magistrate', 'Fashion_Designer', 
                  'Air_traffic_controller', 'Comedian', 'Technical_writer', 'Hotel_Manager',
                  'Financial_Analyst', 'Graphic_Designer', 'Flight_attendant', 'Secretary', 
                  'Software_Developer', 'Police_officer', 'Computer_operator', 'Politician',
                  'Microbiologist', 'Technician', 'Artist', 'Lawyer', 'Consultant', 'Dentist',
                  'Scientist', 'Surgeon', 'Aviator', 'Technology_specialist', 'Surveyor', 'Geologist',
                  'Analyst', 'Army_officer', 'Architect', 'Chef', 'Librarian', 'Civil_engineer', 'Designer',
                  'Economist', 'Firefighter', 'Chartered_Accountant', 'Civil_servant', 'Official']

## Profession selection
profession = st.multiselect('Enter profession', profession_list)

## Yrs in job selection
job_yrs = st.number_input("Enter the number of years at current job.")

## State selection
state_list = ['Uttar_Pradesh', 'Maharashtra', 'Andhra_Pradesh', 'West_Bengal', 'Bihar', 'Tamil_Nadu', 
              'Madhya_Pradesh', 'Karnataka', 'Gujarat', 'Rajasthan', 'Jharkhand','Haryana', 
              'Telangana', 'Assam', 'Kerala', 'Delhi', 'Punjab', 'Odisha', 'Chhattisgarh', 'Other']

state = st.multiselect('In which state do you reside?', state_list)

#reshaped_df = df_selection.pivot_table(index='year', columns='genre', values='gross', aggfunc='sum', fill_value=0)
#reshaped_df = reshaped_df.sort_values(by='year', ascending=False)


# Display DataFrame

#df_editor = st.data_editor(reshaped_df, height=212, use_container_width=True,
#                            column_config={"year": st.column_config.TextColumn("Year")},
#                            num_rows="dynamic")
#df_chart = pd.melt(df_editor.reset_index(), id_vars='year', var_name='genre', value_name='gross')

# Display chart
#chart = alt.Chart(df_chart).mark_line().encode(
#            x=alt.X('year:N', title='Year'),
 #           y=alt.Y('gross:Q', title='Gross earnings ($)'),
#            color='genre:N'
#            ).properties(height=320)
#st.altair_chart(chart, use_container_width=True)
