> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SD_4XUpscale_Conditioning/pt-BR.md)

O nó SD_4XUpscale_Conditioning prepara dados de condicionamento para o processo de aumento de escala (upscaling) de imagens usando modelos de difusão. Ele recebe imagens de entrada e dados de condicionamento, aplica redimensionamento e aumento de ruído para criar um condicionamento modificado que orienta o processo de upscaling. O nó gera como saída tanto o condicionamento positivo quanto o negativo, juntamente com representações latentes para as dimensões da imagem ampliada.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Sim | - | Imagens de entrada a serem ampliadas |
| `positive` | CONDITIONING | Sim | - | Dados de condicionamento positivo que orientam a geração em direção ao conteúdo desejado |
| `negative` | CONDITIONING | Sim | - | Dados de condicionamento negativo que afastam a geração de conteúdos indesejados |
| `scale_ratio` | FLOAT | Não | 0.0 - 10.0 | Fator de escala aplicado às imagens de entrada (padrão: 4.0) |
| `noise_augmentation` | FLOAT | Não | 0.0 - 1.0 | Quantidade de ruído a ser adicionada durante o processo de upscaling (padrão: 0.0) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Condicionamento positivo modificado com as informações de upscaling aplicadas |
| `negative` | CONDITIONING | Condicionamento negativo modificado com as informações de upscaling aplicadas |
| `latent` | LATENT | Representação latente vazia que corresponde às dimensões da imagem ampliada |
