import streamlit as st
import time
import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
if parent_dir not in sys.path:
   sys.path.insert(0, parent_dir)

from ui.sidebar import render_sidebar
from ui.upload_tab import render_upload_tab
from ui.summarize_tab import render_summarize_tab
from ui.result_tab import render_results_tab


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
    
    render_sidebar()

    tab1, tab2, tab3 =  st.tabs(["Upload & Process", "Summarize", "Results"])

    with tab1:
       render_upload_tab()

    with tab2:
       render_summarize_tab()

    with  tab3:
       render_results_tab()


if __name__ == "__main__":
    try:
       main()
    
    except Exception as e:
       st.error(f"An error occured: {str(e)}")
       raise e



   
    