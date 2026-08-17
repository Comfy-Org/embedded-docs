# CLIPMergeSimple

`CLIPMergeSimple` mescla dois modelos de codificador de texto CLIP em um único modelo. Ele clona o primeiro modelo CLIP como base e aplica patches de parâmetros ponderados provenientes do segundo modelo CLIP, de modo que o resultado combine características de ambos. A configuração de `ratio` controla o quão fortemente cada modelo contribui; no valor padrão de 1.0, o primeiro modelo é usado sem alterações.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|--------------|-------------|-----------|
| `clip1` | O primeiro modelo CLIP. Ele é clonado e usado como modelo base para a mesclagem. | CLIP | Sim | — |
| `clip2` | O segundo modelo CLIP. Seus patches principais são aplicados ao modelo base, exceto pelos patches cujas chaves terminam em `.position_ids` ou `.logit_scale`. | CLIP | Sim | — |
| `ratio` | Controla a força relativa dos dois modelos. O modelo base (`clip1`) mantém uma força igual a `ratio`, e os patches de `clip2` são aplicados com uma força de `1.0 - ratio`. No valor padrão de 1.0, a saída é igual a `clip1`; valores menores incorporam mais de `clip2`; em 0.0, os patches de `clip2` são aplicados com força total. | FLOAT | Sim | 0.0 a 1.0 (padrão: 1.0, passo: 0.01) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-----------|--------------|
| `clip` | O modelo CLIP mesclado: um clone de `clip1` com os patches de `clip2` aplicados de acordo com `ratio`. | CLIP |

## Mecanismo de Mesclagem Explicado

### Algoritmo de Mesclagem

O nó utiliza aplicação ponderada de patches para combinar os dois modelos:

1. **Clonar o Modelo Base**: Clona `clip1` para servir como modelo base.
2. **Obter Patches**: Coleta todos os patches principais (valores de parâmetros) de `clip2`.
3. **Filtrar Chaves Especiais**: Ignora chaves que terminam em `.position_ids` e `.logit_scale`, para que esses parâmetros permaneçam inalterados.
4. **Aplicar Mesclagem Ponderada**: Aplica os patches de `clip2` ao modelo base clonado com uma força de patch de `1.0 - ratio`, enquanto o modelo base mantém uma força de `ratio`.

### Explicação do Parâmetro Ratio

- **ratio = 1.0**: A força da base é 1.0 e a força do patch é 0.0, portanto a saída é idêntica a `clip1` (padrão).
- **ratio = 0.5**: A força da base e a força do patch são ambas 0.5, portanto ambos os modelos contribuem com igual intensidade.
- **ratio = 0.0**: A força da base é 0.0 e a força do patch é 1.0, portanto os patches de `clip2` são aplicados com força total.

## Casos de Uso

1. **Fusão de Estilos de Modelo**: Combinar características de modelos CLIP treinados com dados diferentes.
2. **Otimização de Desempenho**: Equilibrar pontos fortes e fracos de diferentes modelos.
3. **Pesquisa Experimental**: Explorar combinações de diferentes codificadores CLIP.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeSimple/pt-BR.md)

---
**Source fingerprint (SHA-256):** `42c4b2042c56c3f21a9416aa577e2d41fef1dcc749c4e5c7953851110a4fb6bc`
