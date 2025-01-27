# AI Travel Planner 🌍

Welcome to the **AI Travel Planner**, an AI-powered application that generates personalized travel itineraries using OpenAI's GPT-4 model. This project is designed to help users plan their trips by collecting preferences, refining inputs, and providing detailed day-by-day itineraries.

---

## 🚀 Features

- **Personalized Itineraries**: Tailored to user preferences, budget, and trip duration.
- **Input Refinement**: Clarifies vague inputs (e.g., "moderate budget") with follow-up questions.
- **Activity Suggestions**: Includes top-rated attractions and hidden gems based on user interests.
- **User-Friendly Interface**: Built with Streamlit for an intuitive and interactive experience.
- **Markdown Formatting**: Displays itineraries with proper headings, bullet points, and styling.

---

## 🛠️ How It Works

1. **Input Collection**: Users provide basic trip details (destination, duration, budget, purpose, and preferences).
2. **Input Refinement**: The app asks clarifying questions (e.g., dietary restrictions, mobility concerns).
3. **Itinerary Generation**: A detailed day-by-day plan is generated using GPT-4.
4. **Output Display**: The itinerary is displayed in a clean, Markdown-formatted layout.

---

## 🖥️ Live Demo

Try the app live: [AI Travel Planner on Streamlit](https://your-streamlit-app-link.streamlit.app)

---

## 🛠️ Installation

To run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/raviraj-441/AI-Travel-Planner.git
   cd AI-Travel-Planner
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up environment variables**:
   - Create a `.env` file in the root directory.
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your-api-key-here
     ```
4. **Run the app**:
   ```bash
   streamlit run app.py
   ```

📂 Project Structure
```
AI-Travel-Planner/
├── app.py                  # Main Streamlit application
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (API key)
└── .gitignore              # Files to ignore in Git
```

🧩 Requirements
- Python 3.8+
- Streamlit
- OpenAI Python SDK
- python-dotenv

Install all dependencies using:
```bash
pip install -r requirements.txt
```

🎨 UI Features
- Progress Bar: Tracks user progress through the planning steps.
- Emoji Icons: Enhances visual appeal and usability.
- Responsive Design: Works seamlessly on desktop and mobile devices.
- Styled Cards: Displays itineraries in a clean, modern layout.

📝 Sample Input/Output
**Input:**
- Destination: Kyoto, Japan
- Duration: 5 days
- Budget: Moderate ($1000)
- Purpose: Cultural immersion
- Preferences: Temples, local cuisine, walking-friendly

**Output:**
# Day 1: Exploring Kyoto
- **Morning**: Visit Fushimi Inari Shrine
- **Afternoon**: Lunch at a traditional ryokan
- **Evening**: Stroll through Gion District

# Day 2: Cultural Immersion
- **Morning**: Tea ceremony experience
- **Afternoon**: Explore Kinkaku-ji (Golden Pavilion)
- **Evening**: Dinner at a local izakaya
...

🚧 Future Improvements
- Multi-Destination Support: Allow users to plan trips with multiple stops.
- Real-Time Data: Integrate weather forecasts and flight information.
- Save & Share: Enable users to save and share itineraries.
- Language Support: Add support for multiple languages.

🤝 Contributing
Contributions are welcome! If you'd like to contribute, please:
- Fork the repository.
- Create a new branch (git checkout -b feature/YourFeature).
- Commit your changes (git commit -m 'Add some feature').
- Push to the branch (git push origin feature/YourFeature).
- Open a pull request.

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

🙏 Acknowledgments
- OpenAI for the GPT-4 API.
- Streamlit for the amazing framework to build interactive apps.
- Icons from Flaticon.

📧 Contact
For questions or feedback, feel free to reach out:
- Name: Ravirajsingh Sodha
- Email: ravirajsinghsodha441@gmail.com
- GitHub: [raviraj-441](https://github.com/raviraj-441)

---
