# BakeAmbientOcclusion

Gera um mapa de oclusão ambiente a partir de uma malha high-poly no layout UV de uma malha low-poly. A saída é uma imagem em tons de cinza na qual texels brancos estão abertos e texels escuros estão em reentrâncias; ela é destinada à entrada de oclusão do nó Apply Texture To Mesh. Conecte a malha low-poly com UVs desdobrados e a malha high-poly da qual ela foi decimada.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|---------------|-------------|-------|
| `low_poly` | A malha low-poly com UVs desdobrados na qual será feita a gravação. Deve ter UVs; o nó gera um erro se estiverem ausentes. | MESH | Sim | - |
| `high_poly` | A malha high-poly da qual a low-poly foi decimada, usada como geometria de origem para a oclusão. | MESH | Sim | - |
| `resolution` | Resolução da textura em pixels; cada texel recebe um valor de oclusão. Padrão: 1024. | INT | Sim | 64 a 8192 (step 64) |
| `samples` | Raios por texel. Mais = mais suave, mais lento. Aumente se ficar granuloso. Padrão: 64. | INT | Sim | 4 a 1024 (step 4) |
| `max_distance` | Comprimento do raio, como fração da diagonal da caixa delimitadora. Menor = mais restrito, oclusão mais local. Padrão: 0.5. | FLOAT | Sim | 0.01 a 2.0 (step 0.01) |
| `strength` | Escala a oclusão. >1 escurece, <1 clareia. Padrão: 1.0. | FLOAT | Sim | 0.0 a 2.0 (step 0.05) |
| `bias` | Elevação da origem do raio em relação à superfície, como fração da diagonal da caixa delimitadora. Aumente se superfícies planas apresentarem manchas/buracos escuros. Padrão: 0.01. | FLOAT | Sim | 0.0001 a 0.2 (step 0.0005) |

Observação: `low_poly` deve ter coordenadas UV — este nó nunca desdobra a malha. Se `high_poly` contiver apenas um item do lote, ele será reutilizado para cada item do lote de `low_poly`; itens do lote de `low_poly` sem faces são ignorados e substituídos por uma imagem totalmente branca, com um aviso registrado no log.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-------------|---------------|
| `occlusion` | Imagem de oclusão ambiente em tons de cinza com valores em [0,1] (branco = aberto, escuro = reentrâncias), uma imagem por item do lote de `low_poly`. Destinada à entrada de oclusão do nó Apply Texture To Mesh (empacotada no mapa ORM / occlusionTexture). | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeAmbientOcclusion/pt-BR.md)

---
**Source fingerprint (SHA-256):** `63ea6ce5289728d351fdd7d722e9a299ebb1283e1128262a817466ec6d23786a`
