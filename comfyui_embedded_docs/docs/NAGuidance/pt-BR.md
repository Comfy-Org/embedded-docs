# Orientação de Atenção Normalizada

O nó NAGuidance aplica Orientação de Atenção Normalizada (Normalized Attention Guidance) a um modelo. Esta técnica permite o uso de prompts negativos com modelos destilados ou schnell, modificando o mecanismo de atenção do modelo durante o processo de amostragem para afastar a geração de conceitos indesejados.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo ao qual aplicar a Orientação de Atenção Normalizada. | MODEL | Sim | - |
| `escala_nag` | O fator de escala de orientação. Valores mais altos afastam mais a geração do prompt negativo. (padrão: 5.0) | FLOAT | Sim | 0.0 - 50.0 |
| `nag_alpha` | O fator de mesclagem para a atenção normalizada. Um valor de 1.0 substitui totalmente a atenção original, enquanto 0.0 não tem efeito. (padrão: 0.5) | FLOAT | Sim | 0.0 - 1.0 |
| `nag_tau` | Um fator de escala usado para limitar a taxa de normalização. (padrão: 1.5) | FLOAT | Sim | 1.0 - 10.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model` | O modelo com patch e com a Orientação de Atenção Normalizada ativada. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NAGuidance/pt-BR.md)

---
**Source fingerprint (SHA-256):** `42b4d601312dcbb1c934c6a79bbb5e9fd6598fa5f32b18f5c0affcb596672cba`
