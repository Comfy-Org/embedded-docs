# HyperTile

O nó HyperTile aplica uma técnica de tiling ao mecanismo de atenção em modelos de difusão para otimizar o uso de memória durante a geração de imagens. Ele divide o espaço latente em tiles menores e os processa separadamente, remontando os resultados em seguida. Isso permite trabalhar com tamanhos de imagem maiores sem esgotar a memória.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo de difusão ao qual aplicar a otimização HyperTile | MODEL | Sim | - |
| `tamanho_do_tile` | O tamanho alvo do tile para processamento (padrão: 256). Internamente, o valor é limitado a um mínimo de 32 e depois dividido por 8 para obter o tamanho efetivo do tile. | INT | Sim | 1 - 2048 |
| `tamanho_da_troca` | Controla como os tiles são reorganizados durante o processamento para melhorar a eficiência. Valores maiores permitem mais variação nos tamanhos dos tiles (padrão: 2) | INT | Sim | 1 - 128 |
| `profundidade_máxima` | O nível máximo de profundidade (escala de resolução) para aplicar o tiling. Um valor de 0 aplica o tiling apenas na resolução mais alta (padrão: 0) | INT | Sim | 0 - 10 |
| `escala_de_profundidade` | Quando habilitado, o tamanho do tile é dimensionado proporcionalmente em níveis de profundidade maiores. Isso pode ajudar a manter a qualidade em resoluções mais baixas (padrão: False) | BOOLEAN | Sim | True / False |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo modificado com a otimização HyperTile aplicada | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HyperTile/pt-BR.md)

---
**Source fingerprint (SHA-256):** `fb2fa29a403b6b7de7d5263240cc51a74126078457a3ff9ea63aeded45b9b74a`
