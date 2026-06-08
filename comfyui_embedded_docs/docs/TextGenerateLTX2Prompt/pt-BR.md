O nó TextGenerateLTX2Prompt é uma versão especializada de um nó de geração de texto. Ele recebe um prompt de texto do usuário e o formata automaticamente com instruções de sistema específicas antes de enviá-lo a um modelo de linguagem para aprimoramento ou conclusão. O nó pode operar em dois modos: apenas texto ou com uma referência de imagem, usando prompts de sistema diferentes para cada caso.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `clip` | O modelo CLIP usado para codificação de texto. | CLIP | Sim |  |
| `prompt` | O texto bruto inserido pelo usuário que será aprimorado ou concluído. | STRING | Sim |  |
| `comprimento_máximo` | O número máximo de tokens que o modelo de linguagem pode gerar. | INT | Sim |  |
| `modo_de_amostragem` | A estratégia de amostragem usada para selecionar o próximo token durante a geração de texto. | COMBO | Sim | `"greedy"`<br>`"top_k"`<br>`"top_p"`<br>`"temperature"` |
| `imagem` | Uma imagem opcional de entrada. Quando fornecida, o nó usa um prompt de sistema diferente que inclui um espaço reservado para o contexto da imagem. | IMAGE | Não |  |
| `pensando` | Quando ativado, o modelo exibirá seu processo de raciocínio antes da resposta final. | BOOLEAN | Não |  |
| `use_default_template` | Quando ativado, o nó usará o template de chat padrão para formatação. | BOOLEAN | Não |  |
| `vídeo` | Uma entrada de vídeo opcional que pode ser usada como contexto adicional para a geração. | VIDEO | Não |  |
| `áudio` | Uma entrada de áudio opcional que pode ser usada como contexto adicional para a geração. | AUDIO | Não |  |

**Nota:** O comportamento do nó muda com base na presença da entrada `image`. Se uma imagem for fornecida, o prompt gerado será formatado para uma tarefa de imagem para vídeo. Se nenhuma imagem for fornecida, a formatação será para uma tarefa de texto para vídeo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | A string de texto aprimorada ou concluída gerada pelo modelo de linguagem. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerateLTX2Prompt/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a3daa0a376a53b9c5613238092cc1289d4c358c7c74b12a6e311681de550d1f8`
