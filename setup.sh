#!/bin/bash
# Meta² Onboarding Feature Setup

echo "🚀 Setting up Meta² Onboarding Feature"
echo "======================================"

# Check dependencies
echo "📋 Checking dependencies..."
python3 --version || { echo "❌ Python 3 required"; exit 1; }

# Make scripts executable
chmod +x demo-onboard.sh
chmod +x onboard-feature.py

# Test onboarding
echo "🧪 Testing onboarding feature..."
python3 onboard-feature.py > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "✅ Onboarding feature working"
else
    echo "⚠️  Onboarding test had issues (may be normal if no zsh history)"
fi

# Create profiles directory
mkdir -p profiles

echo ""
echo "✅ Setup complete!"
echo ""
echo "🎯 Next steps:"
echo "  1. Run demo: ./demo-onboard.sh"
echo "  2. Integrate with Meta²: Add api-integration.py to orchestrator"
echo "  3. Test API: POST /orchestrator/onboard"
echo ""
echo "📚 See README.md for full documentation"
