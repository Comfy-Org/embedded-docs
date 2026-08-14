# MiniMaxMusic3TextEncode

O nó MiniMax Music3 Text Encode usa o modelo MiniMax Music3 CLIP para converter descrições textuais e letras em sequências de condicionamento acústico para geração de música. Este nó retorna os dados CONDITIONING convertidos, bem como a duração real em segundos calculada com base no tempo de entrada.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `clip` | Modelo MiniMax Music3 CLIP usado para codificação de texto e geração de sequências de condicionamento. | CLIP | Sim | - |
| `caption` | Descrição textual do conteúdo musical a ser gerado. Suporta texto multilinha e prompts dinâmicos. | STRING | Sim | - |
| `lyrics` | Texto da letra a ser usado na geração musical. Suporta texto multilinha e prompts dinâmicos. | STRING | Sim | - |
| `seed` | Semente aleatória reprodutível para o processo de geração. Valor padrão: 0. | INT | Sim | 0 a 18446744073709551615 (0xffffffffffffffff) |
| `max_duration` | Duração máxima (em segundos) para a música gerada; o modelo pode encerrar a música antes do tempo. Valor padrão: 120.0. | FLOAT | Sim | 0.04 até a duração máxima de áudio do modelo (MAX_AUDIO_FRAMES / AUDIO_FRAMES_PER_SECOND), passo 0.04 |
| `cfg_scale` | Escala de orientação livre do classificador. Valor padrão: constante do modelo CFG_SCALE. Parâmetro avançado. | FLOAT | Sim | 0.0 a 100.0, passo 0.1 (preserva 2 casas decimais) |
| `top_k` | Valor de amostragem top-k para seleção de tokens acústicos. Valor padrão: constante do modelo CFG_TOP_K. Parâmetro avançado. | INT | Sim | 1 ao tamanho do vocabulário do modelo (C0_VOCAB_SIZE) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `conditioning` | Sequência de condicionamento acústico gerada, usada para orientar a geração musical subsequente. | CONDITIONING |
| `seconds` | Duração real correspondente à sequência de condicionamento, em segundos. | FLOAT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxMusic3TextEncode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c3fbfd189d0358ebf081dd4f9c32be9231a9d0b97fd767401ea4b7955224c25c`
