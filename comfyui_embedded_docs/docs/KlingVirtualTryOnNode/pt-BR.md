# Kling Prova Virtual

Nó de Prova Virtual Kling. Insira uma imagem de uma pessoa e uma imagem de roupa para vestir a roupa na pessoa. Você pode combinar várias imagens de peças de roupa em uma única imagem com fundo branco.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `human_image` | A imagem da pessoa para vestir as roupas | IMAGE | Sim | - |
| `cloth_image` | A imagem da roupa para vestir na pessoa | IMAGE | Sim | - |
| `model_name` | O modelo de prova virtual a ser usado (padrão: "kolors-virtual-try-on-v1") | STRING | Sim | `"kolors-virtual-try-on-v1"` |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | A imagem resultante mostrando a pessoa com a peça de roupa vestida | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVirtualTryOnNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `bfd0da440d3ad85e15ce16851313f2e75421a8a3eb5e4c651350432955afc731`
