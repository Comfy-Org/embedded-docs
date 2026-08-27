# Trellis2UpsampleStage

Este nó recebe o latent de forma em resolução 512 produzido pela primeira passada de amostragem da etapa de forma, aumenta sua resolução para uma resolução alvo mais alta e prepara o conditioning e o latent necessários para a segunda passada de amostragem da etapa de forma. Ele anexa metadados específicos de cada etapa ao conditioning para que o modelo possa usá-los durante a geração.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `positive` | O conditioning positivo ao qual os metadados de forma da etapa de upsampling são anexados. | CONDITIONING | Yes | |
| `negative` | O conditioning negativo ao qual os metadados de forma da etapa de upsampling são anexados. | CONDITIONING | Yes | |
| `shape_latent` | O latent de forma em resolução 512 produzido pelo primeiro KSampler da etapa de forma. | LATENT | Yes | |
| `vae` | O VAE Trellis2 usado para decodificar o latent de forma em coordenadas esparsas de alta resolução. | VAE | Yes | |
| `target_resolution` | Resolução de voxel da forma com upsampling. Maior = mais detalhes, mais VRAM. Padrão: 1024. | INT | Yes | 1024 - 2048 (step 128) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `positive` | Conditioning positivo com os metadados de forma da etapa de upsampling anexados. | CONDITIONING |
| `negative` | Conditioning negativo com os metadados de forma da etapa de upsampling anexados. | CONDITIONING |
| `latent` | Latent preenchido com zeros, preparado para a segunda passada de amostragem da etapa de forma na resolução alvo, carregando as coordenadas com upsampling e os metadados de resolução. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2UpsampleStage/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0582579bfab487718d69789de508a5ec243d98a0e06ad7165c406154a64677d6`
