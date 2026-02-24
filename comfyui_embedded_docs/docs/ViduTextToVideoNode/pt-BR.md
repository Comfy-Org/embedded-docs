> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduTextToVideoNode/pt-BR.md)

O nó Vidu Text To Video Generation cria vídeos a partir de descrições textuais. Ele utiliza vários modelos de geração de vídeo para transformar seus prompts de texto em conteúdo de vídeo com configurações personalizáveis para duração, proporção de tela e estilo visual.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Sim | `vidu_q1`<br>*Outras opções de VideoModelName* | Nome do modelo (padrão: vidu_q1) |
| `prompt` | STRING | Sim | - | Uma descrição textual para a geração do vídeo |
| `duration` | INT | Não | 5-5 | Duração do vídeo de saída em segundos (padrão: 5) |
| `seed` | INT | Não | 0-2147483647 | Semente para a geração do vídeo (0 para aleatório) (padrão: 0) |
| `aspect_ratio` | COMBO | Não | `r_16_9`<br>*Outras opções de AspectRatio* | A proporção de tela do vídeo de saída (padrão: r_16_9) |
| `resolution` | COMBO | Não | `r_1080p`<br>*Outras opções de Resolution* | Os valores suportados podem variar conforme o modelo e a duração (padrão: r_1080p) |
| `movement_amplitude` | COMBO | Não | `auto`<br>*Outras opções de MovementAmplitude* | A amplitude de movimento dos objetos no quadro (padrão: auto) |

**Observação:** O campo `prompt` é obrigatório e não pode estar vazio. O parâmetro `duration` está atualmente fixo em 5 segundos.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O vídeo gerado com base no prompt de texto |
