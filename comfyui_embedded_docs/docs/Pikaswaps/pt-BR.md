> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikaswaps/pt-BR.md)

O nó Pika Swaps permite substituir objetos ou regiões em seu vídeo por novas imagens. Você pode definir as áreas a serem substituídas usando uma máscara ou coordenadas, e o nó trocará perfeitamente o conteúdo especificado ao longo da sequência de vídeo.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | Sim | - | O vídeo no qual um objeto será substituído. |
| `image` | IMAGE | Sim | - | A imagem usada para substituir o objeto mascarado no vídeo. |
| `mask` | MASK | Sim | - | Use a máscara para definir as áreas do vídeo a serem substituídas. |
| `prompt_text` | STRING | Sim | - | Prompt de texto descrevendo a substituição desejada. |
| `negative_prompt` | STRING | Sim | - | Prompt de texto descrevendo o que evitar na substituição. |
| `seed` | INT | Sim | 0 a 4294967295 | Valor de semente aleatória para resultados consistentes. |

**Observação:** Este nó requer que todos os parâmetros de entrada sejam fornecidos. O `video`, a `image` e a `mask` trabalham juntos para definir a operação de substituição, onde a máscara especifica quais áreas do vídeo serão substituídas pela imagem fornecida.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O vídeo processado com o objeto ou região especificada substituída. |
