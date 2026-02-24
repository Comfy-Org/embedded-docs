> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingMotionControl/pt-BR.md)

O nó Kling Motion Control gera um vídeo aplicando o movimento, as expressões e os movimentos de câmera de um vídeo de referência a um personagem definido por uma imagem de referência e um prompt de texto. Ele permite controlar se a orientação final do personagem vem do vídeo de referência ou da imagem de referência.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sim | N/A | Uma descrição textual do vídeo desejado. O comprimento máximo é de 2500 caracteres. |
| `reference_image` | IMAGE | Sim | N/A | Uma imagem do personagem a ser animado. As dimensões mínimas são 340x340 pixels. A proporção deve estar entre 1:2,5 e 2,5:1. |
| `reference_video` | VIDEO | Sim | N/A | Um vídeo de referência de movimento usado para dirigir o movimento e a expressão do personagem. Dimensões mínimas são 340x340 pixels, dimensões máximas são 3850x3850 pixels. Os limites de duração dependem da configuração `character_orientation`. |
| `keep_original_sound` | BOOLEAN | Não | N/A | Determina se o áudio original do vídeo de referência é mantido na saída. O padrão é `True`. |
| `character_orientation` | COMBO | Não | `"video"`<br>`"image"` | Controla de onde vem a direção/orientação do personagem. `"video"`: movimentos, expressões, movimentos de câmera e orientação seguem o vídeo de referência de movimento. `"image"`: movimentos e expressões seguem o vídeo de referência de movimento, mas a orientação do personagem corresponde à imagem de referência. |
| `mode` | COMBO | Não | `"pro"`<br>`"std"` | O modo de geração a ser usado. |

**Restrições:**

* A duração do `reference_video` deve estar entre 3 e 30 segundos quando `character_orientation` estiver definido como `"video"`.
* A duração do `reference_video` deve estar entre 3 e 10 segundos quando `character_orientation` estiver definido como `"image"`.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O vídeo gerado com o personagem executando o movimento do vídeo de referência. |
