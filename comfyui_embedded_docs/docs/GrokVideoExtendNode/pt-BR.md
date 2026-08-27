# Grok Video Extend

O nó Grok Video Extend usa um modelo de IA para criar uma continuação perfeita de um vídeo existente. Você fornece um vídeo curto e um prompt de texto descrevendo o que deve acontecer em seguida, e o nó gera um novo clipe de vídeo que dá continuidade ao original.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `modelo` | O modelo a ser usado para a extensão de vídeo. | DYNAMIC_COMBO | Sim | `"grok-imagine-video"` |
| `prompt` | Descrição textual do que deve acontecer em seguida no vídeo. | STRING | Sim | N/A |
| `vídeo` | Vídeo de origem a ser estendido. Formato MP4, 2 a 15 segundos. | VIDEO | Sim | N/A |
| `semente` | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos independentemente da semente (padrão: 0). | INT | Sim | 0 a 2147483647 |

### Entradas do grok-imagine-video

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `duration` | Duração da extensão em segundos (padrão: 8). | INT | Sim | 2 a 10 |

**Restrições dos parâmetros:**
*   A entrada `video` deve ser um arquivo MP4 com duração entre 2 e 15 segundos e não pode exceder 50MB de tamanho.
*   O `prompt` deve conter pelo menos um caractere após a remoção de espaços em branco.
*   O parâmetro `model` é um combo dinâmico. Selecionar a opção "grok-imagine-video" revela o parâmetro aninhado `duration`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | A extensão de vídeo recém-gerada. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoExtendNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5009c007b6f93cd44f2742b024b65f1ac92ab9bca3b85a55554b1d99649e323b`
