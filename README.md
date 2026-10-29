# ORÁCULO — Agente de IA 100% Offline para Android (Termux)

> **Assistente de voz que ouve, entende, executa e responde — tudo no seu bolso, sem nuvem, sem internet, sem PC.**

## 🎯 Visão Geral

Este projeto implementa um agente de IA completo que roda **inteiramente no seu Android** via Termux:

| Camada | Tecnologia | Função |
|--------|------------|--------|
| 🎤 **Ouvido** | `whisper.cpp` / `termux-stt` / Vosk | STT offline pt-BR |
| 🧠 **Cérebro** | `llama.cpp` + GGUF (Qwen2.5-3B / Llama-3.2-3B / Gemma-3-4B) | LLM local com function calling |
| 💾 **Memória** | `memoria.md` + `sqlite-vec` | Fatos editáveis em linguagem natural + RAG local |
| 🤖 **Mãos** | ADB wireless + Termux:API + AccessibilityService | Automação real: WhatsApp, apps, sistema |
| 🔊 **Boca** | Piper TTS / `espeak-ng` / Sherpa-ONNX | TTS offline pt-BR natural |
| ⚙️ **Orquestrador** | Python 3.11+ no Termux | Loop: ouvir → pensar → agir → falar |

## ✨ Capacidades

- **Comando de voz natural**: *"manda um zap pra minha mãe falando que tô chegando"*
- **Executa ações reais**: abre apps, navega, digita, toca botões, envia WhatsApp, cria alarmes, lê notificações
- **Resposta falada** em português brasileiro
- **Memória editável por voz**: *"aprende que minha mãe é a Maria, contato +55 11 99999-9999"* / *"esquece o que falei sobre o João"*
- **100% offline** após instalação inicial
- **Zero dependência de PC** — tudo instala e roda no Termux do próprio celular

## 📱 Requisitos Mínimos

| Componente | Mínimo | Recomendado |
|------------|--------|-------------|
| Android | 11 (API 30) | 13+ (API 33+) |
| RAM | 4 GB | 6-8 GB |
| Armazenamento livre | 8 GB | 16 GB |
| Arquitetura | arm64-v8a | arm64-v8a |
| Root | ❌ Não necessário | ❌ Não necessário |

> **Importante**: Android 12+ tem *phantom process killer* que mata processos em background. O projeto inclui blindagem (wakelock, serviço foreground, Termux:Boot).

## 🚀 Instalação Rápida (no Termux do celular)

```bash
# 1. Instale Termux (F-Droid/GitHub) + Termux:API (F-Droid)
# 2. No Termux, rode:
pkg update && pkg upgrade -y
pkg install -y git python ffmpeg sox termux-api

# 3. Clone este repositório
git clone https://github.com/SEU_USUARIO/oraculo-termux.git
cd oraculo-termux

# 4. Execute o instalador automático
bash scripts/install_termux.sh

# 5. Baixe modelos (escolha um LLM)
bash scripts/download_models.sh --llm qwen2.5-3b-q4

# 6. Configure ADB wireless (para automação WhatsApp)
bash scripts/setup_adb_wireless.sh

# 7. Inicie o agente
python -m oraculo.main
```

## 📂 Estrutura do Projeto

