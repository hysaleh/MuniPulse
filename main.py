





import streamlit as st
from data.data_handler import load_data
from features.anomaly_detection.anomaly_detection import detect_outliers, plot_anomalies_scatter
import matplotlib.pyplot as plt


def main():
    st.title("MuniPulse")

    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

    if uploaded_file is not None:
        data = load_data(uploaded_file)

        st.subheader("Raw Data")
        st.write(data)

        detect_anomalies = st.checkbox("Detect Anomalies")
        if detect_anomalies:
            st.subheader("Cleaned Data with Anomalies Detection")
            st.write(data)

            if 'is_anomaly' in data.columns and any(data['is_anomaly']):
                features = st.multiselect("Select features", data.columns)
                if len(features) >= 2:
                    plot_simple_scatter(data, features)
                else:
                    st.warning("Please select at least two features.")
            else:
                st.warning("No anomalies detected.")
        else:
            st.subheader("Cleaned Data")
            st.write(data)

            features = st.multiselect("Select features", data.columns)
            if len(features) >= 2:
                plot_simple_scatter(data, features)
            else:
                st.warning("Select at least two features.")

def plot_simple_scatter(data, features):
    fig, ax = plt.subplots()
    ax.scatter(data[features[0]], data[features[1]])
    ax.set_xlabel(features[0])
    ax.set_ylabel(features[1])
    ax.set_title(f'Scatter Plot: {features[0]} vs {features[1]}')

    # Display the plot within Streamlit
    st.pyplot(fig)

if __name__ == "__main__":
    main()




