# Grok Video

O nó Grok Video gera um vídeo curto a partir de uma descrição em texto. Ele pode criar um vídeo do zero usando um prompt, ou animar uma única imagem de entrada, opcionalmente guiada por um prompt. O nó envia uma solicitação para uma API externa e retorna o vídeo gerado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo a ser usado para a geração de vídeo. | COMBO | Sim | "grok-imagine-video"<br>"grok-imagine-video-1.5" |
| `prompt` | Descrição em texto do vídeo desejado. Opcional para grok-imagine-video-1.5 quando uma imagem de entrada é fornecida. | STRING | Sim | - |
| `resolution` | A resolução do vídeo de saída. 1080p está disponível apenas para grok-imagine-video-1.5. | COMBO | Sim | "480p"<br>"720p"<br>"1080p" |
| `aspect_ratio` | A proporção de aspecto do vídeo de saída (padrão: "auto"). | COMBO | Sim | "auto"<br>"16:9"<br>"4:3"<br>"3:2"<br>"1:1"<br>"2:3"<br>"3:4"<br>"9:16" |
| `duration` | A duração do vídeo de saída em segundos (padrão: 6). | INT | Sim | 1 a 15 |
| `seed` | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos independentemente da semente (padrão: 0). | INT | Sim | 0 a 2147483647 |
| `image` | Imagem inicial opcional. Se omitida, o vídeo é gerado apenas a partir do prompt de texto. | IMAGE | Não | - |

**Observação:**
- A resolução "1080p" está disponível apenas com o modelo `grok-imagine-video-1.5`. Selecioná-la com `grok-imagine-video` gera um erro.
- Apenas uma imagem de entrada é suportada. Fornecer várias imagens gera um erro.
- O `prompt` é obrigatório, a menos que o modelo seja definido como `grok-imagine-video-1.5` e uma imagem de entrada seja fornecida. Quando obrigatório, o prompt deve ter pelo menos 1 caractere após a remoção de espaços em branco.
- A `seed` apenas determina se o nó é executado novamente; os resultados gerados são não determinísticos independentemente do valor da semente.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | O vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c708c8cd78749aa533db63e2bc5938ef14fa78cf95f8ba4628d0c586f8723297`
