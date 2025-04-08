# Mangaba AI - Framework de Automação com Agentes Inteligentes

<img src="https://github.com/dheiver2/mangaba_ai/blob/main/img.png" width="300">

Framework Python para criação de equipes de agentes AI autônomos que colaboram para resolver tarefas complexas.

## ✨ Funcionalidades Principais

- **Arquitetura Multi-Agente**: Crie equipes de agentes especializados
- **Memória Contextual**: Histórico individual e compartilhado entre agentes
- **Integração Gemini**: Utilize os modelos mais avançados da Google
- **Ferramentas Externas**: Busca no Google e outras APIs
- **Gerenciamento de Tarefas**: Dependências e priorização automática
- **Processamento Assíncrono**: Execução paralela para maior eficiência

## 🚀 Começando

### Pré-requisitos
- Python 3.9+
- Conta no Google AI Studio (para API key do Gemini)
- Google Colab (recomendado) ou ambiente local

### Instalação
```bash
pip install google-generativeai googlesearch-python
```

### Configuração
1. Obtenha sua API key do Gemini
2. Adicione no Colab Secrets como `GEMINI_API_KEY`
3. Ou configure diretamente no código:
```python
API_KEY = "sua_chave_aqui"
genai.configure(api_key=API_KEY)
```

## 📚 Exemplo de Uso

```python
# Criação dos agentes
memory = ContextualMemory()
model = GeminiModel()
search_tool = GoogleSearchTool()

pesquisador = Agent(name="Pesquisador", 
                   role="Busca dados", 
                   model=model, 
                   tools=[search_tool], 
                   memory=memory)

# Definição de tarefas
tarefas = [
    Task("Buscar inovações em IA", pesquisador, priority=2),
    # ... outras tarefas
]

# Execução
equipe = Crew(agents=[pesquisador, ...], tasks=tarefas)
await equipe.run()
```

## 🏗 Estrutura do Projeto

```
mangaba_ai/
├── agents/          # Módulos de agentes especializados
├── core/            # Componentes principais
│   ├── memory.py    # Sistema de memória
│   ├── models.py    # Integração com LLMs
│   └── tasks.py     # Gerenciamento de tarefas
├── tools/           # Ferramentas externas
└── examples/        # Casos de uso exemplares
```

## 🤝 Como Contribuir

1. Faça um fork do projeto
2. Crie sua branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📄 Licença

Distribuído sob licença MIT. Veja `LICENSE` para mais informações.

## ✉️ Contato

Dheiver Santos - [@dheiver](https://github.com/dheiver2) - dheiver.santos@gmail.com

Project Link: [https://github.com/dheiver2/mangaba_ai](https://github.com/dheiver2/mangaba_ai)
```
