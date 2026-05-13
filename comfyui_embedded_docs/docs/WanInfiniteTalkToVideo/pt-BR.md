> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanInfiniteTalkToVideo/pt-BR.md)

O nó WanInfiniteTalkToVideo gera sequências de vídeo a partir de entrada de áudio. Ele utiliza um modelo de difusão de vídeo, condicionado a características de áudio extraídas de um ou dois falantes, para produzir uma representação latente de um vídeo de cabeça falante. O nó pode gerar uma nova sequência ou estender uma existente usando quadros anteriores para contexto de movimento.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `modo` | COMBO | Sim | `"single_speaker"`<br>`"two_speakers"` | O modo de entrada de áudio. `"single_speaker"` usa uma entrada de áudio. `"two_speakers"` habilita entradas para um segundo falante e máscaras correspondentes. |
| `modelo` | MODEL | Sim | - | O modelo base de difusão de vídeo. |
| `patch do modelo` | MODELPATCH | Sim | - | O patch do modelo contendo as camadas de projeção de áudio. |
| `positivo` | CONDITIONING | Sim | - | O condicionamento positivo para guiar a geração. |
| `negativo` | CONDITIONING | Sim | - | O condicionamento negativo para guiar a geração. |
| `vae` | VAE | Sim | - | O VAE usado para codificar imagens de e para o espaço latente. |
| `largura` | INT | Não | 16 - MAX_RESOLUTION | A largura do vídeo de saída em pixels. Deve ser divisível por 16. (padrão: 832) |
| `altura` | INT | Não | 16 - MAX_RESOLUTION | A altura do vídeo de saída em pixels. Deve ser divisível por 16. (padrão: 480) |
| `duração` | INT | Não | 1 - MAX_RESOLUTION | O número de quadros a serem gerados. (padrão: 81) |
| `saída do clip vision` | CLIPVISIONOUTPUT | Não | - | Saída opcional de visão CLIP para condicionamento adicional. |
| `imagem inicial` | IMAGE | Não | - | Uma imagem inicial opcional para iniciar a sequência de vídeo. |
| `saída do codificador de áudio 1` | AUDIOENCODEROUTPUT | Sim | - | A saída primária do codificador de áudio contendo características para o primeiro falante. |
| `quantidade de quadros de movimento` | INT | Não | 1 - 33 | Número de quadros anteriores a serem usados como contexto de movimento ao estender uma sequência. (padrão: 9) |
| `escala de áudio` | FLOAT | Não | -10.0 - 10.0 | Um fator de escala aplicado ao condicionamento de áudio. (padrão: 1.0) |
| `quadros anteriores` | IMAGE | Não | - | Quadros de vídeo anteriores opcionais para estender a partir deles. |
| `audio_encoder_output_2` | AUDIOENCODEROUTPUT | Não | - | A saída do segundo codificador de áudio. Obrigatório quando `modo` está definido como `"two_speakers"`. |
| `mask_1` | MASK | Não | - | Máscara para o primeiro falante, obrigatória se estiver usando duas entradas de áudio. |
| `mask_2` | MASK | Não | - | Máscara para o segundo falante, obrigatória se estiver usando duas entradas de áudio. |

**Restrições dos Parâmetros:**

* Quando `mode` está definido como `"two_speakers"`, os parâmetros `audio_encoder_output_2`, `mask_1` e `mask_2` tornam-se obrigatórios.
* Se `audio_encoder_output_2` for fornecido, tanto `mask_1` quanto `mask_2` também devem ser fornecidos.
* Se `mask_1` e `mask_2` forem fornecidos, `audio_encoder_output_2` também deve ser fornecido.
* Se `previous_frames` for fornecido, ele deve conter pelo menos tantos quadros quanto o especificado por `motion_frame_count`.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `modelo` | MODEL | O modelo com patch aplicado e condicionamento de áudio. |
| `positivo` | CONDITIONING | O condicionamento positivo, potencialmente modificado com contexto adicional (ex.: imagem inicial, visão CLIP). |
| `negativo` | CONDITIONING | O condicionamento negativo, potencialmente modificado com contexto adicional. |
| `latent` | LATENT | A sequência de vídeo gerada no espaço latente. |
| `trim_image` | INT | O número de quadros do início do contexto de movimento que devem ser cortados ao estender uma sequência. |

---
**Source fingerprint (SHA-256):** `6bb976da5cac0b61edb7d4c9d206c7c7ea9ffc0e982034c23c7f2e891e972888`
