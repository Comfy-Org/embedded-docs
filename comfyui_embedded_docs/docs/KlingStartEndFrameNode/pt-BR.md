# Kling Quadro Inicial-Final para Vídeo

Este nó cria uma sequência de vídeo que faz a transição entre as imagens inicial e final fornecidas. Ele gera todos os quadros intermediários para produzir uma transformação suave do primeiro ao último quadro. Este nó chama a API de imagem para vídeo, mas suporta apenas as opções de entrada que funcionam com o campo de solicitação `image_tail`.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `start_frame` | Imagem de referência - URL ou string codificada em Base64, não pode exceder 10MB, resolução mínima de 300×300px, proporção de aspecto entre 1:2.5 e 2.5:1. O Base64 não deve incluir o prefixo data:image. | IMAGE | Sim | - |
| `end_frame` | Imagem de referência - Controle do quadro final. URL ou string codificada em Base64, não pode exceder 10MB, resolução mínima de 300×300px. O Base64 não deve incluir o prefixo data:image. | IMAGE | Sim | - |
| `prompt` | Prompt de texto positivo. Não deve estar vazio e não pode exceder 500 caracteres. | STRING | Sim | - |
| `negative_prompt` | Prompt de texto negativo. Não pode exceder 500 caracteres. Se ficar vazio, é omitido da solicitação. | STRING | Sim | - |
| `cfg_scale` | Controla a intensidade da orientação do prompt (padrão: 0.5) | FLOAT | Sim | 0.0-1.0 |
| `aspect_ratio` | A proporção de aspecto para o vídeo gerado (padrão: "16:9") | COMBO | Sim | "16:9"<br>"9:16"<br>"1:1" |
| `mode` | A configuração a ser usada para a geração de vídeo seguindo o formato: modo / duração / nome_do_modelo. (padrão: "pro mode / 5s duration / kling-v2-5-turbo") | COMBO | Sim | "pro mode / 5s duration / kling-v2-5-turbo"<br>"pro mode / 10s duration / kling-v2-5-turbo" |

**Restrições das Imagens:**

- Tanto `start_frame` quanto `end_frame` são obrigatórios e não podem exceder 10MB de tamanho de arquivo.
- Resolução mínima: 300×300 pixels para ambas as imagens.
- A proporção de aspecto do `start_frame` deve estar entre 1:2.5 e 2.5:1.
- Imagens codificadas em Base64 não devem incluir o prefixo "data:image".

**Restrições do Prompt:**

- `prompt` não deve estar vazio e não pode exceder 500 caracteres.
- `negative_prompt` não pode exceder 500 caracteres; quando vazio, não é enviado na solicitação.

**Notas sobre o Modo:**

- Ambas as opções de modo usam o pro mode com o modelo kling-v2-5-turbo e diferem apenas na duração (5 segundos ou 10 segundos).
- Preço por geração, conforme exibido no selo de preço do nó: o modo de 5s custa $0.35 USD e o modo de 10s custa $0.70 USD.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | A sequência de vídeo gerada | VIDEO |
| `video_id` | Identificador único do vídeo gerado | STRING |
| `duration` | Duração do vídeo gerado | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingStartEndFrameNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a27977226360a425614255f8330ce7fd8ba94b8c3020eb8fdddc01eb74f035c1`
