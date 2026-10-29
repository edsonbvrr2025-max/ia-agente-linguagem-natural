#!/usr/bin/env python3
"""
ORÁCULO — Setup para instalação via pip
"""

from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="oraculo-termux",
    version="1.0.0",
    author="ORÁCULO Project",
    author_email="oraculo@example.com",
    description="Agente de IA 100% offline para Android (Termux)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SEU_USUARIO/oraculo-termux",
    packages=find_packages(include=["oraculo", "oraculo.*"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Home Automation",
    ],
    python_requires=">=3.11",
    install_requires=[
        "pyyaml>=6.0.1",
        "python-dotenv>=1.0.0",
        "rich>=13.7.0",
        "tqdm>=4.66.0",
        "requests>=2.31.0",
        "psutil>=5.9.0",
    ],
    extras_require={
        "llm": ["llama-cpp-python>=0.2.90"],
        "stt": ["vosk>=0.3.45"],
        "tts": ["piper-tts>=1.2.0", "sherpa-onnx>=1.10.0"],
        "vector": ["sqlite-vec>=0.1.6", "onnxruntime>=1.17.0"],
        "automation": ["pure-python-adb>=0.2.0"],
        "dev": [
            "pytest>=7.4.0",
            "pytest-asyncio>=0.21.0",
            "pytest-cov>=4.1.0",
            "ruff>=0.1.0",
            "mypy>=1.7.0",
            "buildozer>=1.5.0",
            "cython>=3.0.0",
        ],
        "all": [
            "llama-cpp-python>=0.2.90",
            "vosk>=0.3.45",
            "piper-tts>=1.2.0",
            "sherpa-onnx>=1.10.0",
            "sqlite-vec>=0.1.6",
            "onnxruntime>=1.17.0",
            "pure-python-adb>=0.2.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "oraculo=oraculo.main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "oraculo": ["../config.yaml", "../memoria.md", "../perfil.md"],
    },
    zip_safe=False,
)