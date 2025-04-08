### README.md
```markdown
# Mangaba.AI - Orquestração de Agentes de IA no Google Colab

**Mangaba.AI** é uma biblioteca avançada para orquestração de agentes de IA colaborativos, projetada para executar tarefas em sequência ou paralelo, com suporte a memória contextual e ferramentas externas. Esta implementação foi adaptada para o Google Colab, utilizando a API do Gemini (Google Generative AI) e integrando busca real via Google Search.

## Características
- **Agentes Colaborativos**: Define agentes com papéis específicos (ex.: Pesquisador, Analista, Escritor) que trabalham em tarefas interdependentes.
- **Memória Contextual**: Suporte a memória individual por agente e memória global compartilhada.
- **Ferramentas Externas**: Integração com busca no Google para enriquecer os dados processados.
- **Dependências**: Tarefas podem depender de resultados anteriores, garantindo fluxos de trabalho estruturados.
- **Segurança**: Uso de Secrets no Colab para proteger a chave de API do Gemini.
- **Execução Assíncrona**: Otimizado para desempenho com `asyncio`.

## Pré-requisitos
- Conta no Google Colab.
- Chave de API do Gemini (obtida em [Google Maker Suite](https://makersuite.google.com/app/apikey)).
- Acesso à internet para instalação de bibliotecas e busca no Google.

## Instalação e Configuração
### Passo 1: Configurar a Chave de API nos Secrets
1. No Google Colab, clique no ícone de chave (🔑) no menu à esquerda para abrir a aba "Secrets".
2. Clique em "Adicionar novo segredo".
3. Nomeie o segredo como `GEMINI_API_KEY`.
4. Cole sua chave de API do Gemini (ex.: `AIzaSyClWplmEF8_sDgmSbhg0h6xkAoFQcLU4p4`) no campo "Valor".
5. Ative "Acesso ao notebook" e salve.

### Passo 2: Executar o Código
O código está dividido em duas células principais:

#### Célula 1: Instalação e Configuração
```python
# Instala bibliotecas necessárias
!pip install -q google-generativeai googlesearch-python

# Importa bibliotecas
import google.generativeai as genai
from google.colab import userdata
from googlesearch import search

# Obtém a chave de API do Gemini a partir dos Secrets
try:
    API_KEY = userdata.get('GEMINI_API_KEY')
    if not API_KEY:
        raise ValueError("A chave 'GEMINI_API_KEY' não foi encontrada nos Secrets.")
except userdata.SecretNotFoundError:
    raise ValueError("Por favor, adicione a chave 'GEMINI_API_KEY' nos Secrets do Colab. Veja as instruções abaixo.")

# Configura a API do Gemini
genai.configure(api_key=API_KEY)

# Teste simples para verificar a API
try:
    test_model = genai.GenerativeModel("gemini-1.5-pro")
    test_response = test_model.generate_content("Teste de API")
    print("API do Gemini configurada com sucesso!")
except Exception as e:
    raise ValueError(f"Falha ao validar a API do Gemini: {str(e)}")

# Instruções para adicionar o segredo
print("""
Como adicionar a chave nos Secrets:
1. No menu à esquerda do Colab, clique no ícone de chave (🔑).
2. Clique em 'Adicionar novo segredo'.
3. Nomeie como 'GEMINI_API_KEY' e cole sua chave.
4. Ative 'Acesso ao notebook' e reexecute esta célula.
""")
```

#### Célula 2: Implementação do Mangaba.AI
```python
import asyncio
from typing import List, Optional, Dict, Set
from dataclasses import dataclass

# Definição dos módulos (ContextualMemory, GeminiModel, GoogleSearchTool, Agent, Task, Crew)
# [Código completo conforme fornecido anteriormente]

# Exemplo de uso
async def main():
    memory = ContextualMemory(max_context_size=5)
    model = GeminiModel(temperature=0.8, top_k=50)
    search_tool = GoogleSearchTool()

    pesquisador = Agent(name="Pesquisador", role="Busca dados", model=model, tools=[search_tool], memory=memory)
    analista = Agent(name="Analista", role="Analisa dados", model=model, memory=memory)
    escritor = Agent(name="Escritor", role="Escreve relatório", model=model, memory=memory)

    tarefa_pesquisa = Task(description="Buscar dados sobre IA na saúde", agent=pesquisador, priority=2)
    tarefa_analise = Task(description="Analisar os dados encontrados", agent=analista, priority=1, dependencies=[tarefa_pesquisa])
    tarefa_relatorio = Task(description="Gerar relatório executivo", agent=escritor, priority=0, dependencies=[tarefa_analise])

    equipe = Crew(agents=[pesquisador, analista, escritor], tasks=[tarefa_pesquisa, tarefa_analise, tarefa_relatorio])
    await equipe.run()

if __name__ == "__main__":
    await main()
```

### Execução
1. Execute a Célula 1 para instalar dependências e validar a API.
2. Execute a Célula 2 para rodar o Mangaba.AI com o exemplo de "IA na saúde".

## Exemplo de Saída Esperada
```
[Pesquisador] Executando: Buscar dados sobre IA na saúde
[Pesquisador] Resultado: A IA na saúde está transformando diagnósticos...
[Analista] Executando: Analisar os dados encontrados
[Analista] Resultado: Dados indicam 30% mais precisão com IA...
[Escritor] Executando: Gerar relatório executivo
[Escritor] Resultado: Relatório: IA na saúde oferece benefícios claros...
```

## Resolução de Problemas
- **Erro 429 (Quota Excedida)**: Verifique sua quota no [Google Cloud Console](https://console.cloud.google.com/). Aumente o limite ou adicione delays maiores em `GeminiModel.generate` (ex.: `await asyncio.sleep(1)`).
- **Erro de Chave Inválida**: Confirme que o segredo `GEMINI_API_KEY` está correto nos Secrets.
- **Modelo Inválido**: Se `"gemini-1.5-pro"` falhar, consulte a [documentação do Gemini](https://ai.google.dev/gemini-api/docs/models) para modelos disponíveis.

## Contribuições
Sinta-se à vontade para sugerir melhorias, como novas ferramentas ou ajustes nos agentes, enviando um pull request ou abrindo uma issue!

## Licença
MIT - Desenvolvido por [Dr Dheiver Francisco Santos] em 2025.
```

