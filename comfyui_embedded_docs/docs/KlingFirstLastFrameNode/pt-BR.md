> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingFirstLastFrameNode/pt-BR.md)

Este nó utiliza o modelo Kling 3.0 para gerar um vídeo. Ele cria o vídeo com base em um prompt de texto, uma duração especificada e duas imagens fornecidas: um quadro inicial e um quadro final. O nó também pode gerar áudio de acompanhamento para o vídeo.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sim | N/A | A descrição textual que orienta a geração do vídeo. Deve ter entre 1 e 2500 caracteres. |
| `duration` | INT | Não | 3 a 15 | A duração do vídeo em segundos (padrão: 5). |
| `first_frame` | IMAGE | Sim | N/A | A imagem inicial para o vídeo. Deve ter pelo menos 300x300 pixels e uma proporção de aspecto entre 1:2,5 e 2,5:1. |
| `end_frame` | IMAGE | Sim | N/A | A imagem final para o vídeo. Deve ter pelo menos 300x300 pixels e uma proporção de aspecto entre 1:2,5 e 2,5:1. |
| `generate_audio` | BOOLEAN | Não | N/A | Controla se o áudio deve ser gerado para o vídeo (padrão: Verdadeiro). |
| `model` | COMBO | Não | `"kling-v3"` | Modelo e configurações de geração. Selecionar esta opção revela um parâmetro aninhado `resolution`. |
| `model.resolution` | COMBO | Não | `"1080p"`<br>`"720p"` | A resolução para o vídeo gerado. Este parâmetro está disponível apenas quando `model` está definido como `"kling-v3"`. |
| `seed` | INT | Não | 0 a 2147483647 | Um número usado para controlar se o nó deve ser executado novamente. Os resultados são não determinísticos, independentemente do valor da semente (padrão: 0). |

**Observação:** As imagens `first_frame` e `end_frame` devem atender aos requisitos mínimos de tamanho e proporção de aspecto especificados para que o nó funcione corretamente.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O arquivo de vídeo gerado. |