```
oraculo-termux/
├── README.md                 # Este arquivo
├── LICENSE                   # MIT License
├── .gitignore
├── config.yaml               # Configuração central (editável pelo usuário)
├── memoria.md                # Memória de fatos (editável por voz)
├── perfil.md                 # Perfil do usuário
├── requirements.txt          # Dependências Python
├── buildozer.spec            # Build do APK (Kivy/Buildozer)
├── scripts/
│   ├── install_termux.sh     # Instalação completa no Termux
│   ├── download_models.sh    # Baixa modelos GGUF, STT, TTS
│   ├── setup_adb_wireless.sh # Configura ADB sem fio no próprio celular
│   ├── build_apk.sh          # Compila APK via Buildozer no Termux
│   ├── backup.sh             # Backup de memória + modelos
│   └── restore.sh            # Restaura backup
├── oraculo/
│   ├── __init__.py
│   ├── main.py               # Entry point
│   ├── config.py             # Carrega config.yaml
│   ├── stt/
│   │   ├── __init__.py
│   │   ├── whisper_cpp.py    # whisper.cpp wrapper
│   │   ├── vosk_stt.py       # Vosk wrapper
│   │   └── termux_stt.py     # termux-stt wrapper
│   ├── llm/
│   │   ├── __init__.py
│   │   ├── llama_cpp.py      # llama.cpp Python bindings
│   │   ├── tools.py          # Definição de ferramentas (function calling)
│   │   └── prompts.py        # System prompt + templates
│   ├── tts/
│   │   ├── __init__.py
│   │   ├── piper_tts.py      # Piper TTS wrapper
│   │   ├── espeak_ng.py      # espeak-ng wrapper
│   │   └── sherpa_onnx.py    # Sherpa-ONNX TTS wrapper
│   ├── memory/
│   │   ├── __init__.py
│   │   ├── file_memory.py    # memoria.md / perfil.md
│   │   ├── vector_memory.py  # sqlite-vec embeddings
│   │   └── tools.py          # memoria_adicionar, remover, buscar, listar
│   ├── automation/
│   │   ├── __init__.py
│   │   ├── adb.py            # ADB wireless wrapper
│   │   ├── termux_api.py     # Termux:API wrapper
│   │   ├── accessibility.py  # AccessibilityService helper
│   │   └── whatsapp.py       # Fluxo WhatsApp completo + verificação
│   ├── orchestrator/
│   │   ├── __init__.py
│   │   ├── loop.py           # Loop principal: ouvir → pensar → agir → falar
│   │   ├── wakelock.py       # termux-wake-lock management
│   │   └── state.py          # Estado da conversa
│   └── utils/
│       ├── __init__.py
│       ├── logger.py         # Logging colorido
│       ├── audio.py          # Gravação/playback via termux-microphone-record
│       └── helpers.py        # Utilidades diversas
├── models/                   # Modelos baixados (gitignored)
│   ├── llm/
│   ├── stt/
│   └── tts/
└── tests/
    ├── test_stt.py
    ├── test_llm.py
    ├── test_tts.py
    ├── test_automation.py
    └── test_memory.py
```

## ⚙️ Configuração (`config.yaml`)

```yaml
# Edite este arquivo ou use comandos de voz: "a partir de agora responda mais curto"
stt:
  engine: "whisper_cpp"        # whisper_cpp | vosk | termux_stt
  model: "models/stt/ggml-base-pt-br.bin"
  language: "pt"
  silence_threshold: 0.02
  silence_duration: 1.5

llm:
  engine: "llama_cpp"
  model: "models/llm/qwen2.5-3b-instruct-q4_k_m.gguf"
  n_ctx: 4096
  n_gpu_layers: -1             # -1 = offload máximo (Vulkan)
  threads: 4
  temperature: 0.3
  top_p: 0.9

tts:
  engine: "piper"              # piper | espeak_ng | sherpa_onnx
  model: "models/tts/pt_BR-faber-medium.onnx"
  speaker: 0
  speed: 1.0

automation:
  method: "adb"                # adb | termux_api | accessibility
  adb_host: "127.0.0.1"
  adb_port: 5555
  verify_actions: true         # Verifica se ação funcionou antes de confirmar

memory:
  file_path: "memoria.md"
  profile_path: "perfil.md"
  use_vector: true
  vector_db: "memory/vectors.db"
  embedding_model: "models/embeddings/all-MiniLM-L6-v2.onnx"

orchestrator:
  wake_word: "oraculo"         # Palavra de ativação (opcional)
  continuous: false            # true = conversa contínua
  interruptible: true          # Permite interromper resposta
  max_history: 6               # Pares user/assistant no contexto
```

## 🧠 Memória — Formato dos Arquivos

### `memoria.md` — Fatos Aprendidos
```markdown
# Memória do ORÁCULO

## Contatos
- **mãe**: Maria Silva, +55 11 99999-9999, WhatsApp
- **pai**: José Silva, +55 11 88888-8888, WhatsApp
- **trabalho**: Grupo "Equipe Projeto", WhatsApp

## Preferências
- Respostas: curtas e diretas
- Unidade de temperatura: Celsius
- Transporte padrão: Uber

## Rotinas
- Alarme 6:30 dias úteis
- Academia 19:00 seg/qua/sex

## Fatos Diversos
- Alergia: camarão
- Remédio: losartana 50mg manhã
```

### `perfil.md` — Perfil do Usuário
```markdown
# Perfil do Usuário

**Nome**: Nando
**Cidade**: São Paulo, SP
**Fuso**: America/Sao_Paulo
**Idioma**: pt-BR
**Estilo de comunicação**: informal, direto, coloquial
```

> **Edição por voz**: Diga *"aprende que meu irmão é o Carlos, +55 11 77777-7777"* → o agente adiciona em `memoria.md` na seção Contatos. Diga *"esquece o alarme de 6:30"* → remove da seção Rotinas.

## 🤖 Automação WhatsApp — Fluxo Garantido

O agente **nunca diz "enviou" sem verificar**:

1. `am start` abre WhatsApp na conversa do contato
2. `uiautomator dump` + parse XML → localiza campo de texto
3. `input text` digita a mensagem
4. `input tap` no botão enviar
5. `uiautomator dump` → **confirma que a mensagem aparece na tela**
6. Só então fala: *"Mensagem enviada para sua mãe"*

