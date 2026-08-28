# WanInfiniteTalkToVideo

O WanInfiniteTalkToVideo gera sequências de vídeo a partir de entrada de áudio. Ele usa um modelo de difusão de vídeo, condicionado a características de áudio extraídas de um ou dois falantes, para produzir uma representação latente de um vídeo de pessoa falando. O nó pode gerar uma nova sequência ou estender uma existente usando quadros anteriores como contexto de movimento.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modo` | O modo de entrada de áudio. `single_speaker` usa uma entrada de áudio. `two_speakers` ativa a entrada de áudio adicional e as máscaras listadas na seção Entradas de dois falantes. | DYNAMIC_COMBO | Sim | `"single_speaker"`<br>`"two_speakers"` |
| `modelo` | O modelo base de difusão de vídeo. | MODEL | Sim | - |
| `patch do modelo` | O patch do modelo contendo as camadas de projeção de áudio. | MODEL_PATCH | Sim | - |
| `positivo` | O condicionamento positivo para guiar a geração. | CONDITIONING | Sim | - |
| `negativo` | O condicionamento negativo para guiar a geração. | CONDITIONING | Sim | - |
| `vae` | O VAE usado para codificar imagens para o espaço latente e decodificá-las de volta. | VAE | Sim | - |
| `largura` | A largura do vídeo de saída em pixels. Deve ser divisível por 16. (padrão: 832) | INT | Sim | 16 - MAX_RESOLUTION (step 16) |
| `altura` | A altura do vídeo de saída em pixels. Deve ser divisível por 16. (padrão: 480) | INT | Sim | 16 - MAX_RESOLUTION (step 16) |
| `duração` | O número de quadros a serem gerados. (padrão: 81) | INT | Sim | 1 - MAX_RESOLUTION (step 4) |
| `saída do clip vision` | Saída opcional do CLIP vision para condicionamento adicional. | CLIP_VISION_OUTPUT | Não | - |
| `imagem inicial` | Imagem inicial opcional para inicializar a sequência de vídeo. | IMAGE | Não | - |
| `saída do codificador de áudio 1` | A saída principal do codificador de áudio contendo características do primeiro falante. | AUDIO_ENCODER_OUTPUT | Sim | - |
| `quantidade de quadros de movimento` | Número de quadros anteriores a serem usados como contexto de movimento. (padrão: 9) | INT | Sim | 1 - 33 |
| `escala de áudio` | Um fator de escala aplicado ao condicionamento de áudio. (padrão: 1.0) | FLOAT | Sim | -10.0 - 10.0 |
| `quadros anteriores` | Quadros de vídeo anteriores opcionais para estender a partir deles. Os últimos `motion_frame_count` quadros são usados como contexto de movimento. | IMAGE | Não | - |

### Entradas de dois falantes

As entradas nesta seção são exibidas quando `mode` está definido como `"two_speakers"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `audio_encoder_output_2` | A segunda saída do codificador de áudio contendo características do segundo falante. | AUDIO_ENCODER_OUTPUT | Não | - |
| `mask_1` | Máscara para o primeiro falante, obrigatória se estiver usando duas entradas de áudio. | MASK | Não | - |
| `mask_2` | Máscara para o segundo falante, obrigatória se estiver usando duas entradas de áudio. | MASK | Não | - |

**Restrições de parâmetros:**

- Quando `mode` está definido como `"two_speakers"`, `audio_encoder_output_2`, `mask_1` e `mask_2` são obrigatórios para a configuração do segundo falante.
- Se `audio_encoder_output_2` for fornecido, `mask_1` e `mask_2` também devem ser fornecidos.
- Se `mask_1` e `mask_2` forem fornecidos, `audio_encoder_output_2` também deve ser fornecido.
- Se `previous_frames` for fornecido, ele deve conter pelo menos o número de quadros especificado por `motion_frame_count`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `modelo` | O modelo com patch aplicado e com condicionamento de áudio aplicado. | MODEL |
| `positivo` | O condicionamento positivo, potencialmente modificado com contexto adicional, como uma imagem inicial ou saída do CLIP vision. | CONDITIONING |
| `negativo` | O condicionamento negativo, potencialmente modificado com contexto adicional. | CONDITIONING |
| `latente` | A sequência de vídeo gerada no espaço latente. | LATENT |
| `imagem recortada` | O número de quadros a partir do início do contexto de movimento que devem ser removidos ao estender uma sequência. É igual a `motion_frame_count` quando `previous_frames` é fornecido; caso contrário, 0. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanInfiniteTalkToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b7359490c1de86d9c82122bc227295b3b7f8a3493f629365ae0f22f9f34d9a66`
