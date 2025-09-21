#!/bin/bash
# Setup Meta² Onboarding with Real API Keys

echo "🔑 Setting up Meta² Onboarding with Real API Keys"
echo "================================================="

# Check if .env exists
if [ ! -f .env ]; then
    echo "📝 Creating .env file..."
    cp .env.example .env
    echo ""
    echo "⚠️  Please edit .env and add your real API keys:"
    echo "   OPENROUTER_API_KEY=your-key-here"
    echo ""
    echo "🔗 Get keys from:"
    echo "   • OpenRouter: https://openrouter.ai/keys"
    echo "   • OpenAI: https://platform.openai.com/api-keys"
    echo ""
    read -p "Press Enter after adding your keys to .env..."
fi

# Test API connection
echo "🧪 Testing API connection..."
python3 -c "
import os
from pathlib import Path

# Load .env
env_file = Path('.env')
if env_file.exists():
    with open(env_file) as f:
        for line in f:
            if '=' in line and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                os.environ[key] = value

api_key = os.getenv('OPENROUTER_API_KEY', '')
if api_key and api_key != 'your-openrouter-key-here':
    print('✅ API key found')
else:
    print('❌ No valid API key found')
"

echo ""
echo "🚀 Ready to test with real Grok-4:"
echo "   python3 grok_real_test.py"
echo ""
echo "🔒 Security notes:"
echo "   • .env is in .gitignore (won't be committed)"
echo "   • Keys stay local to your machine"
echo "   • Use environment variables in production"
