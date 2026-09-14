# Google Gemini

Gere respostas de texto com os modelos Gemini do Google. Forneça um prompt de texto e, opcionalmente, uma ou mais imagens, clipes de áudio, vídeos ou arquivos como contexto multimodal. O nó envia o prompt e qualquer mídia anexada ao modelo selecionado e retorna a resposta de texto do modelo.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `modelo` | O modelo Gemini usado para gerar a resposta. Selecionar um modelo revela seu próprio conjunto de entradas abaixo. | DYNAMIC_COMBO | Sim | `"Gemini 3.8 Flash"`<br>`"Gemini 3.7 Flash"`<br>`"Gemini 3.5 Flash"`<br>`"Gemini 3.1 Pro"`<br>`"Gemini 3.1 Flash-Lite"` |
| `prompt` | Entrada de texto para o modelo. Inclua instruções detalhadas, perguntas ou contexto. (padrão: "") | STRING | Sim | Deve conter pelo menos um caractere que não seja espaço em branco |
| `semente` | Semente para amostragem. Defina como 0 para uma semente aleatória. Saída determinística não é garantida. (padrão: 42) | INT | Sim | 0 a 2147483647 |
| `prompt_do_sistema` | Instruções fundamentais que determinam o comportamento do modelo. (padrão: "") | STRING | Não |  |

### Entradas do Gemini 3.8 Flash

Estas entradas aparecem quando `model` é definido como `"Gemini 3.8 Flash"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `thinking_level` | Quão intensamente o modelo raciocina internamente antes de responder. HIGH melhora a qualidade em tarefas difíceis, mas consome mais tokens (de raciocínio) e é mais lento. (padrão: "MEDIUM") | COMBO | Sim | `"LOW"`<br>`"MEDIUM"`<br>`"HIGH"` |
| `max_output_tokens` | Número máximo de tokens a gerar, incluindo o raciocínio interno do modelo. Com thinking_level HIGH, um valor baixo pode não deixar espaço para a resposta; aumente isso se as respostas vierem vazias ou truncadas. O modelo para cedo quando termina, então um limite maior não custa nada extra para respostas curtas. (padrão: 32768) | INT | Sim | 16 a 65536 |

**Observação:** Este modelo não expõe os controles de amostragem `temperature` ou `top_p`.

### Entradas do Gemini 3.7 Flash

Estas entradas aparecem quando `model` é definido como `"Gemini 3.7 Flash"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `thinking_level` | Quão intensamente o modelo raciocina internamente antes de responder. HIGH melhora a qualidade em tarefas difíceis, mas consome mais tokens (de raciocínio) e é mais lento. (padrão: "MEDIUM") | COMBO | Sim | `"LOW"`<br>`"MEDIUM"`<br>`"HIGH"` |
| `temperature` | Controla a aleatoriedade. Valores mais baixos são mais focados/determinísticos; valores mais altos são mais criativos. (padrão: 1.0) | FLOAT | Sim | 0.0 a 2.0 |
| `top_p` | Amostragem de núcleo: amostra do menor conjunto de tokens cuja probabilidade acumulada atinge top_p. (padrão: 0.95) | FLOAT | Sim | 0.0 a 1.0 |
| `max_output_tokens` | Número máximo de tokens a gerar, incluindo o raciocínio interno do modelo. Com thinking_level HIGH, um valor baixo pode não deixar espaço para a resposta; aumente isso se as respostas vierem vazias ou truncadas. O modelo para cedo quando termina, então um limite maior não custa nada extra para respostas curtas. (padrão: 32768) | INT | Sim | 16 a 65536 |

### Entradas do Gemini 3.5 Flash

