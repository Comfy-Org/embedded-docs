# Meshy: Rig de Modelo

O nó Meshy: Rig Model recebe um modelo 3D de uma tarefa Meshy anterior e cria automaticamente um esqueleto para ele, produzindo um personagem com rig que pode receber poses e ser animado. O nó gera o modelo com rig nos formatos de arquivo GLB e FBX.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `meshy_task_id` | O ID exclusivo da tarefa de uma operação Meshy anterior (por exemplo, text-to-3D ou image-to-3D) que gerou o modelo que receberá o rig. | MESHY_TASK_ID | Sim | N/A |
| `altura_metros` | A altura aproximada do modelo do personagem em metros. Isso ajuda na precisão de escala e de rigging (padrão: 1,7). | FLOAT | Sim | 0,1 a 15,0 |
| `imagem_de_textura` | A imagem de textura de cor base com UV desdobrado do modelo. | IMAGE | Não | N/A |

**Observação:** O processo de rigging automático atualmente não é adequado para malhas sem textura, ativos não humanoides ou ativos humanoides com estrutura de membros e corpo pouco clara.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `model_file` | Uma saída legada mantida apenas para compatibilidade com versões anteriores, contendo o nome do arquivo do modelo GLB. | STRING |
| `rig_task_id` | O ID exclusivo da tarefa para esta operação de rigging, que pode ser usado para referenciar o resultado em nós Meshy posteriores. | MESHY_RIGGED_TASK_ID |
| `GLB` | O modelo de personagem 3D com rig salvo no formato de arquivo GLB. | FILE3DGLB |
| `FBX` | O modelo de personagem 3D com rig salvo no formato de arquivo FBX. | FILE3DFBX |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyRigModelNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `6ae79359fa54f36dd2491a952fe54fa56866038758e8cd475a2d2f8e9e47e3b3`
