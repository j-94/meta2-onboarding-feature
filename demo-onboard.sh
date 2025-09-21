#!/bin/bash
# Demo: Meta² Onboarding Feature

echo "🚀 Meta² Onboarding Demo"
echo "========================"

# Test the onboarding
echo "📊 Analyzing your shell history..."
python3 onboard-feature.py

echo ""
echo "✅ Onboarding complete!"
echo ""
echo "🔧 This feature learns:"
echo "  • Your preferred tools (git, curl, python, etc.)"
echo "  • Editor choice (VS Code, vim, etc.)"
echo "  • Git workflow patterns"
echo "  • API usage patterns"
echo "  • File operation habits"
echo ""
echo "🤖 Then configures agents to:"
echo "  • Use your preferred tools"
echo "  • Follow your workflow patterns"
echo "  • Suggest commands you actually use"
echo ""
echo "📡 API Integration:"
echo "  POST /orchestrator/onboard {\"user_id\": \"dev123\"}"
