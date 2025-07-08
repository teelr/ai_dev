# 🎯 Visual Workflow Guide

## 🖼️ System Architecture
```
┌─────────────────────────────────────────────────────────┐
│                     magoo (Workstation)                  │
│  ┌─────────────────────────────────────────────────┐   │
│  │                  Cursor AI IDE                   │   │
│  │  ┌───────────┐ ┌─────────────┐ ┌─────────────┐ │   │
│  │  │   File    │ │    Code     │ │  Terminal   │ │   │
│  │  │ Explorer  │ │   Editor    │ │   (SSH)     │ │   │
│  │  └───────────┘ └─────────────┘ └──────┬──────┘ │   │
│  └────────────────────────────────────────┼────────┘   │
└───────────────────────────────────────────┼────────────┘
                                            │ SSH
                                            ▼
┌─────────────────────────────────────────────────────────┐
│                    neurX (AI Server)                     │
│  ┌─────────────────┐      ┌─────────────────────────┐  │
│  │  Claude Code    │      │      Gemini CLI         │  │
│  │      CLI        │      │   (Agentic + Tools)     │  │
│  └─────────────────┘      └─────────────────────────┘  │
│  ┌─────────────────────────────────────────────────┐   │
│  │           Python/Conda Environment               │   │
│  │              ~/dev/ai_dev                        │   │
│  └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

## 🔄 Workflow Patterns

### Pattern 1: Research → Implement → Refine
```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   Research   │ ──► │  Implement   │ ──► │   Refine     │
│   (Gemini)   │     │   (Claude)   │     │   (Claude)   │
└──────────────┘     └──────────────┘     └──────────────┘
       ▼                     ▼                     ▼
  gy "How to..."      ccedit file.py        ccfix file.py
```

### Pattern 2: Dual AI Collaboration
```
Terminal Split View (tmux)
┌─────────────────────┬─────────────────────┐
│   Claude REPL       │    Gemini REPL      │
│                     │                     │
│  > analyze error    │  > find solutions   │
│  > suggest fix      │  > research docs    │
│  > implement        │  > test approach    │
└─────────────────────┴─────────────────────┘
         ▼                       ▼
   Precise edits          Exploration
```

### Pattern 3: Iterative Development
```
    ┌─────────────┐
    │    Start    │
    └──────┬──────┘
           ▼
    ┌─────────────┐     Cursor AI
    │ Code in IDE │ ◄──────┐
    └──────┬──────┘        │
           ▼               │
    ┌─────────────┐        │
    │ Need Help?  │────No──┘
    └──────┬──────┘
          Yes
           ▼
    ┌─────────────┐
    │ Simple Edit?│
    └─┬─────────┬─┘
     Yes        No
      ▼          ▼
 ┌────────┐  ┌────────┐
 │ Claude │  │ Gemini │
 │  Edit  │  │Research│
 └────────┘  └────────┘
```

## 🎮 Command Flow

### Quick Reference Card
```
┌─────────────────────────────────────────────┐
│              QUICK COMMANDS                  │
├─────────────────────────────────────────────┤
│ Start Work:                                 │
│   cd ~/dev/ai_dev                          │
│   ./dev-launch.sh    OR    dualrepl       │
├─────────────────────────────────────────────┤
│ Claude (Precision):                         │
│   cc         → launch claude               │
│   ccedit     → edit with AI               │
│   ccsum      → summarize code              │
│   ccfix      → fix issues                  │
├─────────────────────────────────────────────┤
│ Gemini (Exploration):                       │
│   gc         → chat mode                   │
│   gy         → yolo mode                   │
│   gf         → fetch web                   │
│   gm         → MCP agentic                 │
└─────────────────────────────────────────────┘
```

## 🎯 Decision Tree

```
What do you need to do?
         │
         ├─── Write/Edit Code ──────► Use Claude (ccedit)
         │
         ├─── Fix Errors ──────────► Use Claude (ccfix)
         │
         ├─── Understand Code ─────► Use Claude (ccsum)
         │
         ├─── Research Approach ───► Use Gemini (gy/gc)
         │
         ├─── Fetch Documentation ─► Use Gemini (gf)
         │
         ├─── Complex Problem ─────► Use Both (dualrepl)
         │
         └─── Autonomous Coding ───► Use Gemini MCP (gm)
```

## 📊 Tool Selection Matrix

| Task Type | Best Tool | Command | Why? |
|-----------|-----------|---------|------|
| Code Generation | Claude | `ccedit` | Precise, follows patterns |
| Bug Fixing | Claude | `ccfix` | Understands context deeply |
| Code Review | Claude | `ccsum` | Analyzes structure well |
| Learning/Research | Gemini | `gy/gc` | Explores broadly |
| Web Lookups | Gemini | `gf` | Has web access |
| Architecture Design | Both | `dualrepl` | Research + implement |
| Refactoring | Claude | `ccedit` | Maintains consistency |
| API Integration | Gemini → Claude | `gy` → `ccedit` | Research → implement |

## 🔥 Power User Workflows

### Workflow 1: Full Stack Feature
```bash
# 1. Research best practices
gy "FastAPI + React authentication flow"

# 2. Create backend
ccedit backend/auth.py

# 3. Create frontend  
ccedit frontend/Login.tsx

# 4. Test and refine
ccfix .
npm test && pytest
```

### Workflow 2: Debug Production Issue
```bash
# 1. Dual mode for investigation
dualrepl

# Claude pane:
> show me the error in logs/app.log
> analyze the stack trace

# Gemini pane:
> search for "ConnectionResetError in asyncio"
> what causes this error in production?

# 2. Apply fix
ccedit src/connection_handler.py
```

### Workflow 3: Learn New Framework
```bash
# 1. Get overview
gc
> explain Langchain's agent framework

# 2. See examples
gf "https://python.langchain.com/docs/modules/agents"

# 3. Implement
ccedit my_agent.py

# 4. Iterate
ccfix my_agent.py
```

---

*This visual guide helps you quickly decide which tool to use and how to combine them effectively!*