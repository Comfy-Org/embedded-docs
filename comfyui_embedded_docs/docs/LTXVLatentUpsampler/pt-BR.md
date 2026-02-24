> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVLatentUpsampler/pt-BR.md)

O nó LTXVLatentUpsampler aumenta a resolução espacial de uma representação latente de vídeo por um fator de dois. Ele utiliza um modelo especializado de superamostragem para processar os dados latentes, que são primeiro desnormalizados e depois renormalizados usando as estatísticas de canal do VAE fornecido. Este nó é projetado para fluxos de trabalho de vídeo dentro do espaço latente.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `samples` | LATENT | Sim | | A representação latente de entrada do vídeo a ser superamostrado. |
| `upscale_model` | LATENT_UPSCALE_MODEL | Sim | | O modelo carregado usado para realizar a superamostragem 2x nos dados latentes. |
| `vae` | VAE | Sim | | O modelo VAE usado para desnormalizar os latentes de entrada antes da superamostragem e para normalizar os latentes de saída depois. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `LATENT` | LATENT | A representação latente superamostrada, com as dimensões espaciais dobradas em comparação com a entrada. |
