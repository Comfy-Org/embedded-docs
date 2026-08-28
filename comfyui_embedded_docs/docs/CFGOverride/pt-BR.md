# Substituir CFG

O nó CFG Override permite definir um valor fixo de escala CFG (Classifier-Free Guidance) para um intervalo específico do processo de amostragem, definido como uma porcentagem do total de passos. Quando vários nós CFG Override estão conectados, o mais próximo do amostrador na cadeia tem prioridade para intervalos sobrepostos.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `modelo` | O modelo ao qual aplicar a substituição de CFG | MODEL | Sim | |
| `cfg` | O valor fixo de escala CFG a ser usado durante o intervalo de substituição (padrão: 1.0) | FLOAT | Sim | 0.0 a 100.0 |
| `percentual_inicial` | O ponto inicial do intervalo de substituição como uma porcentagem do processo de amostragem (padrão: 0.0) | FLOAT | Sim | 0.0 a 1.0 |
| `percentual_final` | O ponto final do intervalo de substituição como uma porcentagem do processo de amostragem (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|----------------|-------------|---------------|
| `MODEL` | O modelo com o wrapper de substituição de CFG aplicado | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGOverride/pt-BR.md)

---
**Source fingerprint (SHA-256):** `94c7d3751d90b42479f9cec4bdb3c95eeda405f51224f85d313ff12ec071ec58`
