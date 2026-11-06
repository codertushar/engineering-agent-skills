# Engineering Agent Skills

Opinionated, production-minded skills that make AI coding agents follow real engineering workflows instead of guessing.

They use the open [Agent Skills](https://agentskills.io) `SKILL.md` format, so they work in Claude Code, Codex, Cursor, GitHub Copilot, Gemini CLI and other tools that support the standard.

## Skills

| Skill | What it does | Use it when |
|---|---|---|
| [`bugfix-test-first`](skills/bugfix-test-first/SKILL.md) | Reproduces the bug in a failing test, proves it fails, then makes the smallest fix. Never weakens an existing test. | You report a bug, paste a stack trace, or say "fix this" |

See [`examples/split-bill`](examples/split-bill) for a real run of `bugfix-test-first` on a small project.

Every skill here is used on real work before it is published. More coming. Follow the repo to get notified.

## Install

### Any supported tool (recommended)

Uses the open-source [`skills`](https://github.com/vercel-labs/skills) installer, which puts files in the right folder for your tool:

```bash
npx skills add codertushar/engineering-agent-skills
```

Just one skill, for one tool:

```bash
npx skills add codertushar/engineering-agent-skills --skill bugfix-test-first -a claude-code
```

Add `-g` to install for all your projects instead of only the current one.

### Manual

Copy a folder from `skills/` into your tool's skills directory:

| Tool | Project folder | Global folder |
|---|---|---|
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |
| Codex | `.agents/skills/` | `~/.agents/skills/` |
| Cursor | `.agents/skills/` | `~/.cursor/skills/` |
| GitHub Copilot | `.agents/skills/` | `~/.copilot/skills/` |
| Gemini CLI | `.agents/skills/` | `~/.gemini/skills/` |

Paths taken from the `skills` installer's [supported agents list](https://github.com/vercel-labs/skills/blob/main/docs/agents.md). If your tool's own docs say otherwise, trust those.

## Design principles

1. **Say when NOT to use the skill.** Most misfires come from an agent picking the wrong skill.
2. **Verify, don't trust.** Every skill ends with a check the agent must show you (failing test output, raw activity used).
3. **Small diffs.** Skills stop and ask before large or risky changes.
4. **No invented facts.** If the data isn't there, the agent says so.

## Contributing

Issues and PRs welcome, especially reports of a skill misfiring in a specific tool.

## License

[MIT](LICENSE). Not affiliated with Anthropic, OpenAI, Cursor, GitHub or Google.
