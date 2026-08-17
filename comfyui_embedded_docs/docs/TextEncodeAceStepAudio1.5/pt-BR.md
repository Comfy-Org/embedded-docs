# TextEncodeAceStepAudio1.5

O nó TextEncodeAceStepAudio1.5 prepara metadados de texto e áudio para uso com o modelo AceStepAudio 1.5. Ele recebe tags descritivas, letras e parâmetros musicais e, em seguida, usa um modelo CLIP para convertê-los em um formato de condicionamento adequado para a geração de áudio.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `clip` | O modelo CLIP usado para tokenizar e codificar o texto de entrada. | CLIP | Sim | N/A |
| `tags` | Tags descritivas para o áudio, como gênero, clima ou instrumentos. Suporta entrada multilinha e prompts dinâmicos. | STRING | Sim | N/A |
| `lyrics` | A letra da faixa de áudio. Suporta entrada multilinha e prompts dinâmicos. | STRING | Sim | N/A |
| `seed` | Um valor de seed aleatório para geração reproduzível. Possui um widget control_after_generate. Padrão: 0. | INT | Não | 0 a 18446744073709551615 |
| `bpm` | Os batimentos por minuto (BPM) do áudio gerado. Padrão: 120. | INT | Não | 10 a 300 |
| `duration` | A duração desejada do áudio em segundos. Padrão: 120.0. | FLOAT | Não | 0.0 a 2000.0 |
| `timesignature` | A fórmula de compasso musical. | COMBO | Não | `"2"`<br>`"3"`<br>`"4"`<br>`"6"` |
| `language` | O idioma do texto de entrada. Padrão: "en". | COMBO | Não | `"ar"`<br>`"az"`<br>`"bg"`<br>`"bn"`<br>`"ca"`<br>`"cs"`<br>`"da"`<br>`"de"`<br>`"el"`<br>`"en"`<br>`"es"`<br>`"fa"`<br>`"fi"`<br>`"fr"`<br>`"he"`<br>`"hi"`<br>`"hr"`<br>`"ht"`<br>`"hu"`<br>`"id"`<br>`"is"`<br>`"it"`<br>`"ja"`<br>`"ko"`<br>`"la"`<br>`"lt"`<br>`"ms"`<br>`"ne"`<br>`"nl"`<br>`"no"`<br>`"pa"`<br>`"pl"`<br>`"pt"`<br>`"ro"`<br>`"ru"`<br>`"sa"`<br>`"sk"`<br>`"sr"`<br>`"sv"`<br>`"sw"`<br>`"ta"`<br>`"te"`<br>`"th"`<br>`"tl"`<br>`"tr"`<br>`"uk"`<br>`"ur"`<br>`"vi"`<br>`"yue"`<br>`"zh"`<br>`"unknown"` |
| `keyscale` | A tonalidade e a escala musical (maior ou menor). | COMBO | Não | `"C major"`<br>`"C# major"`<br>`"Db major"`<br>`"D major"`<br>`"D# major"`<br>`"Eb major"`<br>`"E major"`<br>`"F major"`<br>`"F# major"`<br>`"Gb major"`<br>`"G major"`<br>`"G# major"`<br>`"Ab major"`<br>`"A major"`<br>`"A# major"`<br>`"Bb major"`<br>`"B major"`<br>`"C minor"`<br>`"C# minor"`<br>`"Db minor"`<br>`"D minor"`<br>`"D# minor"`<br>`"Eb minor"`<br>`"E minor"`<br>`"F minor"`<br>`"F# minor"`<br>`"Gb minor"`<br>`"G minor"`<br>`"G# minor"`<br>`"Ab minor"`<br>`"A minor"`<br>`"A# minor"`<br>`"Bb minor"`<br>`"B minor"` |
| `generate_audio_codes` | Ativa o LLM que gera códigos de áudio. Isso pode ser lento, mas aumentará a qualidade do áudio gerado. Desative se você estiver fornecendo uma referência de áudio ao modelo. Padrão: True. | BOOLEAN | Não | N/A |
| `cfg_scale` | A escala de orientação livre de classificador. Valores mais altos fazem a saída seguir o prompt mais de perto. Padrão: 2.0. | FLOAT | Não | 0.0 a 100.0 |
| `temperature` | Uma temperatura de amostragem. Valores mais baixos tornam a saída mais determinística. Padrão: 0.85. | FLOAT | Não | 0.0 a 2.0 |
| `top_p` | A probabilidade de amostragem de núcleo (top-p). Padrão: 0.9. | FLOAT | Não | 0.0 a 2000.0 |
| `top_k` | O número de tokens com maior probabilidade a serem considerados (top-k). Padrão: 0. | INT | Não | 0 a 100 |
| `min_p` | O limite mínimo de probabilidade para amostragem de tokens (min-p). Padrão: 0.000. | FLOAT | Não | 0.0 a 1.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `CONDITIONING` | Os dados de condicionamento, que contêm o texto codificado e os parâmetros de áudio para o modelo AceStepAudio 1.5. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeAceStepAudio1.5/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4bc97ec6220514b71fafde610339f2dca4ded26f68b541ed43ea492f127321f8`
