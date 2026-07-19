# Meshy: Imagem para Modelo

O nó Meshy: Image to Model usa a API Meshy para gerar um modelo 3D a partir de uma única imagem de entrada. Ele faz upload da sua imagem, envia uma tarefa de processamento e retorna os arquivos do modelo 3D gerado (GLB e FBX) junto com o ID da tarefa para referência.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | Especifica a versão do modelo de IA a ser usada para geração. | COMBO | Sim | `"latest"` |
| `imagem` | A imagem de entrada para converter em um modelo 3D. | IMAGE | Sim | - |
| `refazer_malha` | Determina se a malha gerada deve ser processada. Quando definido como `"false"`, o nó retorna uma malha triangular não processada. | COMBO DINÂMICO | Sim | `"true"`<br>`"false"` |
| `topology` | A topologia de polígonos alvo para o modelo remalhado. Esta entrada está disponível apenas quando `refazer_malha` está definido como `"true"`. | COMBO | Não* | `"triangle"`<br>`"quad"` |
| `target_polycount` | O número alvo de polígonos para o modelo remalhado. Esta entrada está disponível apenas quando `refazer_malha` está definido como `"true"`. O valor padrão é 300000. | INT | Não* | 100 - 300000 |
| `modo_de_simetria` | Controla a simetria aplicada ao modelo 3D gerado. | COMBO | Sim | `"auto"`<br>`"on"`<br>`"off"` |
| `gerar_textura` | Determina se as texturas são geradas para o modelo. Definir como `"false"` pula a fase de texturização e retorna uma malha sem texturas. | COMBO DINÂMICO | Sim | `"true"`<br>`"false"` |
| `enable_pbr` | Quando `gerar_textura` é `"true"`, esta opção gera mapas PBR (metálico, rugosidade, normal) além da cor base. O valor padrão é `False`. | BOOLEANO | Não* | - |
| `texture_prompt` | Um prompt de texto para guiar o processo de texturização (máximo de 600 caracteres). Esta entrada está disponível apenas quando `gerar_textura` está definido como `"true"`. Não pode ser usado ao mesmo tempo que `texture_image`. | STRING | Não* | - |
| `texture_image` | Uma imagem para guiar o processo de texturização. Esta entrada está disponível apenas quando `gerar_textura` está definido como `"true"`. Não pode ser usado ao mesmo tempo que `texture_prompt`. | IMAGE | Não* | - |
| `modo_de_pose` | Especifica o modo de pose para o modelo gerado. Este é um parâmetro avançado. | COMBO | Sim | `""` (vazio)<br>`"A-pose"`<br>`"T-pose"` |
| `semente` | Um valor de semente para o processo de geração. Os resultados são não determinísticos independentemente do valor da semente. O valor padrão é 0. | INT | Sim | 0 - 2147483647 |

**Nota sobre Restrições de Parâmetros:**

* As entradas `topology` e `target_polycount` estão disponíveis apenas quando `should_remesh` está definido como `"true"`.
* As entradas `enable_pbr`, `texture_prompt` e `texture_image` estão disponíveis apenas quando `should_texture` está definido como `"true"`.
* Você não pode usar `texture_prompt` e `texture_image` ao mesmo tempo. Se ambos forem fornecidos quando `should_texture` for `"true"`, o nó gerará um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model_file` | O nome do arquivo do modelo GLB gerado. (Mantido para compatibilidade retroativa). | STRING |
| `meshy_task_id` | O identificador único para a tarefa da API Meshy, que pode ser usado para referência ou solução de problemas. | MESHY_TASK_ID |
| `GLB` | O modelo 3D gerado no formato de arquivo GLB. | FILE3DGLB |
| `FBX` | O modelo 3D gerado no formato de arquivo FBX. | FILE3DFBX |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyImageToModelNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `134d9250d8b447bbbd2905f827e81b67f491ba355ebb93d4d256324b644100a2`
