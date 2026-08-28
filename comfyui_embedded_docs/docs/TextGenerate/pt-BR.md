# TextGenerate

O nó TextGenerate usa um modelo CLIP para criar texto com base no prompt do usuário. Ele pode opcionalmente usar imagens, vídeo ou áudio como contexto adicional para orientar a geração de texto. Você pode controlar o comprimento da saída, ativar um modo de pensamento para modelos compatíveis e escolher se deseja usar amostragem aleatória com várias configurações ou gerar texto sem amostragem.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modo_de_amostragem` | Controla se a amostragem aleatória é usada durante a geração de texto. Quando definido como "on", parâmetros adicionais de amostragem ficam disponíveis. Quando definido como "off", o nó gera texto sem amostragem aleatória. | DYNAMIC_COMBO | Sim | `"on"`<br>`"off"` |
| `clip` | O modelo CLIP usado para tokenizar o prompt e gerar texto. | CLIP | Sim | N/A |
| `prompt` | O prompt de texto que orienta a geração. Este campo suporta múltiplas linhas e prompts dinâmicos. O valor padrão é uma string vazia. | STRING | Sim | N/A |
| `imagem` | Uma imagem opcional que pode ser usada junto com o prompt de texto para influenciar o texto gerado. | IMAGE | Não | N/A |
| `vídeo` | Quadros de vídeo como um lote de imagens. Presume-se 24 FPS; subamostrado para 1 FPS internamente. | IMAGE | Não | N/A |
| `áudio` | Uma entrada de áudio opcional que pode ser usada junto com o prompt de texto para influenciar o texto gerado. | AUDIO | Não | N/A |
| `comprimento_máximo` | O número máximo de tokens que o modelo irá gerar. O valor padrão é 512. | INT | Sim | 1 a 32768 |
| `pensando` | Operar no modo de pensamento se o modelo suportar. O valor padrão é False. | BOOLEAN | Não | True or False |
| `use_default_template` | Use o prompt/modelo de sistema integrado se o modelo tiver um. O valor padrão é True. Este é um parâmetro avançado. | BOOLEAN | Não | True or False |

### Parâmetros de amostragem (quando `sampling_mode` é "on")

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `temperature` | Controla a aleatoriedade da saída. Valores menores tornam a saída mais previsível, valores maiores a tornam mais criativa. O valor padrão é 0.7. | FLOAT | Sim | 0.01 a 2.0 |
| `top_k` | Limita o conjunto de amostragem aos K tokens mais prováveis como próximos. Um valor de 0 desativa esse filtro. O valor padrão é 64. | INT | Sim | 0 a 1000 |
| `top_p` | Usa amostragem de núcleo, limitando as escolhas a tokens cuja probabilidade cumulativa é menor que esse valor. O valor padrão é 0.95. | FLOAT | Sim | 0.0 a 1.0 |
| `min_p` | Define um limite mínimo de probabilidade para que tokens sejam considerados. O valor padrão é 0.05. | FLOAT | Sim | 0.0 a 1.0 |
| `repetition_penalty` | Penaliza tokens que já foram gerados para reduzir repetição. Um valor de 1.0 não aplica penalidade. O valor padrão é 1.05. | FLOAT | Sim | 0.0 a 5.0 |
| `seed` | Um número usado para inicializar o gerador de números aleatórios para obter resultados reproduzíveis. O valor padrão é 0. | INT | Sim | 0 a 18446744073709551615 |
| `presence_penalty` | Penaliza novos tokens com base em se eles já apareceram no texto até o momento, incentivando o modelo a falar sobre novos tópicos. O valor padrão é 0.0. | FLOAT | Não | 0.0 a 5.0 |

**Nota:** Os parâmetros de amostragem acima estão ativos e visíveis na interface do nó apenas quando `sampling_mode` está definido como "on". Quando `sampling_mode` está definido como "off", nenhum parâmetro de amostragem fica disponível e o nó gera texto sem amostragem aleatória.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `texto_gerado` | O texto gerado pelo modelo com base no prompt de entrada e em imagem, vídeo ou áudio opcionais. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerate/pt-BR.md)

---
**Source fingerprint (SHA-256):** `6274a2db7c9a963304daf6df494b2b20879155e918d73429fd2ce7f3b5b9da02`
