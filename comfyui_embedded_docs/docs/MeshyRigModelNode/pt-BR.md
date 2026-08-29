# Meshy: Rig de Modelo

O nó Meshy: Rig Model recebe um modelo 3D de uma tarefa Meshy anterior e cria automaticamente um esqueleto para ele, produzindo um personagem rigado que pode ser posado e animado. O nó gera o modelo rigado em ambos os formatos de arquivo GLB e FBX.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `meshy_task_id` | O ID exclusivo da tarefa de uma operação Meshy anterior (ex.: texto para 3D ou imagem para 3D) que gerou o modelo a ser rigado. | STRING | Sim | N/A |
| `altura_metros` | A altura aproximada do modelo do personagem em metros. Isso auxilia na escala e na precisão do rig (padrão: 1.7). | FLOAT | Sim | 0.1 a 15.0 |
| `imagem_de_textura` | A imagem de textura de cor base do modelo com UV desembrulhado. | IMAGE | Não | N/A |

**Nota:** O processo de rig automático atualmente não é adequado para malhas sem textura, assets não humanoides ou assets humanoides com estrutura de membros e corpo pouco clara.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `arquivo_do_modelo` | Uma saída legada para compatibilidade reversa, contendo o nome do arquivo do modelo GLB. | STRING |
| `rig_task_id` | O ID exclusivo da tarefa desta operação de rig, que pode ser usado para referenciar o resultado. | STRING |
| `GLB` | O modelo de personagem 3D rigado salvo no formato de arquivo GLB. | FILE3DGLB |
| `FBX` | O modelo de personagem 3D rigado salvo no formato de arquivo FBX. | FILE3DFBX |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyRigModelNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `6ae79359fa54f36dd2491a952fe54fa56866038758e8cd475a2d2f8e9e47e3b3`
