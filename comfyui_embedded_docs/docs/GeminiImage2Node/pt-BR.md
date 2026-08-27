# Nano Banana Pro (Google Gemini Image)

O nó GeminiImage2Node gera ou edita imagens usando o modelo Gemini do Google Vertex AI. Você fornece um prompt de texto e, opcionalmente, imagens ou arquivos de referência; o nó os envia para a API e retorna a imagem gerada, além de uma resposta de texto quando solicitado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto que descreve a imagem a ser gerada ou as edições a serem aplicadas. Inclua quaisquer restrições, estilos ou detalhes que o modelo deve seguir. O prompt deve conter pelo menos um caractere após a remoção de espaços em branco. | STRING | Sim | N/A |
| `model` | O modelo Gemini específico a ser usado para geração. A opção "Nano Banana 2 (Gemini 3.1 Flash Image)" mapeia internamente para o modelo `gemini-3.1-flash-image`, e "gemini-3-pro-image-preview" mapeia para `gemini-3-pro-image`. | COMBO | Sim | `"gemini-3-pro-image-preview"`<br>`"Nano Banana 2 (Gemini 3.1 Flash Image)"` |
| `seed` | Quando a `seed` é fixada em um valor específico, o modelo faz o melhor esforço para fornecer a mesma resposta para solicitações repetidas. A saída determinística não é garantida. Além disso, alterar o modelo ou as configurações de parâmetros, como a temperatura, pode causar variações na resposta mesmo usando o mesmo valor de `seed`. Por padrão, um valor aleatório de `seed` é usado. Padrão: 42. | INT | Sim | 0 a 18446744073709551615 |
| `aspect_ratio` | Se definido como 'auto', corresponde à proporção de aspecto da sua imagem de entrada; se nenhuma imagem for fornecida, uma imagem 16:9 geralmente é gerada. Padrão: "auto". | COMBO | Sim | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"` |
| `resolution` | Resolução de saída desejada. Para 2K/4K, o upscaler nativo do Gemini é utilizado. | COMBO | Sim | `"1K"`<br>`"2K"`<br>`"4K"` |
| `response_modalities` | Escolha 'IMAGE' para saída somente com imagem, ou 'IMAGE+TEXT' para retornar tanto a imagem gerada quanto uma resposta de texto. | COMBO | Sim | `"IMAGE+TEXT"`<br>`"IMAGE"` |
| `images` | Imagem(ns) de referência opcional(is). Para incluir várias imagens, use o nó Batch Images (até 14). | IMAGE | Não | N/A |
| `files` | Arquivo(s) opcional(is) para usar como contexto para o modelo. Aceita entradas do nó Gemini Generate Content Input Files. | GEMINI_INPUT_FILES | Não | N/A |
| `system_prompt` | Instruções fundamentais que definem o comportamento de uma IA. Padrão: um prompt de sistema predefinido para geração de imagens. | STRING | Não | N/A |

**Restrições:**

* A entrada `images` suporta no máximo 14 imagens. Se mais forem fornecidas, um erro é gerado.
* Quando mais de 10 imagens são fornecidas, as primeiras 10 são enviadas como referências de URL e as demais são enviadas inline na requisição.
* A entrada `files` deve ser conectada a um nó que produza o tipo de dados `GEMINI_INPUT_FILES`.
* Quando `response_modalities` está definido como "IMAGE", apenas a imagem é retornada e a saída de texto fica vazia.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `image` | A imagem gerada ou editada pelo modelo Gemini. | IMAGE |
| `string` | A resposta de texto do modelo. Esta saída ficará vazia se `response_modalities` estiver definido como "IMAGE". | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImage2Node/pt-BR.md)

---
**Source fingerprint (SHA-256):** `02293dad786d4b441da3174fa76f6c5847f122d294bd7e1f765ffd72420034a4`
