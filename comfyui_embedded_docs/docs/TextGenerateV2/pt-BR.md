# Generate Text

O nó Generate Text usa um modelo CLIP para produzir texto a partir de um prompt. Diferentemente do nó mais antigo de anexo único, ele aceita pilhas expansíveis de imagens, vídeos e arquivos de áudio como contexto extra, para que você possa fornecer um conjunto completo de referências em um único nó. Você controla o comprimento da saída, se a amostragem é usada e se o próprio template de chat e o modo de raciocínio do modelo são aplicados.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `clip` | O modelo CLIP usado para tokenizar o prompt e gerar o texto. | CLIP | Sim | - |
| `prompt` | O prompt que orienta a geração. Suporta várias linhas e prompts dinâmicos (padrão: string vazia). | STRING | Sim | - |
| `images` | Grupo expansível de até 50 imagens, `image1` a `image50`, usado como contexto visual para o modelo. | AUTOGROW | Não | 0 a 50 imagens |
| `videos` | Grupo expansível de até 100 entradas de vídeo, `video1` a `video100`. Cada vídeo é um lote de quadros considerados a 24 FPS e subamostrados internamente para a taxa de quadros do modelo. | AUTOGROW | Não | 0 a 100 vídeos |
| `audios` | Grupo expansível de até 100 entradas de áudio, `audio1` a `audio100`, usado como contexto de áudio para o modelo. | AUTOGROW | Não | 0 a 100 arquivos de áudio |
| `max_length` | Número máximo de tokens a gerar (padrão: 512). | INT | Sim | 1 a 32768 |
| `sampling_mode` | `on` faz amostragem da saída e revela os parâmetros de amostragem abaixo. `off` gera de forma gulosa, sem amostragem aleatória. | DYNAMIC_COMBO | Sim | `"on"`<br>`"off"` |
| `thinking` | Operar no modo de raciocínio se o modelo oferecer suporte (padrão: False). | BOOLEAN | Não | True ou False |
| `use_default_template` | Usar o prompt de sistema ou template de chat integrado, se o modelo tiver um (padrão: True). Parâmetro avançado. | BOOLEAN | Não | True ou False |
| `mtp` | Decodificação especulativa com a cabeça de predição de múltiplos tokens do checkpoint. Não tem efeito sem pesos MTP. `"auto"` adapta a profundidade e a largura do rascunho aos acertos de tokens observados e ao custo de execução; `"2"` a `"5"` fixam uma profundidade de rascunho constante; e os modos `tree` fixam tanto a largura quanto a profundidade. A saída amostrada permanece corretamente distribuída, mas difere da saída sem MTP para a mesma seed (padrão: `"auto"`). | COMBO | Não | `"auto"`<br>`"off"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"tree2s1"`<br>`"tree2s2"`<br>`"tree3s1"`<br>`"tree4s1m8"` |
| `system_prompt` | Substitui o prompt de sistema no template de chat do modelo. Ignorado quando o template padrão não é usado. Conecte uma entrada STRING em vez de digitar no nó (padrão: vazio). | STRING | Não | - |

### Parâmetros de amostragem (quando `sampling_mode` é `"on"`)

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `temperature` | Controla a aleatoriedade da saída. Valores menores tornam a saída mais previsível; valores maiores a tornam mais criativa (padrão: 0.7). | FLOAT | Sim | 0.01 a 2.0 |
| `top_k` | Limita o conjunto de amostragem aos K próximos tokens mais prováveis. Um valor de 0 desativa o filtro (padrão: 64). | INT | Sim | 0 a 1000 |
| `top_p` | Amostragem de núcleo: mantém o menor conjunto de tokens mais prováveis cuja probabilidade cumulativa atinge este valor (padrão: 0.95). | FLOAT | Sim | 0.0 a 1.0 |
| `min_p` | Probabilidade mínima que um token deve atingir para permanecer no conjunto (padrão: 0.05). | FLOAT | Sim | 0.0 a 1.0 |
| `repetition_penalty` | Penaliza tokens que já foram gerados para reduzir a repetição. Um valor de 1.0 não aplica penalidade (padrão: 1.05). | FLOAT | Sim | 0.0 a 5.0 |
| `presence_penalty` | Penaliza novos tokens com base em se eles já apareceram no texto até o momento, incentivando o modelo a mudar para novos tópicos (padrão: 0.0). | FLOAT | Sim | 0.0 a 5.0 |
| `seed` | Número usado para inicializar o gerador de números aleatórios para resultados reproduzíveis (padrão: 0). | INT | Sim | 0 a 18446744073709551615 |

**Observação:** Os parâmetros de amostragem acima só existem quando `sampling_mode` é `"on"`. Com `"off"`, o nó gera texto sem amostragem aleatória e os parâmetros ficam ocultos.

**Observação:** Quando a saída do modelo abre um bloco de raciocínio com `<think>`, o nó o divide: `generated_text` contém a resposta e `thinking` contém o raciocínio com a tag de abertura removida. Caso contrário, `generated_text` contém tudo o que o modelo produziu e `thinking` fica vazio. O raciocínio que foi cortado por `max_length` permanece em `generated_text`.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `generated_text` | O texto que o modelo gerou, com qualquer bloco de raciocínio separado para a saída `thinking`. | STRING |
| `thinking` | O bloco de raciocínio que o modelo produziu, com a tag de abertura `<think>` removida. Vazio quando o modelo não produziu nenhum bloco de raciocínio. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerateV2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b61210726faa495a342a5eaaebe64f800ec1d2af4e2fc1321d8c3d7c594bd9ca`
