import time
import streamlit as st
import pandas as pd
import numpy as np
import pandas as pd
from pages.finance_tracker_data.finance import PersonalFinance
import pages.finance_tracker_data.markdown as md
from csv import writer
from csv import reader
from datetime import datetime
import plotly.graph_objects as go

df = PersonalFinance()  

st.sidebar.markdown("## FINANCIAL TOOLS")
sidebar_main = st.sidebar.selectbox('Choose Financial Tools', ['HOME','SIP', 'LUMPSUM', 'FINANCE TRACKER','LOAN TRACKER'])

if sidebar_main == 'HOME' :
    st.title("FINANCE TOOLS") 
    monthly_income = st.number_input("Enter monthly income : ")
    invest_amt = 0
    use_amt = 0
    save_amt = 0
    if monthly_income >= 100000:
        invest_amt = 0.5 * monthly_income
        use_amt = 0.3 * monthly_income
        save_amt = 0.2 * monthly_income
    elif monthly_income >= 60000 and monthly_income < 100000:
        invest_amt = 0.3 * monthly_income
        use_amt = 0.5 * monthly_income
        save_amt = 0.2 * monthly_income
    elif monthly_income >= 30000 and monthly_income < 60000:
        invest_amt = 0.2 * monthly_income
        use_amt = 0.5 * monthly_income
        save_amt = 0.3 * monthly_income
    else:
        invest_amt = 0.2 * monthly_income
        use_amt = 0.6 * monthly_income
        save_amt = 0.2 * monthly_income
    st.subheader(f"You should invest {int(invest_amt)}")
    st.subheader(f"You should save {int(save_amt)}")
    st.subheader(f"You should spend {int(use_amt)}")
    L = [monthly_income, invest_amt, save_amt, use_amt]
    submit = st.button("Submit")
    if submit:
        with open('pages/data/income.csv', 'w') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(['income','invest_amt','save_amt','spend_amt'])
            writer_object.writerow(L)
            f_object.close()
    else : 
        # dropdown
        col1, col2 = st.columns(2)
        with col1 :
            st.write('Max amount spent on food :')
        with col2 :
            check = st.button('check', key = 1)
        
        if check : 
            st.write('I ate ', df.find_max('food')[0], ' on ', df.find_max('food')[2].date(), ' with ', df.find_max('food')[1])
        
        col1, col2 = st.columns(2)
        with col1 :
            st.write('Max amount spent on travel :')
        with col2 :
            check = st.button('check', key = 2)
        
        if check : 
            st.write('I used ', df.find_max('travel')[0], ' on ', df.find_max('travel')[2].date(), ' for ', df.find_max('travel')[1])

        col1, col2 = st.columns(2)
        with col1 :
            st.write('Max amount spent on wants :')
        with col2 :
            check = st.button('check', key = 3)
        
        if check : 
            st.write('I have spent on ', df.find_max('wants')[0], ' on ', df.find_max('wants')[2].date(), ' for ', df.find_max('wants')[1])

    footer = md.footerSection()
    st.markdown(footer,unsafe_allow_html=True) 

elif sidebar_main == 'SIP' : 
    data = pd.read_csv('pages/data/income.csv')
    max_investment_value = int(data['invest_amt'])
    st.image('assets/sip-header.png')
    _LOREM_IPSUM = "Supp! Ever wondered how to make your money work for you while you sip on your coffee? \n this tool helps you keep trackof your sip monthly investment amount and how your interest grows with time :sunglasses:"
    def stream_data():
        for word in _LOREM_IPSUM.split(" "):
            yield word + " "
            time.sleep(0.02)
    if st.button("SiP SiP :coffee:"):
            st.write_stream(stream_data)
    monthly_investment = st.slider("monthly investment", min_value = 500, max_value = max_investment_value, step = 500)
    return_rate = st.slider("expected annual return rate", min_value = 1, max_value = 30, step = 1)
    time_period = st.slider("time period", min_value = 1, max_value = 30, step = 1)
    number_of_months = time_period * 12
    monthly_rate = return_rate / 100 / 12
    future_value = 0
    for i in range(int(number_of_months)):
        future_value += monthly_investment
        future_value *= (1 + monthly_rate)
    st.markdown(f"### Amount invested per month: ₹{monthly_investment} \n ### Expected return rate: {return_rate}%\n ### Time period: {time_period} years")
    st.markdown(f"### Future value of investment:  ₹{int(future_value)}")
    st.markdown(f"### Total investment: ₹{monthly_investment * number_of_months}")
    data['invest_amt'] = int(data['invest_amt']) - monthly_investment
    st.markdown(f"### After investing to sip you have: ₹{int(data['invest_amt'])} left to invest")


