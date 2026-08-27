# Visualizar 3D (Avançado)

Este nó exibe uma pré-visualização do modelo 3D na interface sem salvar o arquivo no diretório de saída do ComfyUI. Ele salva o modelo em um arquivo temporário e transmite os dados do modelo, as informações do modelo, as informações da câmera e as dimensões da pré-visualização para processamento posterior.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `modelo_3d` | Arquivo de modelo 3D de um nó 3D anterior. | FILE3D | Sim | GLB, GLTF, FBX, OBJ, STL, USDZ, ou qualquer formato 3D suportado |
| `info_modelo_3d` | Metadados opcionais de informações do modelo. Opção avançada. | LOAD3DMODELINFO | Não | - |
| `estado_da_janela_de_visualização` | O estado atual do viewport contendo informações da câmera e do modelo. | LOAD3D | Sim | - |
| `info_câmera` | Configuração opcional da câmera para a visualização 3D. Opção avançada. | LOAD3DCAMERA | Não | - |
| `largura` | A largura da pré-visualização em pixels. Padrão: 1024. | INT | Sim | 1 a 4096 |
| `altura` | A altura da pré-visualização em pixels. Padrão: 1024. | INT | Sim | 1 a 4096 |

Nota: Quando `camera_info` ou `model_3d_info` não estiverem conectados, seus valores serão obtidos do `viewport_state` quando disponíveis. Se o `viewport_state` não tiver informações do modelo, o `model_3d_info` assume como padrão uma lista vazia. Se o `viewport_state` não for um dicionário, ele será tratado como vazio.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `arquivo_modelo` | O arquivo de modelo 3D repassado da entrada. | FILE3D |
| `info_câmera` | Metadados de informações do modelo, provenientes da entrada ou do estado do viewport. | LOAD3DMODELINFO |
| `info_modelo_3d` | Configuração da câmera, proveniente da entrada ou do estado do viewport. | LOAD3DCAMERA |
| `largura` | A largura da pré-visualização em pixels. | INT |
| `altura` | A altura da pré-visualização em pixels. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Preview3DAdvanced/pt-BR.md)

---
**Source fingerprint (SHA-256):** `eda8c8fdd6ce7c39caf00c3054fc58e6dcab124fc3774d17af2deae651fbbf2e`
