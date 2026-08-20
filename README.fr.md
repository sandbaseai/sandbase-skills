# SandBase Skills

[English](./README.md) | [中文](./README.zh-CN.md) | [日本語](./README.ja.md) | [한국어](./README.ko.md) | [Español](./README.es.md) | Français | [Deutsch](./README.de.md) | [Português](./README.pt-BR.md)

**88 Skills Agent installables** — Recherche, intelligence sociale, marketing et workflows métier. Le Skill de recherche principal fonctionne avec les outils de recherche de l'agent et ne nécessite pas de compte SandBase ; connectez SandBase uniquement pour ajouter des sources spécialisées.

Commencez avec `multi-source-search` : il utilise les outils de recherche existants de l'agent et inclut un exemple de registre de preuves ainsi qu'un validateur hors ligne. S'il améliore un workflow réel, [ajoutez une étoile au dépôt](https://github.com/sandbaseai/sandbase-skills) pour aider d'autres développeurs à le découvrir.

![Flux de recherche multisource : capacités de recherche, traçabilité des sources, registre de preuves et validation hors ligne](assets/multi-source-search-workflow.svg)

## Démarrage Rapide

```bash
# Générez le prompt complet du Skill sans l'installer
npx skills use sandbaseai/sandbase-skills@multi-source-search

# Ou installez-le dans Codex
npx skills add sandbaseai/sandbase-skills --skill multi-source-search --agent codex

# Utilisez-le avec les outils Web et de lecture de pages de l'agent
# "Vérifie cette affirmation avec des sources indépendantes et valide le registre de preuves"
```

### DeepSeek Harness

Depuis la racine d'un projet DeepSeek Harness :

```bash
npx --yes github:sandbaseai/sandbase-skills add multi-source-search
dsh web
```

L'installateur copie le Skill complet dans `.dsh/skills/multi-source-search`, le répertoire de découverte du projet. Il s'exécute directement depuis GitHub, sans publication npm ni compte SandBase.

## Catégories (88 Skills)

| Catégorie | Nombre | Cas d'usage |
|-----------|--------|-------------|
| **Intelligence Sociale** | 14 | Twitter, YouTube, Instagram, TikTok, Reddit, Xiaohongshu |
| **Recherche** | 17 | Multi-sources, académique, tendances, actualités |
| **Intelligence Business** | 20 | Entreprises, concurrence, ventes, talents |
| **Marketing** | 15 | Marque, influenceurs, écoute sociale, crise |
| **SEO** | 5 | Mots-clés, backlinks, SERP, audit |
| **Outils** | 17 | Email, domaines, captures d'écran, traduction |

Liste complète dans le [README anglais](./README.md#skill-catalog-88-skills).

## Agents Supportés

Claude Code, Codex, Cursor, Gemini CLI, OpenClaw, Hermes, Amp, Devin

## Tarification

Les Skills sont gratuits et open source (Apache-2.0). `multi-source-search` ne nécessite ni compte ni frais d'API SandBase lorsqu'il utilise les outils de l'agent ; les Skills spécialisés peuvent ajouter SandBase selon l'usage.

---

**[SandBase Skills](https://github.com/sandbaseai/sandbase-skills)** — 88 Skills open source avec des sources spécialisées facultatives.
