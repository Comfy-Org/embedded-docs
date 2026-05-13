> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingAvatarNode/pt-BR.md)

O nó Kling Avatar 2.0 gera vídeos de humanos digitais no estilo broadcast a partir de uma única foto de referência e um arquivo de áudio. Ele cria um vídeo de avatar falante com um prompt de texto opcional para definir as ações, emoções e movimentos de câmera do avatar.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `imagem` | IMAGE | Sim | - | Imagem de referência do avatar. Largura e altura devem ter no mínimo 300px. A proporção deve estar entre 1:2,5 e 2,5:1. |
| `arquivo_de_áudio` | AUDIO | Sim | - | Entrada de áudio. Deve ter duração entre 2 e 300 segundos. |
| `modo` | COMBO | Sim | `"std"`<br>`"pro"` | O modo de geração a ser utilizado. |
| `prompt` | STRING | Não | - | Prompt opcional para definir ações, emoções e movimentos de câmera do avatar. (padrão: string vazia) |
| `semente` | INT | Sim | 0 a 2147483647 | A semente controla se o nó deve ser reexecutado; os resultados são não determinísticos independentemente da semente. (padrão: 0) |

**Nota:** As entradas `image` e `sound_file` possuem requisitos específicos de validação. A imagem deve ter no mínimo 300x300 pixels com proporção entre 1:2,5 e 2,5:1. O arquivo de áudio deve ter duração entre 2 e 300 segundos.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | VIDEO | O vídeo de humano digital gerado. |

---
**Source fingerprint (SHA-256):** `85793d3820a89ef98bb54cb930486847d4fd64cce5470ba34574ec319f8ea8c6`
