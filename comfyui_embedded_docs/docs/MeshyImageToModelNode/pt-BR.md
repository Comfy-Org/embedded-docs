# Meshy: Imagem para Modelo

O nó Meshy: Image to Model usa a API Meshy para gerar um modelo 3D a partir de uma única imagem de entrada. Ele envia sua imagem, submete uma tarefa de processamento e retorna os arquivos do modelo 3D gerado (GLB e FBX), junto com o ID da tarefa para referência.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | Especifica a versão do modelo de IA a ser usada para a geração. | COMBO | Sim | `"latest"` |
| `imagem` | A imagem de entrada para converter em um modelo 3D. | IMAGE | Sim | - |
| `refazer_malha` | Quando definido como `"false"`, retorna uma malha triangular não processada. | DYNAMIC_COMBO | Sim | `"true"`<br>`"false"` |
| `topology` | A topologia de polígonos alvo para o modelo remalhado. Esta entrada só está disponível quando `should_remesh` está definido como `"true"`. | COMBO | Não* | `"triangle"`<br>`"quad"` |
| `target_polycount` | O número-alvo de polígonos para o modelo remalhado. Esta entrada só está disponível quando `should_remesh` está definido como `"true"`. Padrão: 300000. | INT | Não* | 100 - 300000 |
| `modo_de_simetria` | Controla a simetria aplicada ao modelo 3D gerado. | COMBO | Sim | `"auto"`<br>`"on"`<br>`"off"` |
| `gerar_textura` | Determina se as texturas são geradas. Definir como `"false"` pula a fase de texturização e retorna uma malha sem texturas. | DYNAMIC_COMBO | Sim | `"true"`<br>`"false"` |
| `enable_pbr` | Gera mapas PBR (metálico, rugosidade, normal) além da cor base. Esta entrada só está disponível quando `should_texture` está definido como `"true"`. Padrão: `False`. | BOOLEAN | Não* | - |
| `texture_prompt` | Forneça um prompt de texto para orientar o processo de texturização. Máximo de 600 caracteres. Não pode ser usado ao mesmo tempo que `texture_image`. Esta entrada só está disponível quando `should_texture` está definido como `"true"`. Padrão: string vazia. | STRING | Não* | - |
| `texture_image` | Apenas um entre `texture_image` e `texture_prompt` pode ser usado ao mesmo tempo. Esta entrada só está disponível quando `should_texture` está definido como `"true"`. | IMAGE | Não* | - |
| `modo_de_pose` | Especifica o modo de pose para o modelo gerado. Este é um parâmetro avançado. | COMBO | Sim | `""` (vazio)<br>`"A-pose"`<br>`"T-pose"` |
| `semente` | O parâmetro `seed` controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente do valor de `seed`. Padrão: 0. | INT | Sim | 0 - 2147483647 |

**Nota sobre as restrições dos parâmetros:**

* As entradas `topology` e `target_polycount` só estão disponíveis quando `should_remesh` está definido como `"true"`.
* As entradas `enable_pbr`, `texture_prompt` e `texture_image` só estão disponíveis quando `should_texture` está definido como `"true"`.
* Quando `should_texture` está definido como `"true"`, `texture_prompt` e `texture_image` não podem ser usados ao mesmo tempo. Se ambos forem fornecidos, o nó gera um erro.
* `texture_prompt` tem comprimento máximo de 600 caracteres.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `arquivo_do_modelo` | O nome do arquivo do modelo GLB gerado. Mantido apenas para compatibilidade com versões anteriores. | STRING |
| `meshy_task_id` | O identificador único para a tarefa da API Meshy, que pode ser usado para referência ou solução de problemas. | MESHY_TASK_ID |
| `GLB` | O modelo 3D gerado no formato de arquivo GLB. | FILE3DGLB |
| `FBX` | O modelo 3D gerado no formato de arquivo FBX. | FILE3DFBX |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyImageToModelNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `9f7abcb0db3c78715e4ba7370efe294caf186590f7ab62da8568778848fc838c`
