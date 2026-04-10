#!/usr/bin/env python3
"""
Test script for ActivityFeed and ReasoningDisplay visualization features.

Usage:
    source venv/bin/activate
    python test_activity_feed.py
"""

import sys
import time
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from agent.display import ActivityFeed, ReasoningDisplay


def test_activity_feed():
    """Test the ActivityFeed class."""
    print("\n" + "="*60)
    print("Testing ActivityFeed")
    print("="*60 + "\n")
    
    feed = ActivityFeed(prefix="┊")
    feed.start()
    
    # Simulate various activities
    activities = [
        ("thinking", "Starting conversation", {"message": "Hello"}),
        ("search", "Searching files", {"pattern": "*.py"}),
        ("read", "Reading file", {"path": "run_agent.py"}),
        ("terminal", "Running command", {"command": "pytest tests/"}),
        ("write", "Writing file", {"path": "output.txt"}),
        ("web", "Web search", {"query": "Python best practices"}),
        ("memory", "Saving memory", {"target": "memory", "action": "add"}),
        ("skill", "Loading skill", {"name": "test-driven-development"}),
    ]
    
    for category, desc, args in activities:
        activity_id = feed.add_activity(category, desc, args=args)
        # Simulate work
        time.sleep(0.3)
        
        # Determine status and result preview
        status = "completed"
        result_preview = None
        if category == "terminal":
            result_preview = "exit 0"
        elif category == "read":
            result_preview = "1234 lines"
        elif category == "write":
            result_preview = "success"
        
        feed.complete_activity(activity_id, status=status, result_preview=result_preview)
    
    feed.stop()
    print("\n✓ ActivityFeed test completed!\n")


def test_reasoning_display():
    """Test the ReasoningDisplay class."""
    print("\n" + "="*60)
    print("Testing ReasoningDisplay")
    print("="*60 + "\n")
    
    display = ReasoningDisplay(max_lines=15, collapse_threshold=5)
    
    # Test 1: Short reasoning (should auto-collapse)
    print("Test 1: Short reasoning (auto-collapse)")
    print("-"*40)
    short_reasoning = """First, I need to understand the user's request.
Then I'll search for relevant files.
Finally, I'll provide a summary."""
    display.display(short_reasoning, "思考过程")
    
    # Test 2: Long reasoning (should show expanded panel)
    print("\nTest 2: Long reasoning (expanded panel)")
    print("-"*40)
    long_reasoning = """首先，我需要理解用户的需求。
用户想要查看 Activity Feed 和 Reasoning Display 的功能。

让我分析一下需要做什么：
1. 创建 ActivityFeed 类来显示实时活动流
2. 创建 ReasoningDisplay 类来显示思考过程
3. 在 run_agent.py 中集成这些功能
4. 更新配置文件支持新特性

首先，我需要检查现有的 display.py 文件结构。
然后添加新的类，确保与现有代码兼容。

接下来，我需要考虑如何将这些功能集成到 AIAgent 中。
应该在 run_conversation 方法中初始化这些显示组件。

对于 ActivityFeed，我需要在工具调用时记录开始和结束状态。
对于 ReasoningDisplay，我需要在收到模型响应时显示 reasoning 内容。

最后，我需要测试这些功能确保它们正常工作。
这是一个相当复杂的任务，需要仔细实现每个步骤。

让我开始编写代码吧！"""
    display.display(long_reasoning, "思考过程")
    
    print("\n✓ ReasoningDisplay test completed!\n")


def test_combined():
    """Test combined ActivityFeed and ReasoningDisplay."""
    print("\n" + "="*60)
    print("Testing Combined Display")
    print("="*60 + "\n")
    
    feed = ActivityFeed(prefix="┊")
    display = ReasoningDisplay()
    
    feed.start()
    
    # Simulate a complete workflow
    feed.add_activity("thinking", "Analyzing request", {"query": "test"})
    time.sleep(0.2)
    
    # Show reasoning
    reasoning = """用户想要测试组合显示功能。
我需要模拟一个完整的工作流程。
让我依次执行各个步骤。"""
    display.display(reasoning, "蕾姆的思考")
    
    feed.complete_activity(status="completed", result_preview="analysis done")
    
    feed.add_activity("search", "Searching for files", {"pattern": "*.py"})
    time.sleep(0.3)
    feed.complete_activity(status="completed", result_preview="found 42 files")
    
    feed.add_activity("read", "Reading file content", {"path": "test.py"})
    time.sleep(0.3)
    feed.complete_activity(status="completed", result_preview="read 100 lines")
    
    feed.stop()
    
    print("\n✓ Combined display test completed!\n")


if __name__ == "__main__":
    print("\n" + "╔" + "═"*58 + "╗")
    print("║" + " "*15 + "Hermes Activity Feed Tests" + " "*15 + "║")
    print("╚" + "═"*58 + "╝")
    
    try:
        test_activity_feed()
        test_reasoning_display()
        test_combined()
        
        print("\n" + "╔" + "═"*58 + "╗")
        print("║" + " "*20 + "All Tests Passed!" + " "*21 + "║")
        print("╚" + "═"*58 + "╝\n")
        
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
