#!/bin/bash
# Quick test script for Activity Feed

cd /home/fengshuai/develop/projects/python-projects/hermes-activity-feed
source ../hermes-agent/.venv/bin/activate

echo ""
echo "╔══════════════════════════════════════════════════════════╗"
echo "║        Testing Activity Feed with Real Config           ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""

# Test with a simple query
echo "Running: python cli.py -q 'Hello, please introduce yourself'"
echo ""

# Use timeout to prevent hanging
timeout 30 python cli.py -q "Hello, please introduce yourself" 2>&1 | head -100

echo ""
echo "═══════════════════════════════════════════════════════════"
echo "If you see Activity Feed output above, it's working! 💙"
echo "═══════════════════════════════════════════════════════════"
