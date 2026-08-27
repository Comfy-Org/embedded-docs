# BakeNormalMapFromMesh

Este nó faz o bake de um mapa de normais em espaço tangente de uma malha high-poly para o layout de UV de uma malha low-poly, capturando detalhes de superfície que foram perdidos durante a decimação. Conecte a malha low-poly com UVs e a malha high-poly da qual ela se originou, e o nó gera uma imagem pronta para a entrada `normal_map` do nó Apply Texture To Mesh.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `low_poly` | A malha low-poly com UVs que recebe o detalhe assado. Deve ter UVs existentes; o nó nunca faz unwrap da malha. | MESH | Sim | — |
| `high_poly` | A malha high-poly cujos detalhes de superfície são assados no layout de UV da malha low-poly. | MESH | Sim | — |
| `resolution` | Comprimento do lado, em pixels, do mapa de normais quadrado de saída (padrão: 1024). | INT | Sim | 64 to 8192 (step 64) |
| `cage_distance` | Faixa de busca na superfície, como fração da diagonal do bounding box. Aumente para regiões incorretas ou ausentes sob decimação intensa; diminua se ela capturar através de vãos. Padrão: 0.05. | FLOAT | Sim | 0.001 to 0.5 (step 0.001) |
| `ignore_backfaces` | Ignora superfícies high-poly que estão voltadas para longe do texel, para que frestas/espaços fechados não capturem a parede oposta. Desative apenas se a orientação das faces (winding) da malha high-poly estiver inconsistente. Padrão: true. | BOOLEAN | Sim | true / false |

Nota: `low_poly` deve ter coordenadas de UV. Se não houver nenhuma, o nó gera um erro porque ele faz o bake no layout de UV existente e não faz unwrap da malha. Quando `low_poly` for um lote, cada item passa pelo bake em ordem; se `high_poly` contiver apenas um item, esse item é reutilizado para todos os itens do lote. Malhas vazias no lote são ignoradas com um aviso e produzem um mapa de normais cinza médio uniforme (0.5).

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `normal_map` | O mapa de normais em espaço tangente gerado (convenção glTF/OpenGL +Y) como uma imagem RGB quadrada de resolução × resolução, com valores em [0,1]. Conecte-o à entrada `normal_map` do nó Apply Texture To Mesh. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeNormalMapFromMesh/pt-BR.md)

---
**Source fingerprint (SHA-256):** `29df10014b5998b741d71db21d0c982d7bca85ad966a720063af15062e203322`
