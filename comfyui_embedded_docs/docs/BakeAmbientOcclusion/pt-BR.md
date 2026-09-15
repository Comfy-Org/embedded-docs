# Gerar Oclusão de Ambiente

Gera um mapa de oclusão ambiental de uma malha high-poly no layout UV de uma malha low-poly. A saída é uma imagem em escala de cinza na qual texels brancos são abertos e texels escuros estão em reentrâncias; destina-se à entrada de oclusão do nó Apply Texture To Mesh. Conecte a malha low-poly com UVs desenrolados e a malha high-poly da qual ela foi decimada.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `low_poly` | A malha low-poly com UVs desenrolados na qual fazer o bake. Deve ter UVs; o nó gera um erro se estiverem ausentes. | MESH | Sim | - |
| `high_poly` | A malha high-poly da qual a low-poly foi decimada, usada como geometria de origem para a oclusão. | MESH | Sim | - |
| `resolution` | Resolução da textura em pixels; cada texel recebe um valor de oclusão. Padrão: 1024. | INT | Sim | 64 a 8192 (passo 64) |
| `samples` | Raios por texel. Mais = mais suave, mais lento. Aumente se estiver granuloso. Padrão: 64. | INT | Sim | 4 a 1024 (passo 4) |
| `max_distance` | Comprimento do raio, como uma fração da diagonal da caixa delimitadora. Menor = mais justo, oclusão mais local. Padrão: 0.5. | FLOAT | Sim | 0.01 a 2.0 (passo 0.01) |
| `strength` | Escala a oclusão. >1 escurece, <1 clareia. Padrão: 1.0. | FLOAT | Sim | 0.0 a 2.0 (passo 0.05) |
| `bias` | Elevação da origem do raio a partir da superfície, como uma fração da diagonal da caixa delimitadora. Aumente se mesmo superfícies planas mostrarem manchas escuras/buracos. Padrão: 0.01. | FLOAT | Sim | 0.0001 a 0.2 (passo 0.0005) |

Nota: `low_poly` deve ter coordenadas UV — este nó nunca desenrola a malha. Se `high_poly` contiver apenas um item de lote, ele será reutilizado para cada item de lote de `low_poly`; itens de lote de `low_poly` sem faces são ignorados e substituídos por uma imagem totalmente branca, com um aviso registrado. Se os UVs de `low_poly` ultrapassarem o intervalo 0-1, eles serão ajustados uniformemente de volta para dentro dele, e um aviso será registrado quando um layout no estilo tiled/UDIM for detectado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `occlusion` | Imagem de oclusão ambiental em escala de cinza com valores em [0,1] (branco = aberto, escuro = reentrâncias), uma imagem por item de lote de `low_poly`. Destinada à entrada de oclusão do nó Apply Texture To Mesh (empacotada no mapa ORM / occlusionTexture). | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeAmbientOcclusion/pt-BR.md)

---
**Source fingerprint (SHA-256):** `63ea6ce5289728d351fdd7d722e9a299ebb1283e1128262a817466ec6d23786a`
