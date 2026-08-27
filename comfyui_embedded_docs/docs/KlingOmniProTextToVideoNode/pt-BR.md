# Kling Omni Texto para Vídeo (Pro)

Este nó usa o modelo mais recente da Kling AI para gerar um vídeo a partir de uma descrição de texto. Ele envia seu prompt para uma API remota e retorna o vídeo gerado. O nó permite controlar a duração, o formato, a qualidade do vídeo e até criar storyboards de múltiplas cenas.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model_name` | O modelo Kling específico a ser usado para geração de vídeo (padrão: `"kling-v3-omni"`). | COMBO | Sim | `"kling-v3-omni"`<br>`"kling-video-o1"` |
| `prompt` | Um prompt de texto descrevendo o conteúdo do vídeo. Pode incluir descrições positivas e negativas. Ignorado quando os storyboards estão habilitados. | STRING | Sim | 0 a 2500 caracteres |
| `aspect_ratio` | A forma ou as dimensões do vídeo a ser gerado. | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `duration` | A duração do vídeo em segundos (padrão: 5). | INT | Sim | 3 a 15 segundos |
| `resolution` | A qualidade ou resolução de pixels do vídeo (padrão: `"1080p"`). Internamente mapeia para qualidade padrão, pro ou 4k. | COMBO | Não | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `storyboards` | Gera uma série de segmentos de vídeo com prompts e durações individuais. Ignorado para o modelo o1. | DYNAMIC_COMBO | Não | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `gerar_áudio` | Se deve gerar áudio para o vídeo (padrão: False). | BOOLEAN | Não | True / False |
| `semente` | A seed controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da seed (padrão: 0). | INT | Não | 0 a 2147483647 |

### Sub-entradas de Storyboard

Quando `storyboards` estiver definido para um valor diferente de `"disabled"`, as seguintes entradas aparecem para cada segmento de storyboard. Nos nomes de parâmetros abaixo, `{i}` é o número do segmento, de 1 até a quantidade selecionada de storyboards.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `storyboard_{i}_prompt` | Prompt para o segmento de storyboard {i}. Máximo de 512 caracteres. | STRING | Sim | 1 a 512 caracteres |
| `storyboard_{i}_duration` | Duração para o segmento de storyboard {i} em segundos (padrão: 4). | INT | Sim | 1 a 15 segundos |

### Restrições e Limitações dos Parâmetros

- **Limitações específicas do modelo:**
  - O modelo `kling-video-o1` suporta apenas durações de **5 ou 10 segundos**.
  - O modelo `kling-video-o1` **não** suporta geração de áudio.
  - O modelo `kling-video-o1` **não** suporta resolução 4k.
  - O modelo `kling-video-o1` **não** suporta storyboards.
- **Restrições de storyboard:**
  - Quando os storyboards estão habilitados, o campo `prompt` é ignorado.
  - Cada storyboard requer seu próprio prompt (1 a 512 caracteres) e duração.
  - A duração total de todos os storyboards deve ser exatamente igual ao parâmetro global `duration`.
- **Requisitos de prompt:**
  - Quando os storyboards estão **desabilitados**, o campo `prompt` é obrigatório (mínimo de 1 caractere).
  - Quando os storyboards estão **habilitados**, o campo `prompt` pode ficar vazio (0 caracteres).

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | O vídeo gerado com base no prompt de texto fornecido e nas configurações. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProTextToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d2fbbe7c6aae283eb3fa7f73d788b809098a9a4dd6e8ada54697d43fd5bf10f2`
