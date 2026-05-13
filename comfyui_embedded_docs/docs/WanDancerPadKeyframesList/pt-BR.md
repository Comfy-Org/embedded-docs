> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerPadKeyframesList/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerPadKeyframesList/en.md)

## Visão Geral

Este nó recebe uma sequência de imagens e uma faixa de áudio opcional, e as divide em um número especificado de segmentos preenchidos. Ele foi projetado para preparar sequências de quadros-chave para geração de vídeo, onde cada segmento é preenchido com um comprimento consistente e uma máscara correspondente é criada para indicar quais quadros são válidos.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `images` | IMAGE | Sim | N/A | A sequência de imagens de entrada a ser dividida em segmentos. |
| `segment_length` | INT | Sim | 1 a 10000 | Comprimento de cada segmento em quadros (padrão: 149). |
| `num_segments` | INT | Sim | 1 a 100 | Quantos segmentos preenchidos emitir como listas (padrão: 1). |
| `audio` | AUDIO | Não | N/A | Áudio a ser fatiado para cada segmento emitido. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `keyframes_sequence` | IMAGE | Uma lista de sequências de quadros-chave preenchidas, uma para cada segmento. |
| `keyframes_mask` | MASK | Uma lista de máscaras indicando quadros válidos para cada segmento. |
| `audio_segment` | AUDIO | Uma lista de segmentos de áudio, um para cada segmento de vídeo. |

---
**Source fingerprint (SHA-256):** `c6a3ddca3fd61fcdb287fecb6969796eebd65e70f1174abdab57912586d27d00`
