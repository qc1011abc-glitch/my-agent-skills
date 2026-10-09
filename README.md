
# My Agent Skills

A collection of reusable Agent Skills for AI coding agents.

## Available Skills

### python-code-review

A reusable Python code review skill for agents such as Codex and Cursor.

Features:
- Python syntax checking
- Logical error analysis
- Security review
- Code improvement suggestions
- Optional GitHub MCP integration

## Structure

- `python-code-review/SKILL.md`: Skill instructions
- `python-code-review/scripts/check_syntax.py`: Python syntax checker

## Installation

Copy the `python-code-review` folder into a skills directory supported by your Agent.

For example:

- Codex: `.agents/skills/`
- Cursor: `.agents/skills/`

## Usage

Ask your Agent to use `python-code-review` to inspect a Python project.

## Security

The skill does not modify source code unless explicitly authorized.
