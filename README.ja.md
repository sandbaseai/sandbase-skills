# SandBase Skills

[English](./README.md) | [中文](./README.zh-CN.md) | 日本語 | [한국어](./README.ko.md) | [Español](./README.es.md) | [Français](./README.fr.md) | [Deutsch](./README.de.md) | [Português](./README.pt-BR.md)

**88個のインストール可能なAgent Skill** — リサーチ、ソーシャルインテリジェンス、マーケティング、ビジネスワークフロー向け。主力のリサーチSkillはAgent標準の検索ツールで動作し、SandBaseアカウントは不要です。専門データソースが必要な場合のみSandBaseを追加できます。

## クイックスタート

```bash
# 1. アカウント不要のマルチソース調査Skillをインストール
npx skills add sandbaseai/sandbase-skills --skill multi-source-search --agent codex

# 2. Agent標準のWeb検索・ページ読み取りツールで使う
# 「複数の独立した情報源でこの主張を検証し、証拠台帳も検証して」
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
ユーザーの質問 → AgentがSKILL.mdを読む → 標準ツール（必要に応じてSandBase）を使う → 結果を整理して回答
```

## 料金

Skill自体は無料・オープンソース (Apache-2.0)。`multi-source-search`をAgent標準ツールで使う場合、SandBaseアカウントやSandBase API料金は不要です。専門データソースを使うSkillでは従量制のSandBaseを追加できます。

---

**[SandBase Skills](https://github.com/sandbaseai/sandbase-skills)** — 88個のオープンソースAgent Skill。必要に応じてデータソースを追加。
