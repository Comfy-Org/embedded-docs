O nó Meshy: Textura aplica texturas geradas por IA a um modelo 3D. Ele recebe um ID de tarefa de um nó anterior de geração ou conversão 3D do Meshy e usa uma descrição textual ou uma imagem de referência para criar novas texturas para o modelo. O nó gera o modelo texturizado nos formatos de arquivo GLB e FBX.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | A versão do modelo de IA a ser usada para texturização. Atualmente, apenas a versão "latest" está disponível. | COMBO | Sim | `"latest"` |
| `meshy_task_id` | O identificador único (ID da tarefa) de uma tarefa anterior de geração ou conversão 3D do Meshy. Isso fornece o modelo 3D base a ser texturizado. | MESHY_TASK_ID | Sim | - |
| `habilitar_uv_original` | Usar o UV original do modelo em vez de gerar novos UVs. Quando ativado (padrão: `True`), o Meshy preserva as texturas existentes do modelo enviado. Se o modelo não tiver UV original, a qualidade da saída pode não ser tão boa. | BOOLEAN | Não | - |
| `pbr` | Ativa a saída de material de Renderização Baseada em Física (PBR) para o modelo texturizado (padrão: `False`). | BOOLEAN | Não | - |
| `prompt_de_estilo_textual` | Descreva o estilo de textura desejado do objeto usando texto. Máximo de 600 caracteres. Não pode ser usado ao mesmo tempo que `estilo_de_imagem`. | STRING | Não | - |
| `estilo_de_imagem` | Uma imagem 2D para guiar o processo de texturização. Não pode ser usada ao mesmo tempo que `prompt_de_estilo_textual`. | IMAGE | Não | - |

**Restrições dos Parâmetros:**

* Você deve fornecer um `text_style_prompt` ou um `image_style`, mas não pode fornecer ambos ao mesmo tempo.
* O `text_style_prompt` é limitado a um máximo de 600 caracteres.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model_file` | O nome do arquivo do modelo GLB gerado. Esta saída é fornecida para compatibilidade com versões anteriores. | STRING |
| `meshy_task_id` | O identificador único da tarefa para este trabalho de texturização, que pode ser usado para referenciar o resultado. | MODEL_TASK_ID |
| `GLB` | O modelo 3D texturizado salvo no formato de arquivo GLB. | FILE3DGLB |
| `FBX` | O modelo 3D texturizado salvo no formato de arquivo FBX. | FILE3DFBX |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextureNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `380b682a8290c69e71a204c8c3d6c2d4fb2c15f4bc1679b98c7fc4fd9ec9e1b3`
