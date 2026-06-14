# Converter Geometria DA3 em Malha

Este nó converte um pacote DA3_GEOMETRY em uma malha 3D, reprojetando o mapa de profundidade e triangulando a nuvem de pontos resultante. Ele processa uma única imagem de um lote e produz uma malha texturizada ou não texturizada adequada para renderização 3D.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `da3_geometry` | O pacote DA3_GEOMETRY contendo mapa de profundidade, mapa de confiança opcional, mapa de céu opcional e imagem de origem | DA3_GEOMETRY | Sim | - |
| `batch_index` | Qual imagem de um lote converter. As contagens de vértices por imagem diferem, portanto os lotes não podem ser empilhados (padrão: 0) | INT | Sim | 0 a 4096 |
| `decimation` | Passo do vértice. 1 = resolução total, 2 = metade, etc. (padrão: 1) | INT | Sim | 1 a 8 |
| `discontinuity_threshold` | Descarta triângulos cuja extensão de profundidade 3x3 exceda esta fração. 0 = desligado (padrão: 0,04) | FLOAT | Sim | 0,0 a 1,0 |
| `confidence_threshold` | Exclui pixels cuja confiança normalizada por imagem esteja abaixo deste valor. 0 = manter todos, 1 = manter apenas o pixel mais confiante. Usado quando a geometria possui um mapa de confiança (modelos Pequeno/Base) (padrão: 0,1) | FLOAT | Sim | 0,0 a 1,0 |
| `use_sky_mask` | Exclui pixels de probabilidade de céu (céu >= 0,5) da malha. Usado quando a geometria possui um mapa de céu (modelos Mono/Métrico) (padrão: Verdadeiro) | BOOLEANO | Sim | Verdadeiro ou Falso |
| `texture` | Usa a imagem de origem como textura de cor base (padrão: Verdadeiro) | BOOLEANO | Sim | Verdadeiro ou Falso |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `MESH` | Uma malha 3D triangulada com vértices, faces, coordenadas UV e textura opcional | MALHA |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DA3GeometryToMesh/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1d311223a8d131030bcd4930d21852a21ac9dd5758e7f8b8d20b1cf68698893b`
