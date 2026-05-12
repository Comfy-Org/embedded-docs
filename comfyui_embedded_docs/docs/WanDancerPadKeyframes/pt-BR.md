> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerPadKeyframes/pt-BR.md)

# Visão Geral

Este nó prepara uma sequência de quadros-chave para um segmento específico de um processo de geração de vídeo mais longo. Ele recebe um lote de imagens de entrada e uma faixa de áudio, calcula quantos quadros totais o vídeo completo deve ter com base na duração do áudio e distribui as imagens de entrada como quadros-chave no segmento escolhido, preenchendo o restante com quadros em branco. Ele também extrai a porção correspondente do áudio para aquele segmento.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `images` | IMAGE | Sim | Lote de imagens | As imagens de entrada a serem distribuídas como quadros-chave. |
| `segment_length` | INT | Sim | 1 a 10000 | Comprimento deste segmento em quadros (padrão: 149). |
| `segment_index` | INT | Sim | 0 a 100 | Qual segmento é este (0 para o primeiro, 1 para o segundo, etc., padrão: 0). |
| `audio` | AUDIO | Sim | Dados de áudio | Áudio para calcular o total de quadros de saída e extrair o áudio do segmento. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `keyframes_sequence` | IMAGE | Sequência de quadros-chave preenchida para o segmento especificado. |
| `keyframes_mask` | MASK | Máscara indicando quadros válidos (1 para posições de quadros-chave, 0 para posições preenchidas). |
| `audio_segment` | AUDIO | Segmento de áudio para este segmento de vídeo. |