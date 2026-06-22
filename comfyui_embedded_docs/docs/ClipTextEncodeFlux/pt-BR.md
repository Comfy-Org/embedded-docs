# CLIPTextEncodeFlux

`CLIPTextEncodeFlux` é um nó de codificação de texto avançado projetado para a arquitetura Flux. Ele processa duas entradas de texto separadas por meio de diferentes codificadores — CLIP-L e T5XXL — e as combina com uma escala de orientação para produzir uma saída de condicionamento unificada para geração de imagens.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `clip` | Um modelo CLIP que suporta a arquitetura Flux, incluindo ambos os codificadores CLIP-L e T5XXL. | CLIP | Sim | - |
| `clip_l` | Entrada de texto processada pelo codificador CLIP-L. Adequada para descrições concisas com palavras-chave, como estilo ou tema. Suporta entrada multilinha e prompts dinâmicos. | STRING | Sim | - |
| `t5xxl` | Entrada de texto processada pelo codificador T5XXL. Adequada para descrições detalhadas em linguagem natural, expressando cenas e detalhes complexos. Suporta entrada multilinha e prompts dinâmicos. | STRING | Sim | - |
| `orientação` | Controla a influência das condições de texto no processo de geração. Valores mais altos significam adesão mais rigorosa ao texto. Padrão: 3,5. | FLOAT | Sim | 0.0 - 100.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `CONDITIONING` | Contém os embeddings fundidos de ambos os codificadores e o parâmetro de orientação, usado para geração condicional de imagens. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeFlux/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f168610123410a44f9c5c5c18773603bd47bc7b44b21e65910a6026f86d7eb04`
