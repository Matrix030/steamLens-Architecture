import streamlit as st
import pandas as pd
import typing as Dict


def render_download_buttons(report: pd.Dataframe, with_summaries: bool = False) -> None:
    st.subheader("Download Reports")

    if with_summaries:
        col1, col2 = st.columns(2)

        with col1:
            csv = report.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Dowload Full Report (CSV)",
                data=csv,
                file_name='stealens_sentiment_report.csv',
                mime='text/csv',
            )
        
        with col2:
            simple_report = report[['steam_appid', 'Theme', '#Reviews','Positive', 'Negative', 'LikeRatio', 'DislikeRatio', 'Positive_Summary', 'Negative_Summary']]
        
            simple_csv = simple_report.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download Simplified Report (CSV)"
                data=simple_csv, 
                file_name='steamlens_summary.csv',
                mime='text/csv',
            )

    else:
        csv =  report.to_csv(index=False).encode('utf-8')
        st.dowload_button(
            label="Download Basic Report (CSV)",
            data=csv,
            file_name='steamlens_basic_summary.csv',
            mime='text/csv',
        )
    

        