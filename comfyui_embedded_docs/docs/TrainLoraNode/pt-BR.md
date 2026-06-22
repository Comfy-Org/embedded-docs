# Treinar LoRA

O nó TrainLoraNode cria e treina um modelo LoRA (Adaptação de Baixo Posto) em um modelo de difusão usando latentes fornecidos e dados de condicionamento. Ele permite ajustar um modelo com parâmetros de treinamento personalizados, otimizadores e funções de perda. O nó gera os pesos LoRA treinados, um mapa do histórico de perda e o total de etapas de treinamento concluídas.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo no qual treinar o LoRA. | MODEL | Sim | - |
| `latents` | Os Latentes a serem usados para o treinamento, servem como conjunto de dados/entrada do modelo. | LATENT | Sim | - |
| `positivo` | O condicionamento positivo a ser usado para o treinamento. | CONDITIONING | Sim | - |
| `tamanho_do_lote` | O tamanho do lote a ser usado para o treinamento (padrão: 1). | INT | Sim | 1-10000 |
| `passos_de_acumulo_de_gradiente` | O número de etapas de acumulação de gradiente a serem usadas para o treinamento (padrão: 1). | INT | Sim | 1-1024 |
| `passos` | O número de etapas para treinar o LoRA (padrão: 16). | INT | Sim | 1-100000 |
| `taxa_de_aprendizado` | A taxa de aprendizado a ser usada para o treinamento (padrão: 0.0005). | FLOAT | Sim | 0.0000001-1.0 |
| `rank` | O posto das camadas LoRA (padrão: 8). | INT | Sim | 1-128 |
| `otimizador` | O otimizador a ser usado para o treinamento (padrão: "AdamW"). | COMBO | Sim | "AdamW"<br>"Adam"<br>"SGD"<br>"RMSprop" |
| `função_de_perda` | A função de perda a ser usada para o treinamento (padrão: "MSE"). | COMBO | Sim | "MSE"<br>"L1"<br>"Huber"<br>"SmoothL1" |
| `semente` | A semente a ser usada para o treinamento (usada no gerador para inicialização dos pesos LoRA e amostragem de ruído) (padrão: 0). | INT | Sim | 0-18446744073709551615 |
| `dtype_de_treinamento` | O dtype a ser usado para o treinamento. 'none' preserva o dtype de computação nativo do modelo em vez de substituí-lo. Para modelos fp16, o GradScaler é ativado automaticamente (padrão: "bf16"). | COMBO | Sim | "bf16"<br>"fp32"<br>"none" |
| `lora_dtype` | O dtype a ser usado para o lora (padrão: "bf16"). | COMBO | Sim | "bf16"<br>"fp32" |
| `quantized_backward` | Ao usar training_dtype 'none' e treinar em um modelo quantizado, realiza o backward com matmul quantizado quando ativado (padrão: False). | BOOLEAN | Sim | - |
| `algoritmo` | O algoritmo a ser usado para o treinamento. | COMBO | Sim | Múltiplas opções disponíveis |
| `checkpointing_de_gradiente` | Usar checkpointing de gradiente para o treinamento (padrão: True). | BOOLEAN | Sim | - |
| `checkpoint_depth` | Nível de profundidade para o checkpointing de gradiente (padrão: 1). | INT | Sim | 1-5 |
| `offloading` | Descarregar os pesos do modelo para a CPU durante o treinamento para economizar memória da GPU (padrão: False). | BOOLEAN | Sim | - |
| `lora_existente` | O LoRA existente ao qual anexar. Defina como None para um novo LoRA (padrão: "[None]"). | COMBO | Sim | Múltiplas opções disponíveis |
| `modo_bucket` | Ativar o modo de balde de resolução. Quando ativado, espera latentes pré-agrupados do nó ResolutionBucket (padrão: False). | BOOLEAN | Sim | - |
| `bypass_mode` | Ativar o modo de bypass para o treinamento. Quando ativado, os adaptadores são aplicados via hooks forward em vez de modificação de peso. Útil para modelos quantizados onde os pesos não podem ser modificados diretamente (padrão: False). | BOOLEAN | Sim | - |

**Nota:** O número de entradas de condicionamento positivo deve corresponder ao número de imagens latentes. Se apenas um condicionamento positivo for fornecido com múltiplas imagens, ele será automaticamente repetido para todas as imagens.

**Nota sobre `training_dtype`:** Quando definido como "none", o dtype de computação nativo do modelo é preservado. Para modelos fp16, o GradScaler é ativado automaticamente para evitar underflow durante o cálculo do gradiente. Se `fp16_accumulation` também estiver ativado (via flags `--fast`), esta combinação pode ser numericamente instável e pode causar valores NaN.

**Nota sobre `quantized_backward`:** Este parâmetro só é relevante quando `training_dtype` está definido como "none" e o modelo é um modelo quantizado. Ele ativa a multiplicação de matrizes quantizada durante a passagem backward.

**Nota sobre `bypass_mode`:** Quando ativado, os adaptadores são aplicados via hooks forward em vez de modificar os pesos do modelo diretamente. Isso é particularmente útil para modelos quantizados onde os pesos não podem ser modificados diretamente.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `lora` | Os pesos LoRA treinados que podem ser salvos ou aplicados a outros modelos. | LORA_MODEL |
| `loss_map` | Um dicionário contendo os valores de perda do treinamento ao longo do tempo. | LOSS_MAP |
| `passos` | O número total de etapas de treinamento concluídas (incluindo quaisquer etapas anteriores do LoRA existente). | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrainLoraNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `df315ef416ff3ce81e6a526af2c4e5115980e6c35830825967e7189d4f8541d8`
