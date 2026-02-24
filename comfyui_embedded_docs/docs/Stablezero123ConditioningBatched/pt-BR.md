> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Stablezero123ConditioningBatched/pt-BR.md)

Este nó foi projetado para processar informações de condicionamento de forma em lote, especificamente adaptado para o modelo StableZero123. Ele se concentra no tratamento eficiente de múltiplos conjuntos de dados de condicionamento simultaneamente, otimizando o fluxo de trabalho para cenários onde o processamento em lote é crucial.

## Entradas

| Parâmetro             | Tipo de Dados | Descrição |
|----------------------|--------------|-------------|
| `clip_vision`         | `CLIP_VISION` | As incorporações de visão CLIP que fornecem contexto visual para o processo de condicionamento. |
| `init_image`          | `IMAGE`      | A imagem inicial a ser condicionada, servindo como ponto de partida para o processo de geração. |
| `vae`                 | `VAE`        | O autoencoder variacional usado para codificar e decodificar imagens no processo de condicionamento. |
| `width`               | `INT`        | A largura da imagem de saída. |
| `height`              | `INT`        | A altura da imagem de saída. |
| `batch_size`          | `INT`        | O número de conjuntos de condicionamento a serem processados em um único lote. |
| `elevation`           | `FLOAT`      | O ângulo de elevação para o condicionamento do modelo 3D, afetando a perspectiva da imagem gerada. |
| `azimuth`             | `FLOAT`      | O ângulo de azimute para o condicionamento do modelo 3D, afetando a orientação da imagem gerada. |
| `elevation_batch_increment` | `FLOAT` | A mudança incremental no ângulo de elevação ao longo do lote, permitindo perspectivas variadas. |
| `azimuth_batch_increment` | `FLOAT` | A mudança incremental no ângulo de azimute ao longo do lote, permitindo orientações variadas. |

## Saídas

| Parâmetro     | Tipo de Dados | Descrição |
|---------------|--------------|-------------|
| `positive`    | `CONDITIONING` | A saída de condicionamento positivo, adaptada para promover certas características ou aspectos no conteúdo gerado. |
| `negative`    | `CONDITIONING` | A saída de condicionamento negativo, adaptada para desfavorecer certas características ou aspectos no conteúdo gerado. |
| `latent`      | `LATENT`     | A representação latente derivada do processo de condicionamento, pronta para etapas posteriores de processamento ou geração. |
