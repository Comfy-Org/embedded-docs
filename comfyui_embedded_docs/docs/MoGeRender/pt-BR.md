# MoGe Render

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeRender/en.md)

## Visão Geral

Este nó recebe um pacote MOGE_GEOMETRY (produzido por um nó de estimativa de profundidade/normal MoGe) e o renderiza em um formato de imagem padrão. Você pode optar por gerar um mapa de profundidade, um mapa de profundidade colorido, um mapa normal ou uma máscara.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `moge_geometry` | O pacote de dados geométricos de um nó de estimativa MoGe. | MOGE_GEOMETRY | Sim | N/A |
| `output` | O tipo de imagem a ser renderizada a partir dos dados geométricos. DirectX vs OpenGL controla a convenção do canal verde do mapa normal. DirectX: verde = -Y para baixo (Unreal). OpenGL: verde = +Y para cima (Blender, Substance, Unity, glTF). (padrão: "depth") | COMBO | Sim | `"depth"`<br>`"depth_colored"`<br>`"normal_opengl"`<br>`"normal_directx"`<br>`"mask"` |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `IMAGE` | A imagem renderizada como um lote de tensores RGB. O conteúdo depende do modo de `output`: um mapa de profundidade em escala de cinza, um mapa de profundidade colorido, um mapa normal ou uma máscara. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeRender/pt-BR.md)

---
**Source fingerprint (SHA-256):** `45ba499e746ce46f9b6f7773e3218bcf80ad2e8d65940b38e248cc2f20c8b2fe`
