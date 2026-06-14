# Pré-visualização 3D (Avançado)

Este nó fornece uma pré-visualização avançada de modelos 3D com saída de informações da câmera e do modelo. Ele salva o modelo 3D em um arquivo temporário e o exibe na interface, enquanto também transmite os dados do modelo, informações da câmera e dimensões da janela de visualização para processamento posterior.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-----------|--------------|-------------|-------|
| `modelo_3d` | Arquivo de modelo 3D de um nó 3D anterior. | FILE3D | Sim | GLB, GLTF, FBX, OBJ, STL, USDZ ou qualquer formato 3D suportado |
| `info_modelo_3d` | Metadados opcionais de informações do modelo. | LOAD3DMODELINFO | Não | - |
| `estado_da_janela_de_visualização` | O estado atual da janela de visualização contendo informações da câmera e do modelo. | LOAD3D | Sim | - |
| `info_câmera` | Configuração opcional da câmera para a visualização 3D. | LOAD3DCAMERA | Não | - |
| `largura` | A largura da pré-visualização em pixels. | INT | Sim | 1 a 4096 (padrão: 1024) |
| `altura` | A altura da pré-visualização em pixels. | INT | Sim | 1 a 4096 (padrão: 1024) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-----------|--------------|
| `modelo_3d` | O arquivo de modelo 3D transmitido da entrada. | FILE3D |
| `info_modelo_3d` | Metadados de informações do modelo, seja da entrada ou do estado da janela de visualização. | LOAD3DMODELINFO |
| `info_câmera` | Configuração da câmera, seja da entrada ou do estado da janela de visualização. | LOAD3DCAMERA |
| `largura` | A largura da pré-visualização em pixels. | INT |
| `altura` | A altura da pré-visualização em pixels. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Preview3DAdvanced/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7efe8720f88f7d6234387cd633ea629cbf43a0abea1a9aca6c5dcd43bf7f2145`
