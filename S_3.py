import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Data Analyzer", layout="wide")

st.title("Data Analyzer Dashboard")

f = st.file_uploader("Upload File", type=["csv", "xlsx"])

if f:
    if f.name.endswith(".csv"):
        df = pd.read_csv(f, encoding="latin1")
    else:
        df = pd.read_excel(f)

    page = st.sidebar.radio(
        "Navigation",
        ["Data Understanding", "Analytics Dashboard"]
    )

    if page == "Data Understanding":
        st.header("Data Understanding")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Rows", df.shape[0])

        with col2:
            st.metric("Columns", df.shape[1])

        st.subheader("Columns")
        st.write(list(df.columns))

        st.subheader("Data Preview")
        st.dataframe(df.head())

        selected_cols = st.multiselect("Select columns", df.columns)

        if selected_cols:
            st.dataframe(df[selected_cols])


    else:
        st.header("Analytics Dashboard")

        num_charts = st.number_input(
            "Number of charts",
            min_value=1,
            max_value=5,
            value=1
        )

        for i in range(num_charts):
            st.subheader(f"Chart {i+1}")

            chart_type = st.selectbox(
                "Choose chart type",
                ["Numeric", "Categorical", "Categorical + Numerical"],
                key=f"type{i}"
            )

        
            if chart_type == "Numeric":
                cols = st.multiselect(
                    "Select numeric columns",
                    df.select_dtypes(include="number").columns,
                    key=f"num{i}"
                )

                chart = st.selectbox(
                    "Select chart",
                    ["Line", "Bar", "Pie", "Scatter"],
                    key=f"chart{i}"
                )

                if cols:

                    if chart == "Line":
                        st.line_chart(df[cols])

                    elif chart == "Bar":
                        st.bar_chart(df[cols])

                    elif chart == "Scatter":
                        if len(cols) >= 2:
                            st.scatter_chart(df[cols[:2]])
                        else:
                            st.warning("Select at least 2 numeric columns")

                    elif chart == "Pie":
                        fig, ax = plt.subplots()
                        df[cols[0]].value_counts().plot.pie(
                            autopct="%1.1f%%",
                            ax=ax
                        )
                        ax.set_ylabel("")
                        st.pyplot(fig)

    
            elif chart_type == "Categorical":
                col = st.selectbox(
                    "Select categorical column",
                    df.select_dtypes(include="object").columns,
                    key=f"cat{i}"
                )

                chart = st.selectbox(
                    "Select chart",
                    ["Bar", "Pie"],
                    key=f"cat_chart{i}"
                )

                data = df[col].value_counts()

                if chart == "Bar":
                    st.bar_chart(data)

                else:
                    fig, ax = plt.subplots()
                    data.plot.pie(autopct="%1.1f%%", ax=ax)
                    ax.set_ylabel("")
                    st.pyplot(fig)

    
            else:
                cat_col = st.selectbox(
                    "Select categorical column",
                    df.select_dtypes(include="object").columns,
                    key=f"catnum1{i}"
                )

                num_col = st.selectbox(
                    "Select numerical column",
                    df.select_dtypes(include="number").columns,
                    key=f"catnum2{i}"
                )

                agg = st.selectbox(
                    "Aggregation",
                    ["sum", "mean", "count", "max", "min"],
                    key=f"agg{i}"
                )

                result = df.groupby(cat_col)[num_col].agg(agg)

                st.bar_chart(result)