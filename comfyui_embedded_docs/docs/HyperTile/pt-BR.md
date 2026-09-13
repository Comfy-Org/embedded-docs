# HyperTile

O HyperTile aplica uma técnica de tiling ao mecanismo de atenção dentro de modelos de difusão para reduzir o uso de memória durante a geração de imagens. Ele divide o espaço latente em tiles menores, processa a atenção de cada tile separadamente e, em seguida, remonta os resultados. Isso possibilita trabalhar com tamanhos de imagem maiores sem ficar sem memória.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo de difusão ao qual aplicar a otimização do HyperTile | MODEL | Sim | - |
| `tile_size` | O tamanho do tile de destino para processamento (padrão: 256). Internamente, o valor é limitado a um mínimo de 32 e depois dividido por 8 para obter o tamanho efetivo do tile. | INT | Sim | 1 - 2048 |
| `swap_size` | Controla como os tiles são reorganizados durante o processamento para melhorar a eficiência. Valores maiores permitem mais variação nos tamanhos dos tiles (padrão: 2) | INT | Sim | 1 - 128 |
| `max_depth` | O nível máximo de profundidade (escala de resolução) para aplicar o tiling. Um valor de 0 aplica o tiling apenas na resolução mais alta (padrão: 0) | INT | Sim | 0 - 10 |
| `scale_depth` | Quando ativado, o tamanho do tile é escalado proporcionalmente em níveis mais profundos. Isso pode ajudar a manter a qualidade em resoluções mais baixas (padrão: False) | BOOLEAN | Sim | True / False |

Observação: `tile_size`, `swap_size`, `max_depth` e `scale_depth` são marcados como entradas avançadas, portanto só são exibidos quando as opções avançadas estão ativadas na interface.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo modificado com a otimização do HyperTile aplicada | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HyperTile/pt-BR.md)

---
**Source fingerprint (SHA-256):** `fb2fa29a403b6b7de7d5263240cc51a74126078457a3ff9ea63aeded45b9b74a`
