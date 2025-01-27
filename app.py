#from dotenv import load_dotenv(Uncomment this if using .env file)
import os
import streamlit as st
from openai import OpenAI

# =========================================
# System Prompts
# =========================================

system_prompt_initial = """
You are a friendly AI travel planner. Ask the user for the following details to create a personalized itinerary:
1. Destination
2. Trip duration (days)
3. Budget (low/moderate/high)
4. Purpose (e.g., relaxation, adventure, cultural)
5. Preferences (e.g., food, history, nature)
Ask one question at a time and keep it conversational.
"""

system_prompt_refine = """
Based on the user’s initial inputs, ask clarifying questions to refine:
- If budget is "moderate," ask for a numerical range (e.g., $500-$700).
- If preferences are vague (e.g., "fun activities"), ask for specifics (e.g., museums, hiking).
- Ask about dietary restrictions, mobility concerns, or accommodation preferences.
"""

system_prompt_final = """
Create a detailed {duration}-day itinerary for {destination}:
- Day 1 to Day {duration}: Include 3 activities per day with time slots
- For each activity: add description and cost estimate
- Include lunch/dinner recommendations (consider {dietary_preferences})
- Note transportation tips and accommodation suggestions ({accommodation_type})

"""

# =========================================
# Setup and Configuration
# =========================================

load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY") or st.secrets["OPENAI_API_KEY"])

# Initialize session state
if 'travel_data' not in st.session_state:
    st.session_state.travel_data = {
        'destination': '',
        'duration': 5,
        'budget': '💰💰 Moderate',
        'purpose': '🏖️ Relaxation',
        'preferences': [],
        'dietary': '',
        'mobility': '🚶 No restrictions',
        'accommodation': '🏩 Mid-range Hotel'
    }

if 'step' not in st.session_state:
    st.session_state.step = 1

# =========================================
# Helper Functions
# =========================================

def get_response(prompt, user_input):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content

# =========================================
# Custom CSS Styling
# =========================================

st.markdown("""
    <style>
    .main {background-color: #f8f9fa;}
    h1 {color: #2d3436;}
    .stButton>button {
        background-color: #0984e3!important;
        color: white!important;
        border-radius: 8px;
        transition: all 0.3s;
    }
    .stButton>button:hover {transform: scale(1.05);}
    .stTextInput>div>div>input {border-radius: 8px!important;}
    .block-container {padding-top: 2rem;}
    </style>
""", unsafe_allow_html=True)

# =========================================
# App Interface
# =========================================

st.image("https://cdn-icons-png.flaticon.com/512/1865/1865269.png", width=100)
st.title("AI Travel Planner ✈️")
st.markdown("**Craft your perfect trip with AI-powered recommendations**")

# Progress bar
progress_bar = st.progress(0 if st.session_state.step == 1 else 50 if st.session_state.step == 2 else 100)

# =========================================
# Step 1: Basic Information
# =========================================

if st.session_state.step == 1:
    progress_bar.progress(33)
    with st.form("basic_info"):
        st.subheader("📍 Let's Start Planning!")
        
        col1, col2 = st.columns(2)
        with col1:
            st.session_state.travel_data['destination'] = st.text_input(
                "Where are you going?",
                placeholder="e.g., Paris, France"
            )
            st.session_state.travel_data['duration'] = st.number_input(
                "Trip Duration (days)",
                min_value=1, step=1, value=5
            )
            
        with col2:
            st.session_state.travel_data['budget'] = st.selectbox(
                "Budget Range",
                ["💰 Low", "💰💰 Moderate", "💰💰💰 High"]
            )
            st.session_state.travel_data['purpose'] = st.selectbox(
                "Trip Purpose",
                ["🏖️ Relaxation", "🧗 Adventure", "🎭 Cultural"]
            )
        
        st.session_state.travel_data['preferences'] = st.multiselect(
            "Your Interests (select at least 2)",
            ["🍴 Food", "🏛️ History", "🌳 Nature", "🛍️ Shopping", "🎨 Art", "⚽ Sports"],
            default=["🍴 Food", "🏛️ History"]
        )
        
        if st.form_submit_button("Next →"):
            if len(st.session_state.travel_data['preferences']) < 2:
                st.error("Please select at least 2 interests!")
            else:
                st.session_state.step = 2
                st.rerun()

# =========================================
# Step 2: Refinement Questions
# =========================================

elif st.session_state.step == 2:
    progress_bar.progress(66)
    with st.form("refine_info"):
        st.subheader("🔍 Let's Perfect Your Plan")
        
        col1, col2 = st.columns(2)
        with col1:
            if "Moderate" in st.session_state.travel_data['budget']:
                st.session_state.travel_data['budget'] = st.text_input(
                    "💵 Specify Budget Range (e.g., $800-$1200 USD)",
                    placeholder="Enter amount range"
                )
            
            st.session_state.travel_data['accommodation'] = st.selectbox(
                "🏨 Accommodation Style",
                ["🏠 Budget Hostel", "🏩 Mid-range Hotel", "🏰 Luxury Resort", "📍 Central Location"]
            )
            
        with col2:
            st.session_state.travel_data['mobility'] = st.selectbox(
                "♿ Mobility Needs",
                ["🚶 No restrictions", "🚶 Limited walking", "♿ Wheelchair accessible"]
            )
            st.session_state.travel_data['dietary'] = st.text_input(
                "🍽️ Dietary Preferences",
                placeholder="e.g., Vegetarian, Gluten-free"
            )
        
        if st.form_submit_button("✨ Generate My Itinerary"):
            st.session_state.step = 3
            st.rerun()

# =========================================
# Step 3: Itinerary Display
# =========================================

elif st.session_state.step == 3:
    progress_bar.progress(100)
    st.subheader("🗺️ Your Personalized Itinerary")
    
    with st.spinner("Creating your perfect travel plan..."):
        final_input = f"""
        Destination: {st.session_state.travel_data['destination']}
        Duration: {st.session_state.travel_data['duration']} days
        Budget: {st.session_state.travel_data['budget']}
        Purpose: {st.session_state.travel_data['purpose']}
        Preferences: {", ".join(st.session_state.travel_data['preferences'])}
        Dietary: {st.session_state.travel_data['dietary']}
        Mobility: {st.session_state.travel_data['mobility']}
        Accommodation: {st.session_state.travel_data['accommodation']}
        """
        
        itinerary = get_response(system_prompt_final, final_input)
    st.markdown(f"""
        <div style='
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            margin-top: 20px;
        '>
                {itinerary}
        </div>
    """, unsafe_allow_html=True)
    if st.button("🔄 Plan Another Trip"):
        st.session_state.step = 1
        st.session_state.travel_data = {
            'destination': '',
            'duration': 5,
            'budget': '💰💰 Moderate',
            'purpose': '🏖️ Relaxation',
            'preferences': [],
            'dietary': '',
            'mobility': '🚶 No restrictions',
            'accommodation': '🏩 Mid-range Hotel'
        }
        st.rerun()
