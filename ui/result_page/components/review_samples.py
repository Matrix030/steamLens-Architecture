import streamlit as st
import pandas as pd
from typing import Dict, List, Any

def render_review_sample(theme_data: pd.DataFrame, review_column: str, title:  str) -> None:
    st.subheader(title)
    if (review_column in theme_data.columns and
        isinstance(theme_data[review_column].iloc[0], list) and
        theme_data[review_column].iloc[0]):

        reviews = theme_data[review_column].iloc[0]
        with st.expander(f"Show {min(5, len(reviews))} reviews"):
            for i, review in enumerate(reviews[:5]):
                st.write(f"**Review {i+1}**")
                st.write(review[:300] + "..." if len(review) > 300 else review)
    else:
        st.write(f"No {review_column.lower()} available.")