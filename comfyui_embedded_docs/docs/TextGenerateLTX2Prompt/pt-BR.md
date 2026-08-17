# TextGenerateLTX2Prompt

O nó TextGenerateLTX2Prompt é uma versão especializada de um nó de geração de texto. Ele recebe o prompt de texto do usuário e o formata automaticamente com instruções de sistema específicas do LTX2 antes de enviá-lo a um modelo de linguagem para aprimoramento ou conclusão. O nó pode funcionar em modo somente texto ou com referência de imagem, e adapta automaticamente sua formatação ao modelo CLIP conectado, usando o formato de prompt LTX 2.4 para modelos Gemma 4 e o formato LTX 2.0 para modelos Gemma 3.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `clip` | O modelo CLIP usado para codificação de texto. O modelo determina o formato do prompt: modelos Gemma 4 usam o formato LTX 2.4 e modelos Gemma 3 usam o formato LTX 2.0. | CLIP | Sim |  |
| `prompt` | A entrada de texto bruta do usuário que será aprimorada ou concluída. | STRING | Sim |  |
| `max_length` | O número máximo de tokens que o modelo de linguagem pode gerar. | INT | Sim |  |
| `sampling_mode` | A estratégia de amostragem usada para selecionar o próximo token durante a geração de texto. | COMBO | Sim | `"greedy"`<br>`"top_k"`<br>`"top_p"`<br>`"temperature"` |
| `image` | Uma imagem de entrada opcional. Quando fornecida, o nó usa um prompt de sistema diferente que inclui contexto de imagem para geração de imagem para vídeo. | IMAGE | Não |  |
| `thinking` | Quando ativado, o modelo exibirá seu processo de raciocínio antes da resposta final. O bloco de raciocínio é removido do resultado final. | BOOLEAN | Não |  |
| `use_default_template` | Quando ativado, o nó usará o modelo de chat padrão para formatação. | BOOLEAN | Não |  |
| `video` | Uma entrada de vídeo opcional que pode ser usada como contexto adicional para geração. | VIDEO | Não |  |
| `audio` | Uma entrada de áudio opcional que pode ser usada como contexto adicional para geração. | AUDIO | Não |  |

**Notas:** O comportamento do nó muda com base na presença da entrada `image`. Se uma imagem for fornecida, o prompt é formatado para uma tarefa de imagem para vídeo usando um prompt de sistema que expande o prompt com base no conteúdo da imagem. Se nenhuma imagem for fornecida, a formatação é para uma tarefa de texto para vídeo usando um prompt de sistema que expande o prompt em uma descrição detalhada de geração de vídeo.

O modelo `clip` conectado também afeta a formatação: quando o tokenizador CLIP é um modelo Gemma 4, o nó usa o formato de chat e os prompts de sistema do LTX 2.4; caso contrário, usa o formato de chat Gemma 3 / LTX 2.0. Após a geração, qualquer bloco de raciocínio (por exemplo, `<think>...</think>`) é removido da saída e, se o texto resultante estiver vazio, o `prompt` original é retornado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | A string de texto aprimorada ou concluída gerada pelo modelo de linguagem, com qualquer conteúdo de raciocínio removido. Se o modelo não produzir texto, o prompt original é retornado. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerateLTX2Prompt/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8f524ea60a247217dde8a1edaf7a689e253ae05acc9eb52ad47b91e879dba1df`
