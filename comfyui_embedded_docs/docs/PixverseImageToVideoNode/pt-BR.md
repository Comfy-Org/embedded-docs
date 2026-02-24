> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseImageToVideoNode/pt-BR.md)

Gera vídeos com base em uma imagem de entrada e um prompt de texto. Este nó recebe uma imagem e cria um vídeo animado aplicando as configurações de movimento e qualidade especificadas para transformar a imagem estática em uma sequência em movimento.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sim | - | Imagem de entrada a ser transformada em vídeo |
| `prompt` | STRING | Sim | - | Prompt para a geração do vídeo |
| `quality` | COMBO | Sim | `res_540p`<br>`res_1080p` | Configuração da qualidade do vídeo (padrão: res_540p) |
| `duration_seconds` | COMBO | Sim | `dur_2`<br>`dur_5`<br>`dur_10` | Duração do vídeo gerado em segundos |
| `motion_mode` | COMBO | Sim | `normal`<br>`fast`<br>`slow`<br>`zoom_in`<br>`zoom_out`<br>`pan_left`<br>`pan_right`<br>`pan_up`<br>`pan_down`<br>`tilt_up`<br>`tilt_down`<br>`roll_clockwise`<br>`roll_counterclockwise` | Estilo de movimento aplicado à geração do vídeo |
| `seed` | INT | Sim | 0-2147483647 | Semente para a geração do vídeo (padrão: 0) |
| `negative_prompt` | STRING | Não | - | Uma descrição textual opcional de elementos indesejados na imagem |
| `pixverse_template` | CUSTOM | Não | - | Um modelo opcional para influenciar o estilo da geração, criado pelo nó PixVerse Template |

**Observação:** Ao usar a qualidade 1080p, o modo de movimento é automaticamente definido como normal e a duração é limitada a 5 segundos. Para durações diferentes de 5 segundos, o modo de movimento também é automaticamente definido como normal.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | Vídeo gerado com base na imagem de entrada e nos parâmetros |
