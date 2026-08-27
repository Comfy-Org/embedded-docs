# Nano Banana 2

Este nó gera ou edita imagens enviando um prompt de texto para a API Vertex AI do Google por meio dos modelos de imagem Gemini. Ele cria novas imagens a partir de uma descrição ou modifica imagens existentes usando imagens de referência opcionais.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Seleciona o modelo de imagem Gemini a ser usado. O modelo escolhido determina as opções de resolução disponíveis e as entradas específicas do modelo. | DYNAMIC_COMBO | Sim | `"Nano Banana 2 (Gemini 3.1 Flash Image)"`<br>`"Nano Banana 2 Lite"` |
| `prompt` | Prompt de texto que descreve a imagem a ser gerada ou as edições a serem aplicadas. Inclua quaisquer restrições, estilos ou detalhes que o modelo deve seguir. Não pode estar vazio. (padrão: vazio) | STRING | Sim | N/A |
| `seed` | Quando a semente (seed) é fixada em um valor específico, o modelo faz o melhor esforço para fornecer a mesma resposta para solicitações repetidas. A saída determinística não é garantida. Além disso, alterar o modelo ou as configurações de parâmetros, como a temperatura, pode causar variações na resposta mesmo quando você usa o mesmo valor de semente. Por padrão, um valor de semente aleatório é usado. (padrão: 42) | INT | Sim | 0 a 18446744073709551615 |
| `response_modalities` | Determina o formato da resposta. IMAGE retorna apenas uma imagem; IMAGE+TEXT retorna uma imagem e uma resposta em texto. (padrão: IMAGE) Parâmetro avançado. | COMBO | Sim | `"IMAGE"`<br>`"IMAGE+TEXT"` |
| `system_prompt` | Instruções fundamentais que determinam o comportamento de uma IA. Por padrão, usa um prompt integrado que instrui o modelo a sempre produzir uma imagem. Parâmetro avançado. | STRING | Não | N/A |
| `temperatura` | Controla a aleatoriedade na geração. Valores mais baixos são mais focados/determinísticos. (padrão: 1.0) Parâmetro avançado. | FLOAT | Não | 0.0 a 2.0 (passo 0.01) |
| `top_p` | Limiar da amostragem de núcleo (nucleus sampling). Valores mais baixos são mais focados, valores mais altos são mais diversos. (padrão: 0.95) Parâmetro avançado. | FLOAT | Não | 0.0 a 1.0 (passo 0.01) |

### Entradas do Nano Banana 2 (Gemini 3.1 Flash Image)

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `aspect_ratio` | Se definido como 'auto', corresponde à proporção de aspecto da sua imagem de entrada; se nenhuma imagem for fornecida, geralmente é gerada uma imagem 16:9. (padrão: auto) | COMBO | Sim | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"`<br>`"1:4"`<br>`"4:1"`<br>`"8:1"`<br>`"1:8"` |
| `resolution` | Resolução de saída desejada. | COMBO | Sim | `"1K"`<br>`"2K"`<br>`"4K"` |
| `thinking_level` | Seleciona o nível de raciocínio usado pelo modelo. | COMBO | Sim | `"MINIMAL"`<br>`"HIGH"` |

### Entradas do Nano Banana 2 Lite

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `aspect_ratio` | Se definido como 'auto', corresponde à proporção de aspecto da sua imagem de entrada; se nenhuma imagem for fornecida, geralmente é gerada uma imagem 16:9. (padrão: auto) | COMBO | Sim | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"`<br>`"1:4"`<br>`"4:1"`<br>`"8:1"`<br>`"1:8"` |
| `resolution` | Resolução de saída desejada. | COMBO | Sim | `"1K"` |
| `thinking_level` | Seleciona o nível de raciocínio usado pelo modelo. | COMBO | Sim | `"MINIMAL"`<br>`"HIGH"` |

### Entradas de referência

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `images` | Imagem(ns) de referência opcional(is). Até 14 imagens no total. Slot expansível: conecte `image_1` a `image_14`. | IMAGE | Não | 0 a 14 imagens |
| `files` | Arquivo(s) opcional(is) para usar como contexto para o modelo. Aceita entradas do nó Gemini Generate Content Input Files. | GEMINI_INPUT_FILES | Não | N/A |

**Nota:** No máximo 14 imagens de referência podem ser conectadas à entrada `images`; exceder esse limite gera um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `IMAGE` | A imagem gerada ou editada. | IMAGE |
| `STRING` | Uma descrição em texto ou legenda gerada pelo modelo. Fica vazia quando nenhum texto é retornado, como quando `response_modalities` está definido como `IMAGE`. | STRING |
| `thought_image` | Primeira imagem do processo de raciocínio do modelo. Disponível apenas com `thinking_level` HIGH e modalidade IMAGE+TEXT. | IMAGE |

**Nota:** A saída `STRING` fica vazia quando `response_modalities` está definido como `IMAGE`. Se o modelo não gerar uma imagem nesse modo, o nó gera um erro sugerindo alternar para IMAGE+TEXT para visualizar o raciocínio do modelo.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2V2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `347d28aeb46aa91f7515a31c385a3e3f805a1861116a21dd2ef6575ab7fd4f3e`
