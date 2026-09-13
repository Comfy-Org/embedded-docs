# TextGenerateLTX2Prompt

O nó TextGenerateLTX2Prompt expande um prompt curto do usuário em uma descrição audiovisual detalhada, adequada para gerar vídeo com a série LTX-2 de modelos de vídeo. Ele adiciona automaticamente instruções de sistema específicas da tarefa, envia o prompt formatado para um modelo de linguagem e retorna o texto aprimorado. Quando uma imagem de referência opcional é fornecida, o nó muda para o modo imagem para vídeo e expande o prompt a partir do conteúdo dessa imagem.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `clip` | O modelo CLIP usado para codificação de texto. O nó verifica o nome do tokenizador do modelo para selecionar as instruções correspondentes: modelos baseados no Gemma 4 usam o formato LTX-2.4, enquanto outros modelos usam o formato LTX-2 (Gemma 3). | CLIP | Sim |  |
| `prompt` | A entrada de texto bruta que descreve a cena ou conceito a ser expandido em um prompt detalhado de geração de vídeo. | STRING | Sim |  |
| `max_length` | O número máximo de tokens que o modelo de linguagem tem permissão para gerar. | INT | Sim |  |
| `sampling_mode` | A estratégia de amostragem usada para selecionar o próximo token durante a geração de texto. | COMBO | Sim | `"greedy"`<br>`"top_k"`<br>`"top_p"`<br>`"temperature"` |
| `image` | Uma imagem de entrada opcional usada como o primeiro quadro do vídeo. Quando fornecida, o nó muda para o modo imagem para vídeo e usa um prompt de sistema que expande o prompt do usuário com base no conteúdo da imagem. | IMAGE | Não |  |
| `thinking` | Quando habilitado, o modelo é instruído a raciocinar antes de responder. Qualquer bloco de raciocínio é removido da saída retornada (padrão: False). | BOOLEAN | Não |  |
| `use_default_template` | Quando habilitado, o nó usa o template de chat padrão para formatação (padrão: True). | BOOLEAN | Não |  |
| `video` | Uma entrada de vídeo opcional que pode ser usada como contexto adicional para a geração. | VIDEO | Não |  |
| `audio` | Uma entrada de áudio opcional que pode ser usada como contexto adicional para a geração. | AUDIO | Não |  |

**Nota:** O comportamento do nó muda com base nas suas entradas:

- Se uma `image` for fornecida, o prompt gerado é formatado para uma tarefa de imagem para vídeo usando um prompt de sistema que descreve como expandir o prompt com base no conteúdo da imagem. Se nenhuma imagem for fornecida, a formatação é para uma tarefa de texto para vídeo usando um prompt de sistema que expande o prompt em uma descrição detalhada de geração de vídeo.
- Se o nome do tokenizador do CLIP contiver "gemma4", o nó usa os prompts de sistema do LTX-2.4 e o formato de chat do Gemma 4. Caso contrário, usa os prompts de sistema e o formato de chat do LTX-2 (Gemma 3).
- Quando `thinking` está habilitado com um modelo Gemma 4, o modelo é aberto em seu canal de raciocínio; quando desabilitado, o modelo é aberto diretamente no canal de resposta final. Para modelos que não são Gemma 4, `thinking` é repassado para a etapa de geração subjacente.
- Se o modelo de linguagem não produzir texto utilizável após a remoção dos blocos de raciocínio, o nó retorna o `prompt` original.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | O prompt de geração de vídeo aprimorado produzido pelo modelo de linguagem, com qualquer bloco de raciocínio removido. Se o resultado estiver vazio, o prompt original do usuário é retornado. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerateLTX2Prompt/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8f524ea60a247217dde8a1edaf7a689e253ae05acc9eb52ad47b91e879dba1df`
