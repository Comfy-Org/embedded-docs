# WanInfiniteTalkToVideo

O nó WanInfiniteTalkToVideo gera um clipe de vídeo de uma pessoa falando (talking-head) a partir de áudio. Ele condiciona um modelo de difusão de vídeo com características de áudio de um ou dois locutores, usa opcionalmente uma imagem inicial ou quadros anteriores como contexto e retorna um modelo com patch, condicionamento e um vídeo latente para amostragem.

## Entradas

### Entradas Comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `mode` | O modo de áudio. Selecionar `"single_speaker"` usa uma entrada de áudio. Selecionar `"two_speakers"` adiciona as entradas do segundo locutor listadas abaixo. | DYNAMIC_COMBO | Sim | `"single_speaker"`<br>`"two_speakers"` |
| `model` | O modelo de difusão de vídeo base a receber o patch. | MODEL | Sim | - |
| `model_patch` | O patch do modelo contendo as camadas de projeção de áudio. | MODELPATCH | Sim | - |
| `positive` | O condicionamento positivo usado para guiar a geração de vídeo. | CONDITIONING | Sim | - |
| `negative` | O condicionamento negativo usado para guiar a geração de vídeo. | CONDITIONING | Sim | - |
| `vae` | O VAE usado para codificar imagens e quadros anteriores no espaço latente. | VAE | Sim | - |
| `width` | A largura do vídeo gerado em pixels, em incrementos de 16. (padrão: 832) | INT | Sim | 16 - MAX_RESOLUTION (step 16) |
| `height` | A altura do vídeo gerado em pixels, em incrementos de 16. (padrão: 480) | INT | Sim | 16 - MAX_RESOLUTION (step 16) |
| `length` | O número de quadros a gerar. (padrão: 81) | INT | Sim | 1 - MAX_RESOLUTION (step 4) |
| `audio_encoder_output_1` | A saída do codificador de áudio para o primeiro locutor, contendo as características de áudio usadas para o condicionamento. | AUDIOENCODEROUTPUT | Sim | - |
| `start_image` | Imagem inicial opcional usada para inicializar o início do vídeo. Ela é redimensionada para `width` e `height`. | IMAGE | Não | - |
| `clip_vision_output` | Saída opcional do CLIP vision adicionada ao condicionamento positivo e negativo. | CLIPVISIONOUTPUT | Não | - |
| `motion_frame_count` | Número de quadros anteriores a usar como contexto de movimento. (padrão: 9) | INT | Sim | 1 - 33 (step 1) |
| `audio_scale` | Fator de escala aplicado ao condicionamento de áudio. (padrão: 1.0) | FLOAT | Sim | -10.0 - 10.0 (step 0.01) |
| `previous_frames` | Quadros de vídeo anteriores opcionais usados para estender uma sequência existente. O nó usa os últimos `motion_frame_count` quadros como contexto de movimento. | IMAGE | Não | - |

### Entradas de um locutor

Selecionar `single_speaker` não adiciona nenhuma entrada adicional.

### Entradas de dois locutores

Estas entradas estão disponíveis quando `mode` é `"two_speakers"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `audio_encoder_output_2` | A saída do codificador de áudio para o segundo locutor. Quando fornecida, `mask_1` e `mask_2` também devem ser fornecidas. | AUDIOENCODEROUTPUT | Não | - |
| `mask_1` | Máscara para o primeiro locutor, obrigatória se forem usadas duas entradas de áudio. | MASK | Não | - |
| `mask_2` | Máscara para o segundo locutor, obrigatória se forem usadas duas entradas de áudio. | MASK | Não | - |

**Restrições dos parâmetros:**

- Se `audio_encoder_output_2` for fornecido, `mask_1` e `mask_2` também devem ser fornecidas.
- Se `mask_1` e `mask_2` forem fornecidas, `audio_encoder_output_2` também deve ser fornecido.
- Se `previous_frames` for fornecido, ele deve conter pelo menos tantos quadros quanto o especificado por `motion_frame_count`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo com patch aplicado, com condicionamento de áudio e wrappers de amostragem. | MODEL |
| `positive` | O condicionamento positivo, potencialmente modificado com a imagem inicial ou o contexto do CLIP vision. | CONDITIONING |
| `negative` | O condicionamento negativo, potencialmente modificado com a imagem inicial ou o contexto do CLIP vision. | CONDITIONING |
| `latent` | Um tensor latente inicializado com zeros representando o vídeo a ser gerado. | LATENT |
| `trim_image` | O número de quadros a remover do início ao estender a partir de quadros anteriores; 0 ao iniciar uma nova sequência. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanInfiniteTalkToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b7359490c1de86d9c82122bc227295b3b7f8a3493f629365ae0f22f9f34d9a66`
