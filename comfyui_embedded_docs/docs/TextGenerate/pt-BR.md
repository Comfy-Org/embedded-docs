> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerate/pt-BR.md)

O nó TextGenerate usa um modelo CLIP para criar texto com base no prompt do usuário. Opcionalmente, pode usar imagens, vídeo ou áudio como contexto adicional para orientar a geração de texto. Você pode controlar o comprimento da saída, ativar um modo de raciocínio para modelos compatíveis e escolher entre usar amostragem aleatória com várias configurações ou gerar texto sem amostragem.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `clip` | CLIP | Sim | N/A | O modelo CLIP usado para tokenizar o prompt e gerar texto. |
| `prompt` | STRING | Sim | N/A | O prompt de texto que orienta a geração. Este campo suporta múltiplas linhas e prompts dinâmicos. O valor padrão é uma string vazia. |
| `image` | IMAGE | Não | N/A | Uma imagem opcional que pode ser usada junto com o prompt de texto para influenciar o texto gerado. |
| `video` | IMAGE | Não | N/A | Quadros de vídeo como um lote de imagens. Presume-se que sejam 24 FPS; reamostrados internamente para 1 FPS. |
| `audio` | AUDIO | Não | N/A | Uma entrada de áudio opcional que pode ser usada junto com o prompt de texto para influenciar o texto gerado. |
| `max_length` | INT | Sim | 1 a 2048 | O número máximo de tokens que o modelo irá gerar. O valor padrão é 256. |
| `sampling_mode` | COMBO | Sim | `"on"`<br>`"off"` | Controla se a amostragem aleatória é usada durante a geração de texto. Quando definido como "on", parâmetros adicionais para controlar a amostragem ficam disponíveis. O padrão é "on". |
| `thinking` | BOOLEAN | Não | Verdadeiro ou Falso | Opera no modo de raciocínio se o modelo for compatível. O valor padrão é Falso. |
| `use_default_template` | BOOLEAN | Não | Verdadeiro ou Falso | Usa o prompt/modelo de sistema integrado se o modelo tiver um. O valor padrão é Verdadeiro. Este é um parâmetro avançado. |
| `temperature` | FLOAT | Não | 0.01 a 2.0 | Controla a aleatoriedade da saída. Valores mais baixos tornam a saída mais previsível, valores mais altos a tornam mais criativa. Este parâmetro está disponível apenas quando `sampling_mode` está "on". O valor padrão é 0.7. |
| `top_k` | INT | Não | 0 a 1000 | Limita o conjunto de amostragem aos K tokens seguintes mais prováveis. Um valor de 0 desativa este filtro. Este parâmetro está disponível apenas quando `sampling_mode` está "on". O valor padrão é 64. |
| `top_p` | FLOAT | Não | 0.0 a 1.0 | Usa amostragem de núcleo, limitando as escolhas a tokens cuja probabilidade cumulativa seja menor que este valor. Este parâmetro está disponível apenas quando `sampling_mode` está "on". O valor padrão é 0.95. |
| `min_p` | FLOAT | Não | 0.0 a 1.0 | Define um limite mínimo de probabilidade para que os tokens sejam considerados. Este parâmetro está disponível apenas quando `sampling_mode` está "on". O valor padrão é 0.05. |
| `repetition_penalty` | FLOAT | Não | 0.0 a 5.0 | Penaliza tokens que já foram gerados para reduzir repetições. Um valor de 1.0 não aplica penalidade. Este parâmetro está disponível apenas quando `sampling_mode` está "on". O valor padrão é 1.05. |
| `presence_penalty` | FLOAT | Não | 0.0 a 5.0 | Penaliza novos tokens com base se eles já apareceram no texto até agora, incentivando o modelo a falar sobre novos tópicos. Este parâmetro está disponível apenas quando `sampling_mode` está "on". O valor padrão é 0.0. |
| `seed` | INT | Não | 0 a 18446744073709551615 | Um número usado para inicializar o gerador de números aleatórios para resultados reproduzíveis quando a amostragem está "on". O valor padrão é 0. |

**Nota:** Os parâmetros `temperature`, `top_k`, `top_p`, `min_p`, `repetition_penalty`, `presence_penalty` e `seed` estão ativos e visíveis na interface do nó apenas quando `sampling_mode` está definido como "on".

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `generated_text` | STRING | O texto gerado pelo modelo com base no prompt de entrada e na imagem, vídeo ou áudio opcionais. |

---
**Source fingerprint (SHA-256):** `dc6868bd7ebb63c485a4346113834f845416d7359759b2d428525398bdedf343`
