> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ThresholdMask/pt-BR.md)

O nó ThresholdMask converte uma máscara em uma máscara binária aplicando um valor de limiar. Ele compara cada pixel da máscara de entrada com o valor de limiar especificado e cria uma nova máscara onde os pixels acima do limiar tornam-se 1 (branco) e os pixels abaixo ou iguais ao limiar tornam-se 0 (preto).

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `mask` | MASK | Sim | - | A máscara de entrada a ser processada |
| `valor` | FLOAT | Sim | 0.0 - 1.0 | O valor de limiar para binarização (padrão: 0.5) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `mask` | MASK | A máscara binária resultante após a aplicação do limiar |

---
**Source fingerprint (SHA-256):** `5c61433c05ef8106d928306b64035078e7598605512f20aaf992255f7b166456`
