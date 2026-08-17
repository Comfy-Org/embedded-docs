# Pré-visualizar Nuvem de Pontos

O nó Preview Point Cloud permite visualizar um arquivo de nuvem de pontos 3D (como um arquivo .ply) diretamente na interface do ComfyUI, sem salvá-lo no diretório de saída. O nó grava a nuvem de pontos em um arquivo temporário, exibe-a em uma janela de visualização 3D e repassa os dados do modelo, as informações do modelo, as informações da câmera, a largura e a altura para processamento adicional.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|--------------|-------------|-----------|
| `model_3d` | Arquivo de nuvem de pontos (.ply) | FILE3D | Sim | - |
| `model_3d_info` | Informações sobre o modelo 3D. Entrada avançada. Quando não conectada, o valor armazenado em `viewport_state` é usado. | LOAD3DMODELINFO | Não | - |
| `viewport_state` | O estado atual do viewport, que pode conter informações de câmera e informações do modelo usadas para a visualização. | LOAD3D | Sim | - |
| `camera_info` | Informações da câmera para a visualização 3D. Entrada avançada. Quando não conectada, o valor armazenado em `viewport_state` é usado. | LOAD3DCAMERA | Não | - |
| `width` | Largura da janela de visualização em pixels (padrão: 1024). | INT | Sim | 1 a 4096 |
| `height` | Altura da janela de visualização em pixels (padrão: 1024). | INT | Sim | 1 a 4096 |

Nota: Quando `camera_info` ou `model_3d_info` não estiverem conectados, o nó usa os valores armazenados em `viewport_state`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-------------|--------------|
| `model_3d` | Os dados do modelo de nuvem de pontos, repassados sem alterações. | FILE3D |
| `model_3d_info` | Informações sobre o modelo 3D usadas para a visualização. | LOAD3DMODELINFO |
| `camera_info` | Informações da câmera usadas para a visualização 3D. | LOAD3DCAMERA |
| `width` | Largura da janela de visualização. | INT |
| `height` | Altura da janela de visualização. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewPointCloud/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a192096df29c4d7029f6e7f4f32e0a2f48de5b3d0cd437bd5b03d79e15eb0987`
