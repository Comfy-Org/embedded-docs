O nó SaveGLB salva dados de malha 3D ou arquivos 3D no diretório de saída. Ele aceita dados de malha ou vários formatos de arquivo 3D (GLB, GLTF, OBJ, FBX, STL, USDZ) e os exporta com um prefixo de nome de arquivo especificado. Ao salvar dados de malha, ele pode processar múltiplas malhas e adiciona automaticamente metadados do fluxo de trabalho aos arquivos quando os metadados estão ativados.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `malha` | Malha ou arquivo 3D a ser salvo. Aceita dados de malha ou formatos de arquivo 3D, incluindo GLB, GLTF, OBJ, FBX, STL e USDZ | MESH ou FILE3D | Sim | - |
| `prefixo_do_arquivo` | O prefixo para o nome do arquivo de saída (padrão: "3d/ComfyUI") | STRING | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `ui` | Exibe os arquivos 3D salvos na interface do usuário com informações de nome de arquivo, subpasta e tipo | UI |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveGLB/pt-BR.md)

---
**Source fingerprint (SHA-256):** `bd36600185aeb793cd4e9f37f3b4464267cb36f451fdcf71aff83077bb8c3f53`
