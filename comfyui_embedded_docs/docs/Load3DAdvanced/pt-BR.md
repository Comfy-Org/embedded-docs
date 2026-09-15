# Carregar 3D (Avançado)

O nó Load 3D (Advanced) carrega um arquivo de modelo 3D do diretório `input/3d` do ComfyUI e fornece os dados do modelo junto com as informações de posicionamento do modelo e da câmera capturadas no estado da viewport do visualizador 3D. Ele oferece suporte a formatos comuns de arquivos 3D e permite definir a largura e a altura de renderização da viewport em pixels. Este nó é experimental.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model_file` | O arquivo de modelo 3D a ser carregado. Selecione "none" para ignorar o carregamento de um arquivo de modelo. Arquivos também podem ser enviados pelo widget. | COMBO | Sim | `"none"`<br>Arquivos de modelo 3D disponíveis no diretório `input/3d` |
| `viewport_state` | O estado atual da viewport contendo informações de câmera e modelo do visualizador 3D. | LOAD3D | Sim | - |
| `width` | Largura de renderização da viewport em pixels (padrão: 1024). | INT | Sim | Mín: 1<br>Máx: 4096<br>Padrão: 1024<br>Passo: 1 |
| `height` | Altura de renderização da viewport em pixels (padrão: 1024). | INT | Sim | Mín: 1<br>Máx: 4096<br>Padrão: 1024<br>Passo: 1 |

**Observações sobre os Parâmetros:**
- O parâmetro `model_file` lista apenas arquivos com as seguintes extensões: .gltf, .glb, .obj, .fbx, .stl
- Os arquivos devem ser colocados no diretório `input/3d` da sua instalação do ComfyUI; subpastas também são pesquisadas, e os caminhos dos arquivos são exibidos em relação ao diretório `input`
- Se `model_file` for "none", nenhum dado de modelo será carregado e a saída `model_3d` ficará vazia
- Se `model_file` for definido como um arquivo que não existe, o nó retorna um erro de validação: `Invalid 3D model file: {model_file}`
- Se `viewport_state` não for um objeto de estado de viewport válido, ele será tratado como vazio; assim, `model_3d_info` se torna uma lista vazia e `camera_info` é retornado como vazio

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `model_3d` | Arquivo de modelo 3D carregado (glb/obj/stl/etc.). Vazio se nenhum arquivo de modelo tiver sido selecionado. | FILE3DANY |
| `model_3d_info` | Posicionamento de cada modelo na cena: posição, rotação e escala (espaço de mundo com Y para cima). | LOAD3DMODELINFO |
| `camera_info` | Informações da câmera da viewport: posição, alvo de mira, zoom e tipo. | LOAD3DCAMERA |
| `width` | Largura de renderização da viewport em pixels. | INT |
| `height` | Altura de renderização da viewport em pixels. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Load3DAdvanced/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c79c53dde0c8b3afb7df7b972df749f5040c92d48b47e355c4497d9b0cbf1c22`
