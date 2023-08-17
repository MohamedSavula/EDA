import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns


def load_data():
    uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        return data
    return None


def visualize_data(data):
    st.subheader("Data Visualization")

    # Bar chart
    st.write("Bar Chart")
    selected_column = st.selectbox("Select a column for the X-axis", data.columns)
    st.bar_chart(data[selected_column])

    # Scatter plot
    st.write("Scatter Plot")
    x_column = st.selectbox("Select X-axis column", data.columns)
    y_column = st.selectbox("Select Y-axis column", data.columns)
    plt.scatter(data[x_column], data[y_column])
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

    # Line chart
    st.write("Line Chart")
    x_column_bokeh = st.selectbox("Select X-axis line chart", data.columns)
    y_column_bokeh = st.selectbox("Select Y-axis line chart", data.columns)
    st.line_chart([[x_column_bokeh], [y_column_bokeh]])

    # Pie Chart
    st.title("Pie Chart")
    plt.figure(figsize=(6, 6))
    d = data.head(1000)
    counts = d[st.selectbox("Select a column for the Pie chart", d.columns)].value_counts()
    plt.pie(counts, labels=counts.index.values.tolist())
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

    # Histogram
    st.title("Histogram")
    selected_column_histogram = st.selectbox("Select a column for the histogram", data.columns)
    plt.figure(figsize=(8, 6))
    values, bins, patches = plt.hist(selected_column_histogram, bins=10, edgecolor="white", linewidth=3)
    for i in range(0, 3):
        patches[i].set_facecolor('g')
    for i in range(3, 6):
        patches[i].set_facecolor('r')
    for i in range(6, len(patches)):
        patches[i].set_facecolor('black')
    plt.grid(True)
    st.pyplot()

    # Violin Plot
    st.title("Violin Plot")
    d_v = data.head(100)
    x_column_violinplot = st.selectbox("Select X-axis Violin chart", d_v.columns)
    y_column_violinplot = st.selectbox("Select Y-axis Violin chart", d_v.columns)
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 6))
    sns.violinplot(data=d_v, x=x_column_violinplot, y=y_column_violinplot)
    plt.title("Violin Plot")
    plt.xlabel(x_column_violinplot)
    plt.ylabel(y_column_violinplot)
    st.pyplot()

    # Lite chart
    st.write("Lite Bar Chart")
    x_column_lite = st.selectbox("Select X-axis Lite chart", data.columns)
    y_column_lite = st.selectbox("Select Y-axis Lite chart", data.columns)
    chart_spec = {
        "mark": "bar",
        "encoding": {
            "x": {"field": x_column_lite},
            "y": {"field": y_column_lite},
            "color": {"value": "steelblue"}
        }
    }
    st.vega_lite_chart(data, chart_spec)


def main():
    if st.button("Contact us"):
        st.write('Mobile : 01016704077')
        st.write('Email : mohamedsavula35@gmail.com')
        st.write('Job : odoo developer')
    st.title('Automated EDA tool')
    data = load_data()
    st.title('Author \n Mohamed Saber')
    if data is not None:
        st.write("Data loaded successfully.")
        st.write(data.head())
        st.write("Data Visualization")
        visualize_data(data)


if __name__ == "__main__":
    main()
