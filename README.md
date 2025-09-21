# Meta² Onboarding Feature

**Instantly personalize AI agents by learning from user's shell history**

## 🚀 Quick Start

```bash
# 1. Clone and setup
git clone https://github.com/j-94/meta2-onboarding-feature
cd meta2-onboarding-feature

# 2. Run onboarding
./setup.sh

# 3. Test API
curl -X POST http://127.0.0.1:8080/orchestrator/onboard \
  -H "X-API-Key: change-me" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "your-id"}'
```

## 📋 Deliverables

### Core Components
- ✅ **onboard-feature.py** - Main onboarding engine
- ✅ **api-integration.py** - FastAPI endpoint integration  
- ✅ **setup.sh** - One-command deployment
- ✅ **demo-onboard.sh** - Interactive demo

### Data Processing
- ✅ **Shell history parser** - Extracts 16K+ commands
- ✅ **Pattern analyzer** - Detects tools, workflows, preferences
- ✅ **Profile generator** - Creates personalized agent configs

### API Integration
- ✅ **POST /orchestrator/onboard** - New Meta² endpoint
- ✅ **User profiling** - Automatic preference detection
- ✅ **Agent configuration** - Custom prompts and workflows

## 🎯 What It Learns

From your shell history:
- **Preferred tools**: git, curl, python, docker, etc.
- **Editor choice**: VS Code, vim, nano
- **Git workflow**: CLI vs GitHub CLI patterns
- **API preferences**: curl vs httpie vs wget
- **Development patterns**: Languages, frameworks, deployment

## 🤖 Agent Personalization

Configures agents to:
- Use your preferred editor for file operations
- Follow your git workflow patterns
- Suggest tools you actually use
- Match your command-line style
- Respect your development preferences

## 📊 Example Output

```json
{
  "profile": {
    "command_count": 16717,
    "tools": ["git", "curl", "python", "docker", "code"],
    "preferences": {
      "preferred_editor": "vscode",
      "api_tool": "curl",
      "git_style": "github_cli"
    }
  },
  "agent_config": {
    "custom_prompts": [
      {"trigger": "edit_file", "prompt": "Open files in vscode"},
      {"trigger": "version_control", "prompt": "Use github_cli workflow"}
    ],
    "suggested_tools": ["git", "gh", "curl", "python", "docker"]
  }
}
```

## 🔧 Integration

Add to existing Meta² orchestrator:

```python
# In orchestrator/api.py
from .onboard_feature import onboard_user

@app.post("/orchestrator/onboard")
async def onboard_endpoint(request: OnboardRequest):
    result = onboard_user(request.user_id)
    return {"status": "onboarded", "data": result}
```

## 🎪 Demo

```bash
./demo-onboard.sh
# Analyzes your shell history and shows personalization results
```

## 📈 Benefits

- **Zero training time** - Agents work like you from day one
- **Automatic personalization** - No manual configuration
- **Privacy-first** - Processes history locally
- **Scalable** - Works with any shell history size
- **Extensible** - Easy to add new pattern detection

## 🛠 Technical Details

- **Language**: Python 3.8+
- **Dependencies**: Standard library only
- **Input**: ~/.zsh_history (or any shell history)
- **Output**: JSON profiles and agent configs
- **Integration**: FastAPI endpoint for Meta² orchestrator

---

**Repository**: https://github.com/j-94/meta2-onboarding-feature  
**Demo**: Run `./demo-onboard.sh` to see it in action
