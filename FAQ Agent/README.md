## Internship FAQ Chatbot (Rasa)

This repository contains a minimal Rasa-based FAQ chatbot tailored for common internship questions (duration, stipend, requirements, deadlines, roles, remote work, etc.).

Quick start (Windows PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
rasa train
# In one terminal: start action server
rasa run actions
# In another terminal: start the assistant in shell
rasa shell
```

Files created:
- `config.yml` — model pipeline and policies
- `domain.yml` — intents, responses, actions
- `data/nlu.yml` — intent examples
- `data/rules.yml` — rule-to-response mappings
- `actions/actions.py` — example custom action
- `endpoints.yml` — actions server endpoint
- `requirements.txt` — Python deps

Next steps:
- Run training and test the assistant with `rasa shell`.
- Add/adjust NLU examples for your specific internship program.
- Optionally deploy via Docker, Rasa X, or migrate to Dialogflow (if you prefer a managed platform).

If you'd like, I can now run training here (if environment available) or guide you through running locally. Which do you prefer?
