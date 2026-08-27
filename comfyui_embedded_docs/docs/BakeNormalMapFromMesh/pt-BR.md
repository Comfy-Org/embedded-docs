# BakeNormalMapFromMesh

Este nó grava um mapa normal em espaço tangente de uma malha de alta poligonagem para o layout UV de uma malha de baixa poligonagem, capturando detalhes de superfície perdidos durante a decimação. Conecte a malha de baixa poligonagem com UVs e a malha de alta poligonagem de onde ela veio, e o nó gera uma imagem pronta para a entrada `normal_map` do nó Apply Texture To Mesh.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `low_poly` | A malha de baixa poligonagem com UVs que recebe o detalhe gravado. Deve ter UVs existentes; o nó nunca desembrulha. | MESH | Sim | — |
| `high_poly` | A malha de alta poligonagem cujos detalhes de superfície são gravados no layout UV da malha de baixa poligonagem. | MESH | Sim | — |
| `resolution` | Comprimento da aresta em pixels do mapa normal quadrado de saída (padrão: 1024). | INT | Sim | 64 a 8192 (passo 64) |
| `cage_distance` | Faixa de busca na superfície, como uma fração da diagonal da caixa delimitadora. Aumente para regiões erradas/faltantes sob decimação intensa; diminua se estiver capturando através de lacunas. Padrão: 0,05. | FLOAT | Sim | 0,001 a 0,5 (passo 0,001) |
| `ignore_backfaces` | Ignora superfícies de alta poligonagem voltadas para longe do texel, para que fendas/espaços fechados não capturem a parede oposta. Desative apenas se a orientação (winding) da malha de alta poligonagem estiver inconsistente. Padrão: true. | BOOLEAN | Sim | true / false |

Nota: `low_poly` deve ter coordenadas de UV. Se não tiver, o nó gera um erro porque ele grava no layout UV existente e não desembrulha a malha. Quando `low_poly` é um lote, cada item é gravado em ordem; se `high_poly` contiver apenas um item, esse item é reutilizado para todos os itens do lote. Malhas vazias no lote são ignoradas com um aviso e produzem um mapa normal cinza médio uniforme (0,5).

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `normal_map` | O mapa normal em espaço tangente gravado (convenção glTF/OpenGL +Y) como uma imagem RGB quadrada de resolução × resolução com valores em [0,1]. Conecte-o à entrada `normal_map` do nó Apply Texture To Mesh. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeNormalMapFromMesh/pt-BR.md)

---
**Source fingerprint (SHA-256):** `29df10014b5998b741d71db21d0c982d7bca85ad966a720063af15062e203322`
