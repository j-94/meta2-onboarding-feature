#!/usr/bin/env python3
"""
Test Grok with different endpoints and models
"""
import os
import requests
import json

def test_openrouter_models():
    """Test different models on OpenRouter"""
    api_key = "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"
    
    models_to_try = [
        "x-ai/grok-beta",
        "anthropic/claude-3.5-sonnet",
        "openai/gpt-4o-mini",
        "meta-llama/llama-3.1-70b-instruct"
    ]
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    test_prompt = "Analyze this Meta² onboarding system that processes shell history in 0.23 seconds. Rate it 1-10."
    
    for model in models_to_try:
        print(f"🧪 Testing {model}...")
        
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": test_prompt}],
            "temperature": 0.1,
            "max_tokens": 200
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
                print(f"✅ {model}: {content[:100]}...")
                return model, content
            else:
                print(f"❌ {model}: {response.status_code} - {response.text[:100]}")
                
        except Exception as e:
            print(f"❌ {model}: {e}")
    
    return None, None

if __name__ == "__main__":
    print("🔍 Testing OpenRouter API with real key...")
    working_model, response = test_openrouter_models()
    
    if working_model:
        print(f"\n✅ Working model found: {working_model}")
        print(f"📊 Response: {response}")
    else:
        print("\n❌ No working models found")
        print("🔧 Check API key validity or account status")
