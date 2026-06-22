# Redimensionar Imagens pela Borda Maior

O nó Redimensionar Imagens pela Borda Maior redimensiona uma ou mais imagens para que o lado mais longo corresponda a um comprimento alvo especificado. Ele determina automaticamente se a largura ou altura é maior e dimensiona a outra dimensão proporcionalmente para preservar a proporção original. Isso é útil para padronizar tamanhos de imagem com base em sua maior dimensão.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `image` | A imagem de entrada ou lote de imagens a ser redimensionado. | IMAGE | Sim | - |
| `borda_maior` | Comprimento alvo para a borda maior. A borda menor será dimensionada proporcionalmente. (padrão: 1024) | INT | Sim | 1 - 8192 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `image` | A imagem ou lote de imagens redimensionado. A saída terá o mesmo número de imagens que a entrada, com a borda maior de cada uma correspondendo ao comprimento especificado em `borda_maior`. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImagesByLongerEdge/pt-BR.md)

---
**Source fingerprint (SHA-256):** `687d5f159967eccbf64f0ec529ae6edeb94f4707ae10a3c75a5d0b08c86dd828`
