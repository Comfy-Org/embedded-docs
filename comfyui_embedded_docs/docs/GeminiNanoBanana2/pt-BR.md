# Nano Banana 2

Este nó gera ou edita imagens de forma síncrona usando o modelo Gemini da Vertex AI do Google (Nano Banana 2 / Gemini 3.1 Flash Image). Ele envia um prompt de texto, juntamente com imagens de referência ou arquivos opcionais, para a API e retorna a imagem gerada, qualquer texto associado e, opcionalmente, uma imagem do processo de raciocínio do modelo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto que descreve a imagem a ser gerada ou as edições a serem aplicadas. Inclua quaisquer restrições, estilos ou detalhes que o modelo deve seguir. Deve conter pelo menos um caractere que não seja espaço em branco. | STRING | Sim | N/A |
| `model` | O modelo Gemini específico a ser usado para geração de imagens. A única opção disponível corresponde ao modelo `gemini-3.1-flash-image-preview`. | COMBO | Sim | `"Nano Banana 2 (Gemini 3.1 Flash Image)"` |
| `seed` | Quando a semente é fixada em um valor específico, o modelo faz o melhor esforço para fornecer a mesma resposta para solicitações repetidas. A saída determinística não é garantida. Além disso, alterar o modelo ou as configurações de parâmetros, como a temperatura, pode causar variações na resposta mesmo quando o mesmo valor de semente é usado. Por padrão, um valor de semente aleatório é usado. (padrão: 42) | INT | Sim | 0 a 18446744073709551615 |
| `aspect_ratio` | Se definido como 'auto', corresponde à proporção da sua imagem de entrada; se nenhuma imagem for fornecida, uma imagem 16:9 geralmente é gerada. (padrão: "auto") | COMBO | Sim | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"` |
| `resolution` | Resolução de saída desejada. Para 2K/4K, o upscaler nativo do Gemini é usado. | COMBO | Sim | `"1K"`<br>`"2K"`<br>`"4K"` |
| `response_modalities` | Determina o tipo de conteúdo que o modelo retorna: `IMAGE` retorna apenas a imagem; `IMAGE+TEXT` também retorna o texto de raciocínio do modelo. (avançado) | COMBO | Sim | `"IMAGE"`<br>`"IMAGE+TEXT"` |
| `thinking_level` | Controla a profundidade do processo de raciocínio do modelo. | COMBO | Sim | `"MINIMAL"`<br>`"HIGH"` |
| `images` | Imagem(ns) de referência opcional(is). Para incluir várias imagens, use o nó Batch Images (até 14). | IMAGE | Não | Até 14 imagens |
| `files` | Arquivo(s) opcional(is) para usar como contexto para o modelo. Aceita entradas do nó Gemini Generate Content Input Files. | GEMINI_INPUT_FILES | Não | N/A |
| `system_prompt` | Instruções fundamentais que determinam o comportamento de uma IA. (padrão: instruções integradas que exigem que o modelo sempre produza uma imagem) (avançado) | STRING | Não | N/A |

**Observação:** A entrada `images` aceita no máximo 14 imagens; fornecer mais gera erro. Quando mais de 10 imagens de referência são fornecidas, as 10 primeiras são enviadas como URLs de arquivo e as demais são enviadas como dados inline. O `prompt` não deve ficar vazio após a remoção de espaços em branco. Este nó está marcado como obsoleto.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `image` | A imagem principal gerada ou editada pelo modelo. | IMAGE |
| `string` | Qualquer conteúdo de texto retornado pelo modelo. | STRING |
| `thought_image` | Primeira imagem do processo de raciocínio do modelo. Disponível apenas com `thinking_level` HIGH e modalidade IMAGE+TEXT. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d781c92f04d420985f8a5a593eb5f28f1f7b2af13abd11f2a7f6f285edcd9900`
