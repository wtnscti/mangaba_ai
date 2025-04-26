<img src="https://github.com/dheiver2/mangaba_ai/blob/main/img2.png" width="400" alt="Mangaba.AI logo">
**Mangaba.AI** é um framework avançado em Python para orquestrar equipes de agentes de IA autônomos que colaboram para resolver tarefas complexas de forma eficiente.

---

## ✨ Recursos Principais
- 🔹 **Arquitetura Multi-Agente** — Especialização e colaboração entre agentes
- 🧠 **Memória Contextual** — Histórico individual e compartilhado
- 🧬 **Integração Gemini** — Modelos de ponta da Google
- 🔍 **Ferramentas Externas** — Busca no Google e mais
- ✅ **Gerenciamento de Tarefas** — Com dependências e priorização
- ⚡ **Execução Assíncrona** — Processamento paralelo para alta performance

---

## 🚀 Como Começar

### 🛠 Pré-requisitos
- Python 3.9+
- Conta no [Google AI Studio](https://ai.google.dev/) (para API Key do Gemini)

### 📦 Instalação

**Via pip (mais simples):**
```bash
pip install mangaba
```

**Ou clonando o repositório:**
```bash
git clone https://github.com/dheiver2/mangaba_ai.git
cd mangaba_ai
python setup.py.pre   # Instala dependências
pip install .
```

**Ou utilizando o requirements.txt:**
```bash
git clone https://github.com/dheiver2/mangaba_ai.git
cd mangaba_ai
pip install -r requirements.txt
pip install .
```

---

## 🧪 Verificação da Instalação
```python
import mangaba
print(mangaba.__version__)
```

---

## 🛠 Solução de Problemas
- **Dependências faltando:**  
```bash
pip install google-generativeai googlesearch-python requests aiohttp tenacity
```

- **Windows (problema de codificação):**  
```bash
set PYTHONIOENCODING=utf-8
pip install mangaba
```

- **Erro na instalação em modo editável:**  
```bash
python setup.py develop
```

---

## ⚙️ Configuração Inicial
1. Obtenha sua API Key no [Google AI Studio](https://ai.google.dev/).
2. Configure em seu projeto:

```python
from mangaba.config import configure_api
configure_api("sua_api_key_aqui")
```

---

## 📚 Exemplo de Uso

```python
import asyncio
import mangaba

async def exemplo():
    memory = mangaba.ContextualMemory()
    model = mangaba.GeminiModel()
    search_tool = mangaba.GoogleSearchTool()

    pesquisador = mangaba.Agent(
        name="Pesquisador", 
        role="Busca dados", 
        model=model, 
        tools=[search_tool], 
        memory=memory
    )

    tarefa = mangaba.Task(
        description="Buscar inovações em IA", 
        agent=pesquisador
    )

    equipe = mangaba.Crew(agents=[pesquisador], tasks=[tarefa])
    await equipe.run()
    
    print(tarefa.result)

if __name__ == "__main__":
    asyncio.run(exemplo())
```

---

## 🏗 Estrutura do Projeto
```
mangaba/
├── __init__.py
├── config/
│   ├── __init__.py
│   └── api.py
├── core/
│   ├── __init__.py
│   └── models.py
└── cases/
    ├── __init__.py
    └── cases.py
```

---

## 🤝 Como Contribuir
1. Faça um fork 🍴
2. Crie uma branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'feat: adiciona nova funcionalidade'`)
4. Push para sua branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request 🚀

---

## 📄 Licença
Distribuído sob licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## ✉️ Contato
- Dheiver — [@dheiver2](https://github.com/dheiver2) — dheiver.santos@gmail.com
- Gabriel — [@Dargouls](https://github.com/Dargouls) — gabriel.azevedo_dev@hotmail.com
- Luiz — [@luizfilipelgs](https://github.com/luizfilipelgs) — luizfilipelgs@gmail.com
