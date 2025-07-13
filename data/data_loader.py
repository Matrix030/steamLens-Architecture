import os
import streamlit as st
import pandas as pd
import pyarrow.parquet as pq
from typing import Tuple, Optional, List, Dict, Any
import json

def load_theme_dictionary(theme_file: str) -> Dict[int,  Dict[str, List[str]]]:
    try:
        with open(theme_file, 'r') as f:
            raw = json.load(f)
        return {int(appid): themes for appid, themes in raw.items()}
    except FileNotFoundError:
        st.error(f"Theme file: {theme_file} not found. Please upload it first.")
        return {}
    
    except Exception as e:
        st.error(f"Error loading theme dictionary: {str(e)}")
        return {}
