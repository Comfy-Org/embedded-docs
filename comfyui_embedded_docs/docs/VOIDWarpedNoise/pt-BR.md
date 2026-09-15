# VOIDWarpedNoise

Gera ruído correlacionado temporalmente para a segunda passagem do processo de refinamento de vídeo VOID. Ele recebe o vídeo de saída da Passagem 1 e deforma o ruído Gaussiano ao longo de vetores de fluxo óptico, de modo que o ruído se move de forma consistente com o conteúdo do vídeo. O ruído deformado resultante é usado como latente inicial para a Passagem 2, o que melhora a consistência temporal na saída final.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `optical_flow` | Modelo de fluxo óptico do OpticalFlowLoader (RAFT-large). | OPTICAL_FLOW | Sim | - |
| `video` | Frames de vídeo de saída da Passagem 1 [T, H, W, 3]. | IMAGE | Sim | - |
| `width` | Largura alvo em pixels (padrão: 672). O vídeo de entrada é redimensionado para essa largura antes que o ruído seja gerado, e a largura latente é derivada como largura ÷ 8. | INT | Sim | 16 a MAX_RESOLUTION (passo 8) |
| `height` | Altura alvo em pixels (padrão: 384). O vídeo de entrada é redimensionado para essa altura antes que o ruído seja gerado, e a altura latente é derivada como altura ÷ 8. | INT | Sim | 16 a MAX_RESOLUTION (passo 8) |
| `length` | Número de frames em pixels. Arredondado para baixo para tornar `latent_t` par (requisito `patch_size_t=2`), por exemplo, 49 para 45 (padrão: 45). | INT | Sim | 1 a MAX_RESOLUTION (passo 1) |
| `batch_size` | Número de sequências idênticas de ruído deformado a produzir (padrão: 1). O ruído gerado é repetido essa quantidade de vezes ao longo da dimensão de batch. | INT | Sim | 1 a 64 |

**Observação sobre o parâmetro `length`:** O valor de `length` é automaticamente arredondado para baixo até o valor mais próximo que produz uma dimensão `latent_t` par, conforme exigido pela restrição `patch_size_t=2` do modelo CogVideoX-Fun-V1.5 (por exemplo, 49 se torna 45). O nó registra um aviso quando esse arredondamento ocorre. Frames além do `length` ajustado são ignorados, e o ruído é reamostrado para o número de frames latentes resultante.

**Observação sobre `width` e `height`:** Esses valores são usados tanto para redimensionar os frames de vídeo de entrada (bilinear, corte central) quanto para determinar a resolução latente final (dividida por 8). Se o ruído gerado não corresponder ao tamanho latente solicitado, ele será redimensionado para se ajustar.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `warped_noise` | Um tensor 5D (B, C, T, H, W) contendo ruído Gaussiano deformado por fluxo óptico, pronto para uso como o latente inicial na Passagem 2 do VOID. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoise/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f46b0a73b09a5d2d0bc25676f9571563c6bb8bad8d835e7564ac092c72136107`
