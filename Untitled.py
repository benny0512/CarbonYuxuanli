import streamlit as st
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# Define the fixed destination address
destination_address = "555 Pennsylvania Avenue Northwest, Washington, DC"

# Carbon emission factors (kg CO₂ per km) for different transportation modes
transport_modes = {
    "Gasoline Car (Private/Uber)": 0.192,   # 0.192 kg CO₂ per km
    "Electric Vehicle (EV)": 0.05,          # 0.05 kg CO₂ per km
    "Subway": 0.041,                         # 0.041 kg CO₂ per km
    "Bus": 0.103,                            # 0.103 kg CO₂ per km
    "Walking": 0,                            # No emissions for walking
    "Bicycle": 0                             # No emissions for cycling
}

# Initialize a geolocator object using OpenStreetMap's Nominatim service
geolocator = Nominatim(user_agent="carbon_footprint_calculator")

# Streamlit UI setup
st.title("Carbon Emission Calculator 🌍")
st.markdown("### Calculate the carbon footprint of your travel to JHU DC")

# User input for starting location
origin = st.text_input("Enter your starting address:")

# User selects a mode of transportation
mode = st.selectbox("Select your mode of transport:", list(transport_modes.keys()))

# Button to trigger calculation
if st.button("Calculate Carbon Emission"):
    if origin:
        try:
            # Get latitude and longitude of the user's input location
            origin_location = geolocator.geocode(origin)
            destination_location = geolocator.geocode(destination_address)

            # Check if both locations are valid
            if origin_location and destination_location:
                # Calculate the great-circle (straight-line) distance in kilometers
                distance_km = geodesic(
                    (origin_location.latitude, origin_location.longitude),
                    (destination_location.latitude, destination_location.longitude)
                ).km

                # Compute the carbon emission using the formula:
                # Carbon Emission = Distance (km) × Emission Factor (kg CO₂/km)
                emission = distance_km * transport_modes[mode]

                # Display results in Streamlit UI
                st.success(f"Distance from **{origin}** to **{destination_address}**: **{distance_km:.2f} km**")
                st.info(f"Estimated carbon emission for **{mode}**: **{emission:.2f} kg CO₂**")

                # Display the formula used for calculation
                st.write(f"### Carbon Emission Calculation:")
                st.latex(r"Carbon\ Emission = Distance\ (km) \times Emission\ Factor\ (kg\ CO₂/km)")
                st.write(f"For **{mode}**: {distance_km:.2f} × {transport_modes[mode]} = **{emission:.2f} kg CO₂**")
                
            else:
                st.error("Unable to resolve the address. Please check your input.")

        except Exception as e:
            st.error(f"Error in calculation: {str(e)}")

    else:
        st.warning("Please enter a starting address!")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




