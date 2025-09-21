#!/usr/bin/env python3
"""
Meta² Onboarding Feature - Learn from user's shell history
Usage: POST /orchestrator/onboard {"user_id": "dev123"}
"""
import json
import subprocess
from pathlib import Path

class Meta2Onboarding:
    def __init__(self, user_id):
        self.user_id = user_id
        self.profile_dir = Path(f"profiles/{user_id}")
        self.profile_dir.mkdir(parents=True, exist_ok=True)
    
    def extract_user_patterns(self):
        """Extract patterns from user's shell history"""
        # Get zsh history
        history_cmd = [
            "perl", "-nle", 
            "if(/^: (\\d+):\\d+;(.*)$/){print scalar localtime($1) . '  ' . $2} else {print}",
            str(Path.home() / ".zsh_history")
        ]
        
        try:
            result = subprocess.run(history_cmd, capture_output=True, text=True, errors='ignore')
            commands = result.stdout.strip().split('\n')
            
            # Analyze patterns
            patterns = self.analyze_command_patterns(commands)
            
            # Save user profile
            profile = {
                "user_id": self.user_id,
                "command_count": len(commands),
                "patterns": patterns,
                "preferences": self.infer_preferences(patterns),
                "tools": self.detect_tools(commands)
            }
            
            with open(self.profile_dir / "profile.json", 'w') as f:
                json.dump(profile, f, indent=2)
            
            return profile
            
        except Exception as e:
            return {"error": f"Failed to extract patterns: {e}"}
    
    def analyze_command_patterns(self, commands):
        """Analyze user's command patterns"""
        patterns = {
            "git_workflow": [],
            "dev_tools": [],
            "api_usage": [],
            "file_ops": []
        }
        
        for cmd in commands[-100:]:  # Last 100 commands
            if not cmd.strip():
                continue
                
            # Extract command part (after timestamp)
            if '  ' in cmd:
                command = cmd.split('  ', 1)[1]
            else:
                command = cmd
            
            # Categorize
            if command.startswith('git'):
                patterns["git_workflow"].append(command)
            elif any(tool in command for tool in ['curl', 'http', 'api']):
                patterns["api_usage"].append(command)
            elif any(tool in command for tool in ['python', 'node', 'npm', 'cargo']):
                patterns["dev_tools"].append(command)
            elif any(op in command for op in ['cd', 'ls', 'mkdir', 'cp', 'mv']):
                patterns["file_ops"].append(command)
        
        return patterns
    
    def infer_preferences(self, patterns):
        """Infer user preferences from patterns"""
        prefs = {
            "preferred_editor": "unknown",
            "git_style": "unknown",
            "api_tool": "unknown",
            "shell_style": "unknown"
        }
        
        all_commands = []
        for category in patterns.values():
            all_commands.extend(category)
        
        command_text = ' '.join(all_commands)
        
        # Infer preferences
        if 'code' in command_text or 'vscode' in command_text:
            prefs["preferred_editor"] = "vscode"
        elif 'vim' in command_text or 'nvim' in command_text:
            prefs["preferred_editor"] = "vim"
        
        if 'gh ' in command_text:
            prefs["git_style"] = "github_cli"
        elif len(patterns["git_workflow"]) > 5:
            prefs["git_style"] = "command_line"
        
        if 'curl' in command_text:
            prefs["api_tool"] = "curl"
        elif 'http' in command_text:
            prefs["api_tool"] = "httpie"
        
        return prefs
    
    def detect_tools(self, commands):
        """Detect tools user frequently uses"""
        tools = set()
        
        for cmd in commands:
            if not cmd.strip():
                continue
            
            # Extract first word (command)
            first_word = cmd.split()[0] if cmd.split() else ""
            
            # Common dev tools
            dev_tools = {
                'git', 'gh', 'curl', 'wget', 'docker', 'kubectl', 
                'python', 'node', 'npm', 'yarn', 'cargo', 'go',
                'code', 'vim', 'nvim', 'tmux', 'screen'
            }
            
            if first_word in dev_tools:
                tools.add(first_word)
        
        return list(tools)
    
    def generate_agent_config(self):
        """Generate personalized agent config"""
        profile_file = self.profile_dir / "profile.json"
        if not profile_file.exists():
            return {"error": "No profile found. Run onboarding first."}
        
        with open(profile_file) as f:
            profile = json.load(f)
        
        # Generate config based on user patterns
        config = {
            "user_id": self.user_id,
            "agent_preferences": {
                "editor": profile["preferences"]["preferred_editor"],
                "git_workflow": profile["preferences"]["git_style"],
                "api_tool": profile["preferences"]["api_tool"]
            },
            "suggested_tools": profile["tools"],
            "custom_prompts": self.generate_custom_prompts(profile),
            "workflow_templates": self.generate_workflows(profile)
        }
        
        return config
    
    def generate_custom_prompts(self, profile):
        """Generate custom prompts based on user patterns"""
        prompts = []
        
        if 'git' in profile["tools"]:
            prompts.append({
                "trigger": "version_control",
                "prompt": f"Use {profile['preferences']['git_style']} workflow for git operations"
            })
        
        if profile["preferences"]["preferred_editor"] != "unknown":
            prompts.append({
                "trigger": "edit_file", 
                "prompt": f"Open files in {profile['preferences']['preferred_editor']}"
            })
        
        return prompts
    
    def generate_workflows(self, profile):
        """Generate workflow templates"""
        workflows = []
        
        # Git workflow
        if len(profile["patterns"]["git_workflow"]) > 3:
            workflows.append({
                "name": "user_git_workflow",
                "steps": profile["patterns"]["git_workflow"][-3:]  # Last 3 git commands
            })
        
        return workflows

# API endpoint integration
def onboard_user(user_id):
    """Main onboarding function for Meta² API"""
    onboarder = Meta2Onboarding(user_id)
    
    # Extract patterns
    profile = onboarder.extract_user_patterns()
    if "error" in profile:
        return profile
    
    # Generate config
    config = onboarder.generate_agent_config()
    
    return {
        "status": "onboarded",
        "user_id": user_id,
        "profile": profile,
        "agent_config": config,
        "message": f"Learned from {profile['command_count']} commands"
    }

if __name__ == "__main__":
    # Test onboarding
    result = onboard_user("dev123")
    print(json.dumps(result, indent=2))
