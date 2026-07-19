# SavePointCloud

O nó Save Point Cloud salva um arquivo de nuvem de pontos 3D no diretório de saída e, opcionalmente, fornece dados de pré-visualização para o visualizador 3D. Ele gerencia a nomeação e o salvamento do arquivo, além de transmitir informações de câmera e modelo para fins de exibição.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|---------------|-------------|-------|
| `model_3d` | Arquivo de nuvem de pontos (.ply) | FILE3D_POINT_CLOUD_ANY ou FILE3D_PLY | Sim | - |
| `filename_prefix` | Prefixo para o nome do arquivo salvo (padrão: "3d/ComfyUI") | STRING | Sim | - |
| `viewport_state` | Estado atual da janela de visualização contendo informações de câmera e modelo | LOAD3D | Sim | - |
| `model_3d_info` | Informações adicionais do modelo para o visualizador 3D | LOAD3D_MODEL_INFO | Não | - |
| `camera_info` | Informações da câmera para o visualizador 3D | LOAD3D_CAMERA | Não | - |
| `width` | Largura da exibição de pré-visualização em pixels (padrão: 1024) | INT | Sim | 1 a 4096 |
| `height` | Altura da exibição de pré-visualização em pixels (padrão: 1024) | INT | Sim | 1 a 4096 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-------------|---------------|
| `model_3d` | O arquivo de nuvem de pontos salvo | FILE3D_POINT_CLOUD_ANY |
| `model_3d_info` | Informações do modelo para o visualizador 3D | LOAD3D_MODEL_INFO |
| `camera_info` | Informações da câmera para o visualizador 3D | LOAD3D_CAMERA |
| `width` | Largura da exibição de pré-visualização | INT |
| `height` | Altura da exibição de pré-visualização | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SavePointCloud/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ce8f005c431843a57d87a4aff2eed7a1604ebdf360f83b3aaaadc3ed364d218a`
