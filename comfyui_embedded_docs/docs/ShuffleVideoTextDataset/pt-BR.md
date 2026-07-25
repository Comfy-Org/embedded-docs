# Embaralhar Pares de Vídeo-Texto

Este nó embaralha aleatoriamente a ordem de pares de vídeo-texto, mantendo cada vídeo emparelhado com seu texto correspondente. Ele recebe duas listas de mesmo comprimento e aplica a mesma permutação aleatória a ambas, garantindo que os pares originais sejam preservados após o embaralhamento.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-----------|---------------|-------------|-------|
| `vídeos` | Lista de vídeos para embaralhar. | VIDEO | Sim | Lista de itens de vídeo |
| `textos` | Lista de textos para embaralhar. | STRING | Sim | Lista de strings de texto |
| `semente` | Semente aleatória para controlar a ordem do embaralhamento (padrão: 0). | INT | Sim | 0 a 18446744073709551615 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-----------|---------------|
| `vídeos` | Vídeos embaralhados na nova ordem aleatória. | VIDEO |
| `textos` | Textos embaralhados na mesma nova ordem dos vídeos. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleVideoTextDataset/pt-BR.md)

---
**Source fingerprint (SHA-256):** `33b763a6d48ca1036d5267139f90eadb3b2080a02fa57ce5bcae6087a077efa1`
