> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HyperTile/pt-BR.md)

O nó HyperTile aplica uma técnica de divisão em blocos ao mecanismo de atenção em modelos de difusão para otimizar o uso de memória durante a geração de imagens. Ele divide o espaço latente em blocos menores e os processa separadamente, depois remonta os resultados. Isso permite trabalhar com tamanhos de imagem maiores sem esgotar a memória.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|-----------|----------|-------|-------------|
| `modelo` | MODEL | Sim | - | O modelo de difusão ao qual aplicar a otimização HyperTile |
| `tamanho_do_tile` | INT | Não | 1 - 2048 | O tamanho alvo do bloco para processamento (padrão: 256). O tamanho efetivo do bloco é arredondado para baixo até um múltiplo de 8, com um mínimo de 32. |
| `tamanho_da_troca` | INT | Não | 1 - 128 | Controla como os blocos são reorganizados durante o processamento para melhorar a eficiência (padrão: 2) |
| `profundidade_máxima` | INT | Não | 0 - 10 | O nível máximo de profundidade (escala de resolução) para aplicar a divisão em blocos. Um valor de 0 aplica a divisão apenas na resolução mais alta (padrão: 0) |
| `escala_de_profundidade` | BOOLEAN | Não | Verdadeiro / Falso | Quando ativado, o tamanho do bloco é dimensionado proporcionalmente em níveis de profundidade maiores. Isso pode ajudar a manter a qualidade em resoluções mais baixas (padrão: Falso) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `modelo` | MODEL | O modelo modificado com a otimização HyperTile aplicada |

---
**Source fingerprint (SHA-256):** `d3c55e6a38abecc8fe612dbb91a3ba26de9bc5cf8a187f01cf4746550f62f40a`
