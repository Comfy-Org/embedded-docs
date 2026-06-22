# Pré-visualizar Splat

O nó PreviewGaussianSplat permite visualizar um arquivo de gaussian splat 3D dentro da interface do ComfyUI. Ele aceita um arquivo de modelo 3D em vários formatos de gaussian splat e o renderiza em uma janela de pré-visualização 3D, transmitindo os dados do modelo para processamento posterior.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | Um arquivo 3D do tipo gaussian splat. | FILE3D | Sim | Formatos suportados: splat, ply, spz, ksplat |
| `model_3d_info` | Informações opcionais de metadados sobre o modelo 3D. | LOAD3DMODELINFO | Não | - |
| `viewport_state` | O estado atual da janela de visualização 3D, incluindo informações da câmera e do modelo. | LOAD3D | Sim | - |
| `camera_info` | Informações opcionais da câmera para a pré-visualização. | LOAD3DCAMERA | Não | - |
| `width` | A largura da renderização da pré-visualização em pixels (padrão: 1024). | INT | Sim | 1 a 4096 |
| `height` | A altura da renderização da pré-visualização em pixels (padrão: 1024). | INT | Sim | 1 a 4096 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `model_3d` | O arquivo de gaussian splat 3D de entrada, transmitido sem alterações. | FILE3D |
| `model_3d_info` | Informações de metadados sobre o modelo 3D, provenientes da entrada ou derivadas do estado da janela de visualização. | LOAD3DMODELINFO |
| `camera_info` | Informações da câmera para a pré-visualização, provenientes da entrada ou derivadas do estado da janela de visualização. | LOAD3DCAMERA |
| `width` | A largura da renderização da pré-visualização. | INT |
| `height` | A altura da renderização da pré-visualização. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewGaussianSplat/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7b79e9ab25858e7db6e999313cc11226895aeb4d7fee414f56f0d5fd2363b485`
