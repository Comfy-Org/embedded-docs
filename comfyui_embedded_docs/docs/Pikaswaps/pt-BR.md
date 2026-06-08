O nó Pika Swaps substitui objetos ou regiões no seu vídeo por uma nova imagem. Você define as áreas a serem substituídas usando uma máscara, e o nó troca perfeitamente o conteúdo especificado ao longo da sequência de vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `video` | O vídeo no qual um objeto será trocado. | VIDEO | Sim | - |
| `image` | A imagem usada para substituir o objeto mascarado no vídeo. | IMAGE | Sim | - |
| `mask` | Use a máscara para definir as áreas do vídeo a serem substituídas. | MASK | Sim | - |
| `prompt_text` | Prompt de texto descrevendo a substituição desejada. | STRING | Sim | - |
| `negative_prompt` | Prompt de texto descrevendo o que evitar na substituição. | STRING | Sim | - |
| `seed` | Valor de semente aleatória para resultados consistentes. | INT | Sim | 0 a 4294967295 |

**Observação:** Este nó exige que todos os parâmetros de entrada sejam fornecidos. Os parâmetros `video`, `image` e `mask` trabalham juntos para definir a operação de substituição, onde a máscara especifica quais áreas do vídeo serão substituídas pela imagem fornecida.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | O vídeo processado com o objeto ou região especificada substituída. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikaswaps/pt-BR.md)

---
**Source fingerprint (SHA-256):** `007b7bc429fdada2fb8910392b056ae3a98d482cce9e280bdcd162ede497eb03`