elif sidebar_main == 'LUMPSUM' :
    def compound_interest(principal, rate, time):
        return principal * ((1 + rate / 100) ** time)
    st.title("Compound Interest Calculator")
    st.image('assets/lumpsump.png')
    principal = st.number_input("Enter the principal amount:", min_value=0.0)
    rate = st.number_input("Enter the annual interest rate (%):", min_value=0.0)
    time = st.number_input("Enter the time period (in years):", min_value=0.0)
    if st.button("Calculate"):
        result = compound_interest(principal, rate, time)
        st.subheader(f"The amount after {time} years will be: ₹{result:.2f}")



elif sidebar_main == 'FINANCE TRACKER' :
    
    months = [31,29,31,30,31,30,31,31,30,31,30,31]
    st.sidebar.markdown("## Options")
    sidebar_main = st.sidebar.selectbox('Navigation', ['Home', 'See Finances'])
    
    if sidebar_main == 'Home' : 
        st.title('Personal Finance Dashboard')
        st.subheader("Please head over and set your monthly budget. (Ignore if already done)")
        banner = md.headerSection()
        st.markdown(banner,unsafe_allow_html=True)
        
        st.markdown("""
        ## Enter Expense :  
        """)
        #item_date = st.date_input("Enter date of expense : ")
        now = datetime.now()
        item_date = now.strftime("%m/%d/%Y")
        day = now.strftime("%d")
        month = now.strftime('%m')
        print("month is : ",month)
        print("day:", day)
        print(item_date)
        
        option = st.selectbox(
        'Choose type of expense: ',
        ('Charity', 'Clothes', 'Food','Medicine','Study Materials','Travel',"Utilities","Wants"))
        item_title = st.text_input("Enter name of expense : ")
        if item_title == '':
            st.warning('Please enter the name of expense')
        item_price = st.number_input("Enter cost of expense : ")
        if item_price <=0:
            st.warning('Please enter a valid cost of expense')
        submit = st.button("Submit")
        L = [item_date,option,item_title,item_price]
        print(L)

        if submit:
            with open('pages/data/data  - item.csv', 'a') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(L)
                f_object.close()
            lines = []
            with open('pages/data/income.csv', mode ='r') as file:
                csvFile = reader(file)
                for lines in csvFile:
                        continue
                print(lines)
            lines[3] = float(lines[3])
            lines[3] -= L[3]
            with open('pages/data/income.csv', 'w') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(['income','invest_amt','save_amt','spend_amt'])
                writer_object.writerow(lines)
                f_object.close()
            lines = []
            with open('pages/data/income.csv', mode ='r') as file:
                csvFile = reader(file)
                for lines in csvFile:
                        continue
            st.subheader(f"Your daily budget is : {round(float(lines[3])/(months[0] - int(day)),1)}")
            st.subheader(f"The money you can spend this month is : {round(float(lines[3]),1)}")
            if float(lines[3]) < 0:
                st.subheader("You are over your budget!")

    
    elif sidebar_main == 'See Finances' : 
        st.title('Expense dashboard')
        sidebar_sub = st.sidebar.radio('Navigation', ['Expense', 'Category'])
        
        data = df.preprocess_dataframe().tail()

        st.markdown(
                """
                ##### After preprocessing the data looks like this
                """
            )
        st.dataframe(data.head())
        if sidebar_sub == 'See Finances' : 

            st.markdown(
                """
                ##### Check the expenses 
                """
            ) 
            
            col1, col2 = st.columns(2)
            with col1 : 
                daily = st.button('Daily') 

            with col2 :  
                monthly = st.button('Monthly')
            
            if monthly : 
                st.plotly_chart(df.plot_expenses('month')[0])
                percent = df.plot_expenses('month')[1]

                if percent > 0 : 
                    st.write('which is ',percent,'%',' higher than prev month')
                else : 
                    st.write('which is ',abs(percent),'%',' lower than prev month')

            else : 
                st.plotly_chart(df.plot_expenses('date'))

        elif sidebar_sub == 'Category' :
            st.markdown(
                """
                ##### Category wise expenses 
                """
            ) 
            st.plotly_chart(df.share_of_category())

        

        elif sidebar_sub == 'total expenses' : 
            st.markdown(
                """
                ##### Total Expenses 
                """
            ) 
            st.plotly_chart(df.total_spending()[0])
            st.write('Total amount spent is ',df.total_spending()[1])

        else : 
            st.markdown(
                """
                ##### Spending on items 
                """
            ) 
            st.plotly_chart(df.plot_treemap())        


