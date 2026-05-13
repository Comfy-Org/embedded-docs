> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2/pt-BR.md)

O nó GeminiNanoBanana2 gera ou edita imagens usando o modelo Gemini do Google Vertex AI. Ele funciona enviando um prompt de texto, juntamente com imagens de referência ou arquivos opcionais, para a API e retorna a imagem gerada e qualquer texto de acompanhamento.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `prompt` | STRING | Sim | N/A | Prompt de texto descrevendo a imagem a ser gerada ou as edições a serem aplicadas. Inclua quaisquer restrições, estilos ou detalhes que o modelo deve seguir. |
| `model` | COMBO | Sim | `"Nano Banana 2 (Gemini 3.1 Flash Image)"` | O modelo Gemini específico a ser usado para geração de imagens. |
| `seed` | INT | Sim | 0 a 18446744073709551615 | Quando a semente é fixada em um valor específico, o modelo faz o melhor esforço para fornecer a mesma resposta para requisições repetidas. A saída determinística não é garantida. Além disso, alterar o modelo ou as configurações de parâmetros, como a temperatura, pode causar variações na resposta mesmo quando você usa o mesmo valor de semente. Por padrão, um valor de semente aleatório é usado. (padrão: 42) |
| `aspect_ratio` | COMBO | Sim | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"` | Se definido como 'auto', corresponde à proporção da sua imagem de entrada; se nenhuma imagem for fornecida, geralmente é gerado um quadrado 16:9. (padrão: "auto") |
| `resolution` | COMBO | Sim | `"1K"`<br>`"2K"`<br>`"4K"` | Resolução de saída alvo. Para 2K/4K, o upscaler nativo do Gemini é usado. |
| `response_modalities` | COMBO | Sim | `"IMAGE"`<br>`"IMAGE+TEXT"` | Determina o tipo de conteúdo que o modelo retornará. (avançado) |
| `thinking_level` | COMBO | Sim | `"MINIMAL"`<br>`"HIGH"` | Controla a profundidade do processo de raciocínio do modelo. |
| `images` | IMAGE | Não | N/A | Imagem(ns) de referência opcional(is). Para incluir múltiplas imagens, use o nó Batch Images (até 14). |
| `files` | CUSTOM | Não | N/A | Arquivo(s) opcional(is) para usar como contexto para o modelo. Aceita entradas do nó Gemini Generate Content Input Files. |
| `system_prompt` | STRING | Não | N/A | Instruções fundamentais que ditam o comportamento de uma IA. (avançado) |

**Nota:** A entrada `images` suporta um máximo de 14 imagens. Se mais forem fornecidas, o nó gerará um erro.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `image` | IMAGE | A imagem principal gerada ou editada pelo modelo. |
| `string` | STRING | Qualquer conteúdo de texto retornado pelo modelo. |
| `thought_image` | IMAGE | Primeira imagem do processo de raciocínio do modelo. Disponível apenas com `thinking_level` HIGH e modalidade IMAGE+TEXT. |

---
**Source fingerprint (SHA-256):** `bd53363da73ff0db66a872fc04f1af8ce4dfee1191ca01bd813701b5ad5e4f17`
