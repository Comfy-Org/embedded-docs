> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerate/pt-BR.md)

O nó TextGenerate utiliza um modelo CLIP para criar texto com base em um prompt do usuário. Opcionalmente, pode usar uma imagem como referência visual para orientar a geração de texto. Você pode controlar o comprimento da saída e escolher se deseja usar amostragem aleatória com várias configurações ou gerar texto sem amostragem.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | Sim | N/A | O modelo CLIP usado para tokenizar o prompt e gerar texto. |
| `prompt` | STRING | Sim | N/A | O prompt de texto que orienta a geração. Este campo suporta múltiplas linhas e prompts dinâmicos. O valor padrão é uma string vazia. |
| `image` | IMAGE | Não | N/A | Uma imagem opcional que pode ser usada junto com o prompt de texto para influenciar o texto gerado. |
| `max_length` | INT | Sim | 1 a 2048 | O número máximo de tokens que o modelo irá gerar. O valor padrão é 256. |
| `sampling_mode` | COMBO | Sim | `"on"`<br>`"off"` | Controla se a amostragem aleatória é usada durante a geração de texto. Quando definido como "on", parâmetros adicionais para controlar a amostragem ficam disponíveis. O padrão é "on". |
| `temperature` | FLOAT | Não | 0.01 a 2.0 | Controla a aleatoriedade da saída. Valores mais baixos tornam a saída mais previsível, valores mais altos a tornam mais criativa. Este parâmetro só está disponível quando `sampling_mode` está "on". O valor padrão é 0.7. |
| `top_k` | INT | Não | 0 a 1000 | Limita o conjunto de amostragem aos K tokens mais prováveis a seguir. Um valor de 0 desativa este filtro. Este parâmetro só está disponível quando `sampling_mode` está "on". O valor padrão é 64. |
| `top_p` | FLOAT | Não | 0.0 a 1.0 | Usa amostragem por núcleo (nucleus sampling), limitando as escolhas a tokens cuja probabilidade cumulativa seja menor que este valor. Este parâmetro só está disponível quando `sampling_mode` está "on". O valor padrão é 0.95. |
| `min_p` | FLOAT | Não | 0.0 a 1.0 | Define um limite mínimo de probabilidade para que os tokens sejam considerados. Este parâmetro só está disponível quando `sampling_mode` está "on". O valor padrão é 0.05. |
| `repetition_penalty` | FLOAT | Não | 0.0 a 5.0 | Penaliza tokens que já foram gerados para reduzir repetições. Um valor de 1.0 não aplica penalidade. Este parâmetro só está disponível quando `sampling_mode` está "on". O valor padrão é 1.05. |
| `seed` | INT | Não | 0 a 18446744073709551615 | Um número usado para inicializar o gerador de números aleatórios para resultados reproduzíveis quando a amostragem está "on". O valor padrão é 0. |

**Observação:** Os parâmetros `temperature`, `top_k`, `top_p`, `min_p`, `repetition_penalty` e `seed` só estão ativos e visíveis na interface do nó quando o `sampling_mode` está definido como "on".

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `generated_text` | STRING | O texto gerado pelo modelo com base no prompt de entrada e na imagem opcional. |