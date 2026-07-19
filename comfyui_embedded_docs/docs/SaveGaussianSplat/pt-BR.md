# SaveGaussianSplat

Este nó salva um arquivo 3D de Gaussian splat no diretório de saída. Ele gerencia o processo de salvamento do arquivo e fornece dados de pré-visualização para a janela de visualização 3D.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | Um arquivo 3D de Gaussian splat. | FILE3D | Sim | SplatAny<br>PLY<br>SPLAT<br>SPZ<br>KSPLAT |
| `filename_prefix` | O prefixo para o nome do arquivo salvo (padrão: "3d/ComfyUI"). | STRING | Sim | Qualquer prefixo de nome de arquivo válido |
| `viewport_state` | O estado atual da janela de visualização contendo informações da câmera e do modelo. | LOAD3D | Sim | - |
| `model_3d_info` | Informações adicionais do modelo 3D para a janela de visualização. | LOAD3DMODELINFO | Não | - |
| `camera_info` | Informações da câmera para a pré-visualização da janela de visualização. | LOAD3DCAMERA | Não | - |
| `width` | A largura da pré-visualização (padrão: 1024). | INT | Sim | 1 a 4096 |
| `height` | A altura da pré-visualização (padrão: 1024). | INT | Sim | 1 a 4096 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `model_3d` | O arquivo 3D de Gaussian splat salvo. | FILE3D |
| `model_3d_info` | Informações do modelo 3D para a janela de visualização. | LOAD3DMODELINFO |
| `camera_info` | Informações da câmera para a pré-visualização da janela de visualização. | LOAD3DCAMERA |
| `width` | A largura da pré-visualização. | INT |
| `height` | A altura da pré-visualização. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveGaussianSplat/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f2d6b98d2ce1fe11df8ba440b7f46a21e2308966c15daa5ca0bdca7dab1726cc`
