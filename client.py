# AIzaSyDdagaU9rXnJjWldYUaZnoE8iHj76PThm4

import google.generativeai as genai
from google.generativeai.types import GenerationConfig

# Configure with your API key
API_KEY = "AIzaSyDdagaU9rXnJjWldYUaZnoE8iHj76PThm4"
genai.configure(api_key=API_KEY)

# Model selection - choose one based on your needs
MODEL_NAME = "models/gemini-1.5-pro-latest"  # Default recommendation
# Alternatives:
# MODEL_NAME = "models/gemini-1.5-flash-latest"  # Faster but less capable
# MODEL_NAME = "models/gemini-2.5-pro-preview-03-25"  # If you have access

def ask_gemini(prompt):
    try:
        # Initialize the model
        model = genai.GenerativeModel(MODEL_NAME)
        
        # Configure generation parameters
        generation_config = GenerationConfig(
            temperature=0.9,
            top_p=0.95,
            top_k=40,
            max_output_tokens=2048,
        )
        
        # Generate response
        response = model.generate_content(
            prompt,
            generation_config=generation_config,
            safety_settings={
                "HARASSMENT": "BLOCK_NONE",
                "HATE_SPEECH": "BLOCK_NONE",
                "SEXUAL": "BLOCK_NONE",
                "DANGEROUS": "BLOCK_NONE"
            }
        )
        
        return response.text
    
    except Exception as e:
        print(f"Gemini API Error: {e}")
        return "Sorry, I encountered an error processing your request."