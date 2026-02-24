> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduImageToVideoNode/pt-BR.md)

O nó Vidu Image To Video Generation cria vídeos a partir de uma imagem inicial e de uma descrição textual opcional. Ele utiliza modelos de IA para gerar conteúdo de vídeo que se estende a partir do quadro de imagem fornecido. O nó envia a imagem e os parâmetros para um serviço externo e retorna o vídeo gerado.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Sim | `vidu_q1`<br>*Outras opções de VideoModelName* | Nome do modelo (padrão: vidu_q1) |
| `image` | IMAGE | Sim | - | Uma imagem a ser usada como quadro inicial do vídeo gerado |
| `prompt` | STRING | Não | - | Uma descrição textual para a geração do vídeo (padrão: vazio) |
| `duration` | INT | Não | 5-5 | Duração do vídeo de saída em segundos (padrão: 5, fixado em 5 segundos) |
| `seed` | INT | Não | 0-2147483647 | Semente para a geração do vídeo (0 para aleatório) (padrão: 0) |
| `resolution` | COMBO | Não | `r_1080p`<br>*Outras opções de Resolution* | Os valores suportados podem variar conforme o modelo e a duração (padrão: r_1080p) |
| `movement_amplitude` | COMBO | Não | `auto`<br>*Outras opções de MovementAmplitude* | A amplitude de movimento dos objetos no quadro (padrão: auto) |

**Restrições:**

- Apenas uma imagem de entrada é permitida (não pode processar múltiplas imagens)
- A imagem de entrada deve ter uma proporção de aspecto entre 1:4 e 4:1

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O vídeo gerado na saída |
