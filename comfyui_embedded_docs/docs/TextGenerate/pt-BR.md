# TextGenerate

O nó TextGenerate usa um modelo CLIP para criar texto com base no prompt do usuário. Ele pode, opcionalmente, usar imagens, vídeo ou áudio como contexto adicional para orientar a geração de texto. Você pode controlar o comprimento da saída, ativar um modo de pensamento para modelos compatíveis e escolher se deve usar amostragem aleatória com várias configurações ou gerar texto sem amostragem.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modo_de_amostragem` | Controla se a amostragem aleatória é usada durante a geração de texto. Quando definido como "on", parâmetros adicionais de amostragem ficam disponíveis. Quando definido como "off", o nó gera texto sem amostragem aleatória. | DYNAMIC_COMBO | Sim | `"on"`<br>`"off"` |
| `clip` | O modelo CLIP usado para tokenizar o prompt e gerar texto. | CLIP | Sim | N/A |
| `prompt` | O prompt de texto que orienta a geração. Este campo oferece suporte a múltiplas linhas e prompts dinâmicos. O valor padrão é uma string vazia. | STRING | Sim | N/A |
| `imagem` | Uma imagem opcional que pode ser usada junto com o prompt de texto para influenciar o texto gerado. | IMAGE | Não | N/A |
| `vídeo` | Quadros de vídeo como um lote de imagens. Presume-se 24 FPS; internamente, é subamostrado para 1 FPS. | IMAGE | Não | N/A |
| `áudio` | Uma entrada de áudio opcional que pode ser usada junto com o prompt de texto para influenciar o texto gerado. | AUDIO | Não | N/A |
| `comprimento_máximo` | O número máximo de tokens que o modelo gerará. O valor padrão é 512. | INT | Sim | 1 a 32768 |
| `pensando` | Opera em modo de pensamento se o modelo oferecer suporte a isso. O valor padrão é False. | BOOLEAN | Não | True or False |
| `use_default_template` | Usa o prompt de sistema/template integrado se o modelo tiver um. O valor padrão é True. Este é um parâmetro avançado. | BOOLEAN | Não | True or False |
| `mtp` | Decodificação especulativa com o cabeça de previsão multítoken do checkpoint. Não tem efeito sem pesos MTP. `"auto"` adapta a profundidade do rascunho; `"2"` a `"5"` fixam-na. A saída amostrada permanece corretamente distribuída, mas difere da saída sem MTP para a mesma seed (padrão: `"auto"`). | COMBO | Não | `"auto"`<br>`"off"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"` |
| `system_prompt` | Substitui o prompt de sistema no template de chat do modelo. Ignorado quando o template padrão não é usado. Conecte uma entrada STRING em vez de digitá-lo no nó (padrão: vazio). | STRING | Não | N/A |

### Parâmetros de amostragem (quando `sampling_mode` está definido como "on")

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `temperature` | Controla a aleatoriedade da saída. Valores menores tornam a saída mais previsível; valores maiores a tornam mais criativa. O valor padrão é 0.7. | FLOAT | Sim | 0.01 a 2.0 |
| `top_k` | Limita o conjunto de amostragem aos K tokens mais prováveis a seguir. Um valor de 0 desativa este filtro. O valor padrão é 64. | INT | Sim | 0 a 1000 |
| `top_p` | Usa amostragem por núcleo: mantém o menor conjunto de tokens mais prováveis cuja probabilidade acumulada atinge este valor. O valor padrão é 0.95. | FLOAT | Sim | 0.0 a 1.0 |
| `min_p` | Define um limiar mínimo de probabilidade para que os tokens sejam considerados. O valor padrão é 0.05. | FLOAT | Sim | 0.0 a 1.0 |
| `repetition_penalty` | Penaliza tokens que já foram gerados para reduzir repetições. Um valor de 1.0 não aplica penalidade. O valor padrão é 1.05. | FLOAT | Sim | 0.0 a 5.0 |
| `seed` | Um número usado para inicializar o gerador de números aleatórios para resultados reproduzíveis. O valor padrão é 0. | INT | Sim | 0 a 18446744073709551615 |
| `presence_penalty` | Penaliza novos tokens com base em se eles já apareceram no texto até o momento, incentivando o modelo a falar sobre novos tópicos. O valor padrão é 0.0. | FLOAT | Não | 0.0 a 5.0 |

**Observação:** Os parâmetros de amostragem acima só ficam ativos e visíveis na interface do nó quando `sampling_mode` está definido como "on". Quando `sampling_mode` está definido como "off", nenhum parâmetro de amostragem fica disponível e o nó gera texto sem amostragem aleatória.

**Observação:** Quando o texto gerado contém um bloco de raciocínio (ele começa com `<think>` ou o prompt termina com ele), o raciocínio é retornado separadamente: `generated_text` traz a resposta e `thinking` traz o raciocínio sem a tag de abertura. Caso contrário, `generated_text` traz tudo o que o modelo produziu e `thinking` fica vazio.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `generated_text` | O texto gerado pelo modelo com base no prompt de entrada e na imagem, vídeo ou áudio opcionais, com qualquer bloco de raciocínio separado na saída `thinking`. | STRING |
| `thinking` | O bloco de raciocínio produzido pelo modelo, sem a tag de abertura `<think>`. Vazio quando o modelo não produziu nenhum bloco de raciocínio. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerate/pt-BR.md)

---
**Source fingerprint (SHA-256):** `80813781c06dfb0c3b59ee72c8bd6ebced69a4de8152de916ebc15153a0757fa`
