# Pré-visualizar Nuvem de Pontos

O nó Visualizar Nuvem de Pontos permite visualizar um arquivo de nuvem de pontos 3D na interface do ComfyUI. Ele salva a nuvem de pontos em um arquivo temporário e a exibe em uma janela de visualização 3D, transmitindo os dados do modelo e as configurações da viewport para processamento posterior.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | Arquivo de nuvem de pontos (.ply) | FILE3D | Sim | - |
| `model_3d_info` | Informações sobre o modelo 3D | LOAD3DMODELINFO | Não | - |
| `viewport_state` | O estado atual da viewport | LOAD3D | Sim | - |
| `camera_info` | Informações da câmera para a visualização 3D | LOAD3DCAMERA | Não | - |
| `width` | Largura da janela de visualização (padrão: 1024) | INT | Sim | 1 a 4096 |
| `height` | Altura da janela de visualização (padrão: 1024) | INT | Sim | 1 a 4096 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `model_3d` | Os dados do modelo de nuvem de pontos | FILE3D |
| `model_3d_info` | Informações sobre o modelo 3D | LOAD3DMODELINFO |
| `camera_info` | Informações da câmera para a visualização 3D | LOAD3DCAMERA |
| `width` | Largura da janela de visualização | INT |
| `height` | Altura da janela de visualização | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewPointCloud/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f3121511841d1962aad881c0ac5b93f24842bf4810e84fe241330e9eab90334a`
