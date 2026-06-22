# Luma Referência

Este nó armazena uma imagem e um valor de peso para uso com o nó Gerar Imagem Luma. Ele cria uma cadeia de referência que pode ser passada para outros nós Luma para influenciar a geração de imagens. O nó pode iniciar uma nova cadeia de referência ou adicionar a uma já existente.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `imagem` | Imagem a ser usada como referência. | IMAGE | Sim | - |
| `peso` | Peso da referência de imagem (padrão: 1.0). | FLOAT | Sim | 0.0 - 1.0 |
| `luma_ref` | Cadeia de referência Luma existente opcional para adicionar. | LUMA_REF | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `luma_ref` | A cadeia de referência Luma contendo a imagem e o peso. | LUMA_REF |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaReferenceNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1ad653f0ad7c56702f607ebc3c3d117196295e4e3b044a2c6f1aa3db18869a40`
