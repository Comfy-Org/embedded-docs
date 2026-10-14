# Higgsfield Genjutsu Motion Transfer

O nó **Higgsfield Genjutsu Motion Transfer** recria um vídeo com novos personagens, locais ou estilos obtidos de imagens de referência, mantendo o movimento, o movimento de câmera, o timing e o áudio do clipe de origem. Conecte o clipe a ser reestilizado e uma ou mais imagens de referência que descrevem o novo visual; em seguida, descreva o resultado no prompt. A solicitação é enviada para a API da Higgsfield e o vídeo gerado é retornado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `model` | Modelo a usar. Selecionar um modelo revela os parâmetros específicos dele: `video`, `reference_images`, `prompt`, `resolution` e `seed`. | DYNAMIC_COMBO | Sim | `"genjutsu-v1.0"` |
| `video` | Vídeo de origem cujo movimento, movimento de câmera, timing e áudio são mantidos. Pelo menos 4 segundos; apenas os primeiros 30 segundos são usados. | VIDEO | Sim | 4 a 30 segundos |
| `reference_images` | Slot expansível: conecte de 1 a 8 imagens (`image_1`, `image_2`, ...) dos personagens, locais ou estilos a usar. Uma entrada em lote conta uma vez por imagem. | IMAGE | Sim | 1 a 8 imagens |
| `prompt` | Opcional. Descreva o resultado, por exemplo qual referência substitui qual pessoa, ou um novo cenário. (padrão: vazio) | STRING | Sim | Qualquer texto |
| `resolution` | Resolução do vídeo de saída. (padrão: `"720p"`) | COMBO | Sim | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `seed` | A seed controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da seed. Este parâmetro tem a funcionalidade "controle após gerar" (padrão: 42). | INT | Sim | 0 a 2147483647 |

O vídeo de origem é validado antes de a solicitação ser enviada: um clipe com menos de 4 segundos é rejeitado, e um clipe com mais de 30 segundos é cortado para seus primeiros 30 segundos. O áudio dele é mantido no resultado. As imagens de referência são enviadas primeiro, e o número total de imagens em todos os slots conectados não pode exceder 8, embora o nó exponha oito slots. A moderação de conteúdo da Higgsfield pode rejeitar a entrada ou o resultado, o que gera um erro em vez de retornar um vídeo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `VIDEO` | O arquivo de vídeo reestilizado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiggsfieldMotionTransferNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f0c30fb93dd2af8d564335290fdb6ff61c38e36ab62cef9641fd1aa81cc10cd2`
