#!/usr/bin/env python3
"""
Test with models that should work on OpenRouter
"""
import requests
import json

def test_openrouter_auth():
    """Test OpenRouter authentication"""
    api_key = "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"
    
    # Test with a simple, reliable model
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/j-94/meta2-onboarding-feature",
        "X-Title": "Meta2 Onboarding Test"
    }
    
    # Try free models first
    free_models = [
        "microsoft/phi-3-mini-128k-instruct:free",
        "huggingfaceh4/zephyr-7b-beta:free",
        "openchat/openchat-7b:free"
    ]
    
    test_prompt = "Rate this AI onboarding system: processes 16K shell commands in 0.23 seconds. Score 1-10."
    
    for model in free_models:
        print(f"🧪 Testing {model}...")
        
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": test_prompt}],
            "temperature": 0.1,
            "max_tokens": 100
        }
        
        try:
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=payload,
                timeout=30
            )
            
            print(f"Status: {response.status_code}")
            
            if response.status_code == 200:
                result = response.json()
                content = result["choices"][0]["message"]["content"]
                print(f"✅ SUCCESS with {model}")
                print(f"📊 Response: {content}")
                return model, content
            else:
                print(f"❌ Error: {response.text}")
                
        except Exception as e:
            print(f"❌ Exception: {e}")
    
    # If free models don't work, check account status
    print("\n🔍 Checking account status...")
    try:
        response = requests.get(
            "https://openrouter.ai/api/v1/auth/key",
            headers={"Authorization": f"Bearer {api_key}"}
        )
        print(f"Auth check: {response.status_code}")
        if response.status_code == 200:
            print(f"Account info: {response.json()}")
        else:
            print(f"Auth error: {response.text}")
    except Exception as e:
        print(f"Auth check failed: {e}")
    
    return None, None

if __name__ == "__main__":
    print("🔑 Testing OpenRouter API with Updated Key")
    print("=" * 50)
    
    working_model, response = test_openrouter_auth()
    
    if working_model:
        print(f"\n🎉 SUCCESS! Working model: {working_model}")
        print("🚀 Now we can run real AI analysis of our onboarding system!")
    else:
        print("\n❌ API key may need activation or credits")
        print("💡 Check OpenRouter dashboard: https://openrouter.ai/")
        print("💡 Ensure account has credits or free tier access")
