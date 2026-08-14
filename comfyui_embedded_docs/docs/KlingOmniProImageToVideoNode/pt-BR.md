# Kling Omni Imagem para Vídeo (Pro)

Este nó usa o modelo Kling AI para gerar um vídeo com base em um prompt de texto e até sete imagens de referência. Ele permite controlar a proporção de aspecto, a duração e a resolução do vídeo e, opcionalmente, usar storyboards ou gerar áudio. O nó envia a solicitação para uma API externa e retorna o vídeo gerado.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model_name` | O modelo Kling específico a ser usado para geração de vídeo (padrão: "kling-v3-omni"). | COMBO | Sim | `"kling-v3-omni"`<br>`"kling-video-o1"` |
| `prompt` | Um prompt de texto descrevendo o conteúdo do vídeo. Pode incluir descrições positivas e negativas. Marcadores como `@image` ou `@video` (opcionalmente numerados) são convertidos automaticamente para o formato compatível com a API. Deve ter entre 1 e 2500 caracteres (pode ficar vazio quando storyboards estão habilitados). Ignorado quando storyboards estão habilitados. | STRING | Sim | - |
| `aspect_ratio` | A proporção de aspecto desejada para o vídeo gerado. | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `duration` | A duração do vídeo em segundos, ajustada com um controle deslizante (padrão: 5). | INT | Sim | 3 a 15 |
| `reference_images` | Até 7 imagens de referência. Cada imagem deve ter pelo menos 300x300 pixels e uma proporção de aspecto entre 1:2.5 e 2.5:1. | IMAGE | Sim | 1 a 7 imagens |
| `resolution` | A resolução de saída do vídeo (padrão: "1080p"). | COMBO | Não | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `storyboards` | Gera uma série de segmentos de vídeo com prompts e durações individuais. Suportado apenas para `kling-v3-omni`. Quando habilitado, o `prompt` global é ignorado, e a duração total de todos os segmentos de storyboard deve ser igual à duração global (padrão: "disabled"). | COMBO | Não | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `generate_audio` | Gera áudio para o vídeo. Suportado apenas para `kling-v3-omni` (padrão: false). | BOOLEAN | Não | `true`<br>`false` |
| `seed` | A seed controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da seed (padrão: 0). | INT | Não | 0 a 2147483647 |

### Entradas de Storyboard

Quando `storyboards` está habilitado, as seguintes entradas aparecem para cada segmento de storyboard selecionado. N varia de 1 até o número selecionado de storyboards.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `storyboard_N_prompt` | Prompt para o segmento de storyboard N. Máximo de 512 caracteres. | STRING | Não | 1 a 512 caracteres |
| `storyboard_N_duration` | Duração para o segmento de storyboard N em segundos (padrão: 4). | INT | Não | 1 a 15 |

**Nota:** A entrada `reference_images` aceita um máximo de 7 imagens. Se mais forem fornecidas, o nó gera um erro. Cada imagem é validada quanto às dimensões mínimas e à proporção de aspecto.

**Restrições específicas do modelo:**
- `kling-video-o1` não suporta durações maiores que 10 segundos.
- `kling-video-o1` não suporta geração de áudio.
- `kling-video-o1` não suporta resolução 4k.
- `kling-video-o1` não suporta storyboards.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProImageToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ccf7881065d2a365cdaa0e164b8b1d46c67985067866ab0fe91d492a62015f07`
