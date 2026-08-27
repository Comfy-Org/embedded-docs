# Salvar GLB

O nó SaveGLB salva dados de malha 3D ou entradas de arquivos 3D no diretório de saída. Ele aceita dados de malha e formatos comuns de arquivos 3D (GLB, GLTF, OBJ, FBX, STL, USDZ, PLY, SPLAT, SPZ, KSPLAT) e os exporta com o prefixo de nome de arquivo especificado. As entradas de malha são gravadas como arquivos GLB, um por item do lote, enquanto as entradas de arquivos 3D são salvas em seu formato original.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `malha` | Malha ou arquivo 3D para salvar | MESH or FILE3D | Sim | Mesh data<br>GLB<br>GLTF<br>OBJ<br>FBX<br>STL<br>USDZ<br>PLY<br>SPLAT<br>SPZ<br>KSPLAT<br>Any splat format<br>Any point cloud format<br>Any 3D file format |
| `prefixo_do_arquivo` | O prefixo para o nome do arquivo de saída (padrão: "3d/ComfyUI"). O prefixo pode incluir um caminho de subpasta, então os arquivos são salvos na subpasta "3d" do diretório de saída por padrão | STRING | Não | - |

Nota: Quando a entrada `mesh` é um arquivo 3D, o nó o salva usando a extensão de formato original (GLB é usado se o arquivo não tiver formato). Quando são dados de malha, cada item do lote é salvo como um arquivo `.glb` separado; itens vazios (sem vértices ou faces) são ignorados com um aviso. Os nomes de arquivo de saída seguem o padrão `{filename_prefix}_{counter:05}_.{ext}` com um contador incremental. Os metadados do fluxo de trabalho (prompt e informações extras de PNG) são incorporados aos arquivos salvos quando os metadados estão habilitados.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `ui` | Exibe os arquivos 3D salvos na interface do usuário com informações de nome de arquivo, subpasta e tipo | UI |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveGLB/pt-BR.md)

---
**Source fingerprint (SHA-256):** `366b56c4fd6e3c2f7783222990792a982857b3419a2becfa27ddfa37853bb22c`
