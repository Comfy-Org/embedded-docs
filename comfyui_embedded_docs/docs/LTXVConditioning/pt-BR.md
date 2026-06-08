O nó **LTXVConditioning** adiciona informações de taxa de quadros às entradas de condicionamento positivo e negativo para modelos de geração de vídeo. Ele recebe dados de condicionamento existentes e aplica o valor de taxa de quadros especificado a ambos os conjuntos de condicionamento, tornando-os adequados para o processamento de modelos de vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `positivo` | A entrada de condicionamento positivo que receberá as informações de taxa de quadros | CONDITIONING | Sim | - |
| `negativo` | A entrada de condicionamento negativo que receberá as informações de taxa de quadros | CONDITIONING | Sim | - |
| `taxa_de_quadros` | O valor da taxa de quadros a ser aplicado a ambos os conjuntos de condicionamento (padrão: 25.0) | FLOAT | Sim | 0.0 - 1000.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `positivo` | O condicionamento positivo com as informações de taxa de quadros aplicadas | CONDITIONING |
| `negativo` | O condicionamento negativo com as informações de taxa de quadros aplicadas | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e8c18b73eb009c1b3ebcc2cb8be3dee4e065d75908607a5cf15d41f89963ee09`
