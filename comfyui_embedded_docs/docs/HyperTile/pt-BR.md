> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HyperTile/pt-BR.md)

O nó HyperTile aplica uma técnica de mosaico ao mecanismo de atenção em modelos de difusão para otimizar o uso de memória durante a geração de imagens. Ele divide o espaço latente em blocos menores e os processa separadamente, depois remonta os resultados. Isso permite trabalhar com tamanhos de imagem maiores sem esgotar a memória.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo de difusão ao qual aplicar a otimização HyperTile |
| `tile_size` | INT | Não | 1-2048 | O tamanho alvo do bloco para processamento (padrão: 256) |
| `swap_size` | INT | Não | 1-128 | Controla como os blocos são reorganizados durante o processamento (padrão: 2) |
| `max_depth` | INT | Não | 0-10 | Nível máximo de profundidade para aplicar o mosaico (padrão: 0) |
| `scale_depth` | BOOLEAN | Não | - | Se deve dimensionar o tamanho do bloco com base no nível de profundidade (padrão: False) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo modificado com a otimização HyperTile aplicada |
