# HyperTile

O nó HyperTile aplica uma técnica de tileamento (divisão em tiles) ao mecanismo de atenção em modelos de difusão para otimizar o uso de memória durante a geração de imagens. Ele divide o espaço latente em tiles menores, processa-os separadamente e remonta os resultados. Isso permite trabalhar com tamanhos de imagem maiores sem esgotar a memória.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo de difusão ao qual aplicar a otimização HyperTile | MODEL | Sim | - |
| `tile_size` | O tamanho alvo do tile para processamento (padrão: 256). O tamanho efetivo do tile é arredondado para baixo até um múltiplo de 8, com um mínimo de 32. | INT | Não | 1 - 2048 |
| `swap_size` | O número de divisões candidatas de tiles consideradas quando o nó escolhe aleatoriamente como dividir a imagem. Um valor maior permite mais variação na divisão (padrão: 2) | INT | Não | 1 - 128 |
| `max_depth` | O nível máximo de profundidade (escala de resolução) para aplicar o tileamento. Um valor de 0 aplica o tileamento apenas na resolução mais alta (padrão: 0) | INT | Não | 0 - 10 |
| `scale_depth` | Quando habilitado, o tamanho do tile é escalado proporcionalmente em níveis de profundidade maiores. Isso pode ajudar a manter a qualidade em resoluções mais baixas (padrão: False) | BOOLEAN | Não | True / False |

Nota: `scale_depth` só tem efeito quando `max_depth` é maior que 0, porque no nível de resolução mais alta (profundidade 0) o tamanho do tile nunca é escalado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo modificado com a otimização HyperTile aplicada | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HyperTile/pt-BR.md)

---
**Source fingerprint (SHA-256):** `fb2fa29a403b6b7de7d5263240cc51a74126078457a3ff9ea63aeded45b9b74a`
