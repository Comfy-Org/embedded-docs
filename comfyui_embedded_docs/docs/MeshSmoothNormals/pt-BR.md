# MeshSmoothNormals

Calcula normais suaves por vértice para uma malha e as anexa. Malhas sem normais são sombreadas de forma plana (por face) pelos visualizadores glTF; este nó faz com que sejam sombreadas suavemente. Com um ângulo de vinco abaixo de 180, arestas mais nítidas que o limite são mantidas rígidas, dividindo os vértices ao longo delas.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `mesh` | A malha de entrada a ser processada. | MESH | Sim | - |
| `crease_angle` | Arestas cujo ângulo diedro excede este valor (em graus) permanecem rígidas (os vértices são divididos). 180 = totalmente suave; valores menores preservam arestas afiadas (por exemplo, ~30-60 para superfícies duras). Padrão: 180.0. | FLOAT | Sim | 0.0 a 180.0 (passo 1.0) |

Quando `crease_angle` é 180 ou maior, a topologia da malha permanece inalterada. Quando definido abaixo de 180, os vértices são divididos ao longo das arestas rígidas, o que pode aumentar a contagem de vértices.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `mesh` | A malha de entrada com dados de normais suaves anexados, ou com vértices e normais divididos quando um ângulo de vinco é definido. | MESH |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshSmoothNormals/pt-BR.md)

---
**Source fingerprint (SHA-256):** `bbe9c0fba68369d8e9d3fb68e635869233804f3aac458e7c217d94977e77b9be`
