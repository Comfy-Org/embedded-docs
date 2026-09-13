# YuE2 Gerar Música

Gera tokens de música e condicionamento acústico a partir de um estilo, letras e uma notação ABC. Retorna o condicionamento e a duração gerada em segundos, que deve ser fornecida ao nó Empty YuE2 Latent Audio. Se a entrada ABC for deixada vazia, o modo selecionado é ignorado e o modo off é usado automaticamente.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `clip` | O modelo CLIP usado para tokenizar e codificar as entradas musicais. | CLIP | Sim | - |
| `style` | Texto descrevendo o estilo musical. Suporta entrada multilinha e prompts dinâmicos. | STRING | Sim | Texto multilinha |
| `lyrics` | Letras para a música gerada. Suporta entrada multilinha e prompts dinâmicos. | STRING | Sim | Texto multilinha |
| `abc` | Conecte o gerador ABC ou forneça uma partitura editada. Deixe vazio para usar o modo off automaticamente. padrão: "" | STRING | Sim | Texto multilinha |
| `seed` | Semente aleatória para geração. padrão: 0 | INT | Sim | 0 a 18446744073709551615 |
| `mode` | full: gera melodia e acordes; melody: gera apenas melodia, recomendado para covers. padrão: "full" | COMBO | Sim | "full"<br>"melody" |
| `max_duration` | Duração máxima em segundos. Reduzida automaticamente para prompts longos; a geração pode parar mais cedo. padrão: 360.0 | FLOAT | Sim | 0.04 a 900.0 |
| `temperature` | Temperatura de amostragem para geração. padrão: 1.0 (avançado) | FLOAT | Sim | 0.0 a 5.0 |
| `top_p` | Limite de probabilidade da amostragem de núcleo. padrão: 0.95 (avançado) | FLOAT | Sim | 0.01 a 1.0 |
| `top_k` | Limite de amostragem top-k. padrão: 100 (avançado) | INT | Sim | 1 a 32768 |
| `repetition_penalty` | Penalidade aplicada a tokens repetidos. padrão: 1.2 (avançado) | FLOAT | Sim | 0.01 a 10.0 |

Nota: Se `abc` estiver vazio ou contiver apenas espaços em branco, a seleção de `mode` é ignorada e o modo off é usado automaticamente.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `CONDITIONING` | Condicionamento acústico gerado a partir dos tokens de música. | CONDITIONING |
| `seconds` | A duração do áudio gerado em segundos. Forneça este valor ao nó Empty YuE2 Latent Audio. | FLOAT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/YuE2GenerateMusic/pt-BR.md)

---
**Source fingerprint (SHA-256):** `54f5d46cf083726bdf97c86e5683b2727840f75bb553bddf9525cfbf5affa44c`
