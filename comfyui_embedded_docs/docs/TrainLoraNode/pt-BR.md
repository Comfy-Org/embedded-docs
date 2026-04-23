> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrainLoraNode/pt-BR.md)

O nó TrainLoraNode cria e treina um modelo LoRA (Adaptação de Baixa Classificação) em um modelo de difusão usando latentes e dados de condicionamento fornecidos. Ele permite ajustar um modelo com parâmetros de treinamento personalizados, otimizadores e funções de perda. O nó gera os pesos LoRA treinados, um mapa do histórico de perda e o total de etapas de treinamento concluídas.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `model` | MODEL | Sim | - | O modelo no qual treinar o LoRA. |
| `latents` | LATENT | Sim | - | Os Latentes a serem usados para o treinamento, servem como conjunto de dados/entrada do modelo. |
| `positive` | CONDITIONING | Sim | - | O condicionamento positivo a ser usado para o treinamento. |
| `batch_size` | INT | Sim | 1-10000 | O tamanho do lote a ser usado para o treinamento (padrão: 1). |
| `grad_accumulation_steps` | INT | Sim | 1-1024 | O número de etapas de acumulação de gradiente a serem usadas para o treinamento (padrão: 1). |
| `steps` | INT | Sim | 1-100000 | O número de etapas para treinar o LoRA (padrão: 16). |
| `learning_rate` | FLOAT | Sim | 0.0000001-1.0 | A taxa de aprendizado a ser usada para o treinamento (padrão: 0.0005). |
| `rank` | INT | Sim | 1-128 | A classificação das camadas LoRA (padrão: 8). |
| `optimizer` | COMBO | Sim | "AdamW"<br>"Adam"<br>"SGD"<br>"RMSprop" | O otimizador a ser usado para o treinamento (padrão: "AdamW"). |
| `loss_function` | COMBO | Sim | "MSE"<br>"L1"<br>"Huber"<br>"SmoothL1" | A função de perda a ser usada para o treinamento (padrão: "MSE"). |
| `seed` | INT | Sim | 0-18446744073709551615 | A semente a ser usada para o treinamento (usada no gerador para inicialização de pesos LoRA e amostragem de ruído) (padrão: 0). |
| `training_dtype` | COMBO | Sim | "bf16"<br>"fp32"<br>"none" | O dtype a ser usado para o treinamento. 'none' preserva o dtype de computação nativo do modelo em vez de substituí-lo. Para modelos fp16, o GradScaler é ativado automaticamente (padrão: "bf16"). |
| `lora_dtype` | COMBO | Sim | "bf16"<br>"fp32" | O dtype a ser usado para o lora (padrão: "bf16"). |
| `quantized_backward` | BOOLEANO | Sim | - | Ao usar training_dtype 'none' e treinar em um modelo quantizado, realiza o backward com matmul quantizado quando ativado (padrão: Falso). |
| `algorithm` | COMBO | Sim | Múltiplas opções disponíveis | O algoritmo a ser usado para o treinamento. |
| `gradient_checkpointing` | BOOLEANO | Sim | - | Usar checkpointing de gradiente para o treinamento (padrão: Verdadeiro). |
| `checkpoint_depth` | INT | Sim | 1-5 | Nível de profundidade para checkpointing de gradiente (padrão: 1). |
| `offloading` | BOOLEANO | Sim | - | Descarregar pesos do modelo para a CPU durante o treinamento para economizar memória da GPU (padrão: Falso). |
| `existing_lora` | COMBO | Sim | Múltiplas opções disponíveis | O LoRA existente ao qual anexar. Defina como Nenhum para um novo LoRA (padrão: "[Nenhum]"). |
| `bucket_mode` | BOOLEANO | Sim | - | Ativar o modo de balde de resolução. Quando ativado, espera latentes pré-agrupados do nó ResolutionBucket (padrão: Falso). |
| `bypass_mode` | BOOLEANO | Sim | - | Ativar o modo de bypass para treinamento. Quando ativado, os adaptadores são aplicados via hooks de encaminhamento em vez de modificação de peso. Útil para modelos quantizados onde os pesos não podem ser modificados diretamente (padrão: Falso). |

**Nota:** O número de entradas de condicionamento positivo deve corresponder ao número de imagens latentes. Se apenas um condicionamento positivo for fornecido com múltiplas imagens, ele será repetido automaticamente para todas as imagens.

**Nota sobre `training_dtype`:** Quando definido como "none", o dtype de computação nativo do modelo é preservado. Para modelos fp16, o GradScaler é ativado automaticamente para evitar underflow durante o cálculo do gradiente. Se `fp16_accumulation` também estiver ativado (via flags `--fast`), essa combinação pode ser numericamente instável e pode causar valores NaN.

**Nota sobre `quantized_backward`:** Este parâmetro é relevante apenas quando `training_dtype` está definido como "none" e o modelo é um modelo quantizado. Ele ativa a multiplicação de matriz quantizada durante a passagem backward.

**Nota sobre `bypass_mode`:** Quando ativado, os adaptadores são aplicados via hooks de encaminhamento em vez de modificar os pesos do modelo diretamente. Isso é particularmente útil para modelos quantizados onde os pesos não podem ser modificados diretamente.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `lora` | LORA_MODEL | Os pesos LoRA treinados que podem ser salvos ou aplicados a outros modelos. |
| `loss_map` | LOSS_MAP | Um dicionário contendo os valores de perda de treinamento ao longo do tempo. |
| `steps` | INT | O número total de etapas de treinamento concluídas (incluindo quaisquer etapas anteriores do LoRA existente). |