elif sidebar_main == 'LOAN TRACKER' :
    st.header("Learn how your finances will be impacted if you take a new loan:")

    # Input fields for loan details
    goal = st.text_input("Enter loan title:")
    P = st.number_input("Enter Loan amount:", min_value=0.0)
    interest = st.number_input("Enter interest rate annually:", min_value=0.0) / 100
    interest /= 12  # Convert annual interest to monthly

    # Initialize variables
    expenses = ['Charity', 'Clothes', 'Food', 'Medicine', 'Study Materials', 'Travel', "Utilities", "Wants"]
    expenses_amt = [0] * len(expenses)
    emi = 0

    # Display loan goal
    if goal:
        st.write(f"# {goal}")

    # Calculate EMI if inputs are valid
    if P > 0 and goal and interest > 0:
        n_years = st.slider('Choose Time period in years', step=1, max_value=30)
        n_months = n_years * 12
        emi = P * interest * (((1 + interest) ** n_months) / (((1 + interest) ** n_months) - 1))
        amt_owned = emi * n_months

        # Button to calculate and display results
        if st.button("Calculate"):
            st.markdown(f"### Estimated Monthly Installment: {int(emi)}")
            st.markdown(f"### Total Amount Owed to Lender: {int(amt_owned)}")

            # Read income data
            with open('pages/data/income.csv', mode='r') as file:
                csvFile = reader(file)
                for lines in csvFile:
                    if len(lines) > 3:  # Ensure enough elements
                        income_amount = float(lines[3])
                        st.markdown(f"### Total Amount Left This Month: {int(income_amount - emi)}")
                    else:
                        st.error("Income data format error: insufficient columns.")

            # Read expenses from CSV
            with open('pages/data/data - item.csv', 'r') as f_object:
                csvFile = reader(f_object)
                for lines in csvFile:
                    if len(lines) > 3:  # Ensure enough elements
                        for i, expense in enumerate(expenses):
                            if expense == lines[1]:
                                expenses_amt[i] += int(float(lines[3]))

        # Prepare data for pie charts
        labels = [expense for i, expense in enumerate(expenses) if expenses_amt[i] > 0] + [goal]
        sizes = [amt for amt in expenses_amt if amt > 0] + [int(emi)]

        # Read income data for budget pie chart
        with open('pages/data/income.csv', mode='r') as file:
            csvFile = reader(file)
            for lines in csvFile:
                if len(lines) > 3:  # Ensure enough elements
                    total_budget = float(lines[3])
                    labels2 = ['Total Monthly Budget', goal]
                    sizes2 = [total_budget, int(emi)]
                else:
                    st.error("Income data format error: insufficient columns.")

        # Create pie charts
        fig = go.Figure(data=[go.Pie(labels=labels, values=sizes)])
        fig.update_traces(hoverinfo='label+percent', textinfo='percent', textfont_size=20)
        fig.update_layout(title_text='Monthly Expenses', title_font_size=24)

        fig1 = go.Figure(data=[go.Pie(labels=labels2, values=sizes2)])
        fig1.update_traces(hoverinfo='label+percent', textinfo='percent', textfont_size=20)
        fig1.update_layout(title_text='Loan vs Allocated Monthly Budget', title_font_size=24)

        # Checkbox to display pie charts
        if st.checkbox("Do you want to see your monthly expense pie chart?"):
            st.plotly_chart(fig)
            st.plotly_chart(fig1)
