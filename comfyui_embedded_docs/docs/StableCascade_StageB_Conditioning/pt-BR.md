> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageB_Conditioning/pt-BR.md)

O nó **StableCascade_StageB_Conditioning** prepara dados de condicionamento para a geração do Estágio B do Stable Cascade, combinando informações de condicionamento existentes com representações latentes anteriores do Estágio C. Ele modifica os dados de condicionamento para incluir as amostras latentes do Estágio C, permitindo que o processo de geração aproveite as informações anteriores para obter resultados mais coerentes.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|--------------|-------------|-----------|-----------|
| `conditioning` | CONDITIONING | Sim | - | Os dados de condicionamento a serem modificados com as informações anteriores do Estágio C |
| `stage_c` | LATENT | Sim | - | A representação latente do Estágio C contendo amostras anteriores para condicionamento |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `CONDITIONING` | CONDITIONING | Os dados de condicionamento modificados com as informações anteriores do Estágio C integradas |

---
**Source fingerprint (SHA-256):** `f6ee524889aa324151a91c200fdc2692754cbd1348e32fbc05a26fd7ba27c755`
