# Obter informações da malha

O Get Mesh Info informa o número de vértices e faces em uma malha, junto com os atributos que ela contém (como UVs, cores de vértices, normais e texturas). O relatório é exibido no nó e retornado como uma saída de texto, enquanto a própria malha passa inalterada.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `malha` | A malha a ser inspecionada. O nó conta seus vértices e faces, detecta quais atributos estão presentes e repassa a malha sem alterações. | MESH | Sim | — |

Observação: Quando a entrada contém várias malhas (um lote), o relatório mostra contagens totais de vértices e faces para todo o lote, além de um detalhamento por malha. Para lotes preenchidos com zeros (zero-padded), são usadas as contagens por item armazenadas nos dados da malha.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `mesh` | A malha original, repassada sem qualquer modificação. | MESH |
| `info` | Um relatório de texto multilinha com contagem de vértices, contagem de faces e atributos detectados (uvs, vertex_colors, normals, tangents, texture, metallic_roughness, normal_map). Atributos do tipo textura são exibidos com suas dimensões altura × largura. Contagens grandes são formatadas com vírgulas, por exemplo "1,234,567 (1.23M)" ou "12,345 (12.3K)". O mesmo texto é exibido no nó. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetMeshInfo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `cd168a5e69131a4a37f1f47014af2bc2ac2c8aa69e146cf33c2072480b35ebb2`
