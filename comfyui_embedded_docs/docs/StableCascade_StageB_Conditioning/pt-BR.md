O nó **StableCascade_StageB_Conditioning** prepara dados de condicionamento para a geração do Estágio B do Stable Cascade, combinando informações de condicionamento existentes com representações latentes anteriores do Estágio C. Ele modifica os dados de condicionamento para incluir as amostras latentes do Estágio C, permitindo que o processo de geração aproveite as informações anteriores para obter resultados mais coerentes.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `condicionamento` | Os dados de condicionamento a serem modificados com as informações anteriores do Estágio C | CONDITIONING | Sim | - |
| `stage_c` | A representação latente do Estágio C contendo amostras anteriores para condicionamento | LATENT | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `CONDITIONING` | Os dados de condicionamento modificados com as informações anteriores do Estágio C integradas | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageB_Conditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f6ee524889aa324151a91c200fdc2692754cbd1348e32fbc05a26fd7ba27c755`
