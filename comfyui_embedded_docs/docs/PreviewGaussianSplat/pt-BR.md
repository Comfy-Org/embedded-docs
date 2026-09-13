# Pré-visualizar Splat

The PreviewGaussianSplat node exibe um arquivo 3D gaussian splat em uma janela de pré-visualização sem salvá-lo no diretório de saída do ComfyUI. Ele aceita um arquivo de modelo 3D em vários formatos gaussian splat, salva uma cópia temporária para pré-visualização e repassa os dados do modelo para processamento posterior no workflow. Este nó é marcado como experimental e atua como um nó de saída.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | Um arquivo 3D gaussian splat. | FILE3D | Sim | splat<br>ply<br>spz<br>ksplat |
| `model_3d_info` | Informações opcionais de metadados sobre o modelo 3D. Quando não conectado, o nó usa as informações do modelo de `viewport_state`. | LOAD3DMODELINFO | Não | - |
| `viewport_state` | O estado atual do viewport 3D, incluindo informações de câmera e modelo. | LOAD3D | Sim | - |
| `camera_info` | Informações opcionais de câmera para a pré-visualização. Quando não conectado, o nó usa as informações de câmera de `viewport_state`. | LOAD3DCAMERA | Não | - |
| `width` | A largura da renderização de pré-visualização em pixels (padrão: 1024). | INT | Sim | 1 a 4096 |
| `height` | A altura da renderização de pré-visualização em pixels (padrão: 1024). | INT | Sim | 1 a 4096 |

Nota: Quando `camera_info` ou `model_3d_info` não são fornecidos, o nó recorre às informações de câmera e modelo armazenadas em `viewport_state`. Se `viewport_state` não for um objeto de estado de viewport válido, ele será tratado como vazio.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `model_3d` | O arquivo 3D gaussian splat de entrada, repassado sem alterações. | FILE3D |
| `model_3d_info` | Informações de metadados sobre o modelo 3D, obtidas da entrada ou derivadas do estado do viewport. | LOAD3DMODELINFO |
| `camera_info` | Informações de câmera para a pré-visualização, obtidas da entrada ou derivadas do estado do viewport. | LOAD3DCAMERA |
| `width` | A largura da renderização de pré-visualização. | INT |
| `height` | A altura da renderização de pré-visualização. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewGaussianSplat/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4fc86c692724ce406f9bba9aa9ebe22a92e72a25d11abf8f55d1b99044bb1acd`
