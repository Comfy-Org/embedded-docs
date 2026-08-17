# StableCascade_StageB_Conditioning

O nó StableCascade_StageB_Conditioning prepara dados de condicionamento para a geração na Etapa B do Stable Cascade, combinando informações de condicionamento existentes com representações latentes anteriores da Etapa C. Ele modifica cada entrada de condicionamento para incluir as amostras latentes da Etapa C, permitindo que o processo de geração aproveite as informações anteriores para saídas mais coerentes.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `conditioning` | Os dados de condicionamento a serem modificados com as informações anteriores da Etapa C | CONDITIONING | Sim | - |
| `stage_c` | A representação latente da Etapa C contendo amostras anteriores para condicionamento | LATENT | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `CONDITIONING` | Os dados de condicionamento modificados com as informações anteriores da Etapa C integradas | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageB_Conditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3154457773465e5b93221b6d83d2064b565cb653403e12e88615652c7832d1e8`
