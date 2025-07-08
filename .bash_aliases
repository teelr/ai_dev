# Claude Code CLI
alias cc="claude"
alias ccedit="claude edit"
alias ccsum="claude summarize"
alias ccfix="claude fix"

# Gemini CLI
alias gc="gemini chat"
alias gy="gemini yolo"
alias gm="gemini mcp start"
alias gf="gemini fetch"

# Dual REPL using tmux
alias dualrepl="tmux new-session -d -s dual 'claude repl' \; split-window -h 'gemini repl' \; attach"