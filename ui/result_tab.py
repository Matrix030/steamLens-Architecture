import streamlit as st
import pandas as pd
from typing import Dict, List, Any

from ui.result_page.summarized_results import show_summarized_results
from ui.result_page.unsummarized_results import show_unsummarized_results


def render_results_tab() -> None:
    st.header("Results")
    if 'summarized_report' in st.session_state and not st.session_state.summarized_report.empty:
        show_summarized_results(st.session_state.summarized_report)
    elif 'result' in st.session_state and st.session_state.result:
        show_unsummarized_results(st.session_state.result['final_report'])
    else:
        st.info("Please Complete the 'Upload & Process' steps first") 


