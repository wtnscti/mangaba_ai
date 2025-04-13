# -*- coding: utf-8 -*-
# mangaba/cases/cases.py
# Casos de uso do Mangaba

import asyncio
from mangaba.core.models import ContextualMemory, GeminiModel, GoogleSearchTool, Agent, Task, Crew

# Função para criar e configurar os agentes
def criar_agentes(model, memory, search_tool):
    """
    Cria os agentes necessários para o caso.
    """
    pesquisador = Agent(name="Pesquisador", role="Busca dados", model=model, tools=[search_tool], memory=memory)
    analista = Agent(name="Analista", role="Analisa dados", model=model, memory=memory)
    escritor = Agent(name="Escritor", role="Escreve relatório", model=model, memory=memory)
    return pesquisador, analista, escritor

# Função para criar as tarefas
def criar_tarefas(pesquisador, analista, escritor, descricao_pesquisa, descricao_analise, descricao_relatorio):
    """
    Cria as tarefas e define as dependências entre elas.
    """
    tarefa_pesquisa = Task(description=descricao_pesquisa, agent=pesquisador, priority=2)
    tarefa_analise = Task(description=descricao_analise, agent=analista, priority=1, dependencies=[tarefa_pesquisa])
    tarefa_relatorio = Task(description=descricao_relatorio, agent=escritor, priority=0, dependencies=[tarefa_analise])
    return [tarefa_pesquisa, tarefa_analise, tarefa_relatorio]

# Função genérica para rodar o caso
async def rodar_caso(descricao_pesquisa, descricao_analise, descricao_relatorio):
    """
    Função principal que executa qualquer caso (Mercado ou Educação),
    organizando agentes e tarefas de forma assíncrona.
    """
    print(f"\n=== {descricao_pesquisa.split()[3]} ===")
    
    # Definindo o contexto e modelos
    memory = ContextualMemory(max_context_size=5)
    model = GeminiModel(temperature=0.8, top_k=50)
    search_tool = GoogleSearchTool()

    # Criando os agentes
    pesquisador, analista, escritor = criar_agentes(model, memory, search_tool)

    # Criando as tarefas com as dependências corretas
    tarefas = criar_tarefas(pesquisador, analista, escritor, descricao_pesquisa, descricao_analise, descricao_relatorio)

    # Definindo a equipe e rodando as tarefas
    equipe = Crew(agents=[pesquisador, analista, escritor], tasks=tarefas)
    await equipe.run()


# Case de Uso 1: Análise de Tendências de Mercado
async def case_mercado():
    """
    Função principal para o caso de análise de tendências de mercado.
    """
    await rodar_caso(
        descricao_pesquisa="Buscar dados sobre tendências em tecnologias verdes em 2025",
        descricao_analise="Analisar os dados encontrados",
        descricao_relatorio="Gerar relatório executivo"
    )


# Case de Uso 2: Planejamento Educacional
async def case_educacao():
    """
    Função principal para o caso de planejamento educacional.
    """
    await rodar_caso(
        descricao_pesquisa="Buscar dados sobre IA na educação em 2025",
        descricao_analise="Analisar os dados encontrados",
        descricao_relatorio="Gerar relatório executivo"
    )

# Função principal para execução
async def main():
    await case_mercado()
    await case_educacao()

if __name__ == "__main__":
    asyncio.run(main())  # Usa asyncio.run para execução fora do Colab; no Colab, use await main() 