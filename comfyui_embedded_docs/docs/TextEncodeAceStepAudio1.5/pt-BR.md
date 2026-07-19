# TextEncodeAceStepAudio1.5

O nó TextEncodeAceStepAudio1.5 prepara metadados relacionados a texto e áudio para uso com o modelo AceStepAudio 1.5. Ele recebe tags descritivas, letras e parâmetros musicais, e então utiliza um modelo CLIP para convertê-los em um formato de condicionamento adequado para geração de áudio.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `clip` | O modelo CLIP usado para tokenizar e codificar o texto de entrada. | CLIP | Sim | N/A |
| `tags` | Tags descritivas para o áudio, como gênero, clima ou instrumentos. Suporta entrada multilinha e prompts dinâmicos. | STRING | Sim | N/A |
| `lyrics` | As letras da faixa de áudio. Suporta entrada multilinha e prompts dinâmicos. | STRING | Sim | N/A |
| `seed` | Um valor de semente aleatório para geração reproduzível. Possui um widget de controle pós-geração. Padrão: 0. | INT | Não | 0 a 18446744073709551615 |
| `bpm` | Os batimentos por minuto (BPM) para o áudio gerado. Padrão: 120. | INT | Não | 10 a 300 |
| `duration` | A duração desejada do áudio em segundos. Padrão: 120.0. | FLOAT | Não | 0.0 a 2000.0 |
| `timesignature` | A fórmula de compasso musical. | COMBO | Não | `"2"`<br>`"3"`<br>`"4"`<br>`"6"` |
| `language` | O idioma do texto de entrada. Padrão: "en". | COMBO | Não | `"ar"`<br>`"az"`<br>`"bg"`<br>`"bn"`<br>`"ca"`<br>`"cs"`<br>`"da"`<br>`"de"`<br>`"el"`<br>`"en"`<br>`"es"`<br>`"fa"`<br>`"fi"`<br>`"fr"`<br>`"he"`<br>`"hi"`<br>`"hr"`<br>`"ht"`<br>`"hu"`<br>`"id"`<br>`"is"`<br>`"it"`<br>`"ja"`<br>`"ko"`<br>`"la"`<br>`"lt"`<br>`"ms"`<br>`"ne"`<br>`"nl"`<br>`"no"`<br>`"pa"`<br>`"pl"`<br>`"pt"`<br>`"ro"`<br>`"ru"`<br>`"sa"`<br>`"sk"`<br>`"sr"`<br>`"sv"`<br>`"sw"`<br>`"ta"`<br>`"te"`<br>`"th"`<br>`"tl"`<br>`"tr"`<br>`"uk"`<br>`"ur"`<br>`"vi"`<br>`"yue"`<br>`"zh"`<br>`"unknown"` |
| `keyscale` | A tonalidade e escala musical (maior ou menor). | COMBO | Não | `"C major"`<br>`"C minor"`<br>`"C# major"`<br>`"C# minor"`<br>`"Db major"`<br>`"Db minor"`<br>`"D major"`<br>`"D minor"`<br>`"D# major"`<br>`"D# minor"`<br>`"Eb major"`<br>`"Eb minor"`<br>`"E major"`<br>`"E minor"`<br>`"F major"`<br>`"F minor"`<br>`"F# major"`<br>`"F# minor"`<br>`"Gb major"`<br>`"Gb minor"`<br>`"G major"`<br>`"G minor"`<br>`"G# major"`<br>`"G# minor"`<br>`"Ab major"`<br>`"Ab minor"`<br>`"A major"`<br>`"A minor"`<br>`"A# major"`<br>`"A# minor"`<br>`"Bb major"`<br>`"Bb minor"`<br>`"B major"`<br>`"B minor"` |
| `generate_audio_codes` | Ativa o LLM que gera códigos de áudio. Isso pode ser lento, mas aumentará a qualidade do áudio gerado. Desative esta opção se estiver fornecendo uma referência de áudio ao modelo. Padrão: True. | BOOLEAN | Não | N/A |
| `cfg_scale` | A escala de orientação livre de classificador. Valores mais altos fazem a saída seguir o prompt mais fielmente. Padrão: 2.0. | FLOAT | Não | 0.0 a 100.0 |
| `temperature` | Uma temperatura de amostragem. Valores mais baixos tornam a saída mais determinística. Padrão: 0.85. | FLOAT | Não | 0.0 a 2.0 |
| `top_p` | A probabilidade de amostragem por núcleo (top-p). Padrão: 0.9. | FLOAT | Não | 0.0 a 2000.0 |
| `top_k` | O número de tokens de maior probabilidade a serem considerados (top-k). Padrão: 0. | INT | Não | 0 a 100 |
| `min_p` | O limite mínimo de probabilidade para amostragem de tokens (min-p). Padrão: 0.000. | FLOAT | Não | 0.0 a 1.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `CONDITIONING` | Os dados de condicionamento, que contêm o texto codificado e os parâmetros de áudio para o modelo AceStepAudio 1.5. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeAceStepAudio1.5/pt-BR.md)

---
**Source fingerprint (SHA-256):** `df70a55024812d8c77a3b618cbff6d3148a3f3f5fc4d17dd3c4282ce7f3cbc2c`
