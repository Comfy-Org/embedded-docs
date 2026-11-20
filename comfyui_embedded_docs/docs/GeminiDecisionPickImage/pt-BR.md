# Google Gemini Decision (Pick Image)

Escolha a melhor imagem de um lote. Conecte `index` a Get Image from Batch para manter a imagem escolhida, para que o restante do fluxo de trabalho seja executado apenas na seleção.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modelo a usar (padrão: `"gemini-decision-1"`). | COMBO | Sim | `"gemini-decision-1"` |
| `question` | Qual imagem escolher (padrão: "Which image best matches the prompt in text? If there is no text, which image has the best quality?"). | STRING | Sim | 1 a 5000 caracteres |
| `images` | As imagens dentre as quais escolher, como um lote ou um único lote de quadros. | IMAGE | Sim | 2 a 64 imagens |
| `text` | Texto sobre o qual a pergunta se refere, como o prompt a partir do qual as imagens foram geradas, com até 20000 caracteres. | STRING | Não | Até 20000 caracteres |

O nó precisa de 2 a 64 imagens e gera um erro com uma única imagem. Conecte `text` quando a escolha precisar seguir um prompt em vez de apenas a qualidade da imagem.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `index` | Posição da imagem escolhida no lote, começando em 0. | INT |
| `confidence` | Confiança na escolha, entre 0 e 1. | FLOAT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiDecisionPickImage/pt-BR.md)

---
**Source fingerprint (SHA-256):** `55eb604923cb66b42f23f37d0c710a97033cc2c5d95880d45397bba10e44dab0`
