# Nano Banana Pro (Google Gemini Image)

Gere ou edite imagens de forma síncrona através da API Google Vertex AI Gemini. Você fornece um prompt de texto e pode, opcionalmente, anexar imagens de referência ou arquivos de entrada do Gemini. O nó retorna a imagem gerada e, dependendo do modo de resposta selecionado, uma resposta de texto.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto descrevendo a imagem a ser gerada ou as edições a serem aplicadas. Inclua quaisquer restrições, estilos ou detalhes que o modelo deve seguir. O prompt deve conter pelo menos um caractere após a remoção de espaços em branco. | STRING | Sim | N/A |
| `model` | O modelo Gemini a ser usado para geração. A opção "Nano Banana 2 (Gemini 3.1 Flash Image)" é enviada como `gemini-3.1-flash-image`; "gemini-3-pro-image-preview" é enviada como `gemini-3-pro-image`. | COMBO | Sim | "gemini-3-pro-image-preview"<br>"Nano Banana 2 (Gemini 3.1 Flash Image)" |
| `seed` | Quando a semente é fixada em um valor específico, o modelo faz o possível para fornecer a mesma resposta para solicitações repetidas. Saída determinística não é garantida. Além disso, alterar o modelo ou configurações de parâmetros, como a temperatura, pode causar variações na resposta mesmo quando você usa o mesmo valor de semente. Por padrão, um valor de semente aleatório é usado. Padrão: 42. | INT | Sim | 0 a 18446744073709551615 |
| `aspect_ratio` | Se definido como 'auto', corresponde à proporção da sua imagem de entrada; se nenhuma imagem for fornecida, uma proporção quadrada de 16:9 é geralmente gerada. Padrão: "auto". | COMBO | Sim | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"4:5"<br>"5:4"<br>"9:16"<br>"16:9"<br>"21:9" |
| `resolution` | Resolução de saída desejada. Para 2K/4K, o upscaler nativo do Gemini é usado. | COMBO | Sim | "1K"<br>"2K"<br>"4K" |
| `response_modalities` | Escolha 'IMAGE' para saída apenas de imagem, ou 'IMAGE+TEXT' para retornar tanto a imagem gerada quanto uma resposta de texto. Configuração avançada. | COMBO | Sim | "IMAGE+TEXT"<br>"IMAGE" |
| `images` | Imagem(ns) de referência opcional(is). Para incluir múltiplas imagens, use o nó Batch Images (até 14). | IMAGE | Não | N/A |
| `files` | Arquivo(s) opcional(is) para usar como contexto para o modelo. Aceita entradas do nó Gemini Generate Content Input Files. | GEMINI_INPUT_FILES | Não | N/A |
| `system_prompt` | Instruções fundamentais que determinam o comportamento de uma IA. Padrão: um prompt de sistema pré-definido para geração de imagem. Configuração avançada. | STRING | Não | N/A |

**Restrições:**

* A entrada `images` suporta no máximo 14 imagens. Se mais forem fornecidas, um erro é gerado.
* Quando mais de 10 imagens são fornecidas, as primeiras 10 são enviadas como referências de URL e as imagens restantes são enviadas inline na solicitação.
* A entrada `files` deve ser conectada a um nó que produza o tipo de dados `GEMINI_INPUT_FILES`.
* Quando `response_modalities` é definido como `"IMAGE"`, apenas a imagem é retornada e a saída de texto fica vazia.
* A entrada `prompt` é validada e deve conter pelo menos um caractere após a remoção de espaços em branco.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `image` | A imagem gerada ou editada pelo modelo Gemini. | IMAGE |
| `string` | A resposta de texto do modelo. Esta saída fica vazia se `response_modalities` for definido como `"IMAGE"`. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImage2Node/pt-BR.md)

---
**Source fingerprint (SHA-256):** `02293dad786d4b441da3174fa76f6c5847f122d294bd7e1f765ffd72420034a4`
