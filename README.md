# ibmgenai
An AI-powered web application built with Streamlit and Google's Gemini Pro to generate creative Instagram captions and relevant hashtags based on a user's post description.
🌟 Demo
![alt text](demo.png)
(Note: Replace demo.png with a screenshot of your actual running application.)
✨ Core Features
Creative Captions: Generates multiple distinct and engaging caption options for your post.
Hashtag Suggestions: Provides a list of 15 relevant and trending hashtags to maximize reach.
Tone Customization: Allows you to select the desired tone for your captions (e.g., Casual, Humorous, Inspirational).
Simple UI: An intuitive and easy-to-use web interface built with Streamlit.
🛠️ Technologies Used
Backend: Python
Frontend: Streamlit
AI Model: Google Gemini Pro API
Libraries: google-generativeai, streamlit
🚀 Setup and Installation
Follow these steps to get the application running on your local machine.
1. Prerequisites
Python 3.8 or higher
Git
2. Clone the Repository
Open your terminal and clone the repository:
Generated bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
Use code with caution.
Bash
3. Create a Virtual Environment (Recommended)
It's a best practice to create a virtual environment to manage project dependencies.
Generated bash
# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate
Use code with caution.
Bash
4. Install Dependencies
Install the required Python libraries using the requirements.txt file:
Generated bash
pip install -r requirements.txt
Use code with caution.
Bash
5. Set Up Your Google Gemini API Key
You need an API key from Google AI Studio to use the Gemini model.
Visit the Google AI Studio.
Click on "Get API key" and create a new key.
Copy your generated API key.
Now, you must add this key to the application.
Option 1: Hardcode the Key (Quick & Simple for Local Testing)
⚠️ Security Warning: This method is not secure. Do not share your code publicly if you hardcode your API key.
Open the app.py file in a code editor.
Find this line near the top:
Generated python
api_key = "YOUR_API_KEY_HERE"
Use code with caution.
Python
Replace "YOUR_API_KEY_HERE" with your actual Gemini API key.
Option 2: Use Environment Variables (Recommended & Secure)
This is the safer method, especially if you plan to share your code. You will need to modify app.py slightly to read the key from the environment.
In your terminal, set the environment variable:
Generated bash
# For macOS/Linux
export GEMINI_API_KEY="YOUR_API_KEY_HERE"

# For Windows
set GEMINI_API_KEY="YOUR_API_KEY_HERE"
Use code with caution.
Bash
Then, modify the app.py file to read this variable:
Generated python
# Replace the hardcoded line with this:
import os
api_key = os.getenv("GEMINI_API_KEY")
Use code with caution.
Python
6. Run the Application
Once the dependencies are installed and the API key is set up, run the Streamlit app from your terminal:
Generated bash
streamlit run app.py
Use code with caution.
Bash
Your web browser will automatically open a new tab with the application running at http://localhost:8501.
📖 How to Use
Launch the App: Run the command streamlit run app.py.
Describe Your Post: In the text area, write a description of the photo or video you want to post.
Select a Tone: Choose a tone from the dropdown menu that matches your desired style.
Generate: Click the "🚀 Generate Content" button.
Copy & Paste: The AI will generate 3 captions and a list of hashtags. Copy your favorite ones and use them on Instagram!
📂 Project Structure
