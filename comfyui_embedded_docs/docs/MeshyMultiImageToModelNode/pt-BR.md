# Meshy: Múltiplas Imagens para Modelo

Este nó usa a API Meshy para gerar um modelo 3D a partir de múltiplas imagens de entrada. Ele envia as imagens fornecidas, submete uma tarefa de processamento e retorna os arquivos do modelo 3D resultante (GLB e FBX) junto com o ID da tarefa para referência.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | Especifica a versão do modelo de IA a ser usada. | COMBO | Sim | `"latest"` |
| `refazer_malha` | Determina se a malha gerada deve ser processada. Quando definido como `"false"`, o nó retorna uma malha triangular não processada. Quando definido como `"true"`, as configurações de remesh abaixo são exibidas. | DYNAMIC_COMBO | Sim | `"true"`<br>`"false"` |
| `modo_de_simetria` | Controla se a simetria é aplicada ao modelo gerado. | COMBO | Sim | `"auto"`<br>`"on"`<br>`"off"` |
| `gerar_textura` | Determina se as texturas são geradas. Definir como `"false"` pula a fase de texturização e retorna uma malha sem texturas. Quando definido como `"true"`, as configurações de textura abaixo são exibidas. | DYNAMIC_COMBO | Sim | `"true"`<br>`"false"` |
| `modo_de_pose` | Especifica o modo de pose para o modelo gerado. | COMBO | Sim | `""` (vazio)<br>`"A-pose"`<br>`"T-pose"` |
| `semente` | A `seed` controla se o nó deve ser executado novamente; os resultados não são determinísticos independentemente do valor da `seed`. (padrão: 0) | INT | Sim | 0 a 2147483647 |

### Configurações de remesh (visíveis quando `should_remesh` estiver definido como `"true"`)

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `topology` | O tipo de polígono alvo para a saída remalhada. | COMBO | Não | `"triangle"`<br>`"quad"` |
| `target_polycount` | O número alvo de polígonos para o modelo remalhado (padrão: 300000). | INT | Não | 100 a 300000 |

### Configurações de textura (visíveis quando `should_texture` estiver definido como `"true"`)

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `enable_pbr` | Gera mapas PBR (metálico, rugosidade, normal) além da cor base. (padrão: False) | BOOLEAN | Não | True / False |
| `texture_prompt` | Forneça um prompt de texto para orientar o processo de texturização. Máximo de 600 caracteres. Não pode ser usado ao mesmo tempo que `texture_image`. (padrão: vazio) | STRING | Não | - |
| `texture_image` | Apenas um entre `texture_image` e `texture_prompt` pode ser usado ao mesmo tempo. | IMAGE | Não | - |

### Entradas de imagem

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `imagens` | Slot expansível: conecte de 2 a 4 imagens de entrada (`image_1`, `image_2`, `image_3`, `image_4`). Essas imagens são usadas para gerar o modelo 3D. | IMAGE | Sim | 2 a 4 imagens |

**Notas**

* Você deve fornecer entre 2 e 4 imagens para a entrada `images`.
* Os parâmetros `topology` e `target_polycount` só ficam ativos quando `should_remesh` está definido como `"true"`.
* Os parâmetros `enable_pbr`, `texture_prompt` e `texture_image` só ficam ativos quando `should_texture` está definido como `"true"`.
* `texture_prompt` e `texture_image` são mutuamente exclusivos; você não pode usar ambos ao mesmo tempo. `texture_prompt` é limitado a 600 caracteres.
* O valor de `seed` não torna os resultados determinísticos; alterá-lo apenas faz com que o nó execute novamente a tarefa de geração.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `arquivo_do_modelo` | O nome do arquivo do modelo GLB gerado. Esta saída é fornecida apenas para compatibilidade reversa. | STRING |
| `meshy_task_id` | O identificador exclusivo da tarefa da API Meshy. | MESHY_TASK_ID |
| `GLB` | O modelo 3D gerado no formato GLB. | FILE3DGLB |
| `FBX` | O modelo 3D gerado no formato FBX. | FILE3DFBX |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyMultiImageToModelNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c2282cad611bbbc8c0a618df6a68fcd9f6e3c29c6d08b2c96a117c29765d8a7a`
