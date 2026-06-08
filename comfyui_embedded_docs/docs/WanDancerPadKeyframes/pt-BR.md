## Visão Geral

Este nó prepara uma sequência de quadros-chave para um segmento específico de um processo de geração de vídeo mais longo. Ele recebe um lote de imagens de entrada e uma faixa de áudio, calcula quantos quadros totais o vídeo completo deve ter com base na duração do áudio e distribui as imagens de entrada como quadros-chave no segmento escolhido, preenchendo o restante com quadros em branco. Ele também extrai a porção correspondente do áudio para aquele segmento.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `imagens` | As imagens de entrada a serem distribuídas como quadros-chave. | IMAGE | Sim | Lote de imagens |
| `comprimento_do_segmento` | Comprimento deste segmento em quadros (padrão: 149). | INT | Sim | 1 a 10000 |
| `índice_do_segmento` | Qual segmento é este (0 para o primeiro, 1 para o segundo, etc., padrão: 0). | INT | Sim | 0 a 100 |
| `áudio` | Áudio para calcular o total de quadros de saída e extrair o áudio do segmento. | AUDIO | Sim | Dados de áudio |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `keyframes_sequence` | Sequência de quadros-chave preenchida para o segmento especificado. | IMAGE |
| `keyframes_mask` | Máscara indicando quadros válidos (1 para posições de quadros-chave, 0 para posições preenchidas). | MASK |
| `audio_segment` | Segmento de áudio para este segmento de vídeo. | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerPadKeyframes/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5a104b45faaa870727d4c45e6327e7233110b40dc5a13515a29e5f14de2050e0`
