# Bria Image Edit

O nó de Edição de Imagem Bria FIBO permite modificar uma imagem existente usando uma instrução de texto. Ele envia a imagem e seu prompt para a API Bria, que utiliza o modelo FIBO para gerar uma nova versão editada da imagem com base na sua solicitação. Você também pode fornecer uma máscara para limitar as edições a uma área específica.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | A versão do modelo a ser usada para edição de imagem. | COMBO | Sim | `"FIBO"` |
| `imagem` | A imagem de entrada que você deseja editar. | IMAGE | Sim | - |
| `prompt` | A instrução de texto descrevendo como editar a imagem (padrão: vazio). | STRING | Não | - |
| `prompt_negativo` | Texto descrevendo o que você não deseja que apareça na imagem editada (padrão: vazio). | STRING | Não | - |
| `prompt_estruturado` | Uma string contendo o prompt de edição estruturada no formato JSON. Use este campo em vez do prompt comum para controle preciso e programático (padrão: vazio). | STRING | Não | - |
| `semente` | Um número usado para inicializar a geração aleatória, garantindo resultados reproduzíveis (padrão: 1). | INT | Sim | 1 a 2147483647 |
| `escala_de_guia` | Controla o quão fielmente a imagem gerada segue o prompt. Um valor maior resulta em aderência mais forte (padrão: 3.0). | FLOAT | Sim | 3.0 a 5.0 |
| `passos` | O número de etapas de remoção de ruído que o modelo executará (padrão: 50). | INT | Sim | 20 a 50 |
| `moderação` | Ativa ou desativa a moderação de conteúdo. Selecionar `"true"` revela opções adicionais de moderação para conteúdo do prompt, entrada visual e saída visual. | DYNAMICCOMBO | Sim | `"false"`<br>`"true"` |
| `máscara` | Uma imagem de máscara opcional. Se fornecida, as edições serão aplicadas apenas às áreas mascaradas da imagem. | MASK | Não | - |

**Restrições Importantes:**

* Você deve fornecer pelo menos uma das entradas `prompt` ou `structured_prompt`. Ambas não podem estar vazias.
* Exatamente uma imagem de entrada `image` é necessária.
* Quando o parâmetro `moderation` estiver definido como `"true"`, três entradas booleanas adicionais ficam disponíveis: `prompt_content_moderation` (padrão: false), `visual_input_moderation` (padrão: false) e `visual_output_moderation` (padrão: true).

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `IMAGE` | A imagem editada retornada pela API Bria. | IMAGE |
| `prompt_estruturado` | O prompt estruturado que foi usado ou gerado durante o processo de edição. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaImageEditNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `30148261f43f5bfd14339f5ff1ec250381a615cc05c67eee21b0a2423ebe349d`
