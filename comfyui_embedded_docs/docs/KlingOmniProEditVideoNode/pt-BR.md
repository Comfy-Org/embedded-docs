> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProEditVideoNode/pt-BR.md)

O nó Kling Omni Edit Video (Pro) utiliza um modelo de IA para editar um vídeo existente com base em uma descrição textual. Você fornece um vídeo de origem e um prompt, e o nó gera um novo vídeo com a mesma duração contendo as alterações solicitadas. Ele pode, opcionalmente, usar imagens de referência para orientar o estilo e manter o áudio original do vídeo de origem.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model_name` | COMBO | Sim | `"kling-video-o1"` | O modelo de IA a ser usado para a edição de vídeo. |
| `prompt` | STRING | Sim | | Um prompt de texto descrevendo o conteúdo do vídeo. Pode incluir descrições positivas e negativas. |
| `video` | VIDEO | Sim | | Vídeo a ser editado. A duração do vídeo de saída será a mesma. |
| `keep_original_sound` | BOOLEAN | Sim | | Determina se o áudio original do vídeo de entrada é mantido na saída (padrão: Verdadeiro). |
| `reference_images` | IMAGE | Não | | Até 4 imagens de referência adicionais. |
| `resolution` | COMBO | Não | `"1080p"`<br>`"720p"` | A resolução para o vídeo de saída (padrão: "1080p"). |

**Restrições e Limitações:**

* O `prompt` deve ter entre 1 e 2500 caracteres.
* O `video` de entrada deve ter uma duração entre 3,0 e 10,05 segundos.
* As dimensões do `video` de entrada devem estar entre 720x720 e 2160x2160 pixels.
* Um máximo de 4 `reference_images` pode ser fornecido quando um vídeo é usado.
* Cada `reference_image` deve ter pelo menos 300x300 pixels.
* Cada `reference_image` deve ter uma proporção de aspecto entre 1:2,5 e 2,5:1.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `video` | VIDEO | O vídeo editado gerado pelo modelo de IA. |
