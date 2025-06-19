from setuptools import setup, find_packages

setup(
    name="SylphietteIA",  # Nome único no PyPI!
    version="0.1.1",
    author="__token__",
    author_email="seu@email.com",
    description="Assistente IA estilo Sylphiette com fala, VTube Studio e Gemini.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/seuusuario/SylphietteIA",  # opcional
    packages=find_packages(),
    install_requires=[
        "pyttsx3",
        "google-generativeai",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
