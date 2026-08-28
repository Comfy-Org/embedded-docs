# ClipMergeSimple

`CLIPMergeSimple` é um nó de mesclagem de modelos que combina dois codificadores de texto CLIP com base em uma proporção especificada. Ele clona o primeiro modelo CLIP e aplica patches ponderados do segundo modelo CLIP, ignorando IDs de posição e componentes de escala logit, para produzir um modelo híbrido que combina características de ambas as fontes.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `clip1` | O primeiro modelo CLIP a ser mesclado. Ele serve como modelo base para o processo de mesclagem. | CLIP | Sim | - |
| `clip2` | O segundo modelo CLIP a ser mesclado. Seus patches de chave, exceto IDs de posição e escala logit, são aplicados ao primeiro modelo com base na proporção especificada. | CLIP | Sim | - |
| `ratio` | Determina a proporção de características do segundo modelo a serem incorporadas ao primeiro modelo. Uma proporção de 1.0 significa adotar totalmente as características do segundo modelo, enquanto 0.0 mantém apenas as características do primeiro modelo. Padrão: 1.0. | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `clip` | O modelo CLIP mesclado resultante, que incorpora características de ambos os modelos de entrada de acordo com a proporção especificada. | CLIP |

## Mecanismo de Mesclagem Explicado

### Algoritmo de Mesclagem

O nó usa média ponderada para mesclar os dois modelos:

1. **Clonar Modelo Base**: Primeiro clona `clip1` como modelo base
2. **Obter Patches**: Obtém todos os patches de chave de `clip2`
3. **Filtrar Chaves Especiais**: Ignora chaves que terminam com `.position_ids` e `.logit_scale`
4. **Aplicar Mesclagem Ponderada**: Usa a fórmula `(1.0 - ratio) * clip1 + ratio * clip2`

### Parâmetro Ratio Explicado

- **ratio = 0.0**: Usa totalmente clip1, ignora clip2
- **ratio = 0.5**: Contribuição de 50% de cada modelo
- **ratio = 1.0**: Usa totalmente clip2, ignora clip1

## Casos de Uso

1. **Fusão de Estilos de Modelo**: Combinar características de modelos CLIP treinados em dados diferentes
2. **Otimização de Desempenho**: Equilibrar pontos fortes e fracos de diferentes modelos
3. **Pesquisa Experimental**: Explorar combinações de diferentes codificadores CLIP

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClipMergeSimple/pt-BR.md)

---
**Source fingerprint (SHA-256):** `42c4b2042c56c3f21a9416aa577e2d41fef1dcc749c4e5c7953851110a4fb6bc`
