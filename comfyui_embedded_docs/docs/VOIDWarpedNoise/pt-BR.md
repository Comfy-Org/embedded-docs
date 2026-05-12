> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoise/pt-BR.md)

## Visão Geral

Gera ruído temporalmente correlacionado para a segunda passagem do processo de refinamento de vídeo VOID. Ele recebe o vídeo de saída da Passagem 1 e distorce o ruído Gaussiano ao longo dos vetores de fluxo óptico, criando ruído que se move de forma consistente com o conteúdo do vídeo. Este ruído distorcido é usado como latente inicial para a Passagem 2, que melhora a consistência temporal na saída final.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `optical_flow` | MODEL | Sim | - | Modelo de fluxo óptico do OpticalFlowLoader (RAFT-large). |
| `video` | IMAGE | Sim | - | Quadros de vídeo de saída da Passagem 1 [T, H, W, 3]. |
| `width` | INT | Sim | 16 a MAX_RESOLUTION (passo 8) | Largura do latente de saída (padrão: 672). |
| `height` | INT | Sim | 16 a MAX_RESOLUTION (passo 8) | Altura do latente de saída (padrão: 384). |
| `length` | INT | Sim | 1 a MAX_RESOLUTION (passo 1) | Número de quadros de pixel. Arredondado para baixo para tornar latent_t par (requisito patch_size_t=2), ex: 49 → 45 (padrão: 45). |
| `batch_size` | INT | Sim | 1 a 64 | Número de sequências de ruído idênticas a serem geradas (padrão: 1). |

**Nota sobre o parâmetro `length`:** O valor de `length` é automaticamente arredondado para baixo para o valor válido mais próximo que produz uma dimensão `latent_t` par. Isso é exigido pela restrição `patch_size_t=2` do modelo CogVideoX-Fun-V1.5. Um aviso é registrado quando o arredondamento ocorre.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `warped_noise` | LATENT | Um tensor 5D (B, C, T, H, W) contendo ruído Gaussiano distorcido por fluxo óptico, pronto para uso como latente inicial na Passagem 2 do VOID. |