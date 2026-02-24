> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImage2Node/pt-BR.md)

O GeminiImage2Node gera ou edita imagens usando o modelo Gemini da Vertex AI do Google. Ele envia um prompt de texto e imagens ou arquivos de referência opcionais para a API e retorna a imagem gerada e/ou uma descrição textual.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Range | Descrição |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sim | N/A | Prompt de texto descrevendo a imagem a ser gerada ou as edições a serem aplicadas. Inclua quaisquer restrições, estilos ou detalhes que o modelo deve seguir. |
| `model` | COMBO | Sim | `"gemini-3-pro-image-preview"` | O modelo Gemini específico a ser usado para a geração. |
| `seed` | INT | Sim | 0 a 18446744073709551615 | Quando fixado em um valor específico, o modelo faz o melhor esforço para fornecer a mesma resposta para solicitações repetidas. A saída determinística não é garantida. Alterar o modelo ou outras configurações pode causar variações mesmo com a mesma `seed`. Padrão: 42. |
| `aspect_ratio` | COMBO | Sim | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"` | A proporção de aspecto desejada para a imagem de saída. Se definido como 'auto', corresponde à proporção de aspecto da sua imagem de entrada; se nenhuma imagem for fornecida, geralmente é gerado um quadrado 16:9. Padrão: "auto". |
| `resolution` | COMBO | Sim | `"1K"`<br>`"2K"`<br>`"4K"` | Resolução de saída alvo. Para 2K/4K, o upscaler nativo do Gemini é usado. |
| `response_modalities` | COMBO | Sim | `"IMAGE+TEXT"`<br>`"IMAGE"` | Escolha 'IMAGE' para saída apenas de imagem, ou 'IMAGE+TEXT' para retornar tanto a imagem gerada quanto uma resposta textual. |
| `images` | IMAGE | Não | N/A | Imagem(ns) de referência opcional(is). Para incluir múltiplas imagens, use o nó Batch Images (até 14). |
| `files` | CUSTOM | Não | N/A | Arquivo(s) opcional(is) para usar como contexto para o modelo. Aceita entradas do nó Gemini Generate Content Input Files. |
| `system_prompt` | STRING | Não | N/A | Instruções fundamentais que ditam o comportamento de uma IA. Padrão: Um prompt de sistema predefinido para geração de imagens. |

**Restrições:**

* A entrada `images` suporta um máximo de 14 imagens. Se mais forem fornecidas, um erro será gerado.
* A entrada `files` deve ser conectada a um nó que emita o tipo de dados `GEMINI_INPUT_FILES`.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `image` | IMAGE | A imagem gerada ou editada pelo modelo Gemini. |
| `string` | STRING | A resposta textual do modelo. Esta saída ficará vazia se `response_modalities` estiver definido como "IMAGE". |
