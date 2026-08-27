# StableCascade_StageB_Conditioning

O nó **StableCascade_StageB_Conditioning** prepara os dados de condicionamento para a geração do Estágio B do Stable Cascade, combinando informações de condicionamento existentes com representações latentes prévias do Estágio C. Ele copia cada entrada de condicionamento e adiciona as amostras latentes do Estágio C a ela, permitindo que o processo de geração aproveite a informação prévia para gerar saídas mais coerentes.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `condicionamento` | Os dados de condicionamento a serem modificados com as informações prévias do Estágio C | CONDITIONING | Sim | - |
| `stage_c` | A representação latente do Estágio C contendo amostras prévias para condicionamento | LATENT | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `CONDITIONING` | Os dados de condicionamento modificados com as informações prévias do Estágio C integradas | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageB_Conditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3154457773465e5b93221b6d83d2064b565cb653403e12e88615652c7832d1e8`
