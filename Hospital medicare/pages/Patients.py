import streamlit as st
import pandas as pd
from utils.file_handler import read_csv, add_record


PATIENT_FILE = "data/patients.csv"

PATIENT_COLUMNS = [
    "patient_id",
    "name",
    "age",
    "gender",
    "phone",
    "address"
]


st.title("👨‍⚕️ Patient Management")


menu = st.selectbox(
    "Select Operation",
    [
        "Add Patient",
        "View Patients",
        "Search Patient"
    ]
)


# -------------------------
# ADD PATIENT
# -------------------------

if menu == "Add Patient":

    st.subheader("Add New Patient")

    name = st.text_input("Patient Name")

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female", "Other"]
    )

    phone = st.text_input("Phone Number")

    address = st.text_area("Address")


    if st.button("Add Patient"):

        if name.strip() == "":
            st.error("Patient name is required.")

        elif phone.strip() == "":
            st.error("Phone number is required.")

        elif not phone.isdigit():
            st.error("Phone number must contain only numbers.")

        else:

            df = read_csv(
                PATIENT_FILE,
                PATIENT_COLUMNS
            )

            if len(df) == 0:
                patient_id = 1

            else:
                patient_id = int(df["patient_id"].max()) + 1


            patient = {

                "patient_id": patient_id,
                "name": name,
                "age": age,
                "gender": gender,
                "phone": phone,
                "address": address
            }


            add_record(
                PATIENT_FILE,
                patient,
                PATIENT_COLUMNS
            )

            st.success(
                f"Patient added successfully. Patient ID: {patient_id}"
            )


# -------------------------
# VIEW PATIENTS
# -------------------------

elif menu == "View Patients":

    st.subheader("All Patients")

    df = read_csv(
        PATIENT_FILE,
        PATIENT_COLUMNS
    )

    if df.empty:

        st.info("No patients found.")

    else:

        st.dataframe(
            df,
            use_container_width=True
        )


# -------------------------
# SEARCH PATIENT
# -------------------------

elif menu == "Search Patient":

    st.subheader("Search Patient")

    search_name = st.text_input(
        "Enter Patient Name"
    )


    if search_name:

        df = read_csv(
            PATIENT_FILE,
            PATIENT_COLUMNS
        )

        result = df[
            df["name"]
            .astype(str)
            .str.contains(
                search_name,
                case=False,
                na=False
            )
        ]


        if result.empty:

            st.warning("Patient not found.")

        else:

            st.dataframe(
                result,
                use_container_width=True
            )