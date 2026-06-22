# Kling Avatar 2.0

O nó Kling Avatar 2.0 gera vídeos de humanos digitais no estilo broadcast a partir de uma única foto de referência e um arquivo de áudio. Ele cria um vídeo de avatar falante com um prompt de texto opcional para definir as ações, emoções e movimentos de câmera do avatar.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `imagem` | Imagem de referência do avatar. Largura e altura devem ter no mínimo 300px. A proporção deve estar entre 1:2,5 e 2,5:1. | IMAGE | Sim | - |
| `arquivo_de_áudio` | Entrada de áudio. Deve ter duração entre 2 e 300 segundos. | AUDIO | Sim | - |
| `modo` | O modo de geração a ser utilizado. | COMBO | Sim | `"std"`<br>`"pro"` |
| `prompt` | Prompt opcional para definir ações, emoções e movimentos de câmera do avatar. (padrão: string vazia) | STRING | Não | - |
| `semente` | A semente controla se o nó deve ser reexecutado; os resultados são não determinísticos independentemente da semente. (padrão: 0) | INT | Sim | 0 a 2147483647 |

**Nota:** As entradas `image` e `sound_file` possuem requisitos específicos de validação. A imagem deve ter no mínimo 300x300 pixels com proporção entre 1:2,5 e 2,5:1. O arquivo de áudio deve ter duração entre 2 e 300 segundos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | O vídeo de humano digital gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingAvatarNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `85793d3820a89ef98bb54cb930486847d4fd64cce5470ba34574ec319f8ea8c6`
