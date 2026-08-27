# FillHoles

Este nó preenche buracos em uma malha 3D detectando arestas de fronteira abertas e criando novas faces para fechá-los. Ele é executado na GPU, preserva a geometria existente e as UVs, e pode processar malhas individuais, listas de malhas ou lotes de malhas.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `mesh` | A malha 3D a ser processada. Aceita uma malha individual, uma lista de malhas ou uma malha em lote. | MESH | Sim | - |
| `max_perimeter` | Perímetro máximo do buraco a preencher. 0 desativa. (padrão: 0.03) | FLOAT | Sim | 0.0 to no upper limit |
| `weld_epsilon_rel` | Tolerância de pré-soldagem (fração da diagonal da caixa delimitadora); a detecção de bordas precisa de vértices soldados. 0 ignora. (padrão: 1e-5) | FLOAT | Sim | 0.0 to no upper limit |
| `max_vertices` | Limite de vértices de borda por ciclo; o leque centróide só funciona para buracos pequenos e quase planos. Mantenha ≤16. (padrão: 16) | INT | Sim | 3 a 1024 |
| `fill_chains` | Também preenche cadeias abertas (não apenas ciclos). Ruidoso; DESLIGADO corresponde ao cumesh. (padrão: False) | BOOLEAN | Sim | True or False |

Nota: Quando `weld_epsilon_rel` é maior que 0, o nó pré-solda vértices duplicados antes de detectar buracos. A tolerância de soldagem começa na fração fornecida da diagonal da caixa delimitadora e aumenta automaticamente em dobro até que a malha seja considerada soldada ou que a tolerância atinja um limite de 1e-2. Buracos com mais de 8 vértices de borda usam um preenchimento em leque centróide (inserindo um novo vértice centróide), enquanto buracos menores usam um preenchimento em leque de vértice que reutiliza um vértice de borda existente.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `mesh` | A malha com buracos preenchidos, correspondendo ao formato do lote de entrada. | MESH |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FillHoles/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c0fd7f0c2d6eea098efb1dcfd80eaa52997e185b9c442b483f75318eea082196`
