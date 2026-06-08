Este nó gera vídeos usando o modelo Kling V3. Ele suporta dois modos principais: texto-para-vídeo, onde um vídeo é criado a partir de uma descrição textual, e imagem-para-vídeo, onde uma imagem existente é animada. Também oferece recursos avançados como criar vídeos com múltiplos segmentos usando descrições diferentes para cada parte (storyboards) e, opcionalmente, gerar áudio de acompanhamento.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `multi_shot` | Controla se deve gerar um único vídeo ou uma série de segmentos com descrições e durações individuais. Quando não está "desativado", entradas adicionais para a descrição e duração de cada storyboard aparecem. | COMBO | Sim | `"desativado"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `gerar áudio` | Quando ativado, o nó gerará áudio para o vídeo. O padrão é `Verdadeiro`. | BOOLEANO | Sim | `Verdadeiro` / `Falso` |
| `modelo` | O modelo e suas configurações associadas. Selecionar esta opção revela os subparâmetros `resolution` e `aspect_ratio`. | COMBO | Sim | `"kling-v3"` |
| `model.resolution` | A resolução do vídeo gerado. Esta configuração está disponível quando o `modelo` está definido como "kling-v3". | COMBO | Sim | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `model.aspect_ratio` | A proporção de aspecto do vídeo gerado. Esta configuração é ignorada quando uma imagem é fornecida para `quadro inicial` (modo imagem-para-vídeo). Disponível quando o `modelo` está definido como "kling-v3". | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `seed` | Um valor de semente para a geração. Alterar este valor fará com que o nó seja executado novamente, mas os resultados não são determinísticos. O padrão é `0`. | INT | Sim | 0 a 2147483647 |
| `quadro inicial` | Uma imagem inicial opcional. Quando conectada, o nó muda do modo texto-para-vídeo para o modo imagem-para-vídeo, animando a imagem fornecida. | IMAGEM | Não | - |

**Entradas para o modo `multi_shot`:**

* Quando `multi_shot` está definido como **"desativado"**, as seguintes entradas aparecem:
  * `prompt` (STRING): A descrição textual principal para o vídeo. Obrigatório. Deve ter entre 1 e 2500 caracteres.
  * `negative_prompt` (STRING): Texto descrevendo o que não deve aparecer no vídeo. Opcional.
  * `duration` (INT): A duração do vídeo em segundos. Deve estar entre 3 e 15. O padrão é `5`.
* Quando `multi_shot` está definido como uma opção de storyboard (ex.: `"3 storyboards"`), entradas para cada segmento de storyboard aparecem (ex.: `storyboard_1_prompt`, `storyboard_1_duration`). Cada descrição deve ter entre 1 e 512 caracteres. A **soma total de todas as durações dos storyboards** deve estar entre 3 e 15 segundos.

**Restrições:**

* O nó opera no modo **texto-para-vídeo** quando `start_frame` não está conectado. Ele usa a configuração `model.aspect_ratio` neste modo.
* O nó opera no modo **imagem-para-vídeo** quando `start_frame` está conectado. A configuração `model.aspect_ratio` é ignorada. A imagem de entrada deve ter pelo menos 300x300 pixels e uma proporção de aspecto entre 1:2.5 e 2.5:1.
* No modo storyboard (`multi_shot` não "desativado"), as entradas principais `prompt` e `negative_prompt` ficam ocultas e não são utilizadas.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `video` | O arquivo de vídeo gerado. | VÍDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f7f827d657b1d057d273eba3215ce6848d3ea05c5f348e2f3fccccfdd030dfc3`
