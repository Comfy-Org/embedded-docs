# Kling Quadro Inicial-Final para Vídeo

Este nó cria uma sequência de vídeo que faz a transição entre as imagens inicial e final fornecidas. Ele gera todos os quadros intermediários para produzir uma transformação suave do primeiro ao último quadro. Este nó chama a API de imagem para vídeo, mas suporta apenas as opções de entrada que funcionam com o campo de solicitação `image_tail`.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `start_frame` | Imagem de referência - URL ou string codificada em Base64, não pode exceder 10MB, resolução não inferior a 300*300px, proporção de aspecto entre 1:2.5 ~ 2.5:1. O Base64 não deve incluir o prefixo data:image. | IMAGE | Sim | - |
| `end_frame` | Imagem de referência - Controle do quadro final. URL ou string codificada em Base64, não pode exceder 10MB, resolução não inferior a 300*300px. O Base64 não deve incluir o prefixo data:image. | IMAGE | Sim | - |
| `prompt` | Prompt de texto positivo | STRING | Sim | - |
| `negative_prompt` | Prompt de texto negativo | STRING | Sim | - |
| `cfg_scale` | Controla a força da orientação do prompt (padrão: 0.5) | FLOAT | Não | 0.0-1.0 |
| `aspect_ratio` | A proporção de aspecto do vídeo gerado (padrão: "16:9") | COMBO | Não | "16:9"<br>"9:16"<br>"1:1" |
| `mode` | A configuração a ser usada para a geração do vídeo seguindo o formato: mode / duration / model_name. (padrão: "pro mode / 5s duration / kling-v2-5-turbo"). Todas as opções disponíveis usam o modo pro com o modelo kling-v2-5-turbo e diferem apenas na duração do vídeo. | COMBO | Não | "pro mode / 5s duration / kling-v2-5-turbo"<br>"pro mode / 10s duration / kling-v2-5-turbo" |

**Restrições de Imagem:**

- Tanto `start_frame` quanto `end_frame` devem ser fornecidos e não podem exceder 10MB de tamanho de arquivo
- Resolução mínima: 300×300 pixels para ambas as imagens
- A proporção de aspecto de `start_frame` deve estar entre 1:2.5 e 2.5:1
- Imagens codificadas em Base64 não devem incluir o prefixo "data:image"

**Restrições de Prompt:**

- O prompt positivo não deve estar vazio
- Tanto o prompt positivo quanto o negativo são limitados a 500 caracteres
- Se `negative_prompt` for deixado vazio, ele é omitido da solicitação

**Preços:**

- "pro mode / 5s duration / kling-v2-5-turbo": $0.35 USD por geração
- "pro mode / 10s duration / kling-v2-5-turbo": $0.70 USD por geração

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `output` | A sequência de vídeo gerada | VIDEO |
| `video_id` | Identificador exclusivo para o vídeo gerado | STRING |
| `duration` | Duração do vídeo gerado | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingStartEndFrameNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a27977226360a425614255f8330ce7fd8ba94b8c3020eb8fdddc01eb74f035c1`
