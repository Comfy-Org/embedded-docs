# LatentOperationTonemapReinhard

Este nó cria uma operação latente que aplica mapeamento de tons de Reinhard a vetores latentes. Ele normaliza cada vetor latente, mede a distribuição geral de magnitude (média e desvio padrão) e, em seguida, comprime magnitudes extremas usando a curva de Reinhard, com a força geral controlada por um multiplicador. O nó está marcado como experimental (também pesquisável como "hdr latent").

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `multiplicador` | Controla a intensidade do efeito de mapeamento de tons (padrão: 1.0) | FLOAT | Sim | 0.0 a 100.0 (passo 0.01) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `operation` | Retorna uma operação de mapeamento de tons que pode ser aplicada a vetores latentes | LATENT_OPERATION |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationTonemapReinhard/pt-BR.md)

---
**Source fingerprint (SHA-256):** `19d58c288967ab27eb1e84e60bc35a6d6c8b4e643168de689132396ae0ee3cbe`
