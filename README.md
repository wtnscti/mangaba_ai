Claro, Dheiver! Aqui está um `README.md` formatado em Markdown para o projeto **Mangaba.AI**, incluindo a logo e uma explicação clara sobre seu propósito, instalação e uso.

---

```markdown
<p align="center">
  <img src="https://github.com/dheiver2/mangaba_ai/blob/main/img.png" alt="Mangaba.AI Logo" width="300"/>
</p>

<h1 align="center">Mangaba.AI 🍈</h1>

<p align="center">
  Biblioteca avançada para orquestração de agentes de IA colaborativos.
</p>

---

## ✨ Visão Geral

**Mangaba.AI** é uma biblioteca Python moderna para construção de sistemas com múltiplos agentes de inteligência artificial capazes de cooperar entre si em tarefas complexas. Inspirada por arquiteturas cognitivas e orquestração inteligente, permite a criação de pipelines robustos com memória contextual, busca web, modelos de linguagem e controle de tarefas com dependências.

---

## 🧠 Principais Recursos

- 🔁 **Memória Contextual Compartilhada** (Global e Individual)
- 🔧 **Integração com Ferramentas Externas**, como Google Search
- 🤖 **Agentes Autônomos com Papéis Diferenciados**
- 🔄 **Execução Sequencial com Controle de Dependência**
- ⚡ **Compatível com Gemini API (Google Generative AI)**

---

## 🛠️ Instalação

No Google Colab, execute:

```python
!pip install -q google-generativeai googlesearch-python
```

---

## 🔐 Configuração da API Gemini

Adicione sua chave Gemini no Colab:

1. Clique no ícone de chave (🔑) à esquerda.
2. Adicione um novo segredo com o nome: `GEMINI_API_KEY`
3. Cole sua chave da API do Google Generative AI.
4. Reexecute a célula principal do notebook.

---

## 🚀 Exemplo de Uso

```python
await main()
```

O sistema executa:

1. **Pesquisador** → Busca dados sobre IA na saúde.
2. **Analista** → Analisa os dados encontrados.
3. **Escritor** → Gera um relatório executivo com os resultados.

---

## 🧩 Estrutura de Agentes

- **ContextualMemory**: Armazena e recupera contexto global e individual.
- **GeminiModel**: Wrapper assíncrono para o modelo da Gemini API.
- **GoogleSearchTool**: Permite buscas em tempo real.
- **Agent**: Executor de tarefas com ferramentas e memória.
- **Task**: Define uma tarefa com prioridade e dependências.
- **Crew**: Orquestra a execução entre múltiplos agentes.

---

## 🖼️ Logo

<div align="center">
  <img src="https://github.com/dheiver2/mangaba_ai/blob/main/img.png" width="200"/>
</div>

---

## 🤝 Contribuição

Pull requests são bem-vindos! Sinta-se à vontade para abrir issues com sugestões e melhorias.

---

## 📄 Licença

MIT © 2025 - Desenvolvido por Dheiver Santos e colaboradores.

---

## 🌐 Links Úteis

- [Google Generative AI](https://ai.google.dev)
- [Python asyncio](https://docs.python.org/3/library/asyncio.html)
- [Gemini Models](https://cloud.google.com/vertex-ai/docs/generative-ai/overview)
```

---

Se quiser que eu salve isso como arquivo `.md` para você baixar ou adicionar diretamente no repositório, é só avisar!
