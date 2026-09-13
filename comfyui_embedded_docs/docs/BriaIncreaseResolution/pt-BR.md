# Bria Aumentar Resolução

Bria Increase Resolution amplia a resolução de uma imagem de entrada em 2x ou 4x usando o serviço de ampliação de imagem da Bria, preservando o conteúdo original. O nó faz o upload da imagem, envia-a para processamento no serviço Bria, aguarda o resultado e retorna a imagem ampliada.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image` | A imagem de entrada a ser ampliada. | IMAGE | Sim | Imagem única |
| `desired_increase` | Multiplicador de resolução. A saída deve ter no máximo 8192 pixels em cada lado. | COMBO | Sim | "2"<br>"4" |
| `auto_downscale` | Reduz automaticamente o multiplicador e reduz a escala da imagem de entrada se isso ainda não for suficiente, quando a saída excederia o limite. (padrão: False) | BOOLEAN | Sim | True<br>False |
| `moderation` | Configurações de moderação. Quando definido como "true", habilita as subopções `visual_input_moderation` e `visual_output_moderation`, ambas com padrão False. | DYNAMIC_COMBO | Sim | "false"<br>"true" |

Notas:
- Quando `moderation` é definido como "true", as subopções `visual_input_moderation` e `visual_output_moderation` ficam disponíveis, ambas com padrão False. Elas controlam a moderação do conteúdo da imagem de entrada e da imagem de saída.
- O nó impõe um limite máximo de 8192 pixels por lado na saída. Se o multiplicador selecionado exceder esse limite e `auto_downscale` estiver desabilitado, um erro é gerado. Habilitar `auto_downscale` permite que o nó use automaticamente um multiplicador menor ou reduza a escala da imagem de entrada.
- A Bria primeiro amplia o lado menor da imagem de entrada para pelo menos 224 pixels antes da ampliação. Imagens muito alongadas podem gerar um erro solicitando que sejam cortadas para um formato mais quadrado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `IMAGE` | A imagem ampliada retornada pelo serviço Bria. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaIncreaseResolution/pt-BR.md)

---
**Source fingerprint (SHA-256):** `6db9bf6c0d8a79903893b352658d3a8e02f67d375f3d604e9ab2a69624142885`
