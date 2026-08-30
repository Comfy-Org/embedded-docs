# Obter componentes 3D

O Get3DComponents analisa um arquivo de modelo 3D (GLB, GLTF, OBJ ou STL) e o converte em uma malha editável que pode ser usada por nós de processamento de malha, como decimate, remesh, UV unwrap e bake. Todos os nós e primitivas da cena são mesclados em uma única malha com suas transformações aplicadas, e texturas e configurações de material vêm do primeiro material. É o equivalente ao nó MeshToFile3D.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|--------------|-------------|-----------|
| `model_3d` | Arquivo de modelo 3D do Load 3D ou de outro nó 3D. FBX/USDZ não são suportados — converta para GLB primeiro. | File3DGLB<br>File3DGLTF<br>File3DOBJ<br>File3DSTL<br>File3DAny | Sim | GLB<br>GLTF<br>OBJ<br>STL |

Observação: arquivos FBX e USDZ não são suportados e causam erro; converta-os para GLB ou GLTF primeiro. Se o arquivo 3D contiver vários materiais, apenas as texturas e os fatores de material do primeiro material são mantidos (um aviso é registrado). Todas as primitivas da cena são mescladas em uma única malha com suas transformações aplicadas. Este nó é experimental.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-------------|--------------|
| `mesh` | Malha editável contendo vértices, faces, UVs, cores de vértice, normais, tangentes e informações de material (textura, metalicidade-rugosidade, mapa normal, emissivo, sinalizador unlit) extraídas do arquivo do modelo. | MESH |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Get3DComponents/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f2cdc9767a50503988484f09d2b3d110caf086b8cd84f65034a4a1e17a94405e`
