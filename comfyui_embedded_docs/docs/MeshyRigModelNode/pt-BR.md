O nó Meshy: Rig Model recebe um modelo 3D de uma tarefa anterior do Meshy e cria automaticamente um esqueleto para ele, produzindo um personagem rigado que pode ser posado e animado. O nó gera o modelo rigado nos formatos de arquivo GLB e FBX.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `meshy_task_id` | O ID único da tarefa de uma operação anterior do Meshy (ex.: texto-para-3D ou imagem-para-3D) que gerou o modelo a ser rigado. | STRING | Sim | N/A |
| `altura_metros` | A altura aproximada do modelo do personagem em metros. Isso auxilia na precisão do escalonamento e da rigagem (padrão: 1,7). | FLOAT | Sim | 0,1 a 15,0 |
| `imagem_de_textura` | A imagem de textura de cor base do modelo com mapa UV. | IMAGE | Não | N/A |

**Nota:** O processo de rigagem automática atualmente não é adequado para malhas sem textura, assets não humanoides ou assets humanoides com estrutura de membros e corpo pouco clara.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model_file` | Uma saída legada para compatibilidade reversa, contendo o nome do arquivo do modelo GLB. | STRING |
| `rig_task_id` | O ID único da tarefa para esta operação de rigagem, que pode ser usado para referenciar o resultado. | STRING |
| `GLB` | O modelo 3D de personagem rigado salvo no formato de arquivo GLB. | FILE3DGLB |
| `FBX` | O modelo 3D de personagem rigado salvo no formato de arquivo FBX. | FILE3DFBX |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyRigModelNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `91e06e3465d3d309d2267ae307ec5a704af3903b7a6d7fb6011217dd58a63973`
