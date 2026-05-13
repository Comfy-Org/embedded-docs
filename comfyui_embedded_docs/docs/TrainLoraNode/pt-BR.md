> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrainLoraNode/pt-BR.md)

O nó TrainLoraNode cria e treina um modelo LoRA (Adaptação de Baixo Posto) em um modelo de difusão usando latentes fornecidos e dados de condicionamento. Ele permite ajustar um modelo com parâmetros de treinamento personalizados, otimizadores e funções de perda. O nó gera os pesos LoRA treinados, um mapa do histórico de perda e o total de etapas de treinamento concluídas.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `modelo` | MODEL | Sim | - | O modelo no qual treinar o LoRA. |
| `latents` | LATENT | Sim | - | Os Latentes a serem usados para o treinamento, servem como conjunto de dados/entrada do modelo. |
| `positivo` | CONDITIONING | Sim | - | O condicionamento positivo a ser usado para o treinamento. |
| `tamanho_do_lote` | INT | Sim | 1-10000 | O tamanho do lote a ser usado para o treinamento (padrão: 1). |
| `passos_de_acumulo_de_gradiente` | INT | Sim | 1-1024 | O número de etapas de acumulação de gradiente a serem usadas para o treinamento (padrão: 1). |
| `passos` | INT | Sim | 1-100000 | O número de etapas para treinar o LoRA (padrão: 16). |
| `taxa_de_aprendizado` | FLOAT | Sim | 0.0000001-1.0 | A taxa de aprendizado a ser usada para o treinamento (padrão: 0.0005). |
| `rank` | INT | Sim | 1-128 | O posto das camadas LoRA (padrão: 8). |
| `otimizador` | COMBO | Sim | "AdamW"<br>"Adam"<br>"SGD"<br>"RMSprop" | O otimizador a ser usado para o treinamento (padrão: "AdamW"). |
| `função_de_perda` | COMBO | Sim | "MSE"<br>"L1"<br>"Huber"<br>"SmoothL1" | A função de perda a ser usada para o treinamento (padrão: "MSE"). |
| `semente` | INT | Sim | 0-18446744073709551615 | A semente a ser usada para o treinamento (usada no gerador para inicialização dos pesos LoRA e amostragem de ruído) (padrão: 0). |
| `dtype_de_treinamento` | COMBO | Sim | "bf16"<br>"fp32"<br>"none" | O dtype a ser usado para o treinamento. 'none' preserva o dtype de computação nativo do modelo em vez de substituí-lo. Para modelos fp16, o GradScaler é ativado automaticamente (padrão: "bf16"). |
| `lora_dtype` | COMBO | Sim | "bf16"<br>"fp32" | O dtype a ser usado para o lora (padrão: "bf16"). |
| `quantized_backward` | BOOLEAN | Sim | - | Ao usar training_dtype 'none' e treinar em um modelo quantizado, realiza o backward com matmul quantizado quando ativado (padrão: False). |
| `algoritmo` | COMBO | Sim | Múltiplas opções disponíveis | O algoritmo a ser usado para o treinamento. |
| `checkpointing_de_gradiente` | BOOLEAN | Sim | - | Usar checkpointing de gradiente para o treinamento (padrão: True). |
| `checkpoint_depth` | INT | Sim | 1-5 | Nível de profundidade para o checkpointing de gradiente (padrão: 1). |
| `offloading` | BOOLEAN | Sim | - | Descarregar os pesos do modelo para a CPU durante o treinamento para economizar memória da GPU (padrão: False). |
| `lora_existente` | COMBO | Sim | Múltiplas opções disponíveis | O LoRA existente ao qual anexar. Defina como None para um novo LoRA (padrão: "[None]"). |
| `modo_bucket` | BOOLEAN | Sim | - | Ativar o modo de balde de resolução. Quando ativado, espera latentes pré-agrupados do nó ResolutionBucket (padrão: False). |
| `bypass_mode` | BOOLEAN | Sim | - | Ativar o modo de bypass para o treinamento. Quando ativado, os adaptadores são aplicados via hooks forward em vez de modificação de peso. Útil para modelos quantizados onde os pesos não podem ser modificados diretamente (padrão: False). |

**Nota:** O número de entradas de condicionamento positivo deve corresponder ao número de imagens latentes. Se apenas um condicionamento positivo for fornecido com múltiplas imagens, ele será automaticamente repetido para todas as imagens.

**Nota sobre `training_dtype`:** Quando definido como "none", o dtype de computação nativo do modelo é preservado. Para modelos fp16, o GradScaler é ativado automaticamente para evitar underflow durante o cálculo do gradiente. Se `fp16_accumulation` também estiver ativado (via flags `--fast`), esta combinação pode ser numericamente instável e pode causar valores NaN.

**Nota sobre `quantized_backward`:** Este parâmetro só é relevante quando `training_dtype` está definido como "none" e o modelo é um modelo quantizado. Ele ativa a multiplicação de matrizes quantizada durante a passagem backward.

**Nota sobre `bypass_mode`:** Quando ativado, os adaptadores são aplicados via hooks forward em vez de modificar os pesos do modelo diretamente. Isso é particularmente útil para modelos quantizados onde os pesos não podem ser modificados diretamente.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `lora` | LORA_MODEL | Os pesos LoRA treinados que podem ser salvos ou aplicados a outros modelos. |
| `loss_map` | LOSS_MAP | Um dicionário contendo os valores de perda do treinamento ao longo do tempo. |
| `passos` | INT | O número total de etapas de treinamento concluídas (incluindo quaisquer etapas anteriores do LoRA existente). |

---
**Source fingerprint (SHA-256):** `df315ef416ff3ce81e6a526af2c4e5115980e6c35830825967e7189d4f8541d8`
