#!/bin/bash
# Push changes to your forked repository
# 推送更改到您 fork 的仓库

set -e

echo ""
echo "╔══════════════════════════════════════════════════════════╗"
echo "║        Push Activity Feed Feature to Your Fork          ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""

# Check current branch
BRANCH=$(git branch --show-current)
echo "📍 Current branch: $BRANCH"
echo ""

# Show current remotes
echo "📋 Current remotes:"
git remote -v
echo ""

# Check if fork remote exists
if git remote | grep -q '^fork$'; then
    echo "✅ 'fork' remote already exists"
else
    echo "⚠️  'fork' remote not found"
    echo ""
    echo "Please add your fork remote first:"
    echo ""
    echo "  # Option 1: SSH (recommended)"
    echo "  git remote add fork git@github.com:YOUR_USERNAME/hermes-agent.git"
    echo ""
    echo "  # Option 2: HTTPS"
    echo "  git remote add fork https://github.com/YOUR_USERNAME/hermes-agent.git"
    echo ""
    read -p "Enter your GitHub username (or press Enter to skip): " username
    
    if [ -n "$username" ]; then
        echo ""
        echo "🔧 Adding fork remote for user: $username"
        
        # Try SSH first
        if git remote add fork git@github.com:$username/hermes-agent.git 2>/dev/null; then
            echo "✅ Added SSH remote: git@github.com:$username/hermes-agent.git"
        else
            # If SSH fails, try HTTPS
            git remote remove fork 2>/dev/null || true
            if git remote add fork https://github.com/$username/hermes-agent.git 2>/dev/null; then
                echo "✅ Added HTTPS remote: https://github.com/$username/hermes-agent.git"
            else
                echo "❌ Failed to add remote. Please add manually."
                exit 1
            fi
        fi
    else
        echo "⏭️  Skipping fork remote setup"
        echo ""
        echo "You can push to a new branch on origin instead:"
        echo "  git push -u origin $BRANCH"
        exit 0
    fi
fi

echo ""
echo "═══════════════════════════════════════════════════════════"
echo ""

# Show commit to be pushed
echo "📝 Last commit:"
git log -1 --pretty=format:"  %h %s" 
echo ""
echo ""

# Push to fork
echo "🚀 Pushing to fork/$BRANCH..."
if git push -u fork $BRANCH; then
    echo ""
    echo "╔══════════════════════════════════════════════════════════╗"
    echo "║                    ✅ Push Successful!                   ║"
    echo "╚══════════════════════════════════════════════════════════╝"
    echo ""
    echo "📍 Pushed to: fork/$BRANCH"
    echo ""
    echo "🔗 Next steps:"
    echo "   1. Go to https://github.com/YOUR_USERNAME/hermes-agent"
    echo "   2. Click 'Compare & pull request'"
    echo "   3. Create a PR to NousResearch/hermes-agent"
    echo ""
    echo "💙 Don't forget to mention the Activity Feed feature in your PR!"
    echo ""
else
    echo ""
    echo "❌ Push failed. Please check your remote configuration."
    echo ""
    exit 1
fi
