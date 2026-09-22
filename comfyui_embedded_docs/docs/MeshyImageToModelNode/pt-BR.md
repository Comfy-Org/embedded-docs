# Meshy: Imagem para Modelo

O nó Meshy: Image to Model usa a API Meshy para gerar um modelo 3D a partir de uma única imagem de entrada. Ele faz upload da sua imagem, submete uma tarefa de processamento e retorna os arquivos do modelo 3D gerado (GLB e FBX) juntamente com o ID da tarefa para referência.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | Especifica a versão do modelo de IA a ser usada para a geração. | COMBO | Sim | `"meshy-7.1"`<br>`"meshy-7"`<br>`"meshy-6"`<br>`"latest"` |
| `imagem` | A imagem de entrada para converter em um modelo 3D. | IMAGE | Sim | - |
| `refazer_malha` | Quando definido como `"false"`, retorna uma malha triangular não processada. | DYNAMIC_COMBO | Sim | `"true"`<br>`"false"` |
| `topology` | A topologia de polígonos alvo para o modelo remalhado. Esta entrada está disponível somente quando `should_remesh` está definido como `"true"`. | COMBO | Não* | `"triangle"`<br>`"quad"` |
| `target_polycount` | O número alvo de polígonos para o modelo remalhado. Esta entrada está disponível somente quando `should_remesh` está definido como `"true"`. Padrão: 300000. | INT | Não* | 100 - 300000 |
| `modo_de_simetria` | Controla a simetria aplicada ao modelo 3D gerado. | COMBO | Sim | `"auto"`<br>`"on"`<br>`"off"` |
| `gerar_textura` | Determina se texturas são geradas. Definir como `"false"` pula a fase de texturização e retorna uma malha sem texturas. | DYNAMIC_COMBO | Sim | `"true"`<br>`"false"` |
| `enable_pbr` | Gera mapas PBR (metálico, rugosidade, normal) além da cor base. Esta entrada está disponível somente quando `should_texture` está definido como `"true"`. Padrão: `False`. | BOOLEAN | Não* | - |
| `texture_prompt` | Fornece um prompt de texto para orientar o processo de texturização. Máximo de 600 caracteres. Não pode ser usado ao mesmo tempo que `texture_image`. Esta entrada está disponível somente quando `should_texture` está definido como `"true"`. Padrão: string vazia. | STRING | Não* | - |
| `texture_image` | Apenas um entre `texture_image` ou `texture_prompt` pode ser usado ao mesmo tempo. Esta entrada está disponível somente quando `should_texture` está definido como `"true"`. | IMAGE | Não* | - |
| `texture_resolution` | Resolução da textura da cor base. Resoluções mais altas capturam mais detalhes da superfície. Esta entrada está disponível somente quando `should_texture` está definido como `"true"`. | COMBO | Não* | `"2k"`<br>`"4k"`<br>`"8k"` |
| `modo_de_pose` | Especifica o modo de pose para o modelo gerado. Este é um parâmetro avançado. | COMBO | Sim | `""` (vazio)<br>`"A-pose"`<br>`"T-pose"` |
| `semente` | A seed controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da seed. Padrão: 0. | INT | Sim | 0 - 2147483647 |
| `ultra_mode` | Executa uma etapa extra de refinamento para uma geometria de maior fidelidade com detalhes de superfície mais finos. Padrão: `False`. | BOOLEAN | Sim | - |
| `ultra_resolution` | Resolução da passagem ultra: `"2k"` a executa em 2048³ e `"4k"` em 4096³ para o detalhe de superfície mais fino. `"4k"` requer o modelo `"meshy-7.1"` ou `"latest"`. Usado apenas quando `ultra_mode` está habilitado (padrão: `"2k"`). | COMBO | Não | `"2k"`<br>`"4k"` |

**Nota sobre as restrições de parâmetros:**

* As entradas `topology` e `target_polycount` estão disponíveis somente quando `should_remesh` está definido como `"true"`.
* As entradas `enable_pbr`, `texture_prompt`, `texture_image` e `texture_resolution` estão disponíveis somente quando `should_texture` está definido como `"true"`.
* Quando `should_texture` está definido como `"true"`, `texture_prompt` e `texture_image` não podem ser usados ao mesmo tempo. Se ambos forem fornecidos, o nó gera um erro.
* `texture_prompt` tem comprimento máximo de 600 caracteres.
* Quando `ultra_mode` está habilitado, o parâmetro `model` deve ser definido como `"meshy-7.1"`, `"meshy-7"` ou `"latest"`; qualquer outro modelo gera um erro. Com `"meshy-7"` a passagem ultra sempre é executada em 2048³, e a resolução ultra `"4k"` requer `"meshy-7.1"` ou `"latest"`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `arquivo_do_modelo` | O nome do arquivo do modelo GLB gerado. Mantido apenas para compatibilidade com versões anteriores. | STRING |
| `meshy_task_id` | O identificador único para a tarefa da API Meshy, que pode ser usado para referência ou solução de problemas. | MESHY_TASK_ID |
| `GLB` | O modelo 3D gerado no formato de arquivo GLB. | FILE3DGLB |
| `FBX` | O modelo 3D gerado no formato de arquivo FBX. | FILE3DFBX |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyImageToModelNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `38528b48c3f792a459008a52f65fae248ef1dadafb37fe4dc6b697d25bc89f4f`
