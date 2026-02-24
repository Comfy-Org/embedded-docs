> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchImagesNode/pt-BR.md)

O nó Batch Images combina várias imagens individuais em um único lote. Ele recebe um número variável de entradas de imagem e as emite como um único tensor de imagem em lote, permitindo que sejam processadas juntas em nós subsequentes.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Sim | 2 a 50 entradas | Uma lista dinâmica de entradas de imagem. Você pode adicionar entre 2 e 50 imagens para serem combinadas em um lote. A interface do nó permite adicionar mais slots de entrada de imagem conforme necessário. |

**Observação:** Você deve conectar pelo menos duas imagens para que o nó funcione. O primeiro slot de entrada é sempre obrigatório, e você pode adicionar mais usando o botão "+" que aparece na interface do nó.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | IMAGE | Um único tensor de imagem em lote contendo todas as imagens de entrada empilhadas juntas. |
