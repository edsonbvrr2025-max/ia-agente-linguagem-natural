# Guia de Contribuição — ORÁCULO

Obrigado por contribuir! Este projeto visa criar um assistente de IA 100% offline para Android via Termux.

## 🎯 Princípios

1. **Offline-first**: Tudo deve funcionar sem internet após instalação
2. **Sem PC**: Instalação e uso 100% no celular
3. **Leigo-friendly**: Código claro, comentado, sem jargão desnecessário
4. **Estável > Elegante**: Soluções que funcionam sempre > soluções bonitas que quebram

## 🛠️ Setup de Desenvolvimento

### No PC (para desenvolvimento)
```bash
git clone https://github.com/SEU_USUARIO/oraculo-termux.git
cd oraculo-termux
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .  # Instala em modo desenvolvimento
```

### No Android (Termux) — para testar
```bash
pkg install git python termux-api
git clone https://github.com/SEU_USUARIO/oraculo-termux.git
cd oraculo-termux
bash scripts/install_termux.sh
bash scripts/download_models.sh --all
bash scripts/setup_adb_wireless.sh
python -m tests.test_stt  # testa cada componente
python -m oraculo         # roda o agente
```

## 📝 Padrões de Código

### Python
- **Type hints** obrigatórios em funções públicas
- **Docstrings** no formato Google/NumPy
- **Logs** via `oraculo.utils.logger.get_logger(__name__)`
- **Config** via `oraculo.config.get_config()`
- **Erro handling**: Try/except com log, nunca `pass` silencioso

### Commits
```
feat: nova funcionalidade
fix: correção de bug
docs: documentação
refactor: refatoração sem mudança de comportamento
test: testes
chore: manutenção (scripts, deps, etc.)
```

Exemplo: `feat(automation): adiciona verificação visual no envio WhatsApp`

### Branches
- `main`: estável, pronto para release
- `develop`: integração contínua
- `feature/*`: novas features
- `fix/*`: correções
- `release/*`: preparação de release

## 🧪 Testes

### Testes isolados (obrigatórios antes de PR)
```bash
python -m tests.test_stt      # STT
python -m tests.test_llm      # LLM
python -m tests.test_tts      # TTS
python -m tests.test_automation  # Automação
python -m tests.test_memory   # Memória
```

### Cobertura
```bash
pytest tests/ --cov=oraculo --cov-report=html
```

## 🔧 Adicionando Nova Funcionalidade

### 1. Nova Engine STT/TTS/LLM
1. Crie classe em `oraculo/stt/`, `oraculo/tts/` ou `oraculo/llm/`
2. Herde da base (`STTEngine`, `TTSEngine`, `LLMEngine`)
3. Implemente `load()`, `transcribe()`/`synthesize()`/`generate()`, `unload()`
4. Registre com `register_engine("nome", Classe)`
5. Adicione em `config.yaml` exemplo
6. Crie teste em `tests/test_*.py`

### 2. Nova Ferramenta (Function Calling)
1. Adicione definição em `oraculo/llm/tools.py`
2. Implemente executor em `oraculo/memory/tools.py` ou `oraculo/automation/`
3. Registre em `ALL_TOOLS` e categoria apropriada
4. Teste via `python -m oraculo.llm.tools` (função `execute_memory_tool`)

### 3. Nova Ação de Automação
1. Adicione método no backend apropriado (`ADBAutomation`, `TermuxAPIAutomation`)
2. Registre no `execute_action` dispatch
3. Adicione tool definition em `oraculo/llm/tools.py`
4. Teste isolado

## 🐛 Reportando Bugs

Use o template de Issue no GitHub com:
1. **Ambiente**: Android version, modelo, RAM, Termux version
2. **Passos para reproduzir**
3. **Comportamento esperado vs real**
4. **Logs relevantes** (`oraculo.log`)
5. **Screenshots** se aplicável

## 📦 Release Process

1. Atualiza `oraculo/__init__.py` version
2. Atualiza `CHANGELOG.md`
3. Cria tag: `git tag v1.0.0`
4. Push tag: `git push origin v1.0.0`
5. GitHub Actions builda APK e anexa ao release

## 🤝 Código de Conduta

- Seja respeitoso e inclusivo
- Foque no problema, não na pessoa
- Aceite feedback construtivo
- Ajude iniciantes (o projeto é para leigos!)

## 📄 Licença

MIT — veja [LICENSE](LICENSE)

---

**Dúvidas?** Abra uma Discussion no GitHub ou comente na Issue.