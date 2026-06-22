# Definir Propriedades e Combinar Par de Condições

O nó PairConditioningSetPropertiesAndCombine modifica e combina pares de condicionamento aplicando novos dados de condicionamento às entradas de condicionamento positivo e negativo existentes. Ele permite ajustar a intensidade do condicionamento aplicado e controlar como a área de condicionamento é definida. Este nó é particularmente útil para fluxos de trabalho avançados de manipulação de condicionamento onde é necessário mesclar múltiplas fontes de condicionamento.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `positivo` | A entrada de condicionamento positivo original | CONDITIONING | Sim | - |
| `negativo` | A entrada de condicionamento negativo original | CONDITIONING | Sim | - |
| `positivo_NOVO` | O novo condicionamento positivo a ser aplicado | CONDITIONING | Sim | - |
| `negativo_NOVO` | O novo condicionamento negativo a ser aplicado | CONDITIONING | Sim | - |
| `força` | O fator de intensidade para aplicar o novo condicionamento (padrão: 1.0) | FLOAT | Sim | 0.0 a 10.0 |
| `definir_área_cond` | Controla como a área de condicionamento é aplicada (padrão: "default") | STRING | Sim | "default"<br>"mask bounds" |
| `máscara` | Máscara opcional para restringir a área de aplicação do condicionamento | MASK | Não | - |
| `ganchos` | Grupo de hooks opcional para controle avançado | HOOKS | Não | - |
| `etapas` | Especificação opcional de faixa de timesteps | TIMESTEPS_RANGE | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `positivo` | A saída de condicionamento positivo combinada | CONDITIONING |
| `negativo` | A saída de condicionamento negativo combinada | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetPropertiesAndCombine/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d434fdc1ccbe3ddee6293a6300cc55d30cb5bf357025b26777791746f51e755e`
