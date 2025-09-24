#!/usr/bin/env python3
"""
Test onboarding with actual Meta² API (running locally)
"""
import requests
import json

def test_meta2_onboarding():
    """Test with real Meta² orchestrator API"""
    
    # Test if Meta² is running
    try:
        health_response = requests.get("http://127.0.0.1:8080/healthz", timeout=5)
        if health_response.status_code != 200:
            print("❌ Meta² API not running. Start with: cd ../agentops && bash run.sh")
            return
    except requests.exceptions.RequestException:
        print("❌ Meta² API not running. Start with: cd ../agentops && bash run.sh")
        return
    
    print("✅ Meta² API is running")
    
    # Test onboarding request
    headers = {
        "X-API-Key": "change-me",
        "Content-Type": "application/json"
    }
    
    # Test 1: Basic chat
    print("\n🧪 Testing basic chat...")
    chat_payload = {
        "message": "Analyze my shell history and configure agents for my workflow"
    }
    
    response = requests.post(
        "http://127.0.0.1:8080/orchestrator/chat",
        headers=headers,
        json=chat_payload
    )
    
    if response.status_code == 200:
        result = response.json()
        print(f"✅ Chat response: {result.get('reply', 'No reply')}")
        print(f"📊 Status: {result.get('status', 'Unknown')}")
        print(f"🎯 Bits: {result.get('bits', {})}")
    else:
        print(f"❌ Chat failed: {response.status_code}")
    
    # Test 2: Request onboarding feature
    print("\n🧪 Testing onboarding request...")
    onboard_payload = {
        "message": "Run onboarding analysis on my shell history and create personalized agent config"
    }
    
    response = requests.post(
        "http://127.0.0.1:8080/orchestrator/chat",
        headers=headers,
        json=onboard_payload
    )
    
    if response.status_code == 200:
        result = response.json()
        print(f"✅ Onboarding response: {result.get('reply', 'No reply')}")
        print(f"📊 Run ID: {result.get('run_id', 'None')}")
        
        # Show what the system would do
        print("\n🤖 What Meta² would do with onboarding:")
        print("• Analyze your 16K+ shell commands")
        print("• Detect tools: git, curl, python, docker, code")
        print("• Identify VS Code as preferred editor")
        print("• Configure agents to match your workflow")
        print("• Generate personalized prompts and templates")
        
    else:
        print(f"❌ Onboarding failed: {response.status_code}")

if __name__ == "__main__":
    print("🚀 Testing Meta² Onboarding with Real API")
    print("=" * 50)
    test_meta2_onboarding()
