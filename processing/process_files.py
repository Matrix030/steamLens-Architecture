import os
import time
import numpy as np
import pandas as pd
import datetime
import streamlit as st
import dask.dataframe as dd
from dask.distributed import Client, LocalCluster
from sentence_transformers import SentenceTransformer

from data.data_loader import load_theme_dictionary
from typing import Dict, List, Tuple, Any, Optional
def process_uploaded_files(uploaded_files: List[Any], theme_file: str='game_theme.json') -> Optional[Dict[str, Any]]:
    phase_start_time = time.time()

    if not uploaded_files:
        st.warning("Please upload at least one Parquet File to begin processing")
        return None
    
    #Create progress indicators
    progress_placeholders = st.empty()
    status_placeholder = st.empty()
    dashboad_placeholder = st.empty()

    with progress_placeholders.container():
        status_text = st.empty()

    try:
        GAME_THEMES = load_theme_dictionary(theme_file)
        if not GAME_THEMES:
            return None
        status_text.write(f"Loaded theme dictionary with {len(GAME_THEMES)} games")
    
    except Exception as e:
        st.error(f"Error loading theme dictionary: {str(e)}")
        return None
    
    