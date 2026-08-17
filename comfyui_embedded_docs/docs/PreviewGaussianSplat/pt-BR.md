# Pré-visualizar Splat

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|--------------|--------------|------------|
| `model_3d` | Um arquivo 3D de gaussian splat. | FILE3D | Sim | splat, ply, spz, ksplat |
| `model_3d_info` | Informações opcionais de metadados sobre o modelo 3D. | LOAD3DMODELINFO | Não | - |
| `viewport_state` | O estado atual do viewport 3D, incluindo informações de câmera e modelo. | LOAD3D | Sim | - |
| `camera_info` | Informações opcionais de câmera para a visualização. | LOAD3DCAMERA | Não | - |
| `width` | A largura da renderização de visualização em pixels (padrão: 1024). | INT | Sim | 1 a 4096 |
| `height` | A altura da renderização de visualização em pixels (padrão: 1024). | INT | Sim | 1 a 4096 |

Nota: quando `camera_info` ou `model_3d_info` não são fornecidos, o nó usa os valores correspondentes de `viewport_state`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-------------|--------------|
| `model_3d` | O arquivo 3D de gaussian splat de entrada, repassado sem alterações. | FILE3D |
| `model_3d_info` | Informações de metadados sobre o modelo 3D, vindas da entrada ou do estado do viewport. | LOAD3DMODELINFO |
| `camera_info` | Informações de câmera para a visualização, vindas da entrada ou do estado do viewport. | LOAD3DCAMERA |
| `width` | A largura da renderização de visualização. | INT |
| `height` | A altura da renderização de visualização. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewGaussianSplat/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7157a0b34d7bda3e7ec86cb2ac09e0e10ff96ea7037bb6c9d6ad2c879fdedbb2`
