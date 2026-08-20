# SandBase Skills

[English](./README.md) | [中文](./README.zh-CN.md) | [日本語](./README.ja.md) | [한국어](./README.ko.md) | Español | [Français](./README.fr.md) | [Deutsch](./README.de.md) | [Português](./README.pt-BR.md)

**88 Skills de Agent instalables** — Para investigación, inteligencia social, marketing y flujos de trabajo empresariales. El Skill principal de investigación funciona con las herramientas de búsqueda del agente y no requiere una cuenta de SandBase; conecta SandBase solo cuando necesites fuentes especializadas.

Empieza con `multi-source-search`: usa las herramientas de búsqueda existentes del agente e incluye un ejemplo de registro de evidencias y un validador sin conexión. Si mejora un flujo de trabajo real, [dale una estrella al repositorio](https://github.com/sandbaseai/sandbase-skills) para que otros desarrolladores puedan descubrirlo.

![Flujo de búsqueda multifuente: capacidades de búsqueda, trazabilidad de fuentes, registro de evidencias y validación sin conexión](assets/multi-source-search-workflow.svg)

## Inicio Rápido

```bash
# Genera el prompt completo del Skill sin instalarlo
npx skills use sandbaseai/sandbase-skills@multi-source-search

# O instálalo en Codex
npx skills add sandbaseai/sandbase-skills --skill multi-source-search --agent codex

# Úsalo con las herramientas web y de lectura de páginas del agente
# "Verifica esta afirmación con fuentes independientes y valida el registro de evidencias"
```

### DeepSeek Harness

Desde la raíz de un proyecto de DeepSeek Harness:

```bash
npx --yes github:sandbaseai/sandbase-skills add multi-source-search
dsh web
```

El instalador copia el Skill completo en `.dsh/skills/multi-source-search`, el directorio de descubrimiento del proyecto. Se ejecuta directamente desde GitHub, sin publicación en npm ni cuenta de SandBase.

## Categorías (88 Skills)

| Categoría | Cantidad | Casos de uso |
|-----------|----------|--------------|
| **Inteligencia Social** | 14 | Twitter, YouTube, Instagram, TikTok, Reddit, Xiaohongshu, Weibo |
| **Búsqueda e Investigación** | 17 | Multi-fuente, académico, tendencias, noticias |
| **Inteligencia de Negocios** | 20 | Empresas, competencia, ventas, talento |
| **Marketing** | 15 | Marca, influencers, escucha social, crisis |
| **SEO** | 5 | Keywords, backlinks, SERP, auditoría |
| **Herramientas** | 17 | Email, dominios, screenshots, traducción |

Lista completa en el [README en inglés](./README.md#skill-catalog-88-skills).

## Agentes Soportados

Claude Code, Codex, Cursor, Gemini CLI, OpenClaw, Hermes, Amp, Devin

## Precios

Los Skills son gratuitos y open source (Apache-2.0). `multi-source-search` no requiere una cuenta ni costes de API de SandBase cuando utiliza las herramientas del agente; los Skills con fuentes especializadas pueden añadir SandBase según el uso.

---

**[SandBase Skills](https://github.com/sandbaseai/sandbase-skills)** — 88 Skills open source con fuentes especializadas opcionales.
