# MoGe Render

## Visão Geral

Este nó recebe um pacote MOGE_GEOMETRY (produzido por um nó de estimativa de profundidade/normais MoGe) e o renderiza em um formato de imagem padrão. Você pode optar por gerar um mapa de profundidade, um mapa de profundidade colorido, um mapa de normais ou uma máscara.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `moge_geometry` | O pacote de dados geométricos proveniente de um nó de estimativa MoGe. | MOGE_GEOMETRY | Sim | N/A |
| `output` | O tipo de imagem a ser renderizado a partir dos dados geométricos. DirectX vs OpenGL define a convenção do canal verde do mapa de normais. DirectX: verde = -Y para baixo (Unreal). OpenGL: verde = +Y para cima (Blender, Substance, Unity, glTF). (padrão: "depth") | COMBO | Sim | `"depth"`<br>`"depth_colored"`<br>`"normal_opengl"`<br>`"normal_directx"`<br>`"mask"` |

**Observação:** O modo `output` selecionado determina quais dados devem estar presentes em `moge_geometry`:
- `depth` e `depth_colored` exigem dados de profundidade. A profundidade é convertida em um mapa de disparidade normalizada (1/profundidade) usando recorte por percentis (0.1/99.9).
- `normal_opengl` e `normal_directx` exigem dados de normais, ou dados de pontos a partir dos quais as normais podem ser derivadas. O nó gera um erro se nenhum dos dois estiver presente.
- `mask` exige dados de máscara.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `IMAGE` | A imagem renderizada como um lote de tensores RGB. O conteúdo depende do modo `output`: um mapa de profundidade em tons de cinza, um mapa de profundidade colorido, um mapa de normais ou uma máscara. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeRender/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ca602f7a7d6eb1b1d00986459621d94ecf9331266ff1d3ce7bb759d24448a346`
