# StableCascade_StageB_Conditioning

O nó StableCascade_StageB_Conditioning prepara dados de condicionamento para a geração do Stage B do Stable Cascade, combinando informações de condicionamento existentes com a representação latente prévia produzida pelo Stage C. Ele copia cada entrada de condicionamento e armazena nela as amostras latentes do Stage C, para que etapas posteriores de geração possam usar essa informação prévia e obter resultados mais coerentes.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `conditioning` | Os dados de condicionamento a serem modificados com a informação prévia do Stage C. Cada entrada na lista é copiada e recebe as amostras do Stage C. | CONDITIONING | Sim | - |
| `stage_c` | A representação latente do Stage C. Seu valor `samples` é usado como a informação prévia adicionada ao condicionamento. | LATENT | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `CONDITIONING` | Os dados de condicionamento modificados com a informação prévia do Stage C integrada. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageB_Conditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3154457773465e5b93221b6d83d2064b565cb653403e12e88615652c7832d1e8`
