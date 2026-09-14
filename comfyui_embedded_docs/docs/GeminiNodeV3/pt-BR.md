# GeminiNodeV3

Gere respostas de texto com os modelos Gemini do Google. Forneça um prompt de texto e, opcionalmente, uma ou mais imagens, clipes de áudio, vídeos ou arquivos como contexto multimodal. O modelo selecionado determina quais configurações adicionais aparecem.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo Gemini usado para gerar a resposta. O modelo selecionado determina quais entradas adicionais são exibidas. | DYNAMIC_COMBO | Sim | `"Gemini 3.8 Flash"`<br>`"Gemini 3.7 Flash"`<br>`"Gemini 3.5 Flash"`<br>`"Gemini 3.1 Pro"`<br>`"Gemini 3.1 Flash-Lite"` |

### Entradas de mídia

Essas entradas de mídia expansíveis estão disponíveis para todas as opções de modelo.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `images` | Imagens opcionais a serem usadas como contexto para o modelo. Até 16 imagens. Slot expansível: conecte imagens a `image_1` até `image_16`. | IMAGE | Não | Até 16 imagens |
| `audio` | Clipe de áudio opcional a ser usado como contexto para o modelo. Slot expansível: `audio_1`. | AUDIO | Não | 1 clipe de áudio |
| `video` | Clipe de vídeo opcional a ser usado como contexto para o modelo. Slot expansível: `video_1`. | VIDEO | Não | 1 clipe de vídeo |

### Entradas do Gemini 3.8 Flash

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Entrada de texto para o modelo. Inclua instruções detalhadas, perguntas ou contexto. Não pode ficar vazia. | STRING | Sim | Texto multilinha (deve conter pelo menos um caractere que não seja espaço em branco) |
| `video_processing` | Como o modelo lê o vídeo anexado. `static` amostra quadros a uma taxa fixa e envia todos eles como contexto; `agentic` permite que o modelo navegue pela linha do tempo por conta própria e carregue apenas os quadros, áudio ou transcrição de que precisa, o que custa muito menos tokens de entrada em vídeos longos. | COMBO | Sim | `"static"`<br>`"agentic"` (padrão: `"static"`) |
| `files` | Arquivos opcionais a serem usados como contexto para o modelo. Aceita entradas do nó Gemini Input Files. | GEMINI_INPUT_FILES | Não | N/A |
| `thinking_level` | O quanto o modelo raciocina internamente antes de responder. HIGH melhora a qualidade em tarefas difíceis, mas consome mais tokens (de raciocínio) e é mais lento. | COMBO | Sim | `"LOW"`<br>`"MEDIUM"`<br>`"HIGH"` (padrão: `"MEDIUM"`) |
| `max_output_tokens` | Número máximo de tokens a gerar, incluindo o raciocínio interno do modelo. Com thinking_level HIGH, um valor baixo pode não deixar espaço para a resposta; aumente-o se as respostas vierem vazias ou truncadas. O modelo para antecipadamente quando termina, então um limite maior não custa nada extra para respostas curtas. | INT | Sim | 16-65536 (padrão: 32768) |
| `seed` | Semente para amostragem. Defina como 0 para uma semente aleatória. A saída determinística não é garantida. | INT | Sim | 0-2147483647 (padrão: 42) |
| `system_prompt` | Instruções fundamentais que determinam o comportamento do modelo. | STRING | Sim | Texto multilinha (padrão: vazio) |

