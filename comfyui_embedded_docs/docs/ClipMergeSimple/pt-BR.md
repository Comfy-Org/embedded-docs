> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeSimple/pt-BR.md)

`CLIPMergeSimple` é um nó avançado de mesclagem de modelos usado para combinar dois codificadores de texto CLIP com base em uma proporção especificada.

Este nó é especializado em mesclar dois modelos CLIP com base em uma proporção especificada, combinando efetivamente suas características. Ele aplica seletivamente patches de um modelo a outro, excluindo componentes específicos como IDs de posição e escala logit, para criar um modelo híbrido que combina características de ambos os modelos de origem.

## Entradas

| Parâmetro | Tipo de Dados | Tipo de Entrada | Padrão | Faixa | Descrição |
|-----------|---------------|-----------------|--------|-------|-----------|
| `clip1` | CLIP | OBRIGATÓRIO | - | - | O primeiro modelo CLIP a ser mesclado. Serve como modelo base para o processo de mesclagem. |
| `clip2` | CLIP | OBRIGATÓRIO | - | - | O segundo modelo CLIP a ser mesclado. Seus patches-chave, exceto IDs de posição e escala logit, são aplicados ao primeiro modelo com base na proporção especificada. |
| `ratio` | FLOAT | OBRIGATÓRIO | 1.0 | 0.0 - 1.0 (passo: 0.01) | Determina a proporção de características do segundo modelo a serem mescladas no primeiro modelo. Uma proporção de 1.0 significa adotar totalmente as características do segundo modelo, enquanto 0.0 mantém apenas as características do primeiro modelo. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `clip` | CLIP | O modelo CLIP mesclado resultante, incorporando características de ambos os modelos de entrada de acordo com a proporção especificada. |

## Mecanismo de Mesclagem Explicado

### Algoritmo de Mesclagem

O nó usa média ponderada para mesclar os dois modelos:

1. **Clonar Modelo Base**: Primeiro clona `clip1` como modelo base
2. **Obter Patches**: Obtém todos os patches-chave de `clip2`
3. **Filtrar Chaves Especiais**: Ignora chaves que terminam com `.position_ids` e `.logit_scale`
4. **Aplicar Mesclagem Ponderada**: Usa a fórmula `(1.0 - ratio) * clip1 + ratio * clip2`

### Parâmetro de Proporção Explicado

- **ratio = 0.0**: Usa totalmente clip1, ignora clip2
- **ratio = 0.5**: Contribuição de 50% de cada modelo
- **ratio = 1.0**: Usa totalmente clip2, ignora clip1

## Casos de Uso

1. **Fusão de Estilo de Modelo**: Combine características de modelos CLIP treinados em dados diferentes
2. **Otimização de Desempenho**: Equilibre pontos fortes e fracos de diferentes modelos
3. **Pesquisa Experimental**: Explore combinações de diferentes codificadores CLIP

---
**Source fingerprint (SHA-256):** `0d3c8388dbe88675ea7fb51161ab41ce898bcf63983b3d2817b16ec5bfa613e5`
