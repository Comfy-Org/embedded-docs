# LTXVConditioning

O nó LTXVConditioning adiciona informações de taxa de quadros às entradas de condicionamento positivo e negativo para modelos de geração de vídeo. Ele recebe dados de condicionamento existentes e aplica o valor de taxa de quadros especificado a ambos os conjuntos de condicionamento, tornando-os adequados para o processamento de modelos de vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `positivo` | A entrada de condicionamento positivo que receberá as informações de taxa de quadros | CONDITIONING | Sim | - |
| `negativo` | A entrada de condicionamento negativo que receberá as informações de taxa de quadros | CONDITIONING | Sim | - |
| `taxa_de_quadros` | O valor de taxa de quadros a ser aplicado a ambos os conjuntos de condicionamento (padrão: 25.0) | FLOAT | Sim | 0.0 - 1000.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positivo` | O condicionamento positivo com as informações de taxa de quadros aplicadas | CONDITIONING |
| `negativo` | O condicionamento negativo com as informações de taxa de quadros aplicadas | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c8546b691329f2934995f97a6db2e1393d2928bf1a7438fd079d52f87bee1c35`
