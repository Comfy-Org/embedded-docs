# Embaralhar Lista de Vídeos

Este nó recebe uma lista de vídeos e os reordena aleatoriamente. Ele usa uma semente aleatória para tornar a ordem embaralhada reproduzível, de modo que a mesma semente sempre produz a mesma ordem de saída.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-----------|--------------|-------------|-----------|
| `vídeos` | Lista de vídeos para embaralhar. | VIDEO | Sim | Lista de entradas de vídeo |
| `semente` | Semente aleatória para o embaralhamento (padrão: 0). | INT | Não | 0 a 18446744073709551615 |
Observação: o valor da semente é reduzido módulo 4294967295 (2^32 - 1) antes de ser usado. Como resultado, sementes que diferem por um múltiplo de 4294967295 produzem a mesma ordem de saída.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-----------|--------------|
| `vídeos` | Lista embaralhada de vídeos em ordem aleatória. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleVideoDataset/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0bd32b664197d3bbd4c53f65e29ef38fba836579f07f05cb7fb85f3b8a1024ac`
