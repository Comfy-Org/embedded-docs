> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetPropertiesAndCombine/pt-BR.md)

O nó PairConditioningSetPropertiesAndCombine modifica e combina pares de condicionamento aplicando novos dados de condicionamento às entradas de condicionamento positivo e negativo existentes. Ele permite ajustar a intensidade do condicionamento aplicado e controlar como a área de condicionamento é definida. Este nó é particularmente útil para fluxos de trabalho avançados de manipulação de condicionamento onde é necessário mesclar múltiplas fontes de condicionamento.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `positivo` | CONDITIONING | Sim | - | A entrada de condicionamento positivo original |
| `negativo` | CONDITIONING | Sim | - | A entrada de condicionamento negativo original |
| `positivo_NOVO` | CONDITIONING | Sim | - | O novo condicionamento positivo a ser aplicado |
| `negativo_NOVO` | CONDITIONING | Sim | - | O novo condicionamento negativo a ser aplicado |
| `força` | FLOAT | Sim | 0.0 a 10.0 | O fator de intensidade para aplicar o novo condicionamento (padrão: 1.0) |
| `definir_área_cond` | STRING | Sim | "default"<br>"mask bounds" | Controla como a área de condicionamento é aplicada (padrão: "default") |
| `máscara` | MASK | Não | - | Máscara opcional para restringir a área de aplicação do condicionamento |
| `ganchos` | HOOKS | Não | - | Grupo de hooks opcional para controle avançado |
| `etapas` | TIMESTEPS_RANGE | Não | - | Especificação opcional de faixa de timesteps |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|---------------|-----------|
| `positivo` | CONDITIONING | A saída de condicionamento positivo combinada |
| `negativo` | CONDITIONING | A saída de condicionamento negativo combinada |

---
**Source fingerprint (SHA-256):** `d434fdc1ccbe3ddee6293a6300cc55d30cb5bf357025b26777791746f51e755e`
