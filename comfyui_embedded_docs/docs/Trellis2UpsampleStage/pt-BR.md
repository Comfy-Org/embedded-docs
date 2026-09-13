# Estágio de ampliação Trellis2

Este nó faz upscale de um latent de forma com resolução 512 para coordenadas esparsas de alta resolução e prepara a segunda passagem de amostragem do estágio de forma na resolução alvo. Ele anexa metadados por estágio ao condicionamento para que o modelo possa consumi-los durante a geração.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `positive` | O condicionamento positivo ao qual os metadados de forma do estágio de upsampling são anexados. | CONDITIONING | Sim | |
| `negative` | O condicionamento negativo ao qual os metadados de forma do estágio de upsampling são anexados. | CONDITIONING | Sim | |
| `shape_latent` | O latent de forma com resolução 512 gerado como saída pelo primeiro KSampler do estágio de forma. | LATENT | Sim | |
| `vae` | O VAE Trellis2 usado para decodificar o latent de forma em coordenadas esparsas de alta resolução. | VAE | Sim | |
| `target_resolution` | Resolução de voxel da forma ampliada. Maior = mais detalhe, mais VRAM. Padrão: 1024. | INT | Sim | 1024 - 2048 (passo 128) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `positive` | Condicionamento positivo com os metadados de forma do estágio de upsampling anexados. | CONDITIONING |
| `negative` | Condicionamento negativo com os metadados de forma do estágio de upsampling anexados. | CONDITIONING |
| `latent` | Latent preenchido com zeros, preparado para a segunda passagem de amostragem do estágio de forma na resolução alvo, carregando as coordenadas ampliadas, as contagens de coordenadas por amostra e os metadados de resolução de coordenadas. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2UpsampleStage/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0582579bfab487718d69789de508a5ec243d98a0e06ad7165c406154a64677d6`
