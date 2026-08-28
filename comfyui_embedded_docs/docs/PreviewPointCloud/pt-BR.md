# Pré-visualizar Nuvem de Pontos

## Visão Geral

O nó Preview Point Cloud permite visualizar um arquivo de nuvem de pontos 3D diretamente na interface do ComfyUI, sem salvá-lo no diretório de saída do ComfyUI. Ele salva a nuvem de pontos em um local temporário e a exibe em uma janela de visualização 3D, além de passar os dados do modelo, as informações da câmera e o estado da viewport adiante para processamento adicional.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-----------|---------------|-------------|-----------|
| `model_3d` | Arquivo de nuvem de pontos (.ply) | FILE3D | Sim | - |
| `model_3d_info` | Informações sobre o modelo 3D | LOAD3DMODELINFO | Não | - |
| `viewport_state` | O estado atual da viewport | LOAD3D | Sim | - |
| `camera_info` | Informações da câmera para a visualização 3D | LOAD3DCAMERA | Não | - |
| `width` | Largura da janela de visualização (padrão: 1024) | INT | Sim | 1 a 4096 |
| `height` | Altura da janela de visualização (padrão: 1024) | INT | Sim | 1 a 4096 |

Nota: Quando `camera_info` ou `model_3d_info` não estão conectados, o nó usa os valores correspondentes armazenados em `viewport_state`. O arquivo de nuvem de pontos é salvo no diretório temporário do ComfyUI e não é gravado no diretório de saída. Este é um nó de saída, portanto é usado principalmente para exibir o resultado da visualização na interface.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-----------|---------------|
| `model_3d` | Os dados do modelo de nuvem de pontos | FILE3D |
| `model_3d_info` | Informações sobre o modelo 3D | LOAD3DMODELINFO |
| `camera_info` | Informações da câmera para a visualização 3D | LOAD3DCAMERA |
| `width` | Largura da janela de visualização | INT |
| `height` | Altura da janela de visualização | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewPointCloud/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a192096df29c4d7029f6e7f4f32e0a2f48de5b3d0cd437bd5b03d79e15eb0987`
