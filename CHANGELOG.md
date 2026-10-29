# Changelog — ORÁCULO

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere a [Semantic Versioning](https://semver.org/lang/pt-BR/).

## [Unreleased]

### Adicionado
- Estrutura inicial do projeto
- Arquitetura modular: STT, LLM, TTS, Memória, Automação, Orquestrador
- Suporte a múltiplas engines:
  - STT: whisper.cpp, Vosk, termux-stt
  - LLM: llama.cpp (GGUF)
  - TTS: Piper, espeak-ng, Sherpa-ONNX
- Memória em arquivo Markdown + índice vetorial (sqlite-vec)
- Automação via ADB Wireless + Termux:API
- Fluxo WhatsApp com verificação visual obrigatória
- Scripts de instalação, download, backup, build APK
- Testes isolados por componente
- CI/CD com GitHub Actions
- Dockerfile para simulação Termux

### Corrigido
- N/A (versão inicial)

### Alterado
- N/A

### Removido
- N/A

---

## [1.0.0] - 2025-01-XX (Planejado)

### Adicionado
- Release inicial estável
- APK assinado para distribuição
- Documentação completa em português
- Exemplos de comandos de voz
- Guia de solução de problemas (15 erros comuns)

---

## Tipos de Mudança

- **Adicionado** para novas funcionalidades
- **Corrigido** para correções de bugs
- **Alterado** para mudanças em funcionalidades existentes
- **Removido** para funcionalidades removidas
- **Segurança** para correções de vulnerabilidades
- **Depreciado** para funcionalidades que serão removidas