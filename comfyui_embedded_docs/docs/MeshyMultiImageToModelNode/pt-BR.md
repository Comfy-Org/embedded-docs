> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyMultiImageToModelNode/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyMultiImageToModelNode/en.md)

Este nó utiliza a API Meshy para gerar um modelo 3D a partir de múltiplas imagens de entrada. Ele faz o upload das imagens fornecidas, envia uma tarefa de processamento e retorna os arquivos do modelo 3D resultante (GLB e FBX), juntamente com o ID da tarefa para referência.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
| :--- | :--- | :--- | :--- | :--- |
| `model` | COMBO | Sim | `"latest"` | Especifica a versão do modelo de IA a ser utilizada. |
| `images` | IMAGE | Sim | 2 a 4 imagens | Um conjunto de imagens usado para gerar o modelo 3D. Você deve fornecer entre 2 e 4 imagens. |
| `should_remesh` | COMBO | Sim | `"true"`<br>`"false"` | Determina se a malha gerada deve ser processada. Quando definido como `"false"`, o nó retorna uma malha triangular não processada. |
| `topology` | COMBO | Não | `"triangle"`<br>`"quad"` | O tipo de polígono alvo para a saída remalhada. Este parâmetro está disponível e é obrigatório apenas quando `should_remesh` está definido como `"true"`. |
| `target_polycount` | INT | Não | 100 a 300000 | O número alvo de polígonos para o modelo remalhado (padrão: 300000). Este parâmetro está disponível apenas quando `should_remesh` está definido como `"true"`. |
| `symmetry_mode` | COMBO | Sim | `"auto"`<br>`"on"`<br>`"off"` | Controla se a simetria é aplicada ao modelo gerado. |
| `should_texture` | COMBO | Sim | `"true"`<br>`"false"` | Determina se as texturas são geradas. Definir como `"false"` pula a fase de texturização e retorna uma malha sem texturas. |
| `enable_pbr` | BOOLEAN | Não | Verdadeiro / Falso | Quando `should_texture` é `"true"`, esta opção gera Mapas PBR (metálico, rugosidade, normal) além da cor base (padrão: Falso). |
| `texture_prompt` | STRING | Não | - | Um prompt de texto para guiar o processo de texturização (máximo de 600 caracteres). Não pode ser usado ao mesmo tempo que `texture_image`. Este parâmetro está disponível apenas quando `should_texture` está definido como `"true"`. |
| `texture_image` | IMAGE | Não | - | Uma imagem para guiar o processo de texturização. Apenas um dos parâmetros `texture_image` ou `texture_prompt` pode ser usado por vez. Este parâmetro está disponível apenas quando `should_texture` está definido como `"true"`. |
| `pose_mode` | COMBO | Sim | `""` (vazio)<br>`"A-pose"`<br>`"T-pose"` | Especifica o modo de pose para o modelo gerado. |
| `seed` | INT | Sim | 0 a 2147483647 | Um valor de semente para o processo de geração (padrão: 0). Os resultados são não determinísticos independentemente da semente, mas alterar a semente pode fazer com que o nó seja executado novamente. |

**Restrições dos Parâmetros:**

* Você deve fornecer entre 2 e 4 imagens para a entrada `images`.
* Os parâmetros `topology` e `target_polycount` estão ativos apenas quando `should_remesh` está definido como `"true"`.
* Os parâmetros `enable_pbr`, `texture_prompt` e `texture_image` estão ativos apenas quando `should_texture` está definido como `"true"`.
* Você não pode usar `texture_prompt` e `texture_image` ao mesmo tempo; eles são mutuamente exclusivos.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
| :--- | :--- | :--- |
| `model_file` | STRING | O nome do arquivo do modelo GLB gerado. Esta saída é fornecida para compatibilidade com versões anteriores. |
| `meshy_task_id` | MESHY_TASK_ID | O identificador único para a tarefa da API Meshy. |
| `GLB` | FILE3DGLB | O modelo 3D gerado no formato GLB. |
| `FBX` | FILE3DFBX | O modelo 3D gerado no formato FBX. |

---
**Source fingerprint (SHA-256):** `e6f75f50645c8b2cf5ebbe037edb077ef1eb0ea1baf67c581d60ac0033686d00`
