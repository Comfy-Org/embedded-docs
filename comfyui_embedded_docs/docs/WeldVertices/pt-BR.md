# WeldVertices

Weld Vertices mescla vértices coincidentes em uma malha 3D, de modo que faces que antes tinham pontos de canto separados passem a compartilhar os mesmos vértices. Ela agrupa vértices próximos usando quantização por grade com uma tolerância baseada na caixa delimitadora da malha e calcula a média das cores dos vértices para cada grupo mesclado. Isso é útil quando uma malha chega não soldada, ou seja, cada face possui seus próprios vértices e nenhuma aresta compartilhada.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `mesh` | A malha 3D de entrada cujos vértices coincidentes serão mesclados. | MESH | Sim | - |
| `epsilon_rel` | Tolerância de solda (fração da diagonal da caixa delimitadora). 1e-5 para deduplicação de floats; 1e-3 para vértices visivelmente próximos, porém distintos. Padrão: 1e-5. | FLOAT | Sim | 0.0 to unlimited |
| `epsilon_abs` | Tolerância de solda absoluta (substitui epsilon_rel quando > 0). Padrão: 0.0. | FLOAT | Sim | 0.0 to unlimited |

Nota: Quando `epsilon_abs` é maior que 0, ele tem precedência sobre `epsilon_rel` e a tolerância relativa é ignorada. Quando `epsilon_abs` é 0, a tolerância relativa `epsilon_rel` é usada.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `mesh` | A malha soldada com vértices mesclados, índices de face atualizados e cores de vértices com média calculada (se a malha de entrada tinha cores). | MESH |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WeldVertices/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f8779e764b344de651b8459f6e4c28773509d9596a98fd164dc7044278856435`
