> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioMerge/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioMerge/en.md)

O nó AudioMerge combina duas faixas de áudio sobrepondo suas formas de onda. Ele iguala automaticamente as taxas de amostragem de ambas as entradas de áudio e ajusta suas durações para que fiquem iguais antes da mesclagem. O nó oferece vários métodos matemáticos para combinar os sinais de áudio e garante que a saída permaneça dentro de níveis de volume aceitáveis.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `audio1` | AUDIO | Sim | - | Primeira entrada de áudio a ser mesclada |
| `audio2` | AUDIO | Sim | - | Segunda entrada de áudio a ser mesclada |
| `merge_method` | COMBO | Sim | `"add"`<br>`"mean"`<br>`"subtract"`<br>`"multiply"` | O método usado para combinar as formas de onda de áudio. |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `AUDIO` | AUDIO | A saída de áudio mesclada contendo a forma de onda combinada e a taxa de amostragem |

---
**Source fingerprint (SHA-256):** `2a4a7da42835efd03cc67002e617a70c0514524a0ac0ed61d57e499c1283be95`
