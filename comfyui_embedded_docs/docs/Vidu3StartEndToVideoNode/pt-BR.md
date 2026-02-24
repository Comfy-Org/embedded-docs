> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3StartEndToVideoNode/pt-BR.md)

Este nó gera um vídeo interpolando entre um quadro inicial e um quadro final fornecidos, guiado por um prompt de texto. Ele utiliza o modelo Vidu Q3 para criar uma transição suave entre as duas imagens, produzindo um vídeo com uma duração e resolução especificadas.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Sim | `"viduq3-pro"`<br>`"viduq3-turbo"` | O modelo a ser usado para a geração do vídeo. Selecionar uma opção revela parâmetros de configuração adicionais para `resolution`, `duration` e `audio`. |
| `model.resolution` | COMBO | Sim | `"720p"`<br>`"1080p"` | Resolução do vídeo de saída. Este parâmetro é revelado após a seleção de um `model`. |
| `model.duration` | INT | Sim | 1 a 16 | Duração do vídeo de saída em segundos (padrão: 5). Este parâmetro é revelado após a seleção de um `model`. |
| `model.audio` | BOOLEAN | Sim | `True` / `False` | Quando habilitado, gera vídeo com som (incluindo diálogos e efeitos sonoros) (padrão: False). Este parâmetro é revelado após a seleção de um `model`. |
| `first_frame` | IMAGE | Sim | - | A imagem inicial para a sequência de vídeo. |
| `end_frame` | IMAGE | Sim | - | A imagem final para a sequência de vídeo. |
| `prompt` | STRING | Sim | - | Uma descrição textual que guia a geração do vídeo (máximo de 2000 caracteres). |
| `seed` | INT | Não | 0 a 2147483647 | Um valor de semente para controlar a aleatoriedade da geração (padrão: 1). |

**Observação:** As imagens `first_frame` e `end_frame` devem ter proporções (aspect ratios) semelhantes para resultados ideais.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `video` | VIDEO | O arquivo de vídeo gerado. |