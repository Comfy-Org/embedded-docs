# Bake Texture From Views

Projeta imagens renderizadas de volta no layout UV da malha. Renderize a malha com Render Mesh, edite ou regenere as imagens e depois faça o bake delas com a mesma malha e câmeras. Os texels que nenhuma vista cobre mantêm a textura ou as cores de vértice da própria malha.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `mesh` | A malha com UVs desdobrados que foi renderizada. | MESH | Sim | - |
| `images` | Uma imagem por câmera, na ordem das câmeras (Batch Images). Qualquer resolução com a proporção da renderização; uma resolução maior gera um bake mais nítido. | IMAGE | Sim | - |
| `camera_info` | As câmeras com as quais as imagens foram renderizadas, conforme conectadas ao Render Mesh. Combine rigs com Batch Cameras. Nenhum: vista frontal enquadrada automaticamente do Render Mesh. | LOAD3D_CAMERA | Não | - |
| `resolution` | Resolução quadrada da textura. 0 mantém o tamanho atual da textura da malha, ou 2048 quando ela não tem textura; caso contrário, a textura atual é reamostrada para esse valor. Padrão: 0. | INT | Não | 0 a 8192 (passo: 64) |
| `blend_exponent` | As vistas são ponderadas por cos(ângulo da vista)^expoente. Valores mais altos favorecem a vista mais frontal (mais nítida, emendas mais marcadas); valores mais baixos fazem a média de mais vistas (mais suave). Padrão: 4.0. | FLOAT | Não | 0.0 a 32.0 (passo: 0.5) |
| `fill_unseen` | Os texels que nenhuma vista enxerga recebem cores propagadas a partir da superfície visível, em vez da textura ou das cores de vértice da própria malha. Use essa opção quando as vistas substituírem toda a textura. Padrão: false. | BOOLEAN | Não | true<br>false |
| `mask` | Áreas editadas por vista; apenas os pixels mascarados são projetados. Uma única máscara se aplica a todas as vistas. | MASK | Não | - |

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `base_color` | A textura resultante do bake, para Apply Texture to Mesh. | IMAGE |
| `confidence` | Para cada texel, o quão frontal foi a melhor vista que o viu; 0 significa não visto. | MASK |

Nota: Renderizações feitas com uma transformação de modelo do visualizador não se alinham com o bake, e apenas a primeira malha de um lote é usada.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeTextureFromViews/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e5f2456977693dc09e69ce4d846f2ab775f2520115623d9f63a76807d6c9f797`
