# Converter Geometria DA3 para Malha

Este nó converte um pacote DA3_GEOMETRY em uma malha 3D desprojetando o mapa de profundidade e triangulando a nuvem de pontos resultante. Ele processa uma única imagem de um lote e produz uma malha texturizada ou não texturizada adequada para renderização 3D.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `da3_geometry` | O pacote DA3_GEOMETRY contendo mapa de profundidade, mapa de confiança opcional, mapa de céu opcional e imagem de origem | DA3_GEOMETRY | Sim | - |
| `batch_index` | Qual imagem de um lote converter. As contagens de vértices por imagem diferem, portanto lotes não podem ser empilhados (padrão: 0). Deve ser menor que o tamanho do lote da geometria de entrada, caso contrário, um erro é gerado | INT | Sim | 0 a 4096 |
| `decimation` | Passo de vértices. 1 = resolução total, 2 = metade, etc. (padrão: 1) | INT | Sim | 1 a 8 |
| `discontinuity_threshold` | Descarta triângulos cuja extensão de profundidade 3x3 excede esta fração. 0 = desativado (padrão: 0.04) | FLOAT | Sim | 0.0 a 1.0 |
| `confidence_threshold` | Exclui pixels cuja confiança normalizada por imagem está abaixo deste valor. 0 = manter todos, 1 = manter apenas o único pixel mais confiável. Usado quando a geometria tem um mapa de confiança (modelos Small/Base) (padrão: 0.1) | FLOAT | Sim | 0.0 a 1.0 |
| `use_sky_mask` | Exclui pixels com probabilidade de céu (céu >= 0.5) da malha. Usado quando a geometria tem um mapa de céu (modelos Mono/Metric) (padrão: True) | BOOLEAN | Sim | True ou False |
| `texture` | Usa a imagem de origem como textura de cor base (padrão: True) | BOOLEAN | Sim | True ou False |

Pixels com valores de profundidade não finitos, zero ou negativos são sempre excluídos da malha. Um erro é gerado se a malha resultante estiver vazia; a mensagem de erro sugere aumentar `discontinuity_threshold`, diminuir `confidence_threshold` ou desativar `use_sky_mask`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `MESH` | Uma malha 3D triangulada com vértices, faces, coordenadas UV e textura opcional | MESH |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DA3GeometryToMesh/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1d311223a8d131030bcd4930d21852a21ac9dd5758e7f8b8d20b1cf68698893b`
