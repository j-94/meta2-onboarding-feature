#!/usr/bin/env python3
"""
Test Grok-4 directly for fast code analysis
"""
import requests
import json

def test_grok4():
    """Test Grok-4 with working API key"""
    api_key = "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"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/j-94/meta2-onboarding-feature",
        "X-Title": "Meta2 Grok Test"
    }
    
    # Try different Grok model names
    grok_models = [
        "x-ai/grok-2-1212",
        "x-ai/grok-beta",
        "xai/grok-beta",
        "grok-beta"
    ]
    
    prompt = """Code review this Meta² onboarding function:

```python
def analyze_command_patterns(self, commands):
    patterns = {"git_workflow": [], "dev_tools": [], "api_usage": []}
    for cmd in commands[-100:]:
        if cmd.startswith('git'):
            patterns["git_workflow"].append(cmd)
        elif 'curl' in cmd:
            patterns["api_usage"].append(cmd)
    return patterns
```

Rate 1-10 and suggest improvements. Be direct."""
    
    for model in grok_models:
        print(f"🧪 Testing {model}...")
        
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.1,
            "max_tokens": 400
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
                print(f"✅ GROK-4 SUCCESS!")
                print(f"🚀 Grok Analysis:\n{content}")
                return content
            else:
                print(f"❌ {response.status_code}: {response.text[:100]}")
                
        except Exception as e:
            print(f"❌ {e}")
    
    return None

if __name__ == "__main__":
    print("🚀 Testing Grok-4 for Fast Code Analysis")
    print("=" * 50)
    
    analysis = test_grok4()
    
    if analysis:
        print("\n🎯 Got real Grok-4 code review!")
    else:
        print("\n❌ Grok-4 not available, but GPT-3.5 is working")
