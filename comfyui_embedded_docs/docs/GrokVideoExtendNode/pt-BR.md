# Grok Video Extend

O nó Grok Video Extend usa um modelo de IA para criar uma continuação perfeita de um vídeo existente. Você fornece um vídeo curto e um prompt de texto descrevendo o que deve acontecer em seguida, e o nó gera um novo clipe de vídeo que dá continuidade ao original.

## Entradas

### Entradas Comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `modelo` | O modelo a ser usado para extensão de vídeo. | COMBO | Sim | `"grok-imagine-video"` |
| `prompt` | Descrição textual do que deve acontecer a seguir no vídeo. | STRING | Sim | N/A |
| `vídeo` | Vídeo de origem a ser estendido. Formato MP4, de 2 a 15 segundos. | VIDEO | Sim | N/A |
| `semente` | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos independentemente da semente (padrão: 0). | INT | Não | 0 a 2147483647 |

### Entradas do grok-imagine-video

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `duration` | Duração da extensão em segundos (padrão: 8). | INT | Sim | 2 a 10 |

**Restrições de Parâmetros:**
*   A entrada `video` deve ser um arquivo MP4 com duração entre 2 e 15 segundos e não pode exceder 50MB de tamanho de arquivo.
*   A entrada `prompt` deve conter pelo menos um caractere (espaços em branco são removidos).
*   O parâmetro `model` é uma combinação dinâmica. Selecionar a opção "grok-imagine-video" revela o parâmetro aninhado `duration`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | A extensão de vídeo recém-gerada. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoExtendNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `bfaf56dd12afab13c820345587db9ee871db87d60b8dc003f00f035513dbdf61`
