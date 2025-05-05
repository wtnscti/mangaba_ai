"""
Setup configuration for Mangaba.AI
"""
from setuptools import setup, find_packages
import subprocess
import sys
import os
import json
import shutil
from pathlib import Path

# Garantir que as dependências básicas de build estejam instaladas
try:
    import pip
    print("[-] pip está instalado")
except ImportError:
    print("[!] pip não está instalado corretamente")

# Instalando dependências antes da build
DEPENDENCIES = [
    "google-generativeai>=0.8.3",
    "googlesearch-python>=1.2.1",
    "requests>=2.32.3",
    "aiohttp>=3.10.5",
    "tenacity>=8.5.0",
]

print("[+] Instalando dependências necessárias para a build...")
for dep in DEPENDENCIES:
    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", dep],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        print(f"  [+] {dep}")
    except subprocess.CalledProcessError:
        print(f"  [!] Falha ao instalar {dep}")

# Carrega o README para a descrição longa
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="mangaba-ai",
    version="0.1.0",
    author="Mangaba.AI Team",
    author_email="contact@mangaba.ai",
    description="Framework para desenvolvimento de agentes autônomos",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mangaba-ai/mangaba-ai",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "google-generativeai>=0.8.3",
        "python-dotenv>=1.0.0",
        "aiohttp>=3.9.0",
    ],
) 