# CLIPTextEncodeHiDream

O nó CLIPTextEncodeHiDream processa quatro entradas de texto separadas usando diferentes modelos de linguagem (CLIP-L, CLIP-G, T5-XXL e LLaMA) e as combina em uma única saída de condicionamento. Ele tokeniza cada entrada de texto com seu modelo correspondente e as codifica em conjunto usando uma abordagem de codificação agendada, permitindo um condicionamento de texto mais sofisticado ao aproveitar vários modelos de linguagem simultaneamente.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `clip` | O modelo CLIP usado para tokenização e codificação | CLIP | Sim | - |
| `clip_l` | Entrada de texto para processamento do modelo CLIP-L. Suporta texto multilinha e prompts dinâmicos. | STRING | Sim | - |
| `clip_g` | Entrada de texto para processamento do modelo CLIP-G. Suporta texto multilinha e prompts dinâmicos. | STRING | Sim | - |
| `t5xxl` | Entrada de texto para processamento do modelo T5-XXL. Suporta texto multilinha e prompts dinâmicos. | STRING | Sim | - |
| `llama` | Entrada de texto para processamento do modelo LLaMA. Suporta texto multilinha e prompts dinâmicos. | STRING | Sim | - |

**Nota:** Todas as quatro entradas de texto (`clip_l`, `clip_g`, `t5xxl` e `llama`) são necessárias para o funcionamento adequado, pois cada uma contribui para a saída final de condicionamento através do processo de codificação agendada.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `CONDITIONING` | A saída de condicionamento combinada de todas as entradas de texto processadas, codificada usando o método de codificação agendada | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeHiDream/pt-BR.md)

---
**Source fingerprint (SHA-256):** `51d117d82a9d833f095e874bf442d5cf8c46a12313fda6b98e628fa988797565`
