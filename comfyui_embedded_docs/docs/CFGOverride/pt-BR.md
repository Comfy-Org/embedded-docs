# Substituir CFG

O nó CFG Override substitui a escala CFG (Classifier-Free Guidance) por um valor fixo ao longo de um intervalo percentual (sigma) do processo de amostragem. Quando vários nós CFG Override são usados, a substituição mais próxima do amostrador prevalece em intervalos sobrepostos.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-----------|---------------|-------------|-----------|
| `model` | O modelo ao qual aplicar a substituição de CFG. | MODEL | Sim | |
| `cfg` | O valor fixo da escala CFG a ser usado durante o intervalo de substituição. Padrão: 1.0. | FLOAT | Sim | 0.0 a 100.0 (passo: 0.1) |
| `start_percent` | O ponto inicial do intervalo de substituição como porcentagem do processo de amostragem. Padrão: 0.0. | FLOAT | Sim | 0.0 a 1.0 (passo: 0.001) |
| `end_percent` | O ponto final do intervalo de substituição como porcentagem do processo de amostragem. Padrão: 1.0. | FLOAT | Sim | 0.0 a 1.0 (passo: 0.001) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-----------|---------------|
| `MODEL` | O modelo com o wrapper de substituição de CFG aplicado. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGOverride/pt-BR.md)

---
**Source fingerprint (SHA-256):** `94c7d3751d90b42479f9cec4bdb3c95eeda405f51224f85d313ff12ec071ec58`
