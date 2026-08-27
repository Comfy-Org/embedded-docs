# LatentOperationTonemapReinhard

O nó LatentOperationTonemapReinhard aplica mapeamento de tom de Reinhard a vetores latentes. Essa técnica normaliza os vetores latentes e ajusta sua magnitude usando uma abordagem estatística baseada em média e desvio padrão, com a intensidade controlada por um parâmetro multiplicador. Este nó está atualmente marcado como experimental.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `multiplicador` | Controla a intensidade do efeito de mapeamento de tom (padrão: 1.0) | FLOAT | Sim | 0.0 a 100.0 (passo 0.01) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `operation` | Retorna uma operação de mapeamento de tom que pode ser aplicada a vetores latentes | LATENT_OPERATION |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationTonemapReinhard/pt-BR.md)

---
**Source fingerprint (SHA-256):** `19d58c288967ab27eb1e84e60bc35a6d6c8b4e643168de689132396ae0ee3cbe`
