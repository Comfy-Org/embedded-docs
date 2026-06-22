# CLIPTextEncodeControlnet

O nó CLIPTextEncodeControlnet processa a entrada de texto usando um modelo CLIP e combina com dados de condicionamento existentes para criar uma saída de condicionamento aprimorada para aplicações de controlnet. Ele tokeniza o texto de entrada, codifica-o através do modelo CLIP e adiciona os embeddings resultantes aos dados de condicionamento fornecidos como parâmetros de atenção cruzada do controlnet.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `clip` | O modelo CLIP usado para tokenização e codificação de texto | CLIP | Sim | - |
| `condicionamento` | Dados de condicionamento existentes a serem aprimorados com parâmetros de controlnet | CONDITIONING | Sim | - |
| `texto` | Texto de entrada a ser processado pelo modelo CLIP. Suporta texto multilinha e prompts dinâmicos | STRING | Sim | - |

**Nota:** Este nó requer todas as três entradas (`clip`, `conditioning` e `text`) para funcionar corretamente. A entrada `text` suporta prompts dinâmicos e texto multilinha para processamento flexível de texto.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `CONDITIONING` | Dados de condicionamento aprimorados com parâmetros adicionais de atenção cruzada do controlnet (`cross_attn_controlnet` e `pooled_output_controlnet`) derivados da codificação de texto do CLIP | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeControlnet/pt-BR.md)

---
**Source fingerprint (SHA-256):** `dd6f68d822cc38e27c826b634c938d62e07b075e18a0f46f80b462aecca0b70b`
