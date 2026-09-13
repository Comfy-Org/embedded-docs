# Gerar Mapa Normal da Malha

Este nó realiza o bake de um mapa de normais em espaço tangente de uma malha high-poly sobre o layout de UV de uma malha low-poly, capturando detalhes de superfície que foram perdidos durante a decimação. Conecte a malha low-poly com UV desdobradas e a malha high-poly da qual ela se originou, e o nó produz uma imagem pronta para a entrada `normal_map` de Apply Texture To Mesh.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `low_poly` | A malha low-poly com UV desdobradas que recebe o detalhe gerado. Deve ter UVs existentes; o nó nunca desdobra. | MESH | Sim | — |
| `high_poly` | A malha high-poly cujo detalhe de superfície é gerado no layout de UV da low-poly. | MESH | Sim | — |
| `resolution` | Comprimento da aresta em pixels do mapa de normais quadrado de saída (padrão: 1024). | INT | Sim | 64 a 8192 (passo 64) |
| `cage_distance` | Faixa de busca na superfície, como uma fração da diagonal da caixa delimitadora. Aumente para regiões erradas/ausentes sob decimação pesada; diminua se ela capturar através de lacunas. Padrão: 0.05. | FLOAT | Sim | 0.001 a 0.5 (passo 0.001) |
| `ignore_backfaces` | Ignora superfícies high-poly voltadas para longe do texel, para que fendas/espaços fechados não capturem a parede oposta. Desative apenas se a orientação das faces da malha high-poly for inconsistente. Padrão: true. | BOOLEAN | Sim | true / false |

Observação: `low_poly` deve ter coordenadas UV. Se não tiver nenhuma, o nó lança um erro porque faz o bake sobre o layout de UV existente e não desdobra a malha. Quando `low_poly` é um lote, cada item é processado em ordem; se `high_poly` contiver apenas um item, esse item é reutilizado para cada item do lote. Malhas vazias no lote são ignoradas com um aviso e produzem um mapa de normais cinza médio uniforme (0.5). Se as UVs da low-poly extravasarem o intervalo [0,1], elas são ajustadas uniformemente para [0,1] (com um aviso quando o layout parecer em mosaico/UDIM), para que o bake e Apply Texture To Mesh usem as mesmas UVs.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `normal_map` | O mapa de normais em espaço tangente resultante do bake (convenção glTF/OpenGL +Y) como uma imagem RGB quadrada resolution × resolution com valores em [0,1]. Conecte-o à entrada `normal_map` de Apply Texture To Mesh. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeNormalMapFromMesh/pt-BR.md)

---
**Source fingerprint (SHA-256):** `29df10014b5998b741d71db21d0c982d7bca85ad966a720063af15062e203322`
