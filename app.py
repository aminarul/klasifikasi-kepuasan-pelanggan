import streamlit as st
import pickle
import numpy as np

# ======================
# LOAD MODEL
# ======================
model = pickle.load(open("model.pkl", "rb"))

# ======================
# JUDUL APLIKASI
# ======================
st.title("Klasifikasi Tingkat Kepuasan Pelanggan")
st.write("Menggunakan Algoritma Naive Bayes")

# ======================
# INPUT FITUR
# ======================

gender = st.selectbox(
    "Gender",
    [0, 1],
    format_func=lambda x: "Female" if x == 0 else "Male"
)

customer_type = st.selectbox(
    "Customer Type",
    [0, 1],
    format_func=lambda x: "Disloyal Customer" if x == 0 else "Loyal Customer"
)

age = st.number_input(
    "Age",
    min_value=1,
    max_value=100,
    value=25
)

type_travel = st.selectbox(
    "Type of Travel",
    [0, 1],
    format_func=lambda x: "Personal Travel" if x == 0 else "Business Travel"
)

travel_class = st.selectbox(
    "Class",
    [0, 1, 2],
    format_func=lambda x: ["Eco", "Eco Plus", "Business"][x]
)

flight_distance = st.number_input(
    "Flight Distance",
    min_value=0,
    value=500
)

wifi = st.slider("Inflight Wifi Service", 0, 5, 3)
departure_time = st.slider("Departure/Arrival Time Convenient", 0, 5, 3)
online_booking = st.slider("Ease of Online Booking", 0, 5, 3)
gate_location = st.slider("Gate Location", 0, 5, 3)
food_drink = st.slider("Food and Drink", 0, 5, 3)
online_boarding = st.slider("Online Boarding", 0, 5, 3)
seat_comfort = st.slider("Seat Comfort", 0, 5, 3)
inflight_entertainment = st.slider("Inflight Entertainment", 0, 5, 3)
onboard_service = st.slider("On-board Service", 0, 5, 3)
leg_room = st.slider("Leg Room Service", 0, 5, 3)
baggage_handling = st.slider("Baggage Handling", 0, 5, 3)
checkin_service = st.slider("Checkin Service", 0, 5, 3)
inflight_service = st.slider("Inflight Service", 0, 5, 3)
cleanliness = st.slider("Cleanliness", 0, 5, 3)

departure_delay = st.number_input(
    "Departure Delay in Minutes",
    min_value=0,
    value=0
)

arrival_delay = st.number_input(
    "Arrival Delay in Minutes",
    min_value=0,
    value=0
)

# ======================
# PREDIKSI
# ======================
if st.button("Prediksi"):

    data = np.array([[
        gender,
        customer_type,
        age,
        type_travel,
        travel_class,
        flight_distance,
        wifi,
        departure_time,
        online_booking,
        gate_location,
        food_drink,
        online_boarding,
        seat_comfort,
        inflight_entertainment,
        onboard_service,
        leg_room,
        baggage_handling,
        checkin_service,
        inflight_service,
        cleanliness,
        departure_delay,
        arrival_delay
    ]])

    result = model.predict(data)

    if result[0] == 1:
        st.success("✅ Pelanggan Puas")
    else:
        st.error("❌ Pelanggan Tidak Puas")