# Meshy: Text to Model (Smart Topology)

Este nó gera uma malha triangular pronta para jogos com uma contagem de faces alvo usando o Meshy T2.5. A topologia é construída na contagem de polígonos solicitada em vez de ser decimada depois, portanto o resultado está pronto para uma engine de jogos sem uma etapa separada de retopologia.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | A versão do modelo Meshy a ser usada para geração. | COMBO | Sim | `"meshy-t2.5"` |
| `prompt` | A descrição textual do modelo 3D a ser gerado. | STRING | Sim | 1 a 800 caracteres |
| `target_polycount` | Número aproximado de triângulos na malha gerada. Padrão: 15000. | INT | Sim | 100 a 30000 |
| `pose_mode` | A pose do personagem gerado. Uma string vazia solicita nenhuma pose específica. Esta é uma configuração avançada. Padrão: `""` (string vazia). | COMBO | Sim | `""`<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | A seed controla se o nó deve ser executado novamente; os resultados não são determinísticos independentemente da seed. Padrão: 42. | INT | Sim | 0 a 2147483647 |

**Restrições:**

* O prompt deve conter entre 1 e 800 caracteres.
* `target_polycount` é o número de triângulos a partir do qual a malha é construída, não um limite aplicado após a geração.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `meshy_task_id` | O identificador exclusivo da tarefa da API Meshy. | MESHY_TASK_ID |
| `GLB` | O modelo 3D gerado no formato GLB. | FILE3DGLB |
| `FBX` | O modelo 3D gerado no formato FBX. | FILE3DFBX |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextToModelSmartTopologyNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `9fcdc846a4ba39cf3d099629637fbb0cf6d9c8d65bcee8aff5ec6ac5c76b6af3`
