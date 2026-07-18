# Save3DAdvanced

Este nó salva um modelo 3D no diretório de saída do seu ComfyUI e oferece recursos avançados de pré-visualização. Ele permite que você especifique o nome do arquivo de saída, as dimensões da pré-visualização e, opcionalmente, passe informações de câmera e modelo para uma experiência aprimorada no visualizador 3D.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | Arquivo de modelo 3D de um nó 3D upstream. | FILE3D | Sim | GLB, GLTF, FBX, OBJ, STL, USDZ ou qualquer formato 3D |
| `filename_prefix` | Prefixo para o nome do arquivo salvo. Um contador e a extensão do arquivo serão anexados automaticamente. (padrão: "3d/ComfyUI") | STRING | Sim | Qualquer string de nome de arquivo válida |
| `viewport_state` | O estado atual da janela de visualização, normalmente de um nó visualizador 3D. | LOAD3D | Sim | - |
| `model_3d_info` | Informações opcionais do modelo 3D para a pré-visualização. | LOAD3DMODELINFO | Não | - |
| `camera_info` | Informações opcionais da câmera para a pré-visualização. | LOAD3DCAMERA | Não | - |
| `width` | Largura da pré-visualização em pixels. (padrão: 1024) | INT | Sim | 1 a 4096 |
| `height` | Altura da pré-visualização em pixels. (padrão: 1024) | INT | Sim | 1 a 4096 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `model_3d` | O arquivo de modelo 3D salvo. | FILE3D |
| `model_3d_info` | Informações do modelo 3D transmitidas para nós downstream. | LOAD3DMODELINFO |
| `camera_info` | Informações da câmera transmitidas para nós downstream. | LOAD3DCAMERA |
| `width` | O valor da largura transmitido para nós downstream. | INT |
| `height` | O valor da altura transmitido para nós downstream. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Save3DAdvanced/pt-BR.md)

---
**Source fingerprint (SHA-256):** `2c7d42b1875bb292e675526a2b38fcc8856c8ac45de25ac7b69d92323f0b7ae0`
