# TextGenerateLTX2Prompt

O nó TextGenerateLTX2Prompt expande um prompt curto do usuário em uma descrição audiovisual detalhada, adequada para gerar vídeo com a série LTX-2 de modelos de vídeo. Ele adiciona automaticamente instruções de sistema específicas da tarefa, envia o prompt formatado para um modelo de linguagem e retorna o texto aprimorado. Quando uma imagem de referência opcional é fornecida, o nó alterna para o modo imagem para vídeo e expande o prompt a partir do conteúdo dessa imagem.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `clip` | O modelo CLIP usado para codificação de texto. O nó verifica o nome do tokenizador do modelo para selecionar as instruções correspondentes: modelos baseados no Gemma 4 usam o formato LTX-2.4, enquanto outros modelos usam o formato LTX-2 (Gemma 3). | CLIP | Sim | - |
| `prompt` | A entrada de texto bruta que descreve a cena ou o conceito a ser expandido em um prompt detalhado de geração de vídeo. | STRING | Sim | - |
| `imagem` | Uma imagem de entrada opcional usada como o primeiro quadro do vídeo. Quando fornecida, o nó alterna para o modo imagem para vídeo e usa um prompt de sistema que expande o prompt do usuário com base no conteúdo da imagem. | IMAGE | Não | - |
| `vídeo` | Uma entrada de vídeo opcional usada como contexto adicional. Passada ao modelo de linguagem como um lote de imagens; assume-se 24 FPS e é subamostrada internamente para 1 FPS. | IMAGE | Não | - |
| `áudio` | Uma entrada de áudio opcional que pode ser usada como contexto adicional para a geração. | AUDIO | Não | - |
| `comprimento_máximo` | O número máximo de tokens que o modelo de linguagem tem permissão para gerar (padrão: 512). | INT | Sim | 1 a 32768 |
| `modo_de_amostragem` | Controla se a amostragem aleatória é usada durante a geração de texto. Quando definido como `"on"`, os parâmetros de amostragem abaixo ficam disponíveis; com `"off"`, o nó gera texto sem amostragem aleatória. | DYNAMIC_COMBO | Sim | `"on"`<br>`"off"` |
| `pensando` | Quando habilitado, o modelo é instruído a raciocinar antes de responder. Qualquer bloco de raciocínio é removido da saída retornada (padrão: False). | BOOLEAN | Não | True/False |
| `use_default_template` | Quando habilitado, o nó usa o template de chat padrão para formatação (padrão: True). Configuração avançada. | BOOLEAN | Não | True/False |
| `mtp` | Decodificação especulativa com a cabeça de predição multi-token do checkpoint. Não tem efeito sem pesos MTP. `"auto"` adapta a profundidade do rascunho; `"2"` a `"5"` fixam-na. A saída amostrada permanece corretamente distribuída, mas difere da saída não MTP para a mesma seed (padrão: `"auto"`). | COMBO | Não | `"auto"`<br>`"off"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"` |

### Parâmetros de amostragem (quando `sampling_mode` está "on")

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `temperature` | Controla a aleatoriedade da saída. Valores mais baixos tornam a saída mais previsível; valores mais altos a tornam mais criativa (padrão: 0.7). | FLOAT | Sim | 0.01 a 2.0 |
| `top_k` | Limita o conjunto de amostragem aos K tokens seguintes mais prováveis. Um valor de 0 desativa este filtro (padrão: 64). | INT | Sim | 0 a 1000 |
| `top_p` | Usa amostragem por núcleo: mantém o menor conjunto de tokens mais prováveis cuja probabilidade acumulada atinge este valor. (padrão: 0.95) | FLOAT | Sim | 0.0 a 1.0 |
| `min_p` | Define um limiar mínimo de probabilidade para que os tokens sejam considerados (padrão: 0.05). | FLOAT | Sim | 0.0 a 1.0 |
| `repetition_penalty` | Penaliza tokens que já foram gerados para reduzir repetição. Um valor de 1.0 não aplica penalidade (padrão: 1.05). | FLOAT | Sim | 0.0 a 5.0 |
| `seed` | Um número usado para inicializar o gerador de números aleatórios para resultados reproduzíveis (padrão: 0). | INT | Sim | 0 a 18446744073709551615 |
| `presence_penalty` | Penaliza novos tokens com base em se eles já apareceram no texto até o momento, incentivando o modelo a falar sobre novos tópicos (padrão: 0.0). | FLOAT | Não | 0.0 a 5.0 |

**Nota:** Os parâmetros de amostragem acima só ficam ativos e visíveis na interface do nó quando `sampling_mode` está definido como "on". Quando está definido como "off", nenhum parâmetro de amostragem fica disponível e o nó gera texto sem amostragem aleatória.

**Nota:** O comportamento do nó muda com base em suas entradas:

- Se uma `image` for fornecida, o prompt gerado é formatado para uma tarefa de imagem para vídeo usando um prompt de sistema que descreve como expandir o prompt com base no conteúdo da imagem. Se nenhuma imagem for fornecida, a formatação é para uma tarefa de texto para vídeo usando um prompt de sistema que expande o prompt em uma descrição detalhada de geração de vídeo.
- Se o nome do tokenizador do CLIP contiver "gemma4", o nó usa os prompts de sistema do LTX-2.4 e o formato de chat do Gemma 4. Caso contrário, usa os prompts de sistema do LTX-2 (Gemma 3) e o formato de chat.
- Quando `thinking` está habilitado com um modelo Gemma 4, o modelo é aberto em seu canal de raciocínio; quando desabilitado, o modelo é aberto diretamente no canal de resposta final. Para modelos que não são Gemma 4, `thinking` é repassado para a etapa de geração subjacente.
- Se o modelo de linguagem não produzir texto utilizável após remover os blocos de raciocínio, o nó retorna o `prompt` original.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `generated_text` | O prompt de geração de vídeo aprimorado produzido pelo modelo de linguagem, com qualquer bloco de raciocínio removido. Se o resultado estiver vazio, o prompt original do usuário é retornado. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerateLTX2Prompt/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1da4a388b7c358e5649b4746b9b8d288977ec6fbed3eedc4c8709187c9f7b943`
