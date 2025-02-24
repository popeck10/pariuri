
import streamlit as st
import random

# Titlul aplicației
st.title("Generator Pariuri Sportive Simplu")

# Introducerea echipelor
teams_input = st.text_input("Introdu echipele (separate prin virgulă):")
injuries_input = st.text_input("Introdu jucătorii accidentați (separați prin virgulă):")
forms_input = st.text_input("Introdu forma echipelor (separate prin virgulă):")
meetings_input = st.text_input("Introdu ultimele întâlniri directe (separate prin virgulă):")
goals_input = st.text_input("Introdu media de goluri pe meci (separate prin virgulă):")

if st.button("Generează Pont"):
    if not teams_input:
        st.error("Introdu cel puțin două echipe separate prin virgulă!")
    else:
        teams = [team.strip() for team in teams_input.split(",")]
        injuries = [injury.strip() for injury in injuries_input.split(",")] if injuries_input else []
        forms = [form.strip() for form in forms_input.split(",")] if forms_input else []
        meetings = [meeting.strip() for meeting in meetings_input.split(",")] if meetings_input else []
        goals = [goal.strip() for goal in goals_input.split(",")] if goals_input else []

        if len(teams) < 2:
            st.error("Introdu cel puțin două echipe!")
        else:
            bet_types = ["1", "X", "2", "GG", "Peste 2.5 goluri", "Sub 2.5 goluri"]
            selected_bet = random.choice(bet_types)
            selected_teams = random.sample(teams, 2)

            injury_info = f" (Jucători accidentați: {', '.join(injuries)})" if injuries else ""
            form_info = f" (Formă echipe: {', '.join(forms)})" if forms else ""
            meetings_info = f" (Ultimele întâlniri: {', '.join(meetings)})" if meetings else ""
            goals_info = f" (Media goluri pe meci: {', '.join(goals)})" if goals else ""

            result = f"Pont: {selected_teams[0]} vs {selected_teams[1]} -> {selected_bet}{injury_info}{form_info}{meetings_info}{goals_info}"
            st.success(result)
