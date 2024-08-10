import streamlit as st

# Example data for destinations and their estimated costs
DESTINATIONS = {
    "Paris": {"hotel": 100, "food": 50, "transport": 30},
    "New York": {"hotel": 150, "food": 70, "transport": 40},
    "Tokyo": {"hotel": 120, "food": 60, "transport": 35},
    "London": {"hotel": 110, "food": 65, "transport": 45},
}

def calculate_itinerary(destination, budget):
    if destination in DESTINATIONS:
        costs = DESTINATIONS[destination]
        total_cost = costs['hotel'] + costs['food'] + costs['transport']
        is_within_budget = total_cost <= budget
        return costs, total_cost, is_within_budget
    else:
        return None, None, False

st.title('Travel Itinerary App')

# User input for destination and budget
destination = st.selectbox('Choose your destination:', options=list(DESTINATIONS.keys()))
budget = st.number_input('Enter your budget (USD):', min_value=0)

if st.button('Get Itinerary'):
    costs, total_cost, is_within_budget = calculate_itinerary(destination, budget)
    
    if costs:
        st.subheader(f'Your itinerary for {destination}:')
        st.write(f"**Hotel:** ${costs['hotel']}")
        st.write(f"**Food:** ${costs['food']}")
        st.write(f"**Transport:** ${costs['transport']}")
        st.write(f"**Total Cost:** ${total_cost}")
        
        if is_within_budget:
            st.success('Good news! Your budget is enough for this trip.')
        else:
            st.error('Sorry, your budget is not enough for this trip.')
    else:
        st.error('Destination not found.')

