# CLIPTextEncodeControlnet

O nó CLIPTextEncodeControlnet processa um prompt de texto usando um modelo CLIP e combina a codificação de texto resultante com dados de conditioning existentes. Ele adiciona os embeddings derivados do texto a cada entrada de conditioning como parâmetros de atenção cruzada do controlnet, produzindo uma saída de conditioning aprimorada para aplicações de controlnet.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `clip` | O modelo CLIP usado para tokenização e codificação de texto | CLIP | Sim | - |
| `condicionamento` | Dados de conditioning existentes a serem combinados com a codificação de texto do CLIP | CONDITIONING | Sim | - |
| `texto` | O prompt de texto a ser processado pelo modelo CLIP. Suporta texto multilinha e prompts dinâmicos | STRING | Sim | - |

**Nota:** Todas as três entradas (`clip`, `conditioning` e `text`) são necessárias para o funcionamento deste nó. A entrada `text` suporta texto multilinha e prompts dinâmicos para processamento flexível de texto. Este nó é marcado como experimental no código-fonte.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `CONDITIONING` | Dados de conditioning aprimorados com os parâmetros adicionais de atenção cruzada do controlnet (`cross_attn_controlnet` e `pooled_output_controlnet`) derivados da codificação de texto do CLIP | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeControlnet/pt-BR.md)

---
**Source fingerprint (SHA-256):** `95a798684ca8734bfff53c7b979b320f6834dc1a9553163d0e567243761000f1`
