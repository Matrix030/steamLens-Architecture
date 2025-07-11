import streamlit as st
import pandas as pd
from typing import Dict, List, Any


def show_summarized_results(summarized_report: pd.DataFrame) -> None:
    game_name_mapping = {}
    if 'result' in st.session_state and 'game_name_mapping' in st.session_state.result:
        game_name_mapping = st.session_state.result['game_name_mapping']


    st.subheader("Filter Results")
    app_ids = sorted(summarized_report['steam_appid'].unique())

    app_id_options = []
    for app_id in app_ids:
        if app_id in game_name_mapping and game_name_mapping[app_id]:
            app_id_options.append(f"{app_id} - {game_name_mapping[app_id]}")
        else:
            app_id_options.append(f"{app_id}")
    
    selected_app_id_option = st.selectbox("Select Game", app_id_options)

    selected_app_id = int(selected_app_id_option.split(' - ')[0])

    filtered_df = summarized_report[summarized_report['steam_appid'] == selected_app_id]

    game_name = game_name_mapping.get(selected_app_id, "Unknown Game")

    if selected_app_id in game_name_mapping and game_name_mapping[selected_app_id]:
        st.subheader(f"Game: {game_name} (App ID: {selected_app_id})")
    else:
        st.subheader(f"App ID: {selected_app_id}")
    
    theme = filtered_df['Theme'].unique()
    selected_theme = st.selectbox("Select Theme", theme)

    theme_data =  filtered_df[filtered_df['Theme'] == selected_theme]

    if not theme_data.empty:
        st.subheader(f"Theme:  {selected_theme}")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Reviews", theme_data["#Reviews"].iloc[0])
        with col2:
            st.metric("Positive Reviews", f"{theme_data['Positive'].iloc[0]} ({theme_data['LikeRatio'].iloc[0]})")
        with col3:
            st.metric("Negative Reviews", f"{theme_data['Negative'].iloc[0]} ){theme_data['DislikeRatio'].iloc[0]}")

        st.subheader("What Players Enjoy")  
        st.success(theme_data['Positive_Summary'].iloc(0))

        st.subheader("What Players Dislike")
        st.error(theme_data['Negative_Summary'].iloc[0])

        col1, col2 = st.columns(2)

        with col1:
            #TODO - Complete this
            render_review_sample(theme_data, 'Positive_Reviews', 'Sample Positive Reviews')

        with col2:
            render_review_sample(theme_data, 'Negative_Reviews', 'Sample Negative Reviews')

        render_download_buttons(summarized_report, with_summaries=True)



