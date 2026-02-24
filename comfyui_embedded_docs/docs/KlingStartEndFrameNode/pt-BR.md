> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingStartEndFrameNode/pt-BR.md)

O nó Kling Start-End Frame to Video cria uma sequência de vídeo que faz uma transição entre as imagens de início e fim fornecidas. Ele gera todos os quadros intermediários para produzir uma transformação suave do primeiro ao último quadro. Este nó chama a API de imagem para vídeo, mas suporta apenas as opções de entrada que funcionam com o campo de requisição `image_tail`.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `start_frame` | IMAGE | Sim | - | Imagem de Referência - URL ou string codificada em Base64, não pode exceder 10MB, resolução não inferior a 300*300px, proporção de aspecto entre 1:2.5 ~ 2.5:1. Base64 não deve incluir o prefixo data:image. |
| `end_frame` | IMAGE | Sim | - | Imagem de Referência - Controle do quadro final. URL ou string codificada em Base64, não pode exceder 10MB, resolução não inferior a 300*300px. Base64 não deve incluir o prefixo data:image. |
| `prompt` | STRING | Sim | - | Prompt de texto positivo |
| `negative_prompt` | STRING | Sim | - | Prompt de texto negativo |
| `cfg_scale` | FLOAT | Não | 0.0-1.0 | Controla a força da orientação do prompt (padrão: 0.5) |
| `aspect_ratio` | COMBO | Não | "16:9"<br>"9:16"<br>"1:1"<br>"21:9"<br>"9:21"<br>"3:4"<br>"4:3" | A proporção de aspecto para o vídeo gerado (padrão: "16:9") |
| `mode` | COMBO | Não | Múltiplas opções disponíveis | A configuração a ser usada para a geração do vídeo, seguindo o formato: modo / duração / nome_do_modelo. (padrão: terceira opção dentre os modos disponíveis) |

**Restrições das Imagens:**

- Tanto `start_frame` quanto `end_frame` devem ser fornecidos e não podem exceder 10MB de tamanho de arquivo
- Resolução mínima: 300×300 pixels para ambas as imagens
- A proporção de aspecto de `start_frame` deve estar entre 1:2.5 e 2.5:1
- Imagens codificadas em Base64 não devem incluir o prefixo "data:image"

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | A sequência de vídeo gerada |
| `video_id` | STRING | Identificador único para o vídeo gerado |
| `duration` | STRING | Duração do vídeo gerado |
