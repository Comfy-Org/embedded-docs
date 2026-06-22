# WanInfiniteTalkToVideo

O nó WanInfiniteTalkToVideo gera sequências de vídeo a partir de entrada de áudio. Ele utiliza um modelo de difusão de vídeo, condicionado a características de áudio extraídas de um ou dois falantes, para produzir uma representação latente de um vídeo de cabeça falante. O nó pode gerar uma nova sequência ou estender uma existente usando quadros anteriores para contexto de movimento.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modo` | O modo de entrada de áudio. `"single_speaker"` usa uma entrada de áudio. `"two_speakers"` habilita entradas para um segundo falante e máscaras correspondentes. | COMBO | Sim | `"single_speaker"`<br>`"two_speakers"` |
| `modelo` | O modelo base de difusão de vídeo. | MODEL | Sim | - |
| `patch do modelo` | O patch do modelo contendo as camadas de projeção de áudio. | MODELPATCH | Sim | - |
| `positivo` | O condicionamento positivo para guiar a geração. | CONDITIONING | Sim | - |
| `negativo` | O condicionamento negativo para guiar a geração. | CONDITIONING | Sim | - |
| `vae` | O VAE usado para codificar imagens de e para o espaço latente. | VAE | Sim | - |
| `largura` | A largura do vídeo de saída em pixels. Deve ser divisível por 16. (padrão: 832) | INT | Não | 16 - MAX_RESOLUTION |
| `altura` | A altura do vídeo de saída em pixels. Deve ser divisível por 16. (padrão: 480) | INT | Não | 16 - MAX_RESOLUTION |
| `duração` | O número de quadros a serem gerados. (padrão: 81) | INT | Não | 1 - MAX_RESOLUTION |
| `saída do clip vision` | Saída opcional de visão CLIP para condicionamento adicional. | CLIPVISIONOUTPUT | Não | - |
| `imagem inicial` | Uma imagem inicial opcional para iniciar a sequência de vídeo. | IMAGE | Não | - |
| `saída do codificador de áudio 1` | A saída primária do codificador de áudio contendo características para o primeiro falante. | AUDIOENCODEROUTPUT | Sim | - |
| `quantidade de quadros de movimento` | Número de quadros anteriores a serem usados como contexto de movimento ao estender uma sequência. (padrão: 9) | INT | Não | 1 - 33 |
| `escala de áudio` | Um fator de escala aplicado ao condicionamento de áudio. (padrão: 1.0) | FLOAT | Não | -10.0 - 10.0 |
| `quadros anteriores` | Quadros de vídeo anteriores opcionais para estender a partir deles. | IMAGE | Não | - |
| `audio_encoder_output_2` | A saída do segundo codificador de áudio. Obrigatório quando `modo` está definido como `"two_speakers"`. | AUDIOENCODEROUTPUT | Não | - |
| `mask_1` | Máscara para o primeiro falante, obrigatória se estiver usando duas entradas de áudio. | MASK | Não | - |
| `mask_2` | Máscara para o segundo falante, obrigatória se estiver usando duas entradas de áudio. | MASK | Não | - |

**Restrições dos Parâmetros:**

* Quando `mode` está definido como `"two_speakers"`, os parâmetros `audio_encoder_output_2`, `mask_1` e `mask_2` tornam-se obrigatórios.
* Se `audio_encoder_output_2` for fornecido, tanto `mask_1` quanto `mask_2` também devem ser fornecidos.
* Se `mask_1` e `mask_2` forem fornecidos, `audio_encoder_output_2` também deve ser fornecido.
* Se `previous_frames` for fornecido, ele deve conter pelo menos tantos quadros quanto o especificado por `motion_frame_count`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `modelo` | O modelo com patch aplicado e condicionamento de áudio. | MODEL |
| `positivo` | O condicionamento positivo, potencialmente modificado com contexto adicional (ex.: imagem inicial, visão CLIP). | CONDITIONING |
| `negativo` | O condicionamento negativo, potencialmente modificado com contexto adicional. | CONDITIONING |
| `latent` | A sequência de vídeo gerada no espaço latente. | LATENT |
| `trim_image` | O número de quadros do início do contexto de movimento que devem ser cortados ao estender uma sequência. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanInfiniteTalkToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `6bb976da5cac0b61edb7d4c9d206c7c7ea9ffc0e982034c23c7f2e891e972888`
