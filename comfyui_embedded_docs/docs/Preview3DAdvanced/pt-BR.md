# Visualizar 3D (Avançado)

Este nó fornece uma pré-visualização avançada de modelos 3D com saída de informações de câmera e modelo. Ele pré-visualiza um arquivo de modelo 3D sem salvá-lo no diretório de saída do ComfyUI, gravando o modelo em um arquivo temporário para exibição na interface. Os dados do modelo, as informações do modelo, as informações da câmera e as dimensões da viewport também são repassados para processamento posterior.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|---------------|-------------|-------|
| `model_3d` | Arquivo de modelo 3D de um nó 3D a montante. | FILE3D | Sim | GLB, GLTF, FBX, OBJ, STL, USDZ ou qualquer formato 3D suportado |
| `model_3d_info` | Metadados opcionais de informações do modelo. | LOAD3DMODELINFO | Não | - |
| `viewport_state` | O estado atual da viewport contendo informações de câmera e modelo. | LOAD3D | Sim | - |
| `camera_info` | Configuração opcional de câmera para a visualização 3D. | LOAD3DCAMERA | Não | - |
| `width` | A largura da pré-visualização em pixels. | INT | Sim | 1 a 4096 (padrão: 1024) |
| `height` | A altura da pré-visualização em pixels. | INT | Sim | 1 a 4096 (padrão: 1024) |

Nota: Quando `camera_info` não está conectado, o nó usa o valor de `camera_info` do `viewport_state`. Quando `model_3d_info` não está conectado, o nó usa o valor de `model_3d_info` do `viewport_state`, ou uma lista vazia se o estado da viewport não o contiver.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-------------|---------------|
| `model_3d` | O arquivo de modelo 3D repassado da entrada. | FILE3D |
| `model_3d_info` | Metadados de informações do modelo, da entrada ou do estado da viewport. | LOAD3DMODELINFO |
| `camera_info` | Configuração da câmera, da entrada ou do estado da viewport. | LOAD3DCAMERA |
| `width` | A largura da pré-visualização em pixels. | INT |
| `height` | A altura da pré-visualização em pixels. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Preview3DAdvanced/pt-BR.md)

---
**Source fingerprint (SHA-256):** `eda8c8fdd6ce7c39caf00c3054fc58e6dcab124fc3774d17af2deae651fbbf2e`
