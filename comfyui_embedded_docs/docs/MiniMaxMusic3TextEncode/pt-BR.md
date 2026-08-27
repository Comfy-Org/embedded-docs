# MiniMaxMusic3TextEncode

MiniMax Music3 Text Encode usa um modelo CLIP MiniMax Music3 para converter legendas de texto e letras em uma sequência de condicionamento acústico para geração de música. O nó retorna os dados de CONDITIONING resultantes, juntamente com a duração real do áudio em segundos calculada a partir da duração máxima de entrada.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `clip` | O modelo CLIP MiniMax Music3, usado para codificação de texto e geração de sequência de condicionamento. | CLIP | Sim | - |
| `caption` | Texto que descreve a música a ser gerada. Suporta texto multilinha e prompts dinâmicos. | STRING | Sim | - |
| `letras` | O texto da letra a ser usado para gerar a música. Suporta texto multilinha e prompts dinâmicos. | STRING | Sim | - |
| `semente` | Semente aleatória reproduzível para o processo de geração. Padrão: 0. | INT | Sim | 0 a 18446744073709551615 (0xffffffffffffffff) |
| `max_duration` | Duração máxima em segundos; o modelo pode encerrar a música antes. Padrão: 120.0. | FLOAT | Sim | 0.04 até a duração máxima de áudio do modelo (MAX_AUDIO_FRAMES / AUDIO_FRAMES_PER_SECOND), passo 0.04 |
| `cfg_scale` | Escala de orientação sem classificador. Padrão: constante do modelo CFG_SCALE. Parâmetro avançado. | FLOAT | Sim | 0.0 a 100.0, passo 0.1 (mantém 2 casas decimais) |
| `top_k` | Valor de amostragem top-k usado para seleção de tokens acústicos. Padrão: constante do modelo CFG_TOP_K. Parâmetro avançado. | INT | Sim | 1 até o tamanho do vocabulário do modelo (C0_VOCAB_SIZE) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-------------|---------------|
| `conditioning` | A sequência de condicionamento acústico gerada, usada para orientar a geração subsequente de música. | CONDITIONING |
| `segundos` | A duração real da sequência de condicionamento, em segundos. | FLOAT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxMusic3TextEncode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c3fbfd189d0358ebf081dd4f9c32be9231a9d0b97fd767401ea4b7955224c25c`
