# Meshy: Modelo de Textura

O nó Meshy: Texture aplica texturas geradas por IA a um modelo 3D. Ele recebe um ID de tarefa de um nó anterior de geração ou conversão 3D do Meshy e usa uma descrição de texto ou uma imagem de referência para criar novas texturas para o modelo. O nó gera o modelo texturizado nos formatos de arquivo GLB e FBX.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | A versão do modelo de IA a ser usada para texturização. | COMBO | Sim | `"meshy-7"`<br>`"meshy-6"`<br>`"latest"` |
| `meshy_task_id` | O identificador exclusivo (ID da tarefa) de uma tarefa anterior de geração ou conversão 3D do Meshy. Isso fornece o modelo 3D base a ser texturizado. | MESHY_TASK_ID | Sim | - |
| `habilitar_uv_original` | Use a UV original do modelo em vez de gerar novas UVs. Quando ativado (padrão: `True`), o Meshy preserva as texturas existentes do modelo enviado. Se o modelo não tiver UV original, a qualidade da saída pode não ser tão boa. Esta é uma opção avançada. | BOOLEAN | Não | true / false |
| `pbr` | Ativa a saída de material com renderização baseada em física (PBR) para o modelo texturizado (padrão: `False`). Esta é uma opção avançada. | BOOLEAN | Não | true / false |
| `prompt_de_estilo_textual` | Descreva o estilo de textura desejado do objeto usando texto. Máximo de 600 caracteres. Não pode ser usado ao mesmo tempo que `image_style`. | STRING | Não | - |
| `estilo_de_imagem` | Uma imagem 2D para orientar o processo de texturização. Não pode ser usada ao mesmo tempo que `text_style_prompt`. | IMAGE | Não | - |
| `texture_resolution` | Resolução da textura de cor base. Resoluções mais altas capturam mais detalhes da superfície. | COMBO | Sim | `"2k"`<br>`"4k"`<br>`"8k"` |

**Restrições de Parâmetro:**

* Você deve fornecer um `text_style_prompt` ou um `image_style`, mas não pode fornecer ambos ao mesmo tempo.
* O `text_style_prompt` é limitado a um máximo de 600 caracteres.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `arquivo_do_modelo` | O nome do arquivo do modelo GLB gerado. Esta saída é fornecida apenas para compatibilidade reversa. | STRING |
| `meshy_task_id` | O identificador exclusivo da tarefa para este trabalho de texturização, que pode ser usado para referenciar o resultado. | MESHY_TASK_ID |
| `GLB` | O modelo 3D texturizado salvo no formato de arquivo GLB. | FILE3DGLB |
| `FBX` | O modelo 3D texturizado salvo no formato de arquivo FBX. | FILE3DFBX |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextureNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `30d51f6efe3602f27d99706840c974baf2c4397a4f9a191f3478e7eff372e319`
