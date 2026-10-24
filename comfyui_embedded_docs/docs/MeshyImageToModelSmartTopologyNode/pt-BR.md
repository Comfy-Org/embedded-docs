# Meshy: Image to Model (Smart Topology)

Este nó gera uma malha triangular pronta para jogos a partir de uma imagem de referência, com uma contagem de faces alvo, usando o Meshy T2.5. A topologia é construída na contagem de polígonos solicitada, em vez de ser decimada depois, de modo que o resultado já está pronto para uma engine de jogos sem uma etapa separada de retopologia.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | A versão do modelo Meshy a ser usada para geração. | COMBO | Sim | `"meshy-t2.5"` |
| `image` | A imagem de referência a partir da qual o modelo é gerado. | IMAGE | Sim | - |
| `target_polycount` | Número aproximado de triângulos na malha gerada. Padrão: 15000. | INT | Sim | 100 a 30000 |
| `should_texture` | Determina se as texturas são geradas. `"false"` pula a fase de textura e retorna uma malha sem textura. | DYNAMIC_COMBO | Sim | `"true"`<br>`"false"` |
| `enable_pbr` | Gera mapas PBR (metálico, rugosidade, normal) além da cor base. Esta entrada só está disponível quando `should_texture` está definido como `"true"`. Padrão: `False`. | BOOLEAN | Não | - |
| `texture_prompt` | Prompt de texto para orientar o processo de texturização. Máximo de 800 caracteres. Não pode ser usado ao mesmo tempo que `texture_image`. Esta entrada só está disponível quando `should_texture` está definido como `"true"`. Padrão: `""` (string vazia). | STRING | Não | 1 a 800 caracteres |
| `texture_image` | Imagem de referência para o processo de texturização. Apenas um entre `texture_image` ou `texture_prompt` pode ser usado ao mesmo tempo. Esta entrada só está disponível quando `should_texture` está definido como `"true"`. | IMAGE | Não | - |
| `texture_resolution` | Resolução da textura. Resoluções mais altas capturam mais detalhes da superfície. Esta entrada só está disponível quando `should_texture` está definido como `"true"`. | COMBO | Não | `"2k"`<br>`"4k"`<br>`"8k"` |
| `pose_mode` | A pose do personagem gerado. Uma string vazia indica que nenhuma pose específica é solicitada. Esta é uma configuração avançada. Padrão: `""` (string vazia). | COMBO | Sim | `""`<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | A seed controla se o nó deve ser executado novamente; os resultados não são determinísticos independentemente da seed. Padrão: 42. | INT | Sim | 0 a 2147483647 |

**Observação:** As entradas `enable_pbr`, `texture_prompt`, `texture_image` e `texture_resolution` só estão disponíveis quando `should_texture` está definido como `"true"`.

**Restrições:**

* `target_polycount` é o número de triângulos a partir do qual a malha é construída, não um limite aplicado após a geração.
* Quando `should_texture` está definido como `"true"`, `texture_prompt` e `texture_image` não podem ser usados ao mesmo tempo. Se ambos forem fornecidos, o nó gera um erro.
* `texture_prompt` tem comprimento máximo de 800 caracteres.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `meshy_task_id` | O identificador exclusivo da tarefa da API Meshy. | MESHY_TASK_ID |
| `GLB` | O modelo 3D gerado no formato GLB. | FILE3DGLB |
| `FBX` | O modelo 3D gerado no formato FBX. | FILE3DFBX |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyImageToModelSmartTopologyNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e78034a591825ec6e105df1942cf501e882ac780cc2584bfa04b424ecc34a02e`
