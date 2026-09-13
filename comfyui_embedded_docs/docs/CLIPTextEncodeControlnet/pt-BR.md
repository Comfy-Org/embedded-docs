# CLIPTextEncodeControlnet

O nó CLIP Text Encode (Controlnet) codifica um prompt de texto com um modelo CLIP e adiciona a codificação de texto resultante aos dados de condicionamento existentes. Ele armazena os embeddings de texto como parâmetros de atenção cruzada do controlnet dentro de cada entrada de condicionamento, de modo que o condicionamento retornado carrega essa informação extra do controlnet.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `clip` | O modelo CLIP usado para tokenização e codificação de texto | CLIP | Sim | - |
| `condicionamento` | Dados de condicionamento existentes a serem combinados com a codificação de texto do CLIP | CONDITIONING | Sim | - |
| `texto` | O prompt de texto a ser processado pelo modelo CLIP. Suporta texto multilinha e prompts dinâmicos | STRING | Sim | - |

**Nota:** Todas as três entradas (`clip`, `conditioning` e `text`) são obrigatórias para que este nó funcione. A entrada `text` suporta texto multilinha e prompts dinâmicos para processamento flexível de texto. Este nó está marcado como experimental no código-fonte.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `CONDITIONING` | Dados de condicionamento aprimorados com os parâmetros de atenção cruzada do controlnet adicionados (`cross_attn_controlnet` e `pooled_output_controlnet`) derivados da codificação de texto do CLIP | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeControlnet/pt-BR.md)

---
**Source fingerprint (SHA-256):** `95a798684ca8734bfff53c7b979b320f6834dc1a9553163d0e567243761000f1`
