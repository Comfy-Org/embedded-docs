Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyMultiImageToModelNode/en.md)

Este nó utiliza a API Meshy para gerar um modelo 3D a partir de múltiplas imagens de entrada. Ele faz o upload das imagens fornecidas, envia uma tarefa de processamento e retorna os arquivos do modelo 3D resultante (GLB e FBX), juntamente com o ID da tarefa para referência.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | Especifica a versão do modelo de IA a ser utilizada. | COMBO | Sim | `"latest"` |
| `imagens` | Um conjunto de imagens usado para gerar o modelo 3D. Você deve fornecer entre 2 e 4 imagens. | IMAGE | Sim | 2 a 4 imagens |
| `refazer_malha` | Determina se a malha gerada deve ser processada. Quando definido como `"false"`, o nó retorna uma malha triangular não processada. | COMBO | Sim | `"true"`<br>`"false"` |
| `topology` | O tipo de polígono alvo para a saída remalhada. Este parâmetro está disponível e é obrigatório apenas quando `refazer_malha` está definido como `"true"`. | COMBO | Não | `"triangle"`<br>`"quad"` |
| `target_polycount` | O número alvo de polígonos para o modelo remalhado (padrão: 300000). Este parâmetro está disponível apenas quando `refazer_malha` está definido como `"true"`. | INT | Não | 100 a 300000 |
| `modo_de_simetria` | Controla se a simetria é aplicada ao modelo gerado. | COMBO | Sim | `"auto"`<br>`"on"`<br>`"off"` |
| `gerar_textura` | Determina se as texturas são geradas. Definir como `"false"` pula a fase de texturização e retorna uma malha sem texturas. | COMBO | Sim | `"true"`<br>`"false"` |
| `enable_pbr` | Quando `gerar_textura` é `"true"`, esta opção gera Mapas PBR (metálico, rugosidade, normal) além da cor base (padrão: Falso). | BOOLEAN | Não | Verdadeiro / Falso |
| `texture_prompt` | Um prompt de texto para guiar o processo de texturização (máximo de 600 caracteres). Não pode ser usado ao mesmo tempo que `texture_image`. Este parâmetro está disponível apenas quando `gerar_textura` está definido como `"true"`. | STRING | Não | - |
| `texture_image` | Uma imagem para guiar o processo de texturização. Apenas um dos parâmetros `texture_image` ou `texture_prompt` pode ser usado por vez. Este parâmetro está disponível apenas quando `gerar_textura` está definido como `"true"`. | IMAGE | Não | - |
| `modo_de_pose` | Especifica o modo de pose para o modelo gerado. | COMBO | Sim | `""` (vazio)<br>`"A-pose"`<br>`"T-pose"` |
| `semente` | Um valor de semente para o processo de geração (padrão: 0). Os resultados são não determinísticos independentemente da semente, mas alterar a semente pode fazer com que o nó seja executado novamente. | INT | Sim | 0 a 2147483647 |

**Restrições dos Parâmetros:**

* Você deve fornecer entre 2 e 4 imagens para a entrada `images`.
* Os parâmetros `topology` e `target_polycount` estão ativos apenas quando `should_remesh` está definido como `"true"`.
* Os parâmetros `enable_pbr`, `texture_prompt` e `texture_image` estão ativos apenas quando `should_texture` está definido como `"true"`.
* Você não pode usar `texture_prompt` e `texture_image` ao mesmo tempo; eles são mutuamente exclusivos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model_file` | O nome do arquivo do modelo GLB gerado. Esta saída é fornecida para compatibilidade com versões anteriores. | STRING |
| `meshy_task_id` | O identificador único para a tarefa da API Meshy. | MESHY_TASK_ID |
| `GLB` | O modelo 3D gerado no formato GLB. | FILE3DGLB |
| `FBX` | O modelo 3D gerado no formato FBX. | FILE3DFBX |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyMultiImageToModelNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e6f75f50645c8b2cf5ebbe037edb077ef1eb0ea1baf67c581d60ac0033686d00`
