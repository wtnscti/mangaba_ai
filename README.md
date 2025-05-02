<p align="center">
  <img src="assets/img2.png" width="400" alt="Mangaba.AI logo">
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
pip install mangaba-ai
```

**Clonando o repositório:**
```bash
git clone https://github.com/dheiver2/mangaba_ai.git
cd mangaba_ai
pip install -r requirements.txt
pip install .
```

---

## ✅ Verificando a Instalação

```python
import mangaba_ai
print(mangaba_ai.__version__)  # Exibe a versão instalada
```

---

## 🛠 Solução de Problemas

- **Dependências faltando:**  
```bash
pip install -r requirements.txt
```

- **Problemas de codificação no Windows:**  
```bash
set PYTHONIOENCODING=utf-8
pip install mangaba-ai
```

---

## ⚙️ Configuração Inicial

1. Obtenha sua API Key no [Google AI Studio](https://ai.google.dev/).
2. Configure no seu projeto:

```python
from mangaba_ai.config import configure_api
configure_api("sua_api_key_aqui")
```

---

## 📚 Exemplo de Uso

```python
import asyncio
import mangaba_ai

async def exemplo():
    # Inicializa os componentes
    memory = mangaba_ai.ContextualMemory()
    model = mangaba_ai.GeminiModel()
    search_tool = mangaba_ai.GoogleSearchTool()

    # Cria um agente
    pesquisador = mangaba_ai.Agent(
        name="Pesquisador",
        role="Busca dados",
        model=model,
        tools=[search_tool],
        memory=memory
    )

    # Cria uma tarefa
    tarefa = mangaba_ai.Task(
        description="Buscar inovações em IA",
        agent=pesquisador
    )

    # Cria uma equipe e executa
    equipe = mangaba_ai.Crew(agents=[pesquisador], tasks=[tarefa])
    await equipe.run()

    # Exibe o resultado
    print(tarefa.result)

if __name__ == "__main__":
    asyncio.run(exemplo())
```

---

## 🏗 Estrutura do Projeto

```
mangaba_ai/
├── assets/             # Recursos estáticos (imagens, etc.)
├── docs/              # Documentação detalhada
├── examples/          # Exemplos e notebooks
├── mangaba_ai/        # Código fonte principal
│   ├── __init__.py    # Inicializador do pacote
│   ├── logging_config.py
│   ├── config/        # Configurações
│   ├── core/          # Componentes centrais
│   └── cases/         # Casos de uso
└── tests/             # Testes automatizados
```

---

## 🧪 Testes

O projeto inclui testes automatizados para garantir a qualidade do código:

```bash
# Instalar dependências de teste
pip install -r requirements.txt

# Executar todos os testes
pytest

# Executar testes com cobertura
pytest --cov=mangaba_ai
```

---

## 📚 Documentação

A documentação detalhada está disponível em `docs/`:

```bash
# Gerar documentação
cd docs
make html
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
