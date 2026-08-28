# MoGeGeometryToFOV

Este nó deriva o campo de visão e a distância focal das intrínsecas da câmera armazenadas em um objeto de geometria MoGe. Ele pode retornar o FOV vertical, horizontal ou diagonal, em graus ou radianos. A saída de FOV vertical pode ser usada, por exemplo, para alimentar o nó SAM3DBody_Predict.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `moge_geometry` | O objeto de geometria MoGe. Ele deve conter uma matriz de intrínsecas e pelo menos um dos seguintes: dados de imagem, pontos ou profundidade, usados para ler a altura do pixel para a conversão da distância focal. | MOGE_GEOMETRY | Sim | — |
| `eixo` | O eixo ao longo do qual o FOV é calculado: "vertical" (fov_y), "horizontal" (fov_x) ou "diagonal" (padrão: "vertical"). | COMBO | Sim | "vertical"<br>"horizontal"<br>"diagonal" |
| `unidade` | Unidade de saída para o FOV (padrão: "degrees"). | COMBO | Sim | "degrees"<br>"radians" |

Nota: o nó gera um erro se `moge_geometry` não contiver intrínsecas (geometria panorâmica não possui nenhuma) ou se não contiver dados de imagem, pontos nem profundidade.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `fov` | O campo de visão ao longo do eixo selecionado, na unidade selecionada (degrees ou radians). | FLOAT |
| `focal_pixels` | A distância focal da lente em pixels, derivada da intrínseca vertical e da altura do pixel. | FLOAT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeGeometryToFOV/pt-BR.md)

---
**Source fingerprint (SHA-256):** `983dc984847f93a8e002c73982571ecb38b7bae9c3dc4c201d9be17f785dcaed`