### Entradas do Gemini 3.7 Flash

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Entrada de texto para o modelo. Inclua instruções detalhadas, perguntas ou contexto. Não pode ficar vazia. | STRING | Sim | Texto multilinha (deve conter pelo menos um caractere que não seja espaço em branco) |
| `files` | Arquivos opcionais a serem usados como contexto para o modelo. Aceita entradas do nó Gemini Input Files. | GEMINI_INPUT_FILES | Não | N/A |
| `thinking_level` | O quanto o modelo raciocina internamente antes de responder. HIGH melhora a qualidade em tarefas difíceis, mas consome mais tokens (de raciocínio) e é mais lento. | COMBO | Sim | `"LOW"`<br>`"MEDIUM"`<br>`"HIGH"` (padrão: `"MEDIUM"`) |
| `temperature` | Controla a aleatoriedade. Valores menores são mais focados/determinísticos; valores maiores são mais criativos. | FLOAT | Sim | 0.0-2.0 (padrão: 1.0) |
| `top_p` | Amostragem por núcleo: amostra do menor conjunto de tokens cuja probabilidade acumulada atinge top_p. | FLOAT | Sim | 0.0-1.0 (padrão: 0.95) |
| `max_output_tokens` | Número máximo de tokens a gerar, incluindo o raciocínio interno do modelo. Com thinking_level HIGH, um valor baixo pode não deixar espaço para a resposta; aumente-o se as respostas vierem vazias ou truncadas. O modelo para antecipadamente quando termina, então um limite maior não custa nada extra para respostas curtas. | INT | Sim | 16-65536 (padrão: 32768) |
| `seed` | Semente para amostragem. Defina como 0 para uma semente aleatória. A saída determinística não é garantida. | INT | Sim | 0-2147483647 (padrão: 42) |
| `system_prompt` | Instruções fundamentais que determinam o comportamento do modelo. | STRING | Sim | Texto multilinha (padrão: vazio) |

### Entradas do Gemini 3.5 Flash

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Entrada de texto para o modelo. Inclua instruções detalhadas, perguntas ou contexto. Não pode ficar vazia. | STRING | Sim | Texto multilinha (deve conter pelo menos um caractere que não seja espaço em branco) |
| `files` | Arquivos opcionais a serem usados como contexto para o modelo. Aceita entradas do nó Gemini Input Files. | GEMINI_INPUT_FILES | Não | N/A |
| `thinking_level` | O quanto o modelo raciocina internamente antes de responder. HIGH melhora a qualidade em tarefas difíceis, mas consome mais tokens (de raciocínio) e é mais lento. | COMBO | Sim | `"MINIMAL"`<br>`"LOW"`<br>`"MEDIUM"`<br>`"HIGH"` (padrão: `"MEDIUM"`) |
| `temperature` | Controla a aleatoriedade. Valores menores são mais focados/determinísticos; valores maiores são mais criativos. | FLOAT | Sim | 0.0-2.0 (padrão: 1.0) |
| `top_p` | Amostragem por núcleo: amostra do menor conjunto de tokens cuja probabilidade acumulada atinge top_p. | FLOAT | Sim | 0.0-1.0 (padrão: 0.95) |
| `max_output_tokens` | Número máximo de tokens a gerar, incluindo o raciocínio interno do modelo. Com thinking_level HIGH, um valor baixo pode não deixar espaço para a resposta; aumente-o se as respostas vierem vazias ou truncadas. O modelo para antecipadamente quando termina, então um limite maior não custa nada extra para respostas curtas. | INT | Sim | 16-65536 (padrão: 32768) |
| `seed` | Semente para amostragem. Defina como 0 para uma semente aleatória. A saída determinística não é garantida. | INT | Sim | 0-2147483647 (padrão: 42) |
| `system_prompt` | Instruções fundamentais que determinam o comportamento do modelo. | STRING | Sim | Texto multilinha (padrão: vazio) |

