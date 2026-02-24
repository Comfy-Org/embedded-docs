> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageC_VAEEncode/pt-BR.md)

O nó StableCascade_StageC_VAEEncode processa imagens por meio de um codificador VAE para gerar representações latentes para os modelos Stable Cascade. Ele recebe uma imagem de entrada e a comprime usando o modelo VAE especificado, em seguida, gera duas representações latentes: uma para o estágio C e um espaço reservado para o estágio B. O parâmetro `compression` controla o quanto a imagem é reduzida antes da codificação.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sim | - | A imagem de entrada a ser codificada no espaço latente |
| `vae` | VAE | Sim | - | O modelo VAE usado para codificar a imagem |
| `compression` | INT | Não | 4-128 | O fator de compressão aplicado à imagem antes da codificação (padrão: 42) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `stage_c` | LATENT | A representação latente codificada para o estágio C do modelo Stable Cascade |
| `stage_b` | LATENT | Uma representação latente reservada para o estágio B (atualmente retorna zeros) |
