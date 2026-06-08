# Visão Geral

Gera ruído temporalmente correlacionado para a segunda passagem do processo de refinamento de vídeo VOID. Ele recebe o vídeo de saída da Passagem 1 e distorce o ruído Gaussiano ao longo dos vetores de fluxo óptico, criando ruído que se move de forma consistente com o conteúdo do vídeo. Este ruído distorcido é usado como o latente inicial para a Passagem 2, o que melhora a consistência temporal na saída final.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `optical_flow` | Modelo de fluxo óptico do OpticalFlowLoader (RAFT-large). | MODEL | Sim | - |
| `video` | Quadros de vídeo de saída da Passagem 1 [T, H, W, 3]. | IMAGE | Sim | - |
| `width` | Largura do latente de saída (padrão: 672). | INT | Sim | 16 a MAX_RESOLUTION (passo 8) |
| `height` | Altura do latente de saída (padrão: 384). | INT | Sim | 16 a MAX_RESOLUTION (passo 8) |
| `length` | Número de quadros de pixel. Arredondado para baixo para tornar latent_t par (requisito patch_size_t=2), ex: 49 → 45 (padrão: 45). | INT | Sim | 1 a MAX_RESOLUTION (passo 1) |
| `batch_size` | Número de sequências de ruído idênticas a serem geradas (padrão: 1). | INT | Sim | 1 a 64 |

**Nota sobre o parâmetro `length`:** O valor de `length` é automaticamente arredondado para baixo para o valor válido mais próximo que produz uma dimensão `latent_t` par. Isso é exigido pela restrição `patch_size_t=2` do modelo CogVideoX-Fun-V1.5. Um aviso é registrado quando o arredondamento ocorre.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `warped_noise` | Um tensor 5D (B, C, T, H, W) contendo ruído Gaussiano distorcido por fluxo óptico, pronto para uso como latente inicial na Passagem 2 do VOID. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoise/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a0f986e54bcc6c455220f89f5d840585a9eae081e522ea11e0ce37ab46821bd9`
