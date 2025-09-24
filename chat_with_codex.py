#!/usr/bin/env python3
"""
Chat with codex binary
"""
import subprocess
import json
import sys

def chat_with_codex(message):
    """Send message to codex binary"""
    codex_path = "/Users/imac/Desktop/codex-aarch64-apple-darwin"
    
    try:
        # Try different ways to communicate with the binary
        result = subprocess.run([codex_path, message], 
                              capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return f"Error: {result.stderr.strip()}"
            
    except subprocess.TimeoutExpired:
        return "Timeout: Binary took too long to respond"
    except FileNotFoundError:
        return "Binary not found at /Users/imac/Desktop/codex-aarch64-apple-darwin"
    except Exception as e:
        return f"Error: {e}"

def interactive_chat():
    """Interactive chat loop"""
    print("🤖 Codex Binary Chat")
    print("=" * 30)
    print("Type 'quit' to exit")
    
    while True:
        try:
            user_input = input("\n> ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                break
                
            if not user_input:
                continue
            
            print("🔄 Sending to codex...")
            response = chat_with_codex(user_input)
            print(f"🤖 {response}")
            
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break

def test_codex_binary():
    """Test codex binary with Meta² onboarding question"""
    print("🧪 Testing codex binary...")
    
    test_message = "Analyze this onboarding system: processes 16K shell commands in 0.23s, detects tools automatically. Rate 1-10."
    
    response = chat_with_codex(test_message)
    print(f"📊 Codex response: {response}")
    
    return response

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Single message mode
        message = " ".join(sys.argv[1:])
        response = chat_with_codex(message)
        print(response)
    else:
        # Test first, then interactive
        test_codex_binary()
        print("\n" + "="*50)
        interactive_chat()
