# SandBase Skills

[English](./README.md) | [中文](./README.zh-CN.md) | [日本語](./README.ja.md) | 한국어 | [Español](./README.es.md) | [Français](./README.fr.md) | [Deutsch](./README.de.md) | [Português](./README.pt-BR.md)

**설치 가능한 Agent Skill 88개** — 리서치, 소셜 인텔리전스, 마케팅, 비즈니스 워크플로우용. 하나의 API 키로 모든 데이터 소스에 접근. 호환 Agent(Claude Code, Codex, Cursor, Gemini CLI)에 설치하면 바로 사용 가능합니다.

## 빠른 시작

```bash
# 1. SandBase API 키 설정
export SANDBASE_API_KEY='sk-...'

# 2. Skill 설치
npx skills add sandbaseai/sandbase-skills --skill twitter-intelligence --agent codex

# 3. 사용하기
# "이번 주 [브랜드]에 대한 Twitter 대화를 분석해줘"
```

## Skill 카테고리 (88개)

| 카테고리 | 수 | 용도 |
|---------|-----|------|
| **소셜 인텔리전스** | 14 | Twitter, YouTube, Instagram, TikTok, Weibo, Bilibili 등 |
| **검색 & 리서치** | 17 | 멀티소스 검색, 학술 논문, 트렌드 발견 |
| **비즈니스 인텔리전스** | 20 | 기업 조사, 경쟁 분석, 영업 인텔리전스 |
| **마케팅** | 15 | 브랜드 모니터링, KOL 발굴, 소셜 리스닝 |
| **SEO** | 5 | 키워드 전략, 백링크 분석, SERP 분석 |
| **도구** | 17 | 이메일 검증, 도메인 분석, 스크린샷, 번역 |

전체 Skill 목록은 [영어 README](./README.md#skill-catalog-88-skills)를 참조하세요.

## 지원 Agent

Claude Code, Codex, Cursor, Gemini CLI, OpenClaw, Hermes, Amp, Devin

## 작동 방식

```
사용자 질문 → Agent가 SKILL.md 읽기 → SandBase API 호출 → 결과 종합 및 응답
```

## 가격

Skill 자체는 무료 오픈소스 (Apache-2.0). SandBase API 호출은 사용량 기반 — 일반적으로 $0.001~$0.01/회.

---

**[SandBase](https://sandbase.ai)** — 하나의 API 키. 모든 데이터 소스. 100+ Agent Skill.
