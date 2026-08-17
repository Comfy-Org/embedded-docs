# CLIPTextEncodeHunyuanDiT

O nó `CLIPTextEncodeHunyuanDiT` converte descrições de texto em um formato que o modelo HunyuanDiT pode entender. É um nó de condicionamento avançado, projetado para a arquitetura de codificador duplo de texto do HunyuanDiT, processando duas entradas de texto separadas por meio de diferentes tokenizadores e combinando-as em uma única saída de condicionamento.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `clip` | Uma instância do modelo CLIP usada para tokenização e codificação de texto, que é essencial para gerar condições. | CLIP | Sim | - |
| `bert` | Entrada de texto para codificação via tokenizador BERT. Prefere frases e palavras-chave. Suporta prompts multilinha e dinâmicos. | STRING | Sim | - |
| `mt5xl` | Entrada de texto para codificação via tokenizador mT5-XL. Suporta prompts multilinha e dinâmicos (multilíngues). Pode usar frases completas e descrições complexas. | STRING | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `CONDITIONING` | A saída de condicionamento codificada, combinando o texto tokenizado por BERT e mT5-XL, usada para processamento adicional em tarefas de geração. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeHunyuanDiT/pt-BR.md)

---
**Source fingerprint (SHA-256):** `550e8c09b8b74974576a852a9b690a87a0156ef49fe7ec1050b10415c6af78aa`
