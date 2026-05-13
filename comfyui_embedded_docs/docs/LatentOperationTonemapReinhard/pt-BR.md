> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationTonemapReinhard/pt-BR.md)

O nó LatentOperationTonemapReinhard aplica o mapeamento tonal Reinhard a vetores latentes. Esta técnica normaliza os vetores latentes e ajusta sua magnitude usando uma abordagem estatística baseada em média e desvio padrão, com a intensidade controlada por um parâmetro multiplicador.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `multiplicador` | FLOAT | Não | 0.0 a 100.0 | Controla a intensidade do efeito de mapeamento tonal (padrão: 1.0) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `operation` | LATENT_OPERATION | Retorna uma operação de mapeamento tonal que pode ser aplicada a vetores latentes |

---
**Source fingerprint (SHA-256):** `70c04eaef06b749392a0c65f3d1267e52484f7cf956f87173d10ad935afcf98c`
