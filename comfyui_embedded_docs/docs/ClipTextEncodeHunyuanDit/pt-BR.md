O nó `CLIPTextEncodeHunyuanDiT` converte descrições textuais em um formato compreensível para o modelo HunyuanDiT. É um nó de condicionamento avançado projetado para a arquitetura de codificador de texto duplo do HunyuanDiT, processando duas entradas de texto separadas por meio de diferentes tokenizadores.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `clip` | Uma instância do modelo CLIP usada para tokenização e codificação de texto, essencial para gerar condições. | CLIP | Sim | - |
| `bert` | Entrada de texto para codificação via tokenizador BERT. Prefere frases e palavras-chave. Suporta múltiplas linhas e prompts dinâmicos. | STRING | Sim | - |
| `mt5xl` | Entrada de texto para codificação via tokenizador mT5-XL. Suporta múltiplas linhas e prompts dinâmicos (multilíngue). Pode usar frases completas e descrições complexas. | STRING | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `CONDITIONING` | A saída de condicionamento codificada, combinando o texto tokenizado tanto do BERT quanto do mT5-XL, usada para processamento adicional em tarefas de geração. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeHunyuanDiT/pt-BR.md)

---
**Source fingerprint (SHA-256):** `6a8d649708b315c42b7933b52fad7e0b45aa34c168616f18a2178041148eeea1`
