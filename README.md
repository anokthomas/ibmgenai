# AI-Powered Instagram Caption and Hashtag Generator

A simple web application that generates creative Instagram captions and relevant hashtags using Google's Gemini AI model.

## Features

- Generate 3-5 creative captions based on post descriptions
- Suggest relevant and trending hashtags
- Clean, intuitive web interface
- Real-time AI-powered content generation

## Tech Stack

- **Python** - Backend logic
- **Streamlit** - Web interface
- **Google Gemini API** - AI model for content generation

## Setup

1. Clone the repository
```bash
git clone https://github.com/yourusername/instagram-caption-generator.git
cd instagram-caption-generator
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Set up your Gemini API key
```bash
export GEMINI_API_KEY="your-api-key-here"
```

4. Run the application
```bash
streamlit run app.py
```

## Usage

1. Enter a description of your Instagram post
2. Click generate to get AI-powered captions and hashtags
3. Copy your favorite caption and hashtags to Instagram

## Example

**Input:** "My cat sleeping in a sunbeam"

**Output:**
- "Soaking up the Caturday sun ☀️"
- "Powered by solar energy and naps"
- "Living the dream, one sunbeam at a time"

**Hashtags:** #catsofinstagram #sleepycat #sunbeam #cozyvibes

## Project Structure

```
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

---

*Built as part of a Gen AI project *
