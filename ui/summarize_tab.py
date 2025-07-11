import time
import streamlit as st
from typing import Dict, Any

#from processing.summarize_processor import summarize_report

def render_summarize_tab():
    st.header("Generate Summaries")

    st.write("""
    This step uses GPU-accelerated summarization to generate separate summaries for positive and negative reviews.
    This gives you better insights into what players love and hate about each theme.
""")
    
    if 'result' in st.session_state and st.session_state.result:
        if st.button("Start Summarization", key="summarize_button"):
            start_time = time.time()
            st.session_state.timing_data['summarize_start_time'] = start_time

            st.info("Dask cluster is being intialized. Summarization will start shortly...")

            summarized_report = summarized_report(st.session_state.result['final_report'])

            end_time = time.time()
            elapsed_time = end_time - start_time

            st.session_state.timing_data['summarize_end_time'] = end_time

            if summarized_report is not None:
                st.session_state.summarized_report = summarized_report

                st.success("Summarization Completed in {elapsed_time:.2f} seconds!")

                st.subheader("Execution Time Metrics")

                col = st.columns(1)
                with col:
                    per_item = elapsed_time/len(summarized_report) if len(summarized_report) > 0 else 0
                    st.metric("Average Per Item", f"{per_item:.4f} seconds")

                
                with st.expander("Show sample of summarize"):
                    sample_columns = ['steam_appid', 'Theme', 'Positive_Summary', 'Negative_Summary']
                    st.dataframe(summarized_report[sample_columns].head(5))

                st.info("Go to the 'Results' tab to view the complete analysis")
    
    else:
        st.info("Please complete the 'Upload & Process' step first")