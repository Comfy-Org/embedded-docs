# ConditioningMultiply

Este nó multiplica os valores de condicionamento por um fator especificado, permitindo escalar a influência do condicionamento no processo de geração. Ele funciona aplicando o multiplicador tanto ao tensor principal de condicionamento quanto aos valores de saída agrupados.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|--------------|-------------|-------|
| `conditioning` | Os dados de condicionamento a serem escalados | CONDITIONING | Sim | - |
| `multiplier` | O fator para multiplicar os valores de condicionamento (padrão: 1.0) | FLOAT | Sim | -100.0 a 100.0 (passo: 0.01) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-----------|--------------|
| `CONDITIONING` | Os dados de condicionamento escalados com valores multiplicados | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningMultiply/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8d241e3d5d91e513c24ade5b4bece4bf879fe093a4be6d53dab11a5a0bf55616`
