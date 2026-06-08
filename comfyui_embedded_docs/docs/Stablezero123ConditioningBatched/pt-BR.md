Este nó foi projetado para processar informações de condicionamento em lote, especificamente adaptado para o modelo StableZero123. Ele foca em lidar eficientemente com múltiplos conjuntos de dados de condicionamento simultaneamente, otimizando o fluxo de trabalho para cenários onde o processamento em lote é crucial.

## Entradas

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `clip_vision` | Os embeddings de visão do CLIP que fornecem contexto visual para o processo de condicionamento. | `CLIP_VISION` |
| `init_image` | A imagem inicial a ser condicionada, servindo como ponto de partida para o processo de geração. | `IMAGE` |
| `vae` | O autoencoder variacional usado para codificar e decodificar imagens no processo de condicionamento. | `VAE` |
| `width` | A largura da imagem de saída. | `INT` |
| `height` | A altura da imagem de saída. | `INT` |
| `batch_size` | O número de conjuntos de condicionamento a serem processados em um único lote. | `INT` |
| `elevation` | O ângulo de elevação para condicionamento de modelos 3D, afetando a perspectiva da imagem gerada. | `FLOAT` |
| `azimuth` | O ângulo azimutal para condicionamento de modelos 3D, afetando a orientação da imagem gerada. | `FLOAT` |
| `elevation_batch_increment` | A variação incremental no ângulo de elevação ao longo do lote, permitindo perspectivas variadas. | `FLOAT` |
| `azimuth_batch_increment` | A variação incremental no ângulo azimutal ao longo do lote, permitindo orientações variadas. | `FLOAT` |

## Saídas

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `positive` | A saída de condicionamento positivo, adaptada para promover certas características ou aspectos no conteúdo gerado. | `CONDITIONING` |
| `negative` | A saída de condicionamento negativo, adaptada para desfavorecer certas características ou aspectos no conteúdo gerado. | `CONDITIONING` |
| `latent` | A representação latente derivada do processo de condicionamento, pronta para etapas adicionais de processamento ou geração. | `LATENT` |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Stablezero123ConditioningBatched/pt-BR.md)
