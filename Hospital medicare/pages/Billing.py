import streamlit as st
import pandas as pd
from utils.file_handler import read_csv, add_record, save_csv


PATIENT_FILE = "data/patients.csv"
DOCTOR_FILE = "data/doctors.csv"
APPOINTMENT_FILE = "data/appointments.csv"


APPOINTMENT_COLUMNS = [

    "appointment_id",
    "patient_id",
    "patient_name",
    "doctor_id",
    "doctor_name",
    "date",
    "time",
    "status"

]


st.title("📅 Appointment Management")


menu = st.selectbox(
    "Select Operation",
    [
        "Book Appointment",
        "View Appointments",
        "Cancel Appointment"
    ]
)


patients = read_csv(
    PATIENT_FILE,
    [
        "patient_id",
        "name",
        "age",
        "gender",
        "phone",
        "address"
    ]
)


doctors = read_csv(
    DOCTOR_FILE,
    [
        "doctor_id",
        "name",
        "specialization",
        "phone"
    ]
)


# ----------------------------------
# BOOK APPOINTMENT
# ----------------------------------

if menu == "Book Appointment":

    st.subheader(
        "Book Appointment"
    )


    if patients.empty:

        st.warning(
            "Please add patients first."
        )

    elif doctors.empty:

        st.warning(
            "Please add doctors first."
        )

    else:

        patient_name = st.selectbox(
            "Select Patient",
            patients["name"].tolist()
        )

        doctor_name = st.selectbox(
            "Select Doctor",
            doctors["name"].tolist()
        )

        appointment_date = st.date_input(
            "Appointment Date"
        )

        appointment_time = st.time_input(
            "Appointment Time"
        )


        if st.button(
            "Book Appointment"
        ):

            appointment_df = read_csv(
                APPOINTMENT_FILE,
                APPOINTMENT_COLUMNS
            )


            if appointment_df.empty:

                appointment_id = 1

            else:

                appointment_id = (
                    int(
                        appointment_df[
                            "appointment_id"
                        ].max()
                    )
                    + 1
                )


            selected_patient = patients[
                patients["name"]
                == patient_name
            ].iloc[0]


            selected_doctor = doctors[
                doctors["name"]
                == doctor_name
            ].iloc[0]


            appointment = {

                "appointment_id":
                    appointment_id,

                "patient_id":
                    selected_patient[
                        "patient_id"
                    ],

                "patient_name":
                    patient_name,

                "doctor_id":
                    selected_doctor[
                        "doctor_id"
                    ],

                "doctor_name":
                    doctor_name,

                "date":
                    str(
                        appointment_date
                    ),

                "time":
                    str(
                        appointment_time
                    ),

                "status":
                    "Scheduled"
            }


            add_record(
                APPOINTMENT_FILE,
                appointment,
                APPOINTMENT_COLUMNS
            )


            st.success(
                "Appointment booked successfully."
            )


# ----------------------------------
# VIEW APPOINTMENTS
# ----------------------------------

elif menu == "View Appointments":

    appointments = read_csv(
        APPOINTMENT_FILE,
        APPOINTMENT_COLUMNS
    )


    if appointments.empty:

        st.info(
            "No appointments found."
        )

    else:

        st.dataframe(
            appointments,
            use_container_width=True
        )


# ----------------------------------
# CANCEL APPOINTMENT
# ----------------------------------

else:

    appointments = read_csv(
        APPOINTMENT_FILE,
        APPOINTMENT_COLUMNS
    )


    if appointments.empty:

        st.info(
            "No appointments available."
        )

    else:

        appointment_id = st.number_input(
            "Enter Appointment ID",
            min_value=1,
            step=1
        )


        if st.button(
            "Cancel Appointment"
        ):

            condition = (
                appointments[
                    "appointment_id"
                ]
                ==
                appointment_id
            )


            if condition.any():

                appointments.loc[
                    condition,
                    "status"
                ] = "Cancelled"


                save_csv(
                    APPOINTMENT_FILE,
                    appointments
                )


                st.success(
                    "Appointment cancelled successfully."
                )

            else:

                st.error(
                    "Appointment ID not found."
                )