# EmptyMiniMaxMusic3LatentAudio

Este nó cria um tensor de áudio latente vazio (preenchido com zeros) para o modelo MiniMax Music3. Ele converte a duração solicitada em segundos nos frames de áudio correspondentes e produz um latente em branco do tamanho correto, pronto para ser usado como ponto de partida para a geração de música.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|--------------|-------------|-----------|
| `seconds` | A duração do áudio latente em segundos (padrão: 120.0). O valor é convertido em frames de áudio e limitado aos limites de duração suportados pelo modelo. | FLOAT | Sim | 0.04 a model maximum (MAX_AUDIO_FRAMES / AUDIO_FRAMES_PER_SECOND), passo 0.04 |
| `batch_size` | O número de áudios latentes a serem gerados em um único lote (padrão: 1). | INT | Sim | 1 a 4096 |

Observação: O valor de `seconds` é arredondado para o frame de áudio mais próximo e limitado a um mínimo de 1 frame e um máximo de `MAX_AUDIO_FRAMES` frames, portanto, o comprimento real do latente pode diferir ligeiramente do valor exato inserido.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-------------|--------------|
| `LATENT` | Um tensor de áudio latente preenchido com zeros, de formato (batch_size, 128, latent_length). Inclui metadados que marcam a amostra como dados de áudio com uma razão de redução temporal de 512. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMiniMaxMusic3LatentAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `77e6a69702a837c958c2954bba061c979152f034bc7774a5b6c97ea8d57bda4b`
