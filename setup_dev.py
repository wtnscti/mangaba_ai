#!/usr/bin/env python
"""
Script de setup para ambiente de desenvolvimento do Mangaba.AI
"""
import subprocess
import sys
from pathlib import Path

def run_command(command: str) -> bool:
    """Executa um comando e retorna True se bem sucedido"""
    try:
        print(f"Executando: {command}")
        subprocess.run(command, shell=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar comando: {e}")
        return False

def main():
    """Função principal de setup"""
    # Verifica se está em um ambiente virtual
    if not hasattr(sys, 'real_prefix') and not sys.base_prefix != sys.prefix:
        print("⚠️  Aviso: Não está em um ambiente virtual. Recomendado criar um:")
        print("python -m venv venv")
        print("source venv/bin/activate  # Linux/Mac")
        print("venv\\Scripts\\activate  # Windows")
        return

    # Instala dependências
    print("\n📦 Instalando dependências...")
    if not run_command("pip install -r requirements.txt"):
        return

    # Instala o pacote em modo desenvolvimento
    print("\n🔧 Instalando pacote em modo desenvolvimento...")
    if not run_command("pip install -e ."):
        return

    # Cria diretório de logs
    print("\n📝 Criando diretório de logs...")
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    # Executa testes
    print("\n🧪 Executando testes...")
    if not run_command("pytest"):
        return

    # Verifica linting
    print("\n🔍 Verificando linting...")
    if not run_command("pylint mangaba_ai"):
        return

    # Formata código
    print("\n✨ Formatando código...")
    if not run_command("black mangaba_ai"):
        return
    if not run_command("isort mangaba_ai"):
        return

    print("\n✅ Setup concluído com sucesso!")
    print("\nPara começar a desenvolver:")
    print("1. Ative o ambiente virtual")
    print("2. Execute os testes: pytest")
    print("3. Verifique o linting: pylint mangaba_ai")
    print("4. Formate o código: black mangaba_ai && isort mangaba_ai")

if __name__ == "__main__":
    main() 