# Nano Banana 2

O nó Nano Banana 2 gera ou edita imagens de forma síncrona pela API Google Vertex usando o modelo Gemini 3.1 Flash Image. Ele envia um prompt de texto, junto com imagens ou arquivos de referência opcionais, e retorna a imagem gerada, qualquer texto que a acompanhe e, opcionalmente, uma imagem do processo de raciocínio do modelo. Este nó está marcado como obsoleto.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-----------|---------------|-------------|-----------|
| `prompt` | Prompt de texto que descreve a imagem a ser gerada ou as edições a serem aplicadas. Inclua quaisquer restrições, estilos ou detalhes que o modelo deve seguir. Não pode estar vazio nem conter apenas espaços em branco. (padrão: vazio) | STRING | Sim | N/A |
| `model` | O modelo Gemini a ser usado para geração de imagem. | COMBO | Sim | "Nano Banana 2 (Gemini 3.1 Flash Image)" |
| `seed` | Quando a seed é fixada em um valor específico, o modelo faz o possível para fornecer a mesma resposta em solicitações repetidas. A saída determinística não é garantida. Além disso, alterar o modelo ou as configurações de parâmetros, como a temperatura, pode causar variações na resposta mesmo quando você usa o mesmo valor de seed. Por padrão, um valor de seed aleatório é usado. (padrão: 42) | INT | Sim | 0 a 18446744073709551615 |
| `aspect_ratio` | Se definido como 'auto', corresponde à proporção da sua imagem de entrada; se nenhuma imagem for fornecida, uma imagem 16:9 é geralmente gerada. (padrão: "auto") | COMBO | Sim | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"4:5"<br>"5:4"<br>"9:16"<br>"16:9"<br>"21:9" |
| `resolution` | Resolução de saída desejada. Para 2K/4K, o upscaler nativo do Gemini é usado. | COMBO | Sim | "1K"<br>"2K"<br>"4K" |
| `response_modalities` | Determina o tipo de conteúdo que o modelo retorna: "IMAGE" retorna apenas uma imagem; "IMAGE+TEXT" também retorna texto. (avançado) | COMBO | Sim | "IMAGE"<br>"IMAGE+TEXT" |
| `thinking_level` | Controla a profundidade do processo de raciocínio do modelo. | COMBO | Sim | "MINIMAL"<br>"HIGH" |
| `images` | Imagem(ns) de referência opcional(is). Para incluir várias imagens, use o nó Batch Images (até 14). | IMAGE | Não | 1 a 14 imagens |
| `files` | Arquivo(s) opcional(is) a ser(em) usado(s) como contexto para o modelo. Aceita entradas do nó Gemini Generate Content Input Files. | CUSTOM | Não | N/A |
| `system_prompt` | Instruções fundamentais que ditam o comportamento de uma IA. (padrão: um prompt predefinido que instrui o modelo a sempre produzir uma imagem) (avançado) | STRING | Não | N/A |

**Nota:** A entrada `images` suporta no máximo 14 imagens. Se mais forem fornecidas, o nó gera um erro. A entrada `prompt` não pode estar vazia nem conter apenas espaços em branco.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|---------------|-----------|---------------|
| `image` | A imagem principal gerada ou editada pelo modelo. | IMAGE |
| `string` | Qualquer conteúdo de texto retornado pelo modelo. | STRING |
| `thought_image` | Primeira imagem do processo de raciocínio do modelo. Disponível apenas quando `thinking_level` está definido como HIGH e a modalidade é IMAGE+TEXT. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d781c92f04d420985f8a5a593eb5f28f1f7b2af13abd11f2a7f6f285edcd9900`
