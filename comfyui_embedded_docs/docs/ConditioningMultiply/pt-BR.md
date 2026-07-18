# Condicionamento (Multiplicar)

Este nó multiplica vetores de condicionamento por um fator escalar, permitindo que você dimensione a influência de uma entrada de condicionamento. Ele aplica o multiplicador tanto ao tensor de condicionamento principal quanto à saída agrupada, se presente.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `conditioning` | Os dados de condicionamento a serem dimensionados | CONDITIONING | Sim | - |
| `multiplier` | O fator de escala a ser aplicado ao condicionamento (padrão: 1.0) | FLOAT | Sim | -100.0 a 100.0 (passo: 0.01) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `CONDITIONING` | Os dados de condicionamento dimensionados com o multiplicador aplicado tanto ao tensor principal quanto à saída agrupada | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningMultiply/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8d241e3d5d91e513c24ade5b4bece4bf879fe093a4be6d53dab11a5a0bf55616`
