# Sylphiette Assistant (sylph_ai)

Assistente virtual personalizavel. Inclui:

- IA com Gemini
- Voz com pyttsx3
- Integração com VTube Studio (Bulding)
- Interface terminal personalizada

## Instalação

```bash
pip install SylphietteIA

```

Uso


---


```python
from IA import base


personalidade = (
    "Coloque a personalidade da sua IA"
)
sylph = base.AI("Nome da sua Ia", personalidade, "GOOGLE API KEY")
sylph.run()

```

