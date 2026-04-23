> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoExtendNode/pt-BR.md)

O nó Grok Video Extend usa um modelo de IA para criar uma continuação perfeita de um vídeo existente. Você fornece um vídeo curto e um prompt de texto descrevendo o que deve acontecer em seguida, e o nó gera um novo clipe de vídeo que dá continuidade ao original.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|--------------|-------------|-----------|-----------|
| `prompt` | STRING | Sim | N/A | Descrição textual do que deve acontecer em seguida no vídeo. |
| `video` | VIDEO | Sim | N/A | Vídeo de origem a ser estendido. Formato MP4, de 2 a 15 segundos. |
| `model` | COMBO | Sim | `"grok-imagine-video"` | O modelo a ser usado para extensão de vídeo. Quando selecionado, revela um parâmetro `duration`. |
| `seed` | INT | Não | 0 a 2147483647 | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos, independentemente da semente (padrão: 0). |

**Restrições dos Parâmetros:**
*   A entrada `video` deve ser um arquivo MP4 com duração entre 2 e 15 segundos e não pode exceder 50 MB de tamanho.
*   O `prompt` deve conter pelo menos um caractere (espaços em branco são removidos).
*   O parâmetro `model` é uma combinação dinâmica. Selecionar a opção "grok-imagine-video" revela um parâmetro `duration` aninhado, que controla a duração da extensão em segundos (padrão: 8, intervalo: 2 a 10).

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | VIDEO | A extensão de vídeo recém-gerada. |