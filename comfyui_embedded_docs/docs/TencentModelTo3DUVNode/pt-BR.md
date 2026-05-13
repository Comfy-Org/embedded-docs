> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentModelTo3DUVNode/pt-BR.md)

Este nó utiliza a API Tencent Hunyuan3D para realizar o desdobramento UV em um modelo 3D. Ele recebe um arquivo de modelo 3D como entrada, envia-o para a API para processamento e retorna o modelo processado nos formatos OBJ e FBX, juntamente com uma imagem de textura UV gerada. O modelo de entrada deve ter menos de 30.000 faces.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `model_3d` | FILE3D | Sim | GLB<br>OBJ<br>FBX | Modelo 3D de entrada (GLB, OBJ ou FBX). O modelo deve ter menos de 30.000 faces. |
| `seed` | INT | Não | 0 a 2147483647 | Um valor de semente (padrão: 1). Isso controla se o nó deve ser executado novamente, mas os resultados são não determinísticos independentemente do valor da semente. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `OBJ` | FILE3D | O arquivo de modelo 3D processado no formato OBJ. |
| `FBX` | FILE3D | O arquivo de modelo 3D processado no formato FBX. |
| `uv_image` | IMAGE | A imagem de textura UV gerada. |

---
**Source fingerprint (SHA-256):** `16bf094cfc3146e9d302d73862d2080b94c5aa2d575221d3c8316a3cf69fc5e1`
