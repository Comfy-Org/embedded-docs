> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerpNeg/pt-BR.md)

O nó PerpNeg aplica orientação negativa perpendicular ao processo de amostragem de um modelo. Este nó modifica a função de configuração do modelo para ajustar as previsões de ruído usando condicionamento negativo e fatores de escala. Ele foi descontinuado e substituído pelo nó PerpNegGuider para funcionalidade aprimorada.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|--------------|-------------|-----------|-----------|
| `model` | MODEL | Sim | - | O modelo ao qual aplicar a orientação negativa perpendicular |
| `empty_conditioning` | CONDITIONING | Sim | - | Condicionamento vazio usado para cálculos de orientação negativa |
| `neg_scale` | FLOAT | Não | 0.0 - 100.0 | Fator de escala para orientação negativa (padrão: 1.0) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `model` | MODEL | O modelo modificado com orientação negativa perpendicular aplicada |

**Nota**: Este nó está obsoleto e foi substituído pelo PerpNegGuider. Ele é marcado como experimental e não deve ser usado em fluxos de trabalho de produção.

---
**Source fingerprint (SHA-256):** `6be4ab03cfbda33ed3966ecd579c1a5e3242bdfb163fecefb9c80073a8827cae`
