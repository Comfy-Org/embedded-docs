> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeSimple/pt-BR.md)

`CLIPMergeSimple` é um nó avançado de fusão de modelos utilizado para combinar dois modelos de codificação de texto CLIP com base em uma proporção especificada.

Este nó é especializado em mesclar dois modelos CLIP com base em uma proporção especificada, combinando efetivamente suas características. Ele aplica seletivamente *patches* de um modelo a outro, excluindo componentes específicos como IDs de posição e escala de logit, para criar um modelo híbrido que combina recursos de ambos os modelos de origem.

## Entradas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-----------|-------------|
| `clip1`   | CLIP      | O primeiro modelo CLIP a ser mesclado. Serve como modelo base para o processo de fusão. |
| `clip2`   | CLIP      | O segundo modelo CLIP a ser mesclado. Seus *patches* principais, exceto os IDs de posição e a escala de logit, são aplicados ao primeiro modelo com base na proporção especificada. |
| `ratio`   | FLOAT     | Intervalo `0.0 - 1.0`. Determina a proporção de características do segundo modelo a serem incorporadas ao primeiro. Uma proporção de 1.0 significa adotar totalmente as características do segundo modelo, enquanto 0.0 mantém apenas as características do primeiro modelo. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-----------|-------------|
| `clip`    | CLIP      | O modelo CLIP resultante da fusão, incorporando características de ambos os modelos de entrada de acordo com a proporção especificada. |

## Mecanismo de Fusão Explicado

### Algoritmo de Fusão

O nó utiliza uma média ponderada para mesclar os dois modelos:

1. **Clonar Modelo Base**: Primeiro clona `clip1` como modelo base.
2. **Obter *Patches***: Obtém todos os *patches* principais de `clip2`.
3. **Filtrar Chaves Especiais**: Ignora chaves que terminam com `.position_ids` e `.logit_scale`.
4. **Aplicar Fusão Ponderada**: Usa a fórmula `(1.0 - ratio) * clip1 + ratio * clip2`.

### Explicação do Parâmetro Ratio

- **ratio = 0.0**: Usa totalmente o clip1, ignora o clip2.
- **ratio = 0.5**: Contribuição de 50% de cada modelo.
- **ratio = 1.0**: Usa totalmente o clip2, ignora o clip1.

## Casos de Uso

1. **Fusão de Estilos de Modelo**: Combinar características de modelos CLIP treinados em dados diferentes.
2. **Otimização de Desempenho**: Equilibrar pontos fortes e fracos de diferentes modelos.
3. **Pesquisa Experimental**: Explorar combinações de diferentes codificadores CLIP.
