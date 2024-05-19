from import_raw_data import engine

import streamlit as st
import pandas as pd
import altair as alt


st.title('Meiro questions')


@st.cache_data
def load_data():
    return pd.read_sql("select * from full_denom", con=engine)


data_load_state = st.text('Loading data...')
data = load_data()
data_load_state.text("Done! (using st.cache_data)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Q1: Which user spent the most money on products on all Fridays?')

q1_data: pd.DataFrame = data[data["created_ts"].dt.dayofweek == 4].groupby(["user_id", "user_name"])[
     "price"].sum().sort_values(ascending=False).reset_index()


if len(q1_data["user_name"]) != len(set(q1_data["user_name"])):
    # this never happens while testing but ....
    st.write("There are duplicate user names! Some users share name but are different IDs, therefore fix your data first!")
else:
    st.bar_chart(q1_data,

                 x="user_name",
                 y="price")
    st.write("Sorted would be better, but streamlit's barchart does not support that? Iam sad. With a loooong syntax:")
    st.write(alt.Chart(q1_data).mark_bar().encode(
        x=alt.X('user_name', sort=None),
        y='price',
    ).properties(width=700, height=500, ).configure_header(labelOrient='bottom').configure_view(
        strokeOpacity=0))
    st.write(
        f"User with the most money spent of friday is: {q1_data.at[0, 'user_name']}"
    )


st.subheader('Q2: What are the best 3 products in each location of a user based on quantity?')
q2_data = data.groupby(["product_name", "user_city", ]).size().groupby("user_city").nlargest(3, keep="all").droplevel(level=0).reset_index(name="quantity")

option = st.multiselect(
    label="Select location(s) to know TOP products for",
    options=q2_data["user_city"].unique(),
    placeholder="Choose cities"

)
if option:
    for o in option:
        st.subheader(f'Top products for {o}')

        st.bar_chart(q2_data[q2_data["user_city"] == o],
                     y="quantity",
                     x="product_name", )
