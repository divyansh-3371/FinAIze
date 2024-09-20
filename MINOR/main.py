import streamlit as st
st.set_page_config(
    page_title="FinAIze",
    page_icon="💸",
    layout="centered",
    initial_sidebar_state="expanded")
st.image("assets/logo.png")
st.header("A platform to make people financially literate.")
st.image('assets/pyramid.png', width = 600)
st.write("\n\n")

st.subheader("CHOOSE YOUR IDENTITY:")
col1, col2 = st.columns(2)

# Adding some spacing for better visual separation
st.markdown("<br>", unsafe_allow_html=True)

with col1:
    if st.button("  INVESTOR  ", key="investor_button"):
        st.success("Navigating to Investor Page...")
        st.switch_page("pages/investor.py")
    st.markdown("<small style='color: grey;'>Find financial information of your favourite company.</small>", unsafe_allow_html=True)

with col2:
    if st.button("  COMPANY  ", key="company_button"):
        st.success("Navigating to Company Page...")
        st.switch_page("pages/company.py")
    st.markdown("<small style='color: grey;'>Find financial ratios from your financial statement data</small>", unsafe_allow_html=True)

# Adding some more spacing at the bottom
st.markdown("<br>", unsafe_allow_html=True)

st.write("\n\n")
st.header("What FinAIze Aims ?")
#st.subheader("The FinAIze leverages AI and machine learning to empower investors and companies alike. For investors, it provides comprehensive stock-related information, guiding investment decisions based on data-driven insights. On the company side, it calculates key financial ratios that inform strategic decisions, helping businesses identify growth opportunities. By comparing these ratios to real-time industry standards, it enables companies to make informed financial choices that drive success.")
st.markdown("""
    <div style='color: rgb(88,202,107); font-size: 25px;'>
        The FinAIze leverages AI and machine learning to empower investors and companies alike. For investors, it provides comprehensive stock-related information, guiding investment decisions based on data-driven insights. On the company side, it calculates key financial ratios that inform strategic decisions, helping businesses identify growth opportunities. By comparing these ratios to real-time industry standards, it enables companies to make informed financial choices that drive success.
    </div>
    """, unsafe_allow_html=True)

st.header("Why Financial Tools ?")

st.markdown("""
    <div style='color: rgb(88,202,107); font-size: 25px;'>
        The financial tools in it helps to :(sip)Monitor regular mutual fund investments, tracking contributions and performance over time; (lumpsum)Tracks one-time investments, assessing growth and returns against benchmarks; (finance tracker) Manages overall finances, including income, expenses, and savings for better budgeting; (loan)Manages loan details like balances and payments to ensure timely repayments.
    </div>
    """, unsafe_allow_html=True)

