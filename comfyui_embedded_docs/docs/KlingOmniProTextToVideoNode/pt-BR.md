Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProTextToVideoNode/en.md)

Este nó utiliza o modelo mais recente da Kling AI para gerar um vídeo a partir de uma descrição textual. Ele envia seu prompt para uma API remota e retorna o vídeo gerado. O nó permite controlar a duração, o formato, a qualidade do vídeo e até criar storyboards com múltiplas cenas.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model_name` | O modelo Kling específico a ser usado para geração de vídeo (padrão: `"kling-v3-omni"`). | COMBO | Sim | `"kling-v3-omni"`<br>`"kling-video-o1"` |
| `prompt` | Um prompt textual descrevendo o conteúdo do vídeo. Pode incluir descrições positivas e negativas. Ignorado quando storyboards estão habilitados. | STRING | Sim | 0 a 2500 caracteres |
| `aspect_ratio` | O formato ou dimensões do vídeo a ser gerado. | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `duration` | A duração do vídeo em segundos (padrão: 5). | INT | Sim | 3 a 15 segundos |
| `resolution` | A qualidade ou resolução em pixels do vídeo (padrão: `"1080p"`). | COMBO | Não | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `storyboards` | Gera uma série de segmentos de vídeo com prompts e durações individuais. Ignorado para o modelo o1. | DYNAMIC_COMBO | Não | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `gerar_áudio` | Se deve gerar áudio para o vídeo (padrão: Falso). | BOOLEAN | Não | Verdadeiro / Falso |
| `semente` | A semente controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente (padrão: 0). | INT | Não | 0 a 2147483647 |

### Restrições e Limitações dos Parâmetros

- **Limitações específicas do modelo:**
  - O modelo `kling-video-o1` suporta apenas durações de **5 ou 10 segundos**.
  - O modelo `kling-video-o1` **não** suporta geração de áudio.
  - O modelo `kling-video-o1` **não** suporta resolução 4k.
  - O modelo `kling-video-o1` **não** suporta storyboards.
- **Restrições de storyboard:**
  - Quando storyboards estão habilitados, o campo `prompt` é ignorado.
  - Cada storyboard requer seu próprio prompt (1 a 512 caracteres) e duração.
  - A duração total de todos os storyboards deve ser exatamente igual ao parâmetro global `duration`.
- **Requisitos do prompt:**
  - Quando storyboards estão **desabilitados**, o campo `prompt` é obrigatório (mínimo de 1 caractere).
  - Quando storyboards estão **habilitados**, o campo `prompt` pode ficar vazio (0 caracteres).

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | O vídeo gerado com base no prompt textual fornecido e nas configurações. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProTextToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `2f867e0bd2e7b0ec901a9ad8d2adcfe712ed479c1613b80f86af3a20863e9f4c`
