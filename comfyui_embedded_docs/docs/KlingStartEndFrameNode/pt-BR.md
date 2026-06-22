# Kling Quadro Inicial-Final para Vídeo

O nó Kling Start-End Frame to Video cria uma sequência de vídeo que faz a transição entre as imagens inicial e final fornecidas. Ele gera todos os quadros intermediários para produzir uma transformação suave do primeiro ao último quadro. Este nó utiliza a API de imagem para vídeo, mas suporta apenas as opções de entrada compatíveis com o campo de requisição `image_tail`.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `start_frame` | Imagem de referência - URL ou string codificada em Base64, não pode exceder 10MB, resolução mínima de 300×300px, proporção entre 1:2,5 ~ 2,5:1. Base64 não deve incluir o prefixo data:image. | IMAGE | Sim | - |
| `end_frame` | Imagem de referência - Controle do quadro final. URL ou string codificada em Base64, não pode exceder 10MB, resolução mínima de 300×300px. Base64 não deve incluir o prefixo data:image. | IMAGE | Sim | - |
| `prompt` | Prompt de texto positivo | STRING | Sim | - |
| `negative_prompt` | Prompt de texto negativo | STRING | Sim | - |
| `cfg_scale` | Controla a intensidade da orientação do prompt (padrão: 0,5) | FLOAT | Não | 0,0-1,0 |
| `aspect_ratio` | Proporção de aspecto do vídeo gerado (padrão: "16:9") | COMBO | Não | "16:9"<br>"9:16"<br>"1:1" |
| `mode` | Configuração a ser usada para geração do vídeo seguindo o formato: modo / duração / nome_do_modelo. (padrão: a sétima opção dos modos disponíveis) | COMBO | Não | Múltiplas opções disponíveis |

**Restrições das Imagens:**

- Tanto `start_frame` quanto `end_frame` devem ser fornecidos e não podem exceder 10MB de tamanho
- Resolução mínima: 300×300 pixels para ambas as imagens
- A proporção de aspecto do `start_frame` deve estar entre 1:2,5 e 2,5:1
- Imagens codificadas em Base64 não devem incluir o prefixo "data:image"

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | A sequência de vídeo gerada | VIDEO |
| `video_id` | Identificador único para o vídeo gerado | STRING |
| `duration` | Duração do vídeo gerado | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingStartEndFrameNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1df5820b4f41ccd5afec8e2701888d90c940f164c433c7f81397b41e8fc333c6`
