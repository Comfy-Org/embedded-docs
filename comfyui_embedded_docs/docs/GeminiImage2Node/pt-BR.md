# Nano Banana Pro (Google Gemini Image)

O Nano Banana Pro (Google Gemini Image) gera ou edita imagens usando os modelos de imagem Gemini do Vertex AI do Google. Ele envia um prompt de texto juntamente com imagens ou arquivos de referência opcionais para a API Gemini e retorna a imagem gerada juntamente com uma resposta de texto opcional.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto que descreve a imagem a gerar ou as edições a aplicar. Inclua quaisquer restrições, estilos ou detalhes que o modelo deve seguir. Padrão: string vazia. | STRING | Sim | N/A |
| `model` | O modelo de imagem Gemini a ser usado. A opção "Nano Banana 2 (Gemini 3.1 Flash Image)" é enviada para a API como `gemini-3.1-flash-image`; "gemini-3-pro-image-preview" é enviado como `gemini-3-pro-image`. | COMBO | Sim | `"gemini-3-pro-image-preview"`<br>`"Nano Banana 2 (Gemini 3.1 Flash Image)"` |
| `seed` | Quando a seed é fixada em um valor específico, o modelo faz o melhor possível para fornecer a mesma resposta para solicitações repetidas. A saída determinística não é garantida. Alterar o modelo ou outras configurações de parâmetros pode causar variações na resposta mesmo com o mesmo valor de seed. Padrão: 42. | INT | Sim | 0 a 18446744073709551615 |
| `aspect_ratio` | A proporção de aspecto desejada da imagem de saída. Quando definida como "auto", ela corresponde à proporção de aspecto da imagem de entrada; se nenhuma imagem for fornecida, normalmente é gerada uma imagem no formato 16:9. Padrão: "auto". | COMBO | Sim | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"` |
| `resolution` | Resolução de saída desejada. Para 2K/4K, o upscaler nativo do Gemini é utilizado. | COMBO | Sim | `"1K"`<br>`"2K"`<br>`"4K"` |
| `response_modalities` | Escolha "IMAGE" para saída somente com imagem, ou "IMAGE+TEXT" para retornar tanto a imagem gerada quanto uma resposta de texto. | COMBO | Sim | `"IMAGE+TEXT"`<br>`"IMAGE"` |
| `images` | Imagem(ns) de referência opcional(is) usada(s) como contexto visual. Para incluir várias imagens, use o nó Batch Images (até 14). | IMAGE | Não | N/A |
| `files` | Arquivo(s) opcional(is) para usar como contexto para o modelo. Aceita entradas do nó Gemini Generate Content Input Files. | GEMINI_INPUT_FILES | Não | N/A |
| `system_prompt` | Instruções fundamentais que determinam o comportamento do modelo. Padrão: um prompt de sistema predefinido que instrui o modelo a sempre gerar uma imagem. | STRING | Não | N/A |

**Restrições:**

* O `prompt` não pode estar vazio após a remoção de espaços em branco no início e no final; caso contrário, um erro é gerado.
* A entrada `images` aceita no máximo 14 imagens. Se mais de 14 forem fornecidas, um erro é gerado.
* A entrada `files` deve estar conectada a um nó que produza o tipo de dados `GEMINI_INPUT_FILES`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `image` | A imagem gerada ou editada pelo modelo Gemini. | IMAGE |
| `string` | A resposta de texto do modelo. Esta saída fica vazia quando `response_modalities` está definido como "IMAGE". | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImage2Node/pt-BR.md)

---
**Source fingerprint (SHA-256):** `02293dad786d4b441da3174fa76f6c5847f122d294bd7e1f765ffd72420034a4`
