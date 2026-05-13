> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeHunyuanDiT/pt-BR.md)

O nó `CLIPTextEncodeHunyuanDiT` converte descrições textuais em um formato compreensível para o modelo HunyuanDiT. É um nó de condicionamento avançado projetado para a arquitetura de codificador de texto duplo do HunyuanDiT, processando duas entradas de texto separadas por meio de diferentes tokenizadores.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|---------------|-------------|-----------|-----------|
| `clip` | CLIP | Sim | - | Uma instância do modelo CLIP usada para tokenização e codificação de texto, essencial para gerar condições. |
| `bert` | STRING | Sim | - | Entrada de texto para codificação via tokenizador BERT. Prefere frases e palavras-chave. Suporta múltiplas linhas e prompts dinâmicos. |
| `mt5xl` | STRING | Sim | - | Entrada de texto para codificação via tokenizador mT5-XL. Suporta múltiplas linhas e prompts dinâmicos (multilíngue). Pode usar frases completas e descrições complexas. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `CONDITIONING` | CONDITIONING | A saída de condicionamento codificada, combinando o texto tokenizado tanto do BERT quanto do mT5-XL, usada para processamento adicional em tarefas de geração. |

---
**Source fingerprint (SHA-256):** `6a8d649708b315c42b7933b52fad7e0b45aa34c168616f18a2178041148eeea1`
