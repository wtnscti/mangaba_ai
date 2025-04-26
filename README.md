<p align="center">
  <img src="https://github.com/dheiver2/mangaba_ai/blob/main/img2.png" width="400" alt="Mangaba.AI logo">
</p>

<h1 align="center">Mangaba.AI</h1>
<p align="center"><i>Framework avançado para orquestração de equipes de agentes de IA autônomos.</i></p>

---

## ✨ Recursos Principais

- 🔹 **Arquitetura Multi-Agente** — Especialização e colaboração entre agentes
- 🧠 **Memória Contextual** — Histórico individual e compartilhado
- 🧬 **Integração com Gemini** — Modelos de ponta da Google
- 🔍 **Ferramentas Externas** — Busca no Google e APIs adicionais
- ✅ **Gerenciamento de Tarefas** — Dependências e priorização automática
- ⚡ **Execução Assíncrona** — Processamento paralelo para alta performance

---

## 🚀 Como Começar

### 🛠 Pré-requisitos

- Python **3.9+**
- Conta no [Google AI Studio](https://ai.google.dev/) (para obter sua API Key)

### 📦 Instalação

**Instalação via pip:**
```bash
pip install mangaba
```

**Clonando o repositório:**
```bash
git clone https://github.com/dheiver2/mangaba_ai.git
cd mangaba_ai
python setup.py.pre   # Instala dependências
pip install .
```

**Usando `requirements.txt`:**
```bash
git clone https://github.com/dheiver2/mangaba_ai.git
cd mangaba_ai
pip install -r requirements.txt
pip install .
```

---

## ✅ Verificando a Instalação

```python
import mangaba
print(mangaba.__version__)  # Exibe a versão instalada
```

---

## 🛠 Solução de Problemas

- **Dependências faltando:**  
```bash
pip install google-generativeai googlesearch-python requests aiohttp tenacity
```

- **Problemas de codificação no Windows:**  
```bash
set PYTHONIOENCODING=utf-8
pip install mangaba
```

- **Erro ao instalar no modo editável:**  
```bash
python setup.py develop
```

---

## ⚙️ Configuração Inicial

1. Obtenha sua API Key no [Google AI Studio](https://ai.google.dev/).
2. Configure no seu projeto:

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
├── __init__.py         # Inicializador do pacote
├── config/             # Configurações e API keys
│   ├── __init__.py
│   └── api.py
├── core/               # Componentes centrais (Agentes, Tarefas, Equipes)
│   ├── __init__.py
│   └── models.py
└── cases/              # Casos de uso prontos
    ├── __init__.py
    └── cases.py
```

---

## 🤝 Como Contribuir

1. Faça um **fork** 🍴
2. Crie uma **branch**:  
```bash
git checkout -b feature/sua-nova-funcionalidade
```
3. **Commit** suas mudanças:  
```bash
git commit -m 'feat: adiciona nova funcionalidade'
```
4. **Push** para sua branch:  
```bash
git push origin feature/sua-nova-funcionalidade
```
5. Abra um **Pull Request** 🚀

---

## 📄 Licença

Distribuído sob a licença **MIT**. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## ✉️ Contato

| Nome | GitHub | E-mail |
|:---|:---|:---|
| Dheiver | [@dheiver2](https://github.com/dheiver2) | dheiver.santos@gmail.com |
| Gabriel | [@Dargouls](https://github.com/Dargouls) | gabriel.azevedo_dev@hotmail.com |
| Luiz | [@luizfilipelgs](https://github.com/luizfilipelgs) | luizfilipelgs@gmail.com |
