# SandBase Skills

[English](./README.md) | 中文 | [日本語](./README.ja.md) | [한국어](./README.ko.md) | [Español](./README.es.md) | [Français](./README.fr.md) | [Deutsch](./README.de.md) | [Português](./README.pt-BR.md)

**100 个生产级 Agent Skill** — 覆盖调研、社交媒体情报、营销和商业工作流。一个 API Key，所有数据源。安装到任何兼容 Agent（Claude Code、Codex、Cursor、Gemini CLI）即可使用。

## 什么是 Skill？

Skill 是一个指令文件，教会 AI Agent 如何完成特定工作。每个 Skill 定义了调用哪些 SandBase API、按什么顺序、如何解读结果、如何格式化输出。你的 Agent 已经知道怎么工作 — Skill 给它领域专业知识。

## 快速开始

```bash
# 1. 设置 SandBase API Key
export SANDBASE_API_KEY='sk-...'

# 2. 安装一个 Skill
npx skills add sandbaseai/sandbase-skills --skill twitter-intelligence --agent codex

# 3. 开始使用
# "调研一下人们本周在 Twitter 上对 [品牌] 的讨论"
```

## Skill 分类 (100 个)

| 分类 | 数量 | 场景 |
|------|------|------|
| **社交媒体情报** | 23 | Twitter、YouTube、Instagram、TikTok、小红书、微博、B站、抖音等 |
| **搜索与调研** | 17 | 多源搜索、学术论文、趋势发现、新闻聚合 |
| **商业情报** | 22 | 公司调研、竞品分析、人才情报、销售线索 |
| **营销与内容** | 14 | 品牌监控、KOL 发现、社交聆听、危机监控 |
| **SEO** | 5 | 关键词策略、反链分析、SERP 分析、站点审计 |
| **工具** | 17 | 邮箱验证、域名分析、截图、YouTube 转写、天气 |

完整 Skill 列表请查看 [英文 README](./README.md#skill-catalog-100-skills)。

## 支持的 Agent

- **Claude Code** — `~/.claude/skills/`
- **OpenAI Codex** — `~/.codex/skills/`
- **Cursor** — `~/.cursor/skills/`
- **Gemini CLI** — `~/.gemini/skills/`
- **OpenClaw, Hermes, Amp, Devin** — 通过 `npx skills add`

## 工作原理

```
用户提问 → Agent 读取 SKILL.md → 调用 SandBase API → 综合分析并输出结果
```

## 定价

Skill 本身免费开源 (Apache-2.0)。底层 SandBase API 按用量计费 — 通常 $0.001–$0.01/次。一次典型的调研任务花费 $0.05–$0.20。

---

**[SandBase](https://sandbase.ai)** — 一个 API Key，所有数据源，100+ Agent Skill。
