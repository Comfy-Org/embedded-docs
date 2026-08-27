# MoGe Render

## Visão Geral

Este nó recebe um pacote MOGE_GEOMETRY (produzido por um nó de estimativa de profundidade/normais MoGe) e o renderiza em um formato de imagem padrão. Você pode optar por gerar um mapa de profundidade, um mapa de profundidade colorido, um mapa de normais ou uma máscara.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `moge_geometry` | O pacote de dados de geometria de um nó de estimativa MoGe. | MOGE_GEOMETRY | Sim | N/A |
| `output` | O tipo de imagem a ser renderizado a partir dos dados de geometria. `depth` gera um mapa de profundidade em escala de cinza, `depth_colored` gera um mapa de profundidade colorido, `normal_opengl` e `normal_directx` geram mapas de normais, e `mask` gera uma máscara. DirectX vs OpenGL controla a convenção do canal verde do mapa de normais. DirectX: verde = -Y para baixo (Unreal). OpenGL: verde = +Y para cima (Blender, Substance, Unity, glTF). (padrão: `"depth"`) | COMBO | Sim | `"depth"`<br>`"depth_colored"`<br>`"normal_opengl"`<br>`"normal_directx"`<br>`"mask"` |

**Observação:** O pacote de geometria deve conter dados compatíveis com o modo `output` selecionado. Os modos `depth` e `depth_colored` exigem dados de profundidade no pacote. Os modos `normal_opengl` e `normal_directx` exigem dados de normais, ou dados de pontos a partir dos quais as normais são derivadas. O modo `mask` exige dados de máscara. Se os dados necessários estiverem ausentes, o nó gera um erro.

## Saídas

| Nome de Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `IMAGE` | A imagem renderizada como um lote de tensores RGB. O conteúdo depende do modo `output`: um mapa de profundidade em escala de cinza, um mapa de profundidade colorido, um mapa de normais ou uma máscara convertida em RGB. O tamanho do lote de saída corresponde ao tamanho do lote da geometria de entrada. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeRender/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ca602f7a7d6eb1b1d00986459621d94ecf9331266ff1d3ce7bb759d24448a346`