## 🔨 Compilar APK no Próprio Celular (Termux)

```bash
# No Termux, dentro do repo:
bash scripts/build_apk.sh

# O script:
# 1. Instala buildozer + dependências (openjdk-17, android-sdk, ndk)
# 2. Configura buildozer.spec para seu projeto
# 3. Roda: buildozer -v android debug
# 4. Gera: bin/oraculo-1.0.0-arm64-v8a-debug.apk
# 5. Instala: termux-open bin/oraculo-*.apk
```

> **Nota**: Compilar no celular leva 20-60 min dependendo do aparelho. Use carregador.

## 🛡️ Blindagem contra Morte do Processo (Android 12+)

| Técnica | Comando/Config |
|---------|----------------|
| Wakelock ativo | `termux-wake-lock` no loop principal |
| Serviço foreground | Termux:API `termux-notification` com `ongoing=true` |
| Inicialização automática | Termux:Boot + script em `~/.termux/boot/` |
| Desativar otimização bateria | Configurar manualmente: Config → Apps → Termux → Bateria → Sem restrições |
| Exclusão Doze | `cmd deviceidle whitelist +com.termux` (via ADB) |

## 📦 Modelos Suportados (Download Automático)

### LLM (GGUF, quantizados)
| Modelo | Tamanho | RAM Mín | Qualidade | Velocidade |
|--------|---------|---------|-----------|------------|
| Qwen2.5-3B-Instruct-Q4_K_M | 2.1 GB | 3 GB | ⭐⭐⭐⭐⭐ | Rápido |
| Llama-3.2-3B-Instruct-Q4_K_M | 2.0 GB | 3 GB | ⭐⭐⭐⭐ | Rápido |
| Gemma-3-4B-IT-Q4_K_M | 2.5 GB | 4 GB | ⭐⭐⭐⭐⭐ | Médio |
| Phi-4-mini-Instruct-Q4_K_M | 1.8 GB | 2.5 GB | ⭐⭐⭐ | Muito Rápido |

### STT
| Modelo | Tamanho | Idioma | Precisão pt-BR |
|--------|---------|--------|----------------|
| whisper.cpp base-pt-br | 142 MB | pt-BR | ⭐⭐⭐⭐ |
| Vosk pt-br | 1.2 GB | pt-BR | ⭐⭐⭐ |
| termux-stt (sistema) | 0 MB | pt-BR | ⭐⭐ |

### TTS
| Modelo | Tamanho | Qualidade | Velocidade |
|--------|---------|-----------|------------|
| Piper pt_BR-faber-medium | 50 MB | ⭐⭐⭐⭐⭐ | Rápido |
| espeak-ng pt-BR | 5 MB | ⭐⭐ | Instantâneo |
| Sherpa-ONNX VITS pt-BR | 80 MB | ⭐⭐⭐⭐ | Médio |

## 🧪 Testes Isolados (Execute Antes de Integrar)

```bash
# Teste STT
python -m tests.test_stt

# Teste LLM
python -m tests.test_llm

# Teste TTS
python -m tests.test_tts

# Teste Automação (WhatsApp)
python -m tests.test_automation

# Teste Memória
python -m tests.test_memory
```

## 📋 Fases do Projeto (Conforme Especificação)

- [x] **FASE 0** — Diagnóstico do aparelho
- [ ] **FASE 1** — Dossiê de pesquisa comparativa
- [ ] **FASE 2** — Plano em etapas aprovado
- [ ] **FASE 3** — Instalação guiada (scripts prontos)
- [ ] **FASE 4** — Cérebro (prompts, tools, exemplos)
- [ ] **FASE 5** — Ensinar sem código (tutorial voz)
- [ ] **FASE 6** — Blindagem (wakelock, boot, bateria)
- [ ] **FASE 7** — Solução de problemas (15 erros + reset)
- [ ] **BÔNUS** — Voz natural (wake word, interrupção, disambiguação)

## 🤝 Contribuindo

1. Fork o projeto
2. Crie branch: `git checkout -b feature/nova-funcionalidade`
3. Commit: `git commit -m 'feat: adiciona X'`
4. Push: `git push origin feature/nova-funcionalidade`
5. Abra Pull Request

## 📄 Licença

MIT License — veja [LICENSE](LICENSE)

## ⚠️ Aviso Legal

Este projeto automatiza interações com apps de terceiros (WhatsApp, etc.). Use por sua conta e risco. Respeite os Termos de Serviço de cada aplicativo. O projeto não armazena nem transmite dados para servidores externos.

---

**Feito para rodar no seu bolso. 🤖📱**

*Dúvidas? Abra uma Issue no GitHub.*