Estas entradas aparecem quando `model` é definido como `"Gemini 3.5 Flash"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `thinking_level` | Quão intensamente o modelo raciocina internamente antes de responder. HIGH melhora a qualidade em tarefas difíceis, mas consome mais tokens (de raciocínio) e é mais lento. (padrão: "MEDIUM") | COMBO | Sim | `"MINIMAL"`<br>`"LOW"`<br>`"MEDIUM"`<br>`"HIGH"` |
| `temperature` | Controla a aleatoriedade. Valores mais baixos são mais focados/determinísticos; valores mais altos são mais criativos. (padrão: 1.0) | FLOAT | Sim | 0.0 a 2.0 |
| `top_p` | Amostragem de núcleo: amostra do menor conjunto de tokens cuja probabilidade acumulada atinge top_p. (padrão: 0.95) | FLOAT | Sim | 0.0 a 1.0 |
| `max_output_tokens` | Número máximo de tokens a gerar, incluindo o raciocínio interno do modelo. Com thinking_level HIGH, um valor baixo pode não deixar espaço para a resposta; aumente isso se as respostas vierem vazias ou truncadas. O modelo para cedo quando termina, então um limite maior não custa nada extra para respostas curtas. (padrão: 32768) | INT | Sim | 16 a 65536 |

### Entradas do Gemini 3.1 Pro

Estas entradas aparecem quando `model` é definido como `"Gemini 3.1 Pro"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `thinking_level` | Quão intensamente o modelo raciocina internamente antes de responder. HIGH melhora a qualidade em tarefas difíceis, mas consome mais tokens (de raciocínio) e é mais lento. (padrão: "HIGH") | COMBO | Sim | `"LOW"`<br>`"HIGH"` |
| `temperature` | Controla a aleatoriedade. Valores mais baixos são mais focados/determinísticos; valores mais altos são mais criativos. (padrão: 1.0) | FLOAT | Sim | 0.0 a 2.0 |
| `top_p` | Amostragem de núcleo: amostra do menor conjunto de tokens cuja probabilidade acumulada atinge top_p. (padrão: 0.95) | FLOAT | Sim | 0.0 a 1.0 |
| `max_output_tokens` | Número máximo de tokens a gerar, incluindo o raciocínio interno do modelo. Com thinking_level HIGH, um valor baixo pode não deixar espaço para a resposta; aumente isso se as respostas vierem vazias ou truncadas. O modelo para cedo quando termina, então um limite maior não custa nada extra para respostas curtas. (padrão: 32768) | INT | Sim | 16 a 65536 |

### Entradas do Gemini 3.1 Flash-Lite

Estas entradas aparecem quando `model` é definido como `"Gemini 3.1 Flash-Lite"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `thinking_level` | Quão intensamente o modelo raciocina internamente antes de responder. HIGH melhora a qualidade em tarefas difíceis, mas consome mais tokens (de raciocínio) e é mais lento. (padrão: "LOW") | COMBO | Sim | `"LOW"`<br>`"HIGH"` |
| `temperature` | Controla a aleatoriedade. Valores mais baixos são mais focados/determinísticos; valores mais altos são mais criativos. (padrão: 1.0) | FLOAT | Sim | 0.0 a 2.0 |
| `top_p` | Amostragem de núcleo: amostra do menor conjunto de tokens cuja probabilidade acumulada atinge top_p. (padrão: 0.95) | FLOAT | Sim | 0.0 a 1.0 |
| `max_output_tokens` | Número máximo de tokens a gerar, incluindo o raciocínio interno do modelo. Com thinking_level HIGH, um valor baixo pode não deixar espaço para a resposta; aumente isso se as respostas vierem vazias ou truncadas. O modelo para cedo quando termina, então um limite maior não custa nada extra para respostas curtas. (padrão: 32768) | INT | Sim | 16 a 65536 |

### Entradas de mídia e arquivos

As entradas a seguir são compartilhadas por todos os modelos e aparecem junto com as entradas específicas de cada modelo.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `images` | Slot expansível: conecte de 1 a 16 imagens (`image_1` ... `image_16`). Imagem(ns) opcional(is) para usar como contexto para o modelo. Até 16 imagens. | IMAGE | Não | 0 a 16 imagens |
| `audio` | Slot expansível: conecte um clipe de áudio (`audio_1`). Clipe de áudio opcional para usar como contexto para o modelo. | AUDIO | Não | 0 a 1 clipe |
| `video` | Slot expansível: conecte um clipe de vídeo (`video_1`). Clipe de vídeo opcional para usar como contexto para o modelo. | VIDEO | Não | 0 a 1 clipe |
| `files` | Arquivo(s) opcional(is) para usar como contexto para o modelo. Aceita entradas do nó Gemini Input Files. | GEMINI_INPUT_FILES | Não |  |

**Observação:** Quando mídia (imagens, áudio ou vídeo) é anexada, o nó envia os primeiros 10 itens de mídia para o armazenamento do ComfyAPI e os passa como URLs; esse orçamento de URLs é compartilhado entre todos os tipos de mídia e é consumido em ordem (vídeo primeiro, depois áudio, depois imagens). Qualquer mídia restante é codificada inline como dados base64, com um payload inline combinado máximo de 18 MB. Se o payload inline exceder 18 MB, o nó gera um erro. O parâmetro `prompt` deve conter pelo menos um caractere que não seja espaço em branco. Definir `seed` como 0 solicita uma semente aleatória.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | A resposta de texto gerada pelo modelo Gemini. Se o modelo não produzir texto, a string "Empty response from Gemini model..." é retornada. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNodeV2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8ae14c6465569695e1e99b0040cb2c745e5f3d9ddcd3b03013530dc7e7135b87`
