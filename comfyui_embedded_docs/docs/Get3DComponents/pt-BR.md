# Obter componentes 3D

Get3DComponents analisa um arquivo de modelo 3D (GLB, GLTF, OBJ ou STL) e o converte em uma malha editável que pode ser usada por nós de processamento de malha, como decimate, remesh, UV unwrap e bake. Todos os nós de cena e primitivas são mesclados em uma única malha com suas transformações aplicadas, e as texturas e configurações de material vêm do primeiro material. É a contraparte do nó MeshToFile3D.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | Arquivo de modelo 3D de Load 3D ou outro nó 3D. FBX/USDZ não são suportados - converta para GLB primeiro. | File3DGLB<br>File3DGLTF<br>File3DOBJ<br>File3DSTL<br>File3DAny | Sim | GLB<br>GLTF<br>OBJ<br>STL |

Nota: arquivos FBX e USDZ não são suportados e causam erro; converta-os para GLB ou GLTF primeiro. Se o formato do arquivo não puder ser reconhecido como GLB, GLTF, OBJ ou STL, o nó gera um erro listando os formatos suportados. Se a cena glTF não contiver geometria de triângulos, ou se o arquivo contiver índices de face que apontam para fora da lista de vértices (um sinal de arquivo corrompido), o nó gera um erro. Se o arquivo 3D contiver vários materiais, apenas as texturas e os fatores de material do primeiro material serão mantidos (um aviso é registrado no log). Todas as primitivas da cena são mescladas em uma única malha com suas transformações aplicadas. Este nó é experimental.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `mesh` | Malha editável contendo vértices, faces, UVs, cores de vértices, normais e tangentes, além de informações de material obtidas do arquivo (textura, metallic-roughness, normal map, cor emissiva, flag unlit, flag de oclusão em metallic-roughness e dados de material). | MESH |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Get3DComponents/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f2cdc9767a50503988484f09d2b3d110caf086b8cd84f65034a4a1e17a94405e`
