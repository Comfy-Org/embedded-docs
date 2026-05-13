> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NAGuidance/pt-BR.md)

O nó NAGuidance aplica Orientação de Atenção Normalizada a um modelo. Esta técnica permite o uso de prompts negativos com modelos destilados ou schnell, modificando o mecanismo de atenção do modelo durante o processo de amostragem para direcionar a geração para longe de conceitos indesejados.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `modelo` | MODEL | Sim | - | O modelo ao qual aplicar a Orientação de Atenção Normalizada. |
| `escala_nag` | FLOAT | Sim | 0.0 - 50.0 | O fator de escala da orientação. Valores mais altos afastam ainda mais a geração do prompt negativo. (padrão: 5.0) |
| `nag_alpha` | FLOAT | Sim | 0.0 - 1.0 | O fator de mesclagem para a atenção normalizada. Um valor de 1.0 substitui completamente a atenção original, enquanto 0.0 não tem efeito. (padrão: 0.5) |
| `nag_tau` | FLOAT | Sim | 1.0 - 10.0 | Um fator de escala usado para limitar a taxa de normalização. (padrão: 1.5) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `modelo` | MODEL | O modelo modificado com a Orientação de Atenção Normalizada ativada. |

---
**Source fingerprint (SHA-256):** `ea3d7fea94e62c8a0784887f3df9d8a503c3dbaa552bf860bd4dde1ae576fa9c`
