import streamlit as st
from multiapp import MultiApp
from apps import home, data_stats, dna_app # import your app modules here
from apps import covid, simple_stockprice

app = MultiApp()

st.set_page_config(page_title='My Collection of Streamlit Apps')

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Data Stats", data_stats.app)
app.add_app("Covid 19 Data", covid.app)
app.add_app("Simple Stock Price App", simple_stockprice.app)
app.add_app("DNA Nucleotide Count", dna_app.app)


# The main app
app.run()