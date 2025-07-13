import time
import streamlit as st
from typing import Dict, Any, Callable

from config.app_config import DEFAULT_THEME_FILE
#from processing.process_files import process_uploaded_files
from utils.system_utils import format_time
from processing.process_files import process_uploaded_files

def render_upload_tab() -> None:
    st.header("Upload and Process Parquet Files")
    st.write("""
    Upload your Steam reviews Parquet files for processing. The app will:
    1. Check if each file's app ID exists in the theme dictionary
    2. Process only the files with matching app IDs
    3. Filter for English reviews and perform topic assignment
    4. Separate positive and negative reviews for each theme
""")

    uploaded_files = st.file_uploader(
        "Upload Parquet Files",
        type = ['parquet'],
        accept_multiple_files=True,
        help="Upload one or more Parquet files containing Steam reviews data"
    )

    theme_file_exists = check_theme_file_exists()

    if uploaded_files:
        st.write(f"Uploaded {len(uploaded_files)} files")
        if st.button("Start Processing", key="process_button", disabled=not
                     theme_file_exists):
            start_time = time.time()
            st.session_state.timing_data['process_start_time'] = start_time

            st.info("Dask cluster is being initialized. Processing will start shortly...")
            result = process_uploaded_files(uploaded_files, theme_file=DEFAULT_THEME_FILE)

            elapsed_time = time.time() - start_time
            st.session_state.timing_data['process_end_time'] = time.time()

            if result:
                st.session_state.result = result

                st.subheader("Processing Summary")            
                st.write(f"Processed {len(result['skipped_files'])} files (app IDs not in theme dictionary)")

                if result['skipped_files']:
                    with st.expander("Show skipped files"):
                        for file_name, app_id in result['skipped_files']:
                            st.write(f"- {file_name} (App ID: {app_id if app_id else 'Unknown'})")

                with st.expander("Show sample of processed data"):
                    sample_df = result['final_report'][['steam_appid', 'Theme', '#Reviews', 'Positive', 'Negative', 'LikeRatio', 'DislikeRatio']].head(10)
                
                st.info("Summarize next")
        

def check_theme_file_exists() -> bool:
    import os
    return os.path.exists(DEFAULT_THEME_FILE)

