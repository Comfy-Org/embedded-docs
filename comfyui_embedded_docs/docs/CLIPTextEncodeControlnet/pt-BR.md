# CLIPTextEncodeControlnet

O nó CLIPTextEncodeControlnet processa a entrada de texto usando um modelo CLIP e combina com dados de condicionamento existentes para criar uma saída de condicionamento aprimorada para aplicações de ControlNet. Ele tokeniza o texto de entrada, codifica-o por meio do modelo CLIP e adiciona os embeddings resultantes aos dados de condicionamento fornecidos como parâmetros de ControlNet de atenção cruzada.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `clip` | O modelo CLIP usado para tokenização e codificação de texto | CLIP | Sim | - |
| `conditioning` | Dados de condicionamento existentes a serem aprimorados com parâmetros de ControlNet | CONDITIONING | Sim | - |
| `text` | Entrada de texto a ser processada pelo modelo CLIP. Suporta texto multilinha e prompts dinâmicos | STRING | Sim | - |

**Nota:** Este nó requer todas as três entradas (`clip`, `conditioning` e `text`) para funcionar corretamente. A entrada `text` suporta prompts dinâmicos e texto multilinha para processamento flexível de texto. Este nó está marcado como experimental.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `CONDITIONING` | Dados de condicionamento aprimorados com parâmetros de atenção cruzada do ControlNet (`cross_attn_controlnet` e `pooled_output_controlnet`) derivados da codificação de texto do CLIP | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeControlnet/pt-BR.md)

---
**Source fingerprint (SHA-256):** `95a798684ca8734bfff53c7b979b320f6834dc1a9553163d0e567243761000f1`
