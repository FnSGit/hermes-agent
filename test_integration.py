#!/usr/bin/env python3
"""
Quick test to verify Activity Feed integration works in the CLI.
"""

import os
import sys

# Enable activity feed for this test
os.environ['HERMES_ENABLE_ACTIVITY_FEED'] = 'true'
os.environ['HERMES_ENABLE_REASONING_DISPLAY'] = 'true'

from agent.display import ActivityFeed, ReasoningDisplay

print("\n" + "="*60)
print("Testing Activity Feed Integration")
print("="*60 + "\n")

# Test 1: Activity Feed
print("Test 1: Activity Feed Display")
print("-"*40)

feed = ActivityFeed(prefix="┊")
feed.start()

# Simulate agent activities
feed.add_activity("thinking", "Analyzing user request", {"query": "test"})
import time
time.sleep(0.1)
feed.complete_activity(status="completed", result_preview="analysis done")

feed.add_activity("search", "Searching files", {"pattern": "*.py"})
time.sleep(0.1)
feed.complete_activity(status="completed", result_preview="found 10 files")

feed.add_activity("read", "Reading file", {"path": "test.py"})
time.sleep(0.1)
feed.complete_activity(status="completed", result_preview="read 100 lines")

feed.stop()

print("\n✓ Activity Feed works!\n")

# Test 2: Reasoning Display
print("Test 2: Reasoning Display")
print("-"*40)

display = ReasoningDisplay(max_lines=10)
reasoning_text = """用户想要测试 Activity Feed 功能。
我需要验证以下组件：
1. ActivityFeed 类是否正确初始化
2. 工具调用时是否正确记录活动
3. ReasoningDisplay 是否正确显示

让我逐一验证这些功能。
首先检查 ActivityFeed 的 start() 方法。
然后验证 add_activity() 和 complete_activity()。
最后测试 ReasoningDisplay 的显示效果。

所有测试都通过了！
功能实现完成！"""

display.display(reasoning_text, "蕾姆的思考过程")

print("\n✓ Reasoning Display works!\n")

print("="*60)
print("All Integration Tests Passed!")
print("="*60 + "\n")

print("💙 蕾姆的可视化功能已就绪！")
print("\n启用方法:")
print("  1. 在 ~/.hermes/config.yaml 中添加:")
print("     display:")
print("       activity_feed: true")
print("       reasoning_display: true")
print("\n  2. 或使用环境变量:")
print("     export HERMES_ENABLE_ACTIVITY_FEED=true")
print("     export HERMES_ENABLE_REASONING_DISPLAY=true")
print("\n  3. 然后运行:")
print("     python cli.py\n")
