# EmptyMiniMaxMusic3LatentAudio

Este nó cria um latente de áudio vazio (preenchido com zeros) para o modelo MiniMax Music3. Ele converte a duração solicitada em segundos para os quadros de áudio correspondentes e produz um tensor latente em branco do tamanho correto, pronto para ser usado como ponto de partida para a geração de música.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `seconds` | A duração do latente de áudio em segundos (padrão: 120.0). O valor é convertido em quadros de áudio e limitado aos limites de duração suportados pelo modelo. | FLOAT | Sim | 0.04 a (MAX_AUDIO_FRAMES / AUDIO_FRAMES_PER_SECOND), step 0.04 |
| `batch_size` | O número de latentes de áudio a serem gerados em um único lote (padrão: 1). | INT | Sim | 1 a 4096 |

Nota: O valor de `seconds` é arredondado para o quadro de áudio mais próximo e limitado a um mínimo de 1 quadro e um máximo de `MAX_AUDIO_FRAMES` quadros, portanto, o comprimento real do latente pode diferir ligeiramente do valor exato inserido.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-----------|---------------|
| `LATENT` | Um tensor latente de áudio preenchido com zeros, de forma (batch_size, 128, latent_length). Inclui metadados que marcam a amostra como dados de áudio com uma razão de redução temporal de 512. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMiniMaxMusic3LatentAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `77e6a69702a837c958c2954bba061c979152f034bc7774a5b6c97ea8d57bda4b`
