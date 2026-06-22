# Substituir CFG

O nó Substituição de CFG permite definir um valor fixo de escala CFG (Orientação Livre de Classificador) para um intervalo específico do processo de amostragem, definido como uma porcentagem do total de etapas. Quando vários nós de Substituição de CFG estão conectados, o mais próximo do amostrador na cadeia tem prioridade para intervalos sobrepostos.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-----------|--------------|-------------|-----------|
| `modelo` | O modelo ao qual aplicar a substituição de CFG | MODEL | Sim | |
| `cfg` | O valor fixo da escala CFG a ser usado durante o intervalo de substituição (padrão: 1.0) | FLOAT | Sim | 0.0 a 100.0 |
| `percentual_inicial` | O ponto inicial do intervalo de substituição como porcentagem do processo de amostragem (padrão: 0.0) | FLOAT | Sim | 0.0 a 1.0 |
| `percentual_final` | O ponto final do intervalo de substituição como porcentagem do processo de amostragem (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-----------|--------------|
| `MODEL` | O modelo com o invólucro de substituição de CFG aplicado | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGOverride/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1fe57a4e78a2f18c4e7da49fa7a6c473d64dc0ebf6662535dfb5379c37936662`
