import streamlit as st

STREAMLIT_PAGE_CONFIG = {
   "page_title": "SteamLens - Developer Tool",
   "layout": "wide",
   "initial_sidebar_state": "expanded"
}
def main():
   #config for the page
    st.set_page_config(**STREAMLIT_PAGE_CONFIG)
   
    if 'timing_data' not in st.session_state:
      st.session_state.timing_data = {
         "process_start_time": None,
         "process_end_time": None,
         "summarize_start_time": None,
         "summarize_end_time": None,
    }

    #Render the title and description   
    st.title("Steamlens: What ever the fuc this")
    st.write("this does something i am not here for this")

    


   
    