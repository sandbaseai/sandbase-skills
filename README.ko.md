# SandBase Skills

[English](./README.md) | [中文](./README.zh-CN.md) | [日本語](./README.ja.md) | 한국어 | [Español](./README.es.md) | [Français](./README.fr.md) | [Deutsch](./README.de.md) | [Português](./README.pt-BR.md)

**설치 가능한 Agent Skill 88개** — 리서치, 소셜 인텔리전스, 마케팅, 비즈니스 워크플로우용. 대표 리서치 Skill은 Agent가 제공하는 검색 도구로 바로 실행되며 SandBase 계정이 필요하지 않습니다. 전문 데이터 소스가 필요할 때만 SandBase를 추가할 수 있습니다.

## 빠른 시작

```bash
# 설치 없이 전체 Skill 프롬프트 생성
npx skills use sandbaseai/sandbase-skills@multi-source-search

# 또는 Codex에 설치
npx skills add sandbaseai/sandbase-skills --skill multi-source-search --agent codex

# Agent의 기존 웹 검색 및 페이지 읽기 도구로 사용
# "여러 독립 출처로 이 주장을 검증하고 증거 원장도 확인해줘"
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
사용자 질문 → Agent가 SKILL.md 읽기 → 기존 도구(선택적으로 SandBase) 사용 → 결과 종합 및 응답
```

## 가격

Skill 자체는 무료 오픈소스 (Apache-2.0)입니다. Agent의 기존 도구로 `multi-source-search`를 사용할 때는 SandBase 계정이나 SandBase API 비용이 필요하지 않습니다. 전문 데이터 소스용 Skill에는 사용량 기반 SandBase를 선택적으로 연결할 수 있습니다.

---

**[SandBase Skills](https://github.com/sandbaseai/sandbase-skills)** — 88개의 오픈소스 Agent Skill과 선택형 데이터 소스 확장.
