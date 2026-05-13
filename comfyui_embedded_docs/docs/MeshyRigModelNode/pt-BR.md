> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyRigModelNode/pt-BR.md)

O nó Meshy: Rig Model recebe um modelo 3D de uma tarefa anterior do Meshy e cria automaticamente um esqueleto para ele, produzindo um personagem rigado que pode ser posado e animado. O nó gera o modelo rigado nos formatos de arquivo GLB e FBX.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `meshy_task_id` | STRING | Sim | N/A | O ID único da tarefa de uma operação anterior do Meshy (ex.: texto-para-3D ou imagem-para-3D) que gerou o modelo a ser rigado. |
| `height_meters` | FLOAT | Sim | 0,1 a 15,0 | A altura aproximada do modelo do personagem em metros. Isso auxilia na precisão do escalonamento e da rigagem (padrão: 1,7). |
| `texture_image` | IMAGE | Não | N/A | A imagem de textura de cor base do modelo com mapa UV. |

**Nota:** O processo de rigagem automática atualmente não é adequado para malhas sem textura, assets não humanoides ou assets humanoides com estrutura de membros e corpo pouco clara.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `model_file` | STRING | Uma saída legada para compatibilidade reversa, contendo o nome do arquivo do modelo GLB. |
| `rig_task_id` | STRING | O ID único da tarefa para esta operação de rigagem, que pode ser usado para referenciar o resultado. |
| `GLB` | FILE3DGLB | O modelo 3D de personagem rigado salvo no formato de arquivo GLB. |
| `FBX` | FILE3DFBX | O modelo 3D de personagem rigado salvo no formato de arquivo FBX. |

---
**Source fingerprint (SHA-256):** `91e06e3465d3d309d2267ae307ec5a704af3903b7a6d7fb6011217dd58a63973`
