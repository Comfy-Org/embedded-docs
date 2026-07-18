# SaveGaussianSplat

Este nó salva um arquivo 3D de splat gaussiano no diretório de saída do ComfyUI e fornece dados de pré-visualização para o visualizador 3D.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-----------|--------------|-------------|-------|
| `model_3d` | Um arquivo 3D de splat gaussiano. | FILE3D | Sim | - |
| `filename_prefix` | Prefixo para o nome do arquivo salvo (padrão: "3d/ComfyUI") | STRING | Sim | - |
| `viewport_state` | O estado atual da janela de visualização de um nó carregador 3D. | LOAD3D | Sim | - |
| `model_3d_info` | Informações adicionais do modelo 3D para a pré-visualização. | LOAD3DMODELINFO | Não | - |
| `camera_info` | Informações da câmera para a pré-visualização. | LOAD3DCAMERA | Não | - |
| `width` | Largura da pré-visualização em pixels (padrão: 1024) | INT | Sim | min: 1, max: 4096, step: 1 |
| `height` | Altura da pré-visualização em pixels (padrão: 1024) | INT | Sim | min: 1, max: 4096, step: 1 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-----------|--------------|
| `model_3d` | O arquivo 3D de splat gaussiano salvo. | FILE3D |
| `model_3d_info` | Informações do modelo 3D para a pré-visualização. | LOAD3DMODELINFO |
| `camera_info` | Informações da câmera para a pré-visualização. | LOAD3DCAMERA |
| `width` | Largura da pré-visualização. | INT |
| `height` | Altura da pré-visualização. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveGaussianSplat/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f2d6b98d2ce1fe11df8ba440b7f46a21e2308966c15daa5ca0bdca7dab1726cc`
