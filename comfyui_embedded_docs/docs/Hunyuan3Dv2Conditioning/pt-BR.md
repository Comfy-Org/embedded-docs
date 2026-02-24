> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2Conditioning/pt-BR.md)

O nó Hunyuan3Dv2Conditioning processa a saída de visão do CLIP para gerar dados de condicionamento para modelos de vídeo. Ele extrai os embeddings do último estado oculto da saída de visão e cria pares de condicionamento tanto positivo quanto negativo. O condicionamento positivo utiliza os embeddings reais, enquanto o condicionamento negativo utiliza embeddings de valor zero com a mesma forma.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `clip_vision_output` | CLIP_VISION_OUTPUT | Sim | - | A saída de um modelo de visão CLIP contendo embeddings visuais |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Dados de condicionamento positivo contendo os embeddings de visão do CLIP |
| `negative` | CONDITIONING | Dados de condicionamento negativo contendo embeddings de valor zero que correspondem à forma dos embeddings positivos |
