> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerEncode/pt-BR.md)

O nó PhotoMakerEncode processa imagens e texto para gerar dados de condicionamento para geração de imagens por IA. Ele recebe uma imagem de referência e um prompt de texto, criando embeddings que podem ser usados para orientar a geração de imagens com base nas características visuais da imagem de referência. O nó procura especificamente pelo token "photomaker" no texto para determinar onde aplicar o condicionamento baseado em imagem.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `photomaker` | PHOTOMAKER | Sim | - | O modelo PhotoMaker usado para processar a imagem e gerar embeddings |
| `image` | IMAGE | Sim | - | A imagem de referência que fornece características visuais para o condicionamento |
| `clip` | CLIP | Sim | - | O modelo CLIP usado para tokenização e codificação de texto |
| `text` | STRING | Sim | - | O prompt de texto para geração de condicionamento (padrão: "photograph of photomaker") |

**Observação:** Quando o texto contém a palavra "photomaker", o nó aplica o condicionamento baseado em imagem naquela posição do prompt. Se "photomaker" não for encontrado no texto, o nó gera um condicionamento de texto padrão sem influência da imagem.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Os dados de condicionamento contendo embeddings de imagem e texto para orientar a geração de imagens |
