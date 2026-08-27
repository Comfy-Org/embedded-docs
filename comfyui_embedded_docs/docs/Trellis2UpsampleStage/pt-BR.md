# Trellis2UpsampleStage

Este nó recebe o latente de forma de resolução 512 produzido pela primeira passagem de amostragem do estágio de forma, amplia-o para uma resolução alvo mais alta e prepara o condicionamento e o latente necessários para a segunda passagem de amostragem do estágio de forma. Ele anexa metadados por estágio ao condicionamento para que o modelo possa usá-los durante a geração.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|---------------|-------------|-------|
| `positive` | O condicionamento positivo ao qual os metadados de forma do estágio de aumento de resolução são anexados. | CONDITIONING | Sim | |
| `negative` | O condicionamento negativo ao qual os metadados de forma do estágio de aumento de resolução são anexados. | CONDITIONING | Sim | |
| `shape_latent` | O latente de forma de resolução 512 produzido pelo primeiro KSampler do estágio de forma. | LATENT | Sim | |
| `vae` | O VAE Trellis2 usado para decodificar o latente de forma em coordenadas esparsas de alta resolução. | VAE | Sim | |
| `target_resolution` | Resolução de voxel da forma ampliada. Maior = mais detalhes, mais VRAM. Padrão: 1024. | INT | Sim | 1024 - 2048 (step 128) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|---------------|
| `positive` | Condicionamento positivo com os metadados de forma do estágio de aumento de resolução anexados. | CONDITIONING |
| `negative` | Condicionamento negativo com os metadados de forma do estágio de aumento de resolução anexados. | CONDITIONING |
| `latent` | Latente preenchido com zeros preparado para a segunda passagem de amostragem do estágio de forma na resolução alvo, contendo as coordenadas ampliadas e os metadados de resolução. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2UpsampleStage/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0582579bfab487718d69789de508a5ec243d98a0e06ad7165c406154a64677d6`
