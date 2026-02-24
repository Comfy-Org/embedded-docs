> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProFirstLastFrameNode/pt-BR.md)

Este nó utiliza o modelo Kling AI para gerar um vídeo. Ele requer uma imagem inicial e um prompt de texto. Opcionalmente, você pode fornecer uma imagem final ou até seis imagens de referência para orientar o conteúdo e o estilo do vídeo. O nó processa essas entradas para criar um vídeo com uma duração e resolução especificadas.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model_name` | COMBO | Sim | `"kling-video-o1"` | O modelo específico do Kling AI a ser usado para a geração do vídeo. |
| `prompt` | STRING | Sim | - | Um prompt de texto descrevendo o conteúdo do vídeo. Pode incluir descrições positivas e negativas. |
| `duration` | INT | Sim | 3 a 10 | A duração desejada do vídeo gerado, em segundos (padrão: 5). |
| `first_frame` | IMAGE | Sim | - | A imagem inicial para a sequência do vídeo. |
| `end_frame` | IMAGE | Não | - | Um quadro final opcional para o vídeo. Não pode ser usado simultaneamente com `reference_images`. |
| `reference_images` | IMAGE | Não | - | Até 6 imagens de referência adicionais. |
| `resolution` | COMBO | Não | `"1080p"`<br>`"720p"` | A resolução de saída para o vídeo gerado (padrão: "1080p"). |

**Restrições Importantes:**

* A entrada `end_frame` não pode ser usada ao mesmo tempo que a entrada `reference_images`.
* Se você não fornecer um `end_frame` ou qualquer `reference_images`, a `duration` só poderá ser definida como 5 ou 10 segundos.
* Todas as imagens de entrada (`first_frame`, `end_frame` e quaisquer `reference_images`) devem ter uma dimensão mínima de 300 pixels tanto em largura quanto em altura.
* A proporção de aspecto de todas as imagens de entrada deve estar entre 1:2,5 e 2,5:1.
* Um máximo de 6 imagens pode ser fornecido via entrada `reference_images`.
* O texto do `prompt` deve ter entre 1 e 2500 caracteres.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O arquivo de vídeo gerado. |
