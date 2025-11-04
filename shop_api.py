from flask import Flask, request, jsonify
import requests
import os
import textwrap
import re

app = Flask(__name__)

TOGETHER_API_KEY = "tgp_v1_PIjZvu20Ljfly1KpASmkyV3efe5Y0BuhPmX7JGg5gTQ"

def construir_prompt_estilos(estilos_actuales, instruccion_usuario):
    """
    Construye un prompt especializado para modificación de CSS
    """
    prompt = f"""<s>[INST] Eres un asistente especializado en CSS. Modifica los estilos proporcionados según la instrucción del usuario.

ESTILOS CSS ACTUALES:
```css
{estilos_actuales}
