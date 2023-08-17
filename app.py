import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the title and description of the app
st.title("Simple Streamlit App")
st.write("Upload a CSV file and visualize its contents.")

# Upload CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the uploaded CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)

    # Display the contents of the DataFrame
    st.write("## Data Preview")
    st.dataframe(df)

    # Display basic statistics
    st.write("## Basic Statistics")
    st.write(df.describe())

    # Visualize data
    st.write("## Data Visualization")
    st.write("### Count Plot of a Categorical Column")
    column = st.selectbox("Select a categorical column", df.columns)
    if df[column].dtype == "object":
        sns.countplot(x=column, data=df)
        st.pyplot(plt)
    else:
        st.write("Selected column is not categorical.")

    st.write("### Histogram of a Numerical Column")
    num_column = st.selectbox("Select a numerical column", df.select_dtypes(include=["float64", "int64"]).columns)
    plt.hist(df[num_column], bins=20, edgecolor="k")
    st.pyplot(plt)
