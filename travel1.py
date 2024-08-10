import streamlit as st

# Example data for destinations with various categories
DESTINATIONS = {
    "Paris": {
        "sightseeing": ["Eiffel Tower", "Louvre Museum", "Notre-Dame Cathedral"],
        "adventure": ["Seine River Cruise", "Montmartre Walking Tour"],
        "food": ["Croissants", "Escargot", "Crepes"],
        "tourist_places": ["Champs-Élysées", "Luxembourg Gardens", "Versailles Palace"]
    },
    "New York": {
        "sightseeing": ["Statue of Liberty", "Central Park", "Times Square"],
        "adventure": ["Helicopter Tour", "Broadway Shows"],
        "food": ["Bagels", "Pizza", "Cheesecake"],
        "tourist_places": ["Empire State Building", "Metropolitan Museum of Art", "Brooklyn Bridge"]
    },
    "Tokyo": {
        "sightseeing": ["Tokyo Tower", "Senso-ji Temple", "Shibuya Crossing"],
        "adventure": ["Sumida River Cruise", "Mount Takao Hiking"],
        "food": ["Sushi", "Ramen", "Tempura"],
        "tourist_places": ["Shinjuku Gyoen", "Meiji Shrine", "Akihabara"]
    },
    "London": {
        "sightseeing": ["Big Ben", "London Eye", "Buckingham Palace"],
        "adventure": ["Thames River Cruise", "Jack the Ripper Tour"],
        "food": ["Fish and Chips", "Afternoon Tea", "Pies"],
        "tourist_places": ["British Museum", "Trafalgar Square", "Tower of London"]
    }
}

def get_travel_info(destination):
    return DESTINATIONS.get(destination, {})

st.title('Travel Information App')

# User input for destination
destination = st.selectbox('Choose your destination:', options=list(DESTINATIONS.keys()))

if st.button('Get Information'):
    info = get_travel_info(destination)
    
    if info:
        st.subheader(f'Local Information for {destination}:')
        
        st.write('### Sightseeing')
        for place in info['sightseeing']:
            st.write(f"- {place}")
        
        st.write('### Adventure Activities')
        for activity in info['adventure']:
            st.write(f"- {activity}")
        
        st.write('### Food')
        for food in info['food']:
            st.write(f"- {food}")
        
        st.write('### Tourist Places')
        for tourist_place in info['tourist_places']:
            st.write(f"- {tourist_place}")
    else:
        st.error('Information not found for the selected destination.')
