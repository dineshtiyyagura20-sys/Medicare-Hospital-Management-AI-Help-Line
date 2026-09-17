import streamlit as st
from utils.file_handler import read_csv, add_record

print('-----------------------')
DOCTOR_FILE = "data/doctors.csv"

DOCTOR_COLUMNS = [
    "doctor_id",
    "name",
    "specialization",
    "phone"
]


st.title("🩺 Doctor Management")


menu = st.selectbox(
    "Select Operation",
    [
        "Add Doctor",
        "View Doctors"
    ]
)


# ------------------------
# ADD DOCTOR
# ------------------------

if menu == "Add Doctor":

    st.subheader("Add Doctor")

    name = st.text_input("Doctor Name")

    specialization = st.text_input(
        "Specialization"
    )

    phone = st.text_input(
        "Phone Number"
    )


    if st.button("Add Doctor"):

        if not name.strip():

            st.error(
                "Doctor name is required."
            )

        elif not specialization.strip():

            st.error(
                "Specialization is required."
            )

        elif not phone.isdigit():

            st.error(
                "Enter a valid phone number."
            )

        else:

            df = read_csv(
                DOCTOR_FILE,
                DOCTOR_COLUMNS
            )

            if df.empty:

                doctor_id = 1

            else:

                doctor_id = (
                    int(df["doctor_id"].max())
                    + 1
                )


            doctor = {

                "doctor_id": doctor_id,

                "name": name,

                "specialization": specialization,

                "phone": phone
            }


            add_record(
                DOCTOR_FILE,
                doctor,
                DOCTOR_COLUMNS
            )

            st.success(
                f"Doctor added successfully. Doctor ID: {doctor_id}"
            )


# ------------------------
# VIEW DOCTORS
# ------------------------

else:

    st.subheader("Doctors")

    df = read_csv(
        DOCTOR_FILE,
        DOCTOR_COLUMNS
    )


    if df.empty:

        st.info(
            "No doctors available."
        )

    else:

        st.dataframe(
            df,
            use_container_width=True
        )