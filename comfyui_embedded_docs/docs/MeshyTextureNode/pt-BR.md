> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextureNode/pt-BR.md)

O nó Meshy: Textura aplica texturas geradas por IA a um modelo 3D. Ele recebe um ID de tarefa de um nó anterior de geração ou conversão 3D do Meshy e usa uma descrição textual ou uma imagem de referência para criar novas texturas para o modelo. O nó gera o modelo texturizado nos formatos de arquivo GLB e FBX.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `model` | COMBO | Sim | `"latest"` | A versão do modelo de IA a ser usada para texturização. Atualmente, apenas a versão "latest" está disponível. |
| `meshy_task_id` | MESHY_TASK_ID | Sim | - | O identificador único (ID da tarefa) de uma tarefa anterior de geração ou conversão 3D do Meshy. Isso fornece o modelo 3D base a ser texturizado. |
| `enable_original_uv` | BOOLEAN | Não | - | Usar o UV original do modelo em vez de gerar novos UVs. Quando ativado (padrão: `True`), o Meshy preserva as texturas existentes do modelo enviado. Se o modelo não tiver UV original, a qualidade da saída pode não ser tão boa. |
| `pbr` | BOOLEAN | Não | - | Ativa a saída de material de Renderização Baseada em Física (PBR) para o modelo texturizado (padrão: `False`). |
| `text_style_prompt` | STRING | Não | - | Descreva o estilo de textura desejado do objeto usando texto. Máximo de 600 caracteres. Não pode ser usado ao mesmo tempo que `image_style`. |
| `image_style` | IMAGE | Não | - | Uma imagem 2D para guiar o processo de texturização. Não pode ser usada ao mesmo tempo que `text_style_prompt`. |

**Restrições dos Parâmetros:**

* Você deve fornecer um `text_style_prompt` ou um `image_style`, mas não pode fornecer ambos ao mesmo tempo.
* O `text_style_prompt` é limitado a um máximo de 600 caracteres.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `model_file` | STRING | O nome do arquivo do modelo GLB gerado. Esta saída é fornecida para compatibilidade com versões anteriores. |
| `meshy_task_id` | MODEL_TASK_ID | O identificador único da tarefa para este trabalho de texturização, que pode ser usado para referenciar o resultado. |
| `GLB` | FILE3DGLB | O modelo 3D texturizado salvo no formato de arquivo GLB. |
| `FBX` | FILE3DFBX | O modelo 3D texturizado salvo no formato de arquivo FBX. |

---
**Source fingerprint (SHA-256):** `380b682a8290c69e71a204c8c3d6c2d4fb2c15f4bc1679b98c7fc4fd9ec9e1b3`
