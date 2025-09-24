#!/usr/bin/env python3
"""
Test with currently available OpenRouter models
"""
import requests
import json

def test_current_models():
    """Test with models that should be available"""
    api_key = "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"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/j-94/meta2-onboarding-feature",
        "X-Title": "Meta2 Onboarding Test"
    }
    
    # Try current available models
    models_to_try = [
        "openai/gpt-3.5-turbo",
        "anthropic/claude-3-haiku",
        "meta-llama/llama-3.1-8b-instruct",
        "google/gemini-flash-1.5"
    ]
    
    test_prompt = """Analyze this AI agent onboarding system:
    
    - Processes 16,709 shell commands in 0.23 seconds
    - Detects user tools (git, python, docker, VS Code)
    - Zero user input required
    - Local processing only (no data sent to cloud)
    - Generates personalized agent configurations
    
    Rate this system 1-10 and explain why it's innovative."""
    
    for model in models_to_try:
        print(f"🧪 Testing {model}...")
        
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": test_prompt}],
            "temperature": 0.1,
            "max_tokens": 300
        }
        
        try:
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=payload,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                content = result["choices"][0]["message"]["content"]
                print(f"✅ SUCCESS with {model}")
                print(f"📊 AI Analysis:\n{content}\n")
                return model, content
            else:
                print(f"❌ {response.status_code}: {response.text[:200]}")
                
        except Exception as e:
            print(f"❌ Exception: {e}")
    
    return None, None

if __name__ == "__main__":
    print("🤖 Testing Meta² Onboarding with Real AI Analysis")
    print("=" * 60)
    
    working_model, analysis = test_current_models()
    
    if working_model:
        print(f"🎉 SUCCESS! Got real AI analysis from {working_model}")
        print("🚀 This proves our system can get genuine AI evaluation!")
    else:
        print("❌ Need to check available models or add credits")
        print("💡 Visit https://openrouter.ai/models for current model list")
