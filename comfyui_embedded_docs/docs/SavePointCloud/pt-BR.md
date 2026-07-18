# SavePointCloud

O nó Salvar Nuvem de Pontos salva um arquivo de nuvem de pontos 3D no diretório de saída do seu ComfyUI. Ele também transmite os dados da nuvem de pontos e informações opcionais de câmera e modelo para uso por outros nós no seu fluxo de trabalho.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|---------------|-------------|-------|
| `model_3d` | Arquivo de nuvem de pontos (.ply) | FILE3D | Sim | - |
| `filename_prefix` | Prefixo para o nome do arquivo salvo (padrão: "3d/ComfyUI") | STRING | Sim | - |
| `viewport_state` | Estado de um nó de viewport 3D | LOAD3D | Sim | - |
| `model_3d_info` | Informações opcionais do modelo 3D para uso avançado | LOAD3DMODELINFO | Não | - |
| `camera_info` | Informações opcionais da câmera para uso avançado | LOAD3DCAMERA | Não | - |
| `width` | Largura da imagem de visualização em pixels (padrão: 1024) | INT | Sim | min: 1, max: 4096, passo: 1 |
| `height` | Altura da imagem de visualização em pixels (padrão: 1024) | INT | Sim | min: 1, max: 4096, passo: 1 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-----------|---------------|
| `model_3d` | O arquivo de nuvem de pontos salvo | FILE3D |
| `model_3d_info` | Informações sobre o modelo 3D | LOAD3DMODELINFO |
| `camera_info` | Informações da câmera para o viewport | LOAD3DCAMERA |
| `width` | Largura da imagem de visualização | INT |
| `height` | Altura da imagem de visualização | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SavePointCloud/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ce8f005c431843a57d87a4aff2eed7a1604ebdf360f83b3aaaadc3ed364d218a`
