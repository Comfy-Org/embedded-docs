# TextGenerateLTX2Prompt

O nó TextGenerateLTX2Prompt expande um prompt curto do usuário em uma descrição detalhada, audiovisual e adequada para a geração de vídeo com os modelos de vídeo da série LTX-2. Ele adiciona automaticamente instruções de sistema específicas para a tarefa, envia o prompt formatado para um modelo de linguagem e retorna o texto aprimorado. Quando uma imagem de referência opcional é fornecida, o nó alterna para o modo imagem-para-vídeo e expande o prompt a partir do conteúdo dessa imagem.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `clip` | O modelo CLIP usado para codificação de texto. O nó verifica o nome do tokenizador do modelo para selecionar as instruções correspondentes: modelos baseados em Gemma 4 usam o formato LTX-2.4, enquanto outros modelos usam o formato LTX-2 (Gemma 3). | CLIP | Sim |  |
| `prompt` | A entrada de texto bruta que descreve a cena ou o conceito a ser expandido em um prompt detalhado de geração de vídeo. | STRING | Sim |  |
| `comprimento_máximo` | O número máximo de tokens que o modelo de linguagem pode gerar. | INT | Sim |  |
| `modo_de_amostragem` | A estratégia de amostragem usada para selecionar o próximo token durante a geração de texto. | COMBO | Sim | `"greedy"`<br>`"top_k"`<br>`"top_p"`<br>`"temperature"` |
| `imagem` | Uma imagem de entrada opcional usada como primeiro quadro do vídeo. Quando fornecida, o nó alterna para o modo imagem-para-vídeo e usa um prompt de sistema que expande o prompt do usuário com base no conteúdo da imagem. | IMAGE | Não |  |
| `pensando` | Quando ativado, o modelo recebe instruções para raciocinar antes de responder. Qualquer bloco de raciocínio é removido da saída retornada (padrão: False). | BOOLEAN | Não |  |
| `use_default_template` | Quando ativado, o nó usa o template de chat padrão para formatação (padrão: True). | BOOLEAN | Não |  |
| `vídeo` | Uma entrada de vídeo opcional que pode ser usada como contexto adicional para a geração. | VIDEO | Não |  |
| `áudio` | Uma entrada de áudio opcional que pode ser usada como contexto adicional para a geração. | AUDIO | Não |  |

**Observação:** O comportamento do nó muda de acordo com suas entradas:

- Se uma `image` for fornecida, o prompt gerado é formatado para uma tarefa de imagem-para-vídeo usando um prompt de sistema que descreve como expandir o prompt com base no conteúdo da imagem. Se nenhuma imagem for fornecida, a formatação é para uma tarefa de texto-para-vídeo usando um prompt de sistema que expande o prompt em uma descrição detalhada de geração de vídeo.
- Se o nome do tokenizador do CLIP contiver "gemma4", o nó usa os prompts de sistema do LTX-2.4 e o formato de chat do Gemma 4. Caso contrário, ele usa os prompts de sistema e o formato de chat do LTX-2 (Gemma 3).
- Se o modelo de linguagem não produzir texto utilizável após remover os blocos de raciocínio, o nó retorna o `prompt` original.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `texto_gerado` | O prompt aprimorado de geração de vídeo produzido pelo modelo de linguagem, com qualquer bloco de raciocínio removido. Se o resultado estiver vazio, o prompt original do usuário é retornado. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerateLTX2Prompt/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8f524ea60a247217dde8a1edaf7a689e253ae05acc9eb52ad47b91e879dba1df`
