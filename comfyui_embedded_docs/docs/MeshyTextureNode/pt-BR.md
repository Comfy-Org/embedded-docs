# Meshy: Modelo de Textura

O nó Meshy: Texture Model aplica texturas geradas por IA a um modelo 3D existente. Ele usa um ID de tarefa de uma tarefa anterior de geração ou conversão 3D do Meshy e orienta o processo de texturização com um prompt de estilo em texto ou uma imagem de referência. O nó retorna o modelo texturizado nos formatos de arquivo GLB e FBX.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | A versão do modelo de IA a ser usada para texturização. | COMBO | Sim | `"meshy-7"`<br>`"meshy-6"`<br>`"latest"` |
| `meshy_task_id` | O identificador exclusivo (ID da tarefa) de uma tarefa anterior de geração ou conversão 3D do Meshy. Ele fornece o modelo 3D base a ser texturizado. | MESHY_TASK_ID | Sim | - |
| `enable_original_uv` | Usa o UV original do modelo em vez de gerar novos UVs. Quando habilitado (padrão: `True`), o Meshy preserva texturas existentes do modelo enviado. Se o modelo não tiver UV original, a qualidade da saída pode não ser tão boa. Esta é uma opção avançada. | BOOLEAN | Sim | true / false |
| `pbr` | Habilita a saída de material com Renderização Baseada em Física (PBR) para o modelo texturizado (padrão: `False`). Esta é uma opção avançada. | BOOLEAN | Sim | true / false |
| `text_style_prompt` | Descreva o estilo de textura desejado para o objeto usando texto (padrão: string vazia). Máximo de 600 caracteres. Não pode ser usado ao mesmo tempo que `image_style`. | STRING | Sim | - |
| `image_style` | Uma imagem 2D para orientar o processo de texturização. Não pode ser usada ao mesmo tempo que `text_style_prompt`. | IMAGE | Não | - |
| `texture_resolution` | Resolução da textura de cor base. Resoluções mais altas capturam mais detalhes da superfície. | COMBO | Sim | `"2k"`<br>`"4k"`<br>`"8k"` |

**Restrições de parâmetros:**

* Você deve fornecer um `text_style_prompt` ou uma `image_style`, mas não pode fornecer ambos ao mesmo tempo.
* O `text_style_prompt` é limitado a um máximo de 600 caracteres.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `model_file` | O nome do arquivo do modelo GLB gerado. Esta saída é fornecida apenas para compatibilidade com versões anteriores. | STRING |
| `meshy_task_id` | O identificador exclusivo da tarefa para este trabalho de texturização, que pode ser usado para referenciar o resultado. | MESHY_TASK_ID |
| `GLB` | O modelo 3D texturizado salvo no formato de arquivo GLB. | FILE3DGLB |
| `FBX` | O modelo 3D texturizado salvo no formato de arquivo FBX. | FILE3DFBX |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextureNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `30d51f6efe3602f27d99706840c974baf2c4397a4f9a191f3478e7eff372e319`
