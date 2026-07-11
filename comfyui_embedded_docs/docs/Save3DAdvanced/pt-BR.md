# Save3DAdvanced

Este nó salva um modelo 3D em um arquivo no diretório de saída do ComfyUI, com controle avançado sobre as dimensões de saída e as configurações de câmera/viewport. Ele também encaminha o modelo 3D, as informações do modelo, as informações da câmera e as dimensões para nós subsequentes.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | Arquivo de modelo 3D proveniente de um nó 3D anterior. | FILE3D | Sim | GLB, GLTF, FBX, OBJ, STL, USDZ, Qualquer |
| `filename_prefix` | Prefixo para o nome do arquivo salvo (padrão: "3d/ComfyUI"). | STRING | Sim | Texto livre |
| `viewport_state` | Estado do viewport proveniente de um nó Carregar 3D, contendo informações da câmera e do modelo. | LOAD3D | Sim | - |
| `model_3d_info` | Informações opcionais do modelo 3D para substituir o estado do viewport. | LOAD3DMODELINFO | Não | - |
| `camera_info` | Informações opcionais da câmera para substituir o estado do viewport. | LOAD3DCAMERA | Não | - |
| `width` | Largura da pré-visualização de saída em pixels (padrão: 1024). | INT | Sim | 1 a 4096 |
| `height` | Altura da pré-visualização de saída em pixels (padrão: 1024). | INT | Sim | 1 a 4096 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `model_3d` | O arquivo de modelo 3D encaminhado da entrada. | FILE3D |
| `model_3d_info` | Informações do modelo, seja do estado do viewport ou da entrada opcional. | LOAD3DMODELINFO |
| `camera_info` | Informações da câmera, seja do estado do viewport ou da entrada opcional. | LOAD3DCAMERA |
| `width` | O valor da largura encaminhado da entrada. | INT |
| `height` | O valor da altura encaminhado da entrada. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Save3DAdvanced/pt-BR.md)

---
**Source fingerprint (SHA-256):** `2c7d42b1875bb292e675526a2b38fcc8856c8ac45de25ac7b69d92323f0b7ae0`
