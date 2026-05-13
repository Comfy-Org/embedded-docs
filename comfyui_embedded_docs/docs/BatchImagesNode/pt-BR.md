> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchImagesNode/pt-BR.md)

O nó **Agrupar Imagens** combina várias imagens individuais em um único lote. Ele aceita um número variável de entradas de imagem e as agrupa em um tensor de imagem único, permitindo que sejam processadas juntas em nós subsequentes.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `images` | IMAGE | Sim | 2 a 50 entradas | Uma lista dinâmica de entradas de imagem. Você pode adicionar entre 2 e 50 imagens para serem combinadas em um lote. A interface do nó permite adicionar mais slots de entrada de imagem conforme necessário. |

**Observação:** Você deve conectar pelo menos duas imagens para que o nó funcione. O primeiro slot de entrada é sempre obrigatório, e você pode adicionar mais usando o botão "+" que aparece na interface do nó.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | IMAGE | Um único tensor de imagem em lote contendo todas as imagens de entrada empilhadas juntas. |

---
**Source fingerprint (SHA-256):** `f756fb15760cd2518da9c3f88281d3ab3361b4c2b4820fe2be152e4db1cf102c`
