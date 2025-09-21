#!/usr/bin/env python3
"""
Real Grok-4 Testing with API Keys from Environment
"""
import os
import json
import requests
from pathlib import Path

class RealGrokTester:
    def __init__(self):
        # Load from environment or .env file
        self.api_key = os.getenv('OPENROUTER_API_KEY')
        if not self.api_key:
            env_file = Path('.env')
            if env_file.exists():
                with open(env_file) as f:
                    for line in f:
                        if line.startswith('OPENROUTER_API_KEY='):
                            self.api_key = line.split('=', 1)[1].strip()
                            break
        
        self.grok_api = "https://openrouter.ai/api/v1/chat/completions"
        self.model = "x-ai/grok-beta"
    
    def ask_grok(self, prompt: str) -> str:
        """Real Grok API call"""
        if not self.api_key or self.api_key == "your-openrouter-key-here":
            return "❌ No API key found. Set OPENROUTER_API_KEY or create .env file"
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.1,
            "max_tokens": 1000
        }
        
        try:
            response = requests.post(self.grok_api, headers=headers, json=payload)
            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"]
            else:
                return f"❌ API Error {response.status_code}: {response.text}"
        except Exception as e:
            return f"❌ Request failed: {e}"

def test_with_real_grok():
    """Test onboarding with real Grok-4"""
    grok = RealGrokTester()
    
    print("🤖 Testing Meta² Onboarding with Real Grok-4")
    print("=" * 50)
    
    # Test 1: Validate our actual profile data
    try:
        with open('empirical_evidence.json') as f:
            evidence = json.load(f)
        
        profile_prompt = f"""
        Analyze this REAL user profile data from shell history analysis:
        
        Setup time: {evidence.get('setup_time_seconds', 0):.2f} seconds
        Commands processed: {evidence.get('commands_processed', 0)}
        Processing speed: {evidence.get('commands_per_second', 0):.0f} commands/second
        Tools detected: {evidence.get('detected_tools', [])}
        Local processing: {evidence.get('local_processing_verified', False)}
        
        Rate the effectiveness of this onboarding approach 1-10 and explain why.
        What improvements would you suggest?
        """
        
        print("🔍 Asking Grok to analyze REAL profile data...")
        analysis = grok.ask_grok(profile_prompt)
        print(f"📊 Grok Analysis:\n{analysis}\n")
        
    except FileNotFoundError:
        print("⚠️  No empirical evidence file found. Run empirical_evidence.py first")
    
    # Test 2: Code review with real Grok
    code_review_prompt = """
    Review this ACTUAL Python code for shell history onboarding:
    
    ```python
    def analyze_command_patterns(self, commands):
        patterns = {
            "git_workflow": [],
            "dev_tools": [],
            "api_usage": [],
            "file_ops": []
        }
        
        for cmd in commands[-100:]:  # Last 100 commands
            if not cmd.strip():
                continue
                
            if '  ' in cmd:
                command = cmd.split('  ', 1)[1]
            else:
                command = cmd
            
            if command.startswith('git'):
                patterns["git_workflow"].append(command)
            elif any(tool in command for tool in ['curl', 'http', 'api']):
                patterns["api_usage"].append(command)
            elif any(tool in command for tool in ['python', 'node', 'npm', 'cargo']):
                patterns["dev_tools"].append(command)
            elif any(op in command for op in ['cd', 'ls', 'mkdir', 'cp', 'mv']):
                patterns["file_ops"].append(command)
        
        return patterns
    ```
    
    What are the specific weaknesses and how would you improve it?
    """
    
    print("👨‍💻 Asking Grok for code review...")
    code_review = grok.ask_grok(code_review_prompt)
    print(f"🔧 Grok Code Review:\n{code_review}\n")
    
    # Test 3: SOTA validation
    sota_prompt = """
    Based on these REAL metrics for an AI agent onboarding system:
    
    - Setup time: 0.23 seconds
    - Processes 16,709 commands in 0.003 seconds
    - Zero network calls (local processing)
    - Detects 5+ development tools automatically
    - Requires zero user input
    
    Compare this to existing solutions like GitHub Copilot, Cursor, or ChatGPT onboarding.
    Is this genuinely state-of-the-art? What would make it more compelling?
    """
    
    print("🏆 Asking Grok about SOTA claims...")
    sota_analysis = grok.ask_grok(sota_prompt)
    print(f"🎯 Grok SOTA Analysis:\n{sota_analysis}\n")
    
    print("✅ Real Grok testing complete!")

if __name__ == "__main__":
    test_with_real_grok()
