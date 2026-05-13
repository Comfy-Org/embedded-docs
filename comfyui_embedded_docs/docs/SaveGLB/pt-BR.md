> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveGLB/pt-BR.md)

O nó SaveGLB salva dados de malha 3D ou arquivos 3D no diretório de saída. Ele aceita dados de malha ou vários formatos de arquivo 3D (GLB, GLTF, OBJ, FBX, STL, USDZ) e os exporta com um prefixo de nome de arquivo especificado. Ao salvar dados de malha, ele pode processar múltiplas malhas e adiciona automaticamente metadados do fluxo de trabalho aos arquivos quando os metadados estão ativados.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `mesh` | MESH ou FILE3D | Sim | - | Malha ou arquivo 3D a ser salvo. Aceita dados de malha ou formatos de arquivo 3D, incluindo GLB, GLTF, OBJ, FBX, STL e USDZ |
| `filename_prefix` | STRING | Não | - | O prefixo para o nome do arquivo de saída (padrão: "3d/ComfyUI") |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `ui` | UI | Exibe os arquivos 3D salvos na interface do usuário com informações de nome de arquivo, subpasta e tipo |

---
**Source fingerprint (SHA-256):** `bd36600185aeb793cd4e9f37f3b4464267cb36f451fdcf71aff83077bb8c3f53`
