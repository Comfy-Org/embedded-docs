Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProImageToVideoNode/en.md)

Este nó utiliza o modelo Kling AI para gerar um vídeo com base em um prompt de texto e até sete imagens de referência. Ele permite controlar a proporção de aspecto, duração, resolução do vídeo e, opcionalmente, usar storyboards ou gerar áudio. O nó envia a solicitação para uma API externa e retorna o vídeo gerado.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model_name` | O modelo Kling específico a ser usado para geração de vídeo (padrão: "kling-v3-omni"). | COMBO | Sim | `"kling-v3-omni"`<br>`"kling-video-o1"` |
| `prompt` | Um prompt de texto descrevendo o conteúdo do vídeo. Pode incluir descrições positivas e negativas. O texto é normalizado automaticamente e deve ter entre 1 e 2500 caracteres. Ignorado quando storyboards estão habilitados. | STRING | Sim | - |
| `aspect_ratio` | A proporção de aspecto desejada para o vídeo gerado. | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `duration` | A duração do vídeo em segundos. O valor pode ser ajustado com um controle deslizante (padrão: 5). | INT | Sim | 3 a 15 |
| `reference_images` | Até 7 imagens de referência. Cada imagem deve ter no mínimo 300x300 pixels e uma proporção de aspecto entre 1:2,5 e 2,5:1. | IMAGE | Sim | - |
| `resolution` | A resolução de saída do vídeo. Este parâmetro é opcional (padrão: "1080p"). | COMBO | Não | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `storyboards` | Gera uma série de segmentos de vídeo com prompts e durações individuais. Suportado apenas para `kling-v3-omni`. Quando habilitado, o `prompt` global é ignorado e a duração total de todos os segmentos do storyboard deve ser igual à `duration` global. | DYNAMIC_COMBO | Não | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `gerar_áudio` | Gera áudio para o vídeo. Suportado apenas para `kling-v3-omni` (padrão: false). | BOOLEAN | Não | `true`<br>`false` |
| `semente` | A semente controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente (padrão: 0). | INT | Não | 0 a 2147483647 |

**Nota:** A entrada `reference_images` aceita no máximo 7 imagens. Se mais forem fornecidas, o nó gerará um erro. Cada imagem é validada quanto às dimensões mínimas e proporção de aspecto.

**Restrições específicas do modelo:**
- `kling-video-o1` não suporta durações maiores que 10 segundos.
- `kling-video-o1` não suporta geração de áudio.
- `kling-video-o1` não suporta resolução 4k.
- `kling-video-o1` não suporta storyboards.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProImageToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `80f4568be81b23c75bfff2bd3f21a61b242563c3c9fb1985a03e76ace24dceb2`
