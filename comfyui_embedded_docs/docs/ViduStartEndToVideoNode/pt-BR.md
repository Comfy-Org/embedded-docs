> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduStartEndToVideoNode/pt-BR.md)

O nó Vidu Start End To Video Generation cria um vídeo gerando quadros entre um quadro inicial e um quadro final. Ele usa um prompt de texto para orientar o processo de geração de vídeo e suporta vários modelos de vídeo com diferentes configurações de resolução e movimento. O nó valida que os quadros inicial e final têm proporções de aspecto compatíveis antes do processamento.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Sim | `"vidu_q1"`<br>[Outros valores de modelo do enum VideoModelName] | Nome do modelo (padrão: "vidu_q1") |
| `first_frame` | IMAGE | Sim | - | Quadro inicial |
| `end_frame` | IMAGE | Sim | - | Quadro final |
| `prompt` | STRING | Não | - | Uma descrição textual para a geração do vídeo |
| `duration` | INT | Não | 5-5 | Duração do vídeo de saída em segundos (padrão: 5, fixado em 5 segundos) |
| `seed` | INT | Não | 0-2147483647 | Semente para a geração do vídeo (0 para aleatório) (padrão: 0) |
| `resolution` | COMBO | Não | `"1080p"`<br>[Outros valores de resolução do enum Resolution] | Os valores suportados podem variar conforme o modelo e a duração (padrão: "1080p") |
| `movement_amplitude` | COMBO | Não | `"auto"`<br>[Outros valores de amplitude de movimento do enum MovementAmplitude] | A amplitude de movimento dos objetos no quadro (padrão: "auto") |

**Observação:** Os quadros inicial e final devem ter proporções de aspecto compatíveis (validado com tolerância de proporção min_rel=0.8, max_rel=1.25).

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O arquivo de vídeo gerado |