### Entradas do Gemini 3.1 Pro

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Entrada de texto para o modelo. Inclua instruções detalhadas, perguntas ou contexto. Não pode ficar vazia. | STRING | Sim | Texto multilinha (deve conter pelo menos um caractere que não seja espaço em branco) |
| `files` | Arquivos opcionais a serem usados como contexto para o modelo. Aceita entradas do nó Gemini Input Files. | GEMINI_INPUT_FILES | Não | N/A |
| `thinking_level` | O quanto o modelo raciocina internamente antes de responder. HIGH melhora a qualidade em tarefas difíceis, mas consome mais tokens (de raciocínio) e é mais lento. | COMBO | Sim | `"LOW"`<br>`"HIGH"` (padrão: `"HIGH"`) |
| `temperature` | Controla a aleatoriedade. Valores menores são mais focados/determinísticos; valores maiores são mais criativos. | FLOAT | Sim | 0.0-2.0 (padrão: 1.0) |
| `top_p` | Amostragem por núcleo: amostra do menor conjunto de tokens cuja probabilidade acumulada atinge top_p. | FLOAT | Sim | 0.0-1.0 (padrão: 0.95) |
| `max_output_tokens` | Número máximo de tokens a gerar, incluindo o raciocínio interno do modelo. Com thinking_level HIGH, um valor baixo pode não deixar espaço para a resposta; aumente-o se as respostas vierem vazias ou truncadas. O modelo para antecipadamente quando termina, então um limite maior não custa nada extra para respostas curtas. | INT | Sim | 16-65536 (padrão: 32768) |
| `seed` | Semente para amostragem. Defina como 0 para uma semente aleatória. A saída determinística não é garantida. | INT | Sim | 0-2147483647 (padrão: 42) |
| `system_prompt` | Instruções fundamentais que determinam o comportamento do modelo. | STRING | Sim | Texto multilinha (padrão: vazio) |

### Entradas do Gemini 3.1 Flash-Lite

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Entrada de texto para o modelo. Inclua instruções detalhadas, perguntas ou contexto. Não pode ficar vazia. | STRING | Sim | Texto multilinha (deve conter pelo menos um caractere que não seja espaço em branco) |
| `files` | Arquivos opcionais a serem usados como contexto para o modelo. Aceita entradas do nó Gemini Input Files. | GEMINI_INPUT_FILES | Não | N/A |
| `thinking_level` | O quanto o modelo raciocina internamente antes de responder. HIGH melhora a qualidade em tarefas difíceis, mas consome mais tokens (de raciocínio) e é mais lento. | COMBO | Sim | `"LOW"`<br>`"HIGH"` (padrão: `"LOW"`) |
| `temperature` | Controla a aleatoriedade. Valores menores são mais focados/determinísticos; valores maiores são mais criativos. | FLOAT | Sim | 0.0-2.0 (padrão: 1.0) |
| `top_p` | Amostragem por núcleo: amostra do menor conjunto de tokens cuja probabilidade acumulada atinge top_p. | FLOAT | Sim | 0.0-1.0 (padrão: 0.95) |
| `max_output_tokens` | Número máximo de tokens a gerar, incluindo o raciocínio interno do modelo. Com thinking_level HIGH, um valor baixo pode não deixar espaço para a resposta; aumente-o se as respostas vierem vazias ou truncadas. O modelo para antecipadamente quando termina, então um limite maior não custa nada extra para respostas curtas. | INT | Sim | 16-65536 (padrão: 32768) |
| `seed` | Semente para amostragem. Defina como 0 para uma semente aleatória. A saída determinística não é garantida. | INT | Sim | 0-2147483647 (padrão: 42) |
| `system_prompt` | Instruções fundamentais que determinam o comportamento do modelo. | STRING | Sim | Texto multilinha (padrão: vazio) |

Observação: para o Gemini 3.8 Flash, `temperature` e `top_p` não estão disponíveis, e `video_processing` está disponível apenas para esta opção de modelo. As opções e o padrão de `thinking_level` variam conforme o modelo, como listado acima.

Observação: a entrada `prompt` não deve estar vazia. O nó valida que ela contém pelo menos um caractere que não seja espaço em branco.

Observação: o nó faz upload de até os primeiros 10 itens de mídia como URLs, priorizando vídeo, depois áudio e depois imagens. Quaisquer mídias restantes são enviadas embutidas como base64. O total de mídia embutida é limitado a 18 MB; se excedido, o nó gera um erro solicitando que você reduza o número ou o tamanho das mídias anexadas.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `STRING` | A resposta de texto gerada pelo modelo Gemini selecionado. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNodeV3/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d04d1e97a9c213297899291ad30db14a9f946b07506d0377fead4e29510c5ad9`
