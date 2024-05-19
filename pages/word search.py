import streamlit as st
import pandas as pd
import preprocessor
import helper

st.title("Word search")
if st.session_state["my_input"]  is not None:
    bytes_data = st.session_state["my_input"] .getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)
    st.dataframe(df)
if st.session_state["my_input1"]:
    tit = st.text_input("Enter the word to be searched", "")
    most_common = helper.word_count(df, tit)
            #         st.session_state["tit"] = most_common
    st.dataframe(most_common)
else:
    st.write("You need to choose overall")