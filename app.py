import streamlit as st
import google.generativeai as genai
import os

# --- Page Configuration ---
st.set_page_config(
    page_title="AI Instagram Caption Generator",
    page_icon="📸",
    layout="centered",
)


api_key = "YOUR_API_KEY_HERE"


# --- Function to call Gemini API ---
def generate_content_with_gemini(api_key, post_description, tone, platform="Instagram"):
    """
    Calls the Gemini API to generate captions and hashtags.
    """
    try:
        genai.configure(api_key=api_key)
        
    
        prompt = f"""
        You are an expert social media manager and content creator specializing in {platform}.
        Your task is to generate creative and engaging content based on a user's description.

        **Post Description:** "{post_description}"
        **Desired Tone:** {tone}

        **Instructions:**
        1.  Generate 3 distinct and creative captions for an {platform} post.
        2.  Each caption must perfectly match the desired tone: **{tone}**.
        3.  After the captions, generate a list of 15 relevant and trending hashtags.
        4.  The hashtags should be a mix of popular and niche tags to maximize reach.
        5.  Format your entire response in Markdown.
        
        **Output Format:**
        **✨ Captions**
        1. [First caption here]
        2. [Second caption here]
        3. [Third caption here]

        ---

        **#️⃣ Hashtags**
        [#hashtag1 #hashtag2 #hashtag3 ...]
        
        Do not include any other introductory text, explanations, or closing remarks.
        """

        model = genai.GenerativeModel('gemini-2.0-flash')
        response = model.generate_content(prompt)
        
        if response and response.text:
            return response.text
        else:
            return "❌ **Error:** Failed to generate content. The API returned an empty response."

    except Exception as e:
        return f"❌ **Error:** An error occurred: {str(e)}"

# --- Streamlit App UI ---

# --- Header ---
st.title("AI Instagram Caption & Hashtag Generator 📸")
st.markdown("Struggling with creative block? Describe your post, and let AI craft the perfect captions and hashtags for you!")

# --- Main Content ---
st.subheader("✍️ Describe Your Post")

# User Inputs
post_description = st.text_area(
    "Enter a description of your photo or video (e.g., 'a photo of my golden retriever playing fetch at the beach during sunset').",
    height=150,
    placeholder="What's on your mind?"
)

tone_options = ["Casual 😎", "Humorous 😂", "Inspirational ✨", "Formal 👔", "Adventurous 🧗‍♀️", "Cozy 🧣"]
selected_tone = st.selectbox("Select the desired tone for your captions:", tone_options)

# Generate Button
if st.button("🚀 Generate Content", type="primary"):
    # Check if the user has replaced the placeholder API key
    if not api_key or api_key == "YOUR_API_KEY_HERE":
        st.error("Please replace 'YOUR_API_KEY_HERE' in the app.py file with your actual Gemini API key.")
    elif not post_description:
        st.warning("Please enter a description for your post.")
    else:
        with st.spinner("Crafting the perfect post... This might take a moment!"):
            # Call the Gemini function
            generated_content = generate_content_with_gemini(api_key, post_description, selected_tone)
            
            # Display the results
            st.divider()
            st.subheader("🎉 Your Generated Content")
            st.markdown(generated_content)

# --- Footer in Sidebar ---
with st.sidebar:
    st.header("About this App")
    st.markdown(
        "This tool uses Google's Gemini Pro model to generate creative content for social media."
    )
    st.markdown(
        "**Developed by:**\n"
        "Student Anok"
    )
