# Hermes Activity Feed & Reasoning Display 使用说明

## 🎉 新功能概述

本次更新为 Hermes Agent 添加了类似 Claude Code 的**实时活动流显示**和**思考过程面板**功能，让您可以清晰地看到 AI 的工作状态和思考过程。

---

## ✨ 功能特性

### 1. Activity Feed（活动流）

实时显示 AI 的所有操作，包括：
- 📖 文件读取
- ✍️ 文件写入
- 💻 终端命令执行
- 🔍 文件搜索
- 🌍 网络搜索
- 🧠 记忆操作
- 📚 技能加载

**显示效果：**
```
┊ ── Activity Feed ────────────────────────────
┊ 💭 Starting conversation [0ms]
┊ 🔍 Searching files → *.py [50ms]
┊   ✓ Searching files (120ms): found 42 files
┊ 📖 Reading file → run_agent.py [170ms]
┊   ✓ Reading file (80ms): 1234 lines
┊ 💻 Running command → pytest tests/ [250ms]
┊   ✓ Running command (2.5s): exit 0
┊ ── 5 activities, 5 completed (2.8s) ──────
```

### 2. Reasoning Display（思考显示）

以精美的折叠面板显示 AI 的思考过程：

**短思考（自动折叠）：**
```
💭 思考过程：First, I need to understand the user's request. Then I'll search for relevant files...
```

**长思考（展开面板）：**
```
╔══════════════════════════════════════════════════════════╗
║ 💭 思考过程                                                 ║
╠══════════════════════════════════════════════════════════╣
║ 首先，我需要理解用户的需求。                                         ║
║ 用户想要查看 Activity Feed 和 Reasoning Display 的功能。          ║
║                                                        ║
║ 让我分析一下需要做什么：                                           ║
║ 1. 创建 ActivityFeed 类来显示实时活动流                           ║
║ 2. 创建 ReasoningDisplay 类来显示思考过程                        ║
║                    ... (more lines)                    ║
╚══════════════════════════════════════════════════════════╝
```

---

## 🔧 启用方法

### 方法 1：配置文件（推荐）

在 `~/.hermes/config.yaml` 中添加：

```yaml
display:
  # 启用活动流显示
  activity_feed: true
  
  # 启用思考过程面板
  reasoning_display: true
  
  # 可选：同时启用现有功能
  show_reasoning: true
  tool_progress: "verbose"
```

### 方法 2：环境变量

在运行前设置环境变量：

```bash
export HERMES_ENABLE_ACTIVITY_FEED=true
export HERMES_ENABLE_REASONING_DISPLAY=true
python cli.py
```

### 方法 3：临时启用

单次运行时使用：

```bash
HERMES_ENABLE_ACTIVITY_FEED=true HERMES_ENABLE_REASONING_DISPLAY=true python cli.py
```

---

## 📋 配置选项详解

| 配置项 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `activity_feed` | boolean | `false` | 启用 Claude Code 风格的实时活动流 |
| `reasoning_display` | boolean | `false` | 启用可折叠的思考过程面板 |
| `show_reasoning` | boolean | `false` | 显示模型的 reasoning 内容（现有功能） |
| `tool_progress` | string | `"all"` | 工具进度显示级别：`off`/`new`/`all`/`verbose` |

---

## 🎨 自定义样式

### Activity Feed 图标

活动流使用彩色图标区分不同类型的操作：

| 图标 | 类别 | 颜色 |
|------|------|------|
| 💭 | thinking | 淡紫色 |
| 🔍 | search | 浅蓝色 |
| 📖 | read | 青色 |
| ✍️ | write | 橙色 |
| 💻 | terminal | 红色 |
| 🌐 | browser | 蓝色 |
| 🌍 | web | 天蓝色 |
| 📚 | skill | 薰衣草紫 |
| 🧠 | memory | 粉色 |
| ✅ | success | 绿色 |
| ❌ | error | 亮红色 |

### Reasoning Display 面板

- **短思考**（≤10 行）：自动折叠为单行显示
- **长思考**（>10 行）：展开为精美边框面板
- **最大显示**：30 行后显示 truncation 提示

---

## 🧪 测试

运行测试脚本验证功能：

```bash
cd /path/to/hermes-activity-feed
source ../hermes-agent/.venv/bin/activate
python test_activity_feed.py
```

**预期输出：**
```
╔══════════════════════════════════════════════════════════╗
║               Hermes Activity Feed Tests               ║
╚══════════════════════════════════════════════════════════╝

Testing ActivityFeed
...
✓ ActivityFeed test completed!

Testing ReasoningDisplay
...
✓ ReasoningDisplay test completed!

╔══════════════════════════════════════════════════════════╗
║                    All Tests Passed!                     ║
╚══════════════════════════════════════════════════════════╝
```

---

## 💡 使用技巧

### 1. 性能考虑

- Activity Feed 会增加少量输出开销，在长时间运行时建议关闭
- Reasoning Display 对短思考自动折叠，不会影响输出速度

### 2. 调试模式

结合 verbose 模式使用获得最详细的输出：

```yaml
display:
  activity_feed: true
  reasoning_display: true
  tool_progress: "verbose"
  
agent:
  verbose: true
```

### 3. 安静模式

在脚本或自动化任务中关闭所有显示：

```yaml
display:
  activity_feed: false
  reasoning_display: false
  compact: true
```

---

## 🔮 未来计划

- [ ] 支持活动流历史记录滚动
- [ ] 添加活动统计面板（成功/失败/平均耗时）
- [ ] 支持自定义图标和颜色主题
- [ ] 导出活动日志为 JSON/CSV
- [ ] 支持 Gateway/Messaging 平台

---

## 📝 技术实现

### 核心文件

| 文件 | 功能 |
|------|------|
| `agent/display.py` | ActivityFeed 和 ReasoningDisplay 类实现 |
| `run_agent.py` | 工具执行时集成活动流记录 |
| `cli.py` | 配置加载和环境变量设置 |
| `cli-config.yaml.example` | 配置选项示例 |

### 关键代码

**ActivityFeed 使用示例：**
```python
from agent.display import ActivityFeed

feed = ActivityFeed(prefix="┊")
feed.start()

# 记录活动开始
activity_id = feed.add_activity(
    category="terminal",
    description="Running tests",
    args={"command": "pytest"}
)

# 记录活动完成
feed.complete_activity(
    activity_id,
    status="completed",
    result_preview="exit 0"
)

feed.stop()
```

**ReasoningDisplay 使用示例：**
```python
from agent.display import ReasoningDisplay

display = ReasoningDisplay(max_lines=30)
display.display(reasoning_text, title="思考过程")
```

---

## 🙏 致谢

本功能灵感来源于 Claude Code 的优雅显示设计，旨在为 Hermes Agent 用户提供更直观、更透明的 AI 工作可视化体验。

(蕾姆精心制作 💙)
