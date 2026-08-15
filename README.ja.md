# SandBase Skills

[English](./README.md) | [中文](./README.zh-CN.md) | 日本語 | [한국어](./README.ko.md) | [Español](./README.es.md) | [Français](./README.fr.md) | [Deutsch](./README.de.md) | [Português](./README.pt-BR.md)

**88個のインストール可能なAgent Skill** — リサーチ、ソーシャルインテリジェンス、マーケティング、ビジネスワークフロー向け。1つのAPIキーで全データソースにアクセス。対応Agent（Claude Code、Codex、Cursor、Gemini CLI）にインストールしてすぐに使えます。

## クイックスタート

```bash
# 1. SandBase APIキーを設定
export SANDBASE_API_KEY='sk-...'

# 2. Skillをインストール
npx skills add sandbaseai/sandbase-skills --skill twitter-intelligence --agent codex

# 3. 使う
# 「今週[ブランド]についてTwitterで何が言われているか調べて」
```

## Skillカテゴリ (88個)

| カテゴリ | 数 | ユースケース |
|---------|-----|-------------|
| **ソーシャルインテリジェンス** | 14 | Twitter、YouTube、Instagram、TikTok、Weibo、Bilibili等 |
| **検索・リサーチ** | 17 | マルチソース検索、学術論文、トレンド発見 |
| **ビジネスインテリジェンス** | 20 | 企業調査、競合分析、セールスインテリジェンス |
| **マーケティング** | 15 | ブランドモニタリング、KOL発見、ソーシャルリスニング |
| **SEO** | 5 | キーワード戦略、被リンク分析、SERP分析 |
| **ツール** | 17 | メール検証、ドメイン分析、スクリーンショット、翻訳 |

全Skillリストは[英語README](./README.md#skill-catalog-88-skills)をご覧ください。

## 対応Agent

Claude Code、Codex、Cursor、Gemini CLI、OpenClaw、Hermes、Amp、Devin

## 仕組み

```
ユーザーの質問 → AgentがSKILL.mdを読む → SandBase APIを呼び出す → 結果を整理して回答
```

## 料金

Skill自体は無料・オープンソース (Apache-2.0)。SandBase API呼び出しは従量制 — 通常$0.001〜$0.01/回。

---

**[SandBase](https://sandbase.ai)** — 1つのAPIキー。全データソース。100+ Agent Skill。
