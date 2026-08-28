# VOIDWarpedNoise

Gera ruído temporalmente correlacionado para a segunda passada do processo de refinamento de vídeo VOID. Ele pega o vídeo de saída da Passada 1 e distorce o ruído gaussiano ao longo dos vetores de fluxo óptico, criando ruído que se move de forma consistente com o conteúdo do vídeo. Esse ruído distorcido é usado como latent inicial para a Passada 2, o que melhora a consistência temporal na saída final.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `optical_flow` | Modelo de fluxo óptico do OpticalFlowLoader (RAFT-large). | OPTICAL_FLOW | Sim | - |
| `video` | Quadros de vídeo de saída da Passada 1 [T, H, W, 3]. | IMAGE | Sim | - |
| `width` | Largura do latent de saída (padrão: 672). | INT | Sim | 16 to MAX_RESOLUTION (step 8) |
| `height` | Altura do latent de saída (padrão: 384). | INT | Sim | 16 to MAX_RESOLUTION (step 8) |
| `length` | Número de quadros de pixel. Arredondado para baixo para tornar `latent_t` par (requisito `patch_size_t=2`), ex.: 49 → 45 (padrão: 45). | INT | Sim | 1 to MAX_RESOLUTION (step 1) |
| `batch_size` | Número de sequências de ruído idênticas a gerar (padrão: 1). | INT | Sim | 1 a 64 |

**Nota sobre o parâmetro `length`:** O valor de `length` é arredondado automaticamente para baixo até o valor válido mais próximo que produza uma dimensão `latent_t` par. Isso é necessário devido à restrição `patch_size_t=2` do modelo CogVideoX-Fun-V1.5. Um aviso é registrado no log quando o arredondamento ocorre.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `warped_noise` | Um tensor 5D (B, C, T, H, W) contendo ruído gaussiano distorcido por fluxo óptico, pronto para uso como latent inicial na Passada 2 do VOID. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoise/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f46b0a73b09a5d2d0bc25676f9571563c6bb8bad8d835e7564ac092c72136107`
