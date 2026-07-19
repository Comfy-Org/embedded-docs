# Grok Video Extend

O nó Grok Video Extend usa um modelo de IA para criar uma continuação perfeita de um vídeo existente. Você fornece um vídeo curto e um prompt de texto descrevendo o que deve acontecer em seguida, e o nó gera um novo clipe de vídeo que dá continuidade ao original.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `prompt` | Descrição textual do que deve acontecer em seguida no vídeo. | STRING | Sim | N/A |
| `vídeo` | Vídeo de origem a ser estendido. Formato MP4, de 2 a 15 segundos. | VIDEO | Sim | N/A |
| `modelo` | O modelo a ser usado para extensão de vídeo. Quando selecionado, revela um parâmetro `duration` aninhado. | COMBO | Sim | `"grok-imagine-video"` |
| `semente` | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos independentemente da semente (padrão: 0). | INT | Não | 0 a 2147483647 |

**Restrições dos Parâmetros:**
*   A entrada `video` deve ser um arquivo MP4 com duração entre 2 e 15 segundos e não pode exceder 50 MB de tamanho.
*   O `prompt` deve conter pelo menos um caractere (espaços em branco são removidos).
*   O parâmetro `model` é uma combinação dinâmica. Selecionar a opção "grok-imagine-video" revela um parâmetro `duration` aninhado, que controla a duração da extensão em segundos (padrão: 8, faixa: 2 a 10).

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | A extensão de vídeo recém-gerada. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoExtendNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a33383be0eb6857538a75e1b901ee58df0153dfeaf95a7ee19933d651b745b5f`
