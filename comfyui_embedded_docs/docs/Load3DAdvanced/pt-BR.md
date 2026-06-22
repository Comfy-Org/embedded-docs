# Load3DAdvanced

Este nó carrega um arquivo de modelo 3D do diretório de entrada do seu ComfyUI e fornece os dados do modelo, juntamente com informações de câmera e viewport. Ele suporta formatos de arquivo 3D comuns e permite que você especifique as dimensões da imagem de saída para renderização.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `model_file` | O arquivo de modelo 3D a ser carregado. Selecione "none" para pular o carregamento de um modelo. | STRING | Sim | `"none"`<br>Lista de arquivos 3D disponíveis no diretório input/3d |
| `viewport_state` | O estado atual do viewport contendo informações de câmera e modelo do visualizador 3D. | LOAD3D | Sim | - |
| `width` | A largura da imagem de saída em pixels (padrão: 1024) | INT | Sim | Mín: 1<br>Máx: 4096<br>Passo: 1 |
| `height` | A altura da imagem de saída em pixels (padrão: 1024) | INT | Sim | Mín: 1<br>Máx: 4096<br>Passo: 1 |

**Notas sobre os Parâmetros:**
- O parâmetro `model_file` exibe apenas arquivos com as seguintes extensões: .gltf, .glb, .obj, .fbx, .stl
- Os arquivos devem ser colocados no diretório `input/3d` da sua instalação do ComfyUI
- Se `model_file` estiver definido como "none", nenhum dado de modelo 3D será carregado (a saída `model_3d` ficará vazia)

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `model_3d` | Os dados do modelo 3D carregado, ou vazio se nenhum arquivo de modelo foi selecionado | FILE3DANY |
| `model_3d_info` | Informações sobre o modelo 3D carregado a partir do estado do viewport | LOAD3DMODELINFO |
| `camera_info` | Informações da câmera a partir do estado do viewport | LOAD3DCAMERA |
| `width` | A largura especificada da imagem de saída | INT |
| `height` | A altura especificada da imagem de saída | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Load3DAdvanced/pt-BR.md)

---
**Source fingerprint (SHA-256):** `fdacea8abf627621150e1196743e36f61534333837c33cc9a7416a6d11700c4d`
