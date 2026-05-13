> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaImageEditNode/pt-BR.md)

O nó de Edição de Imagem Bria FIBO permite modificar uma imagem existente usando uma instrução de texto. Ele envia a imagem e seu prompt para a API Bria, que utiliza o modelo FIBO para gerar uma nova versão editada da imagem com base na sua solicitação. Você também pode fornecer uma máscara para limitar as edições a uma área específica.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `model` | COMBO | Sim | `"FIBO"` | A versão do modelo a ser usada para edição de imagem. |
| `image` | IMAGE | Sim | - | A imagem de entrada que você deseja editar. |
| `prompt` | STRING | Não | - | A instrução de texto descrevendo como editar a imagem (padrão: vazio). |
| `negative_prompt` | STRING | Não | - | Texto descrevendo o que você não deseja que apareça na imagem editada (padrão: vazio). |
| `structured_prompt` | STRING | Não | - | Uma string contendo o prompt de edição estruturada no formato JSON. Use este campo em vez do prompt comum para controle preciso e programático (padrão: vazio). |
| `seed` | INT | Sim | 1 a 2147483647 | Um número usado para inicializar a geração aleatória, garantindo resultados reproduzíveis (padrão: 1). |
| `guidance_scale` | FLOAT | Sim | 3.0 a 5.0 | Controla o quão fielmente a imagem gerada segue o prompt. Um valor maior resulta em aderência mais forte (padrão: 3.0). |
| `steps` | INT | Sim | 20 a 50 | O número de etapas de remoção de ruído que o modelo executará (padrão: 50). |
| `moderation` | DYNAMICCOMBO | Sim | `"false"`<br>`"true"` | Ativa ou desativa a moderação de conteúdo. Selecionar `"true"` revela opções adicionais de moderação para conteúdo do prompt, entrada visual e saída visual. |
| `mask` | MASK | Não | - | Uma imagem de máscara opcional. Se fornecida, as edições serão aplicadas apenas às áreas mascaradas da imagem. |

**Restrições Importantes:**

* Você deve fornecer pelo menos uma das entradas `prompt` ou `structured_prompt`. Ambas não podem estar vazias.
* Exatamente uma imagem de entrada `image` é necessária.
* Quando o parâmetro `moderation` estiver definido como `"true"`, três entradas booleanas adicionais ficam disponíveis: `prompt_content_moderation` (padrão: false), `visual_input_moderation` (padrão: false) e `visual_output_moderation` (padrão: true).

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `IMAGE` | IMAGE | A imagem editada retornada pela API Bria. |
| `structured_prompt` | STRING | O prompt estruturado que foi usado ou gerado durante o processo de edição. |

---
**Source fingerprint (SHA-256):** `30148261f43f5bfd14339f5ff1ec250381a615cc05c67eee21b0a2423ebe349d`
