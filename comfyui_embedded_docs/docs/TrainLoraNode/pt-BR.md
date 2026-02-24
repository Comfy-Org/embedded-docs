> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrainLoraNode/pt-BR.md)

O TrainLoraNode cria e treina um modelo LoRA (Low-Rank Adaptation) em um modelo de difusão usando latentes e dados de condicionamento fornecidos. Ele permite ajustar um modelo com parâmetros de treinamento, otimizadores e funções de perda personalizados. O nó retorna o modelo treinado com o LoRA aplicado, os pesos do LoRA, métricas de perda de treinamento e o total de etapas de treinamento concluídas.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo no qual o LoRA será treinado. |
| `latents` | LATENT | Sim | - | Os Latentes a serem usados para o treinamento, servem como conjunto de dados/entrada do modelo. |
| `positive` | CONDITIONING | Sim | - | O condicionamento positivo a ser usado para o treinamento. |
| `batch_size` | INT | Sim | 1-10000 | O tamanho do lote a ser usado para o treinamento (padrão: 1). |
| `grad_accumulation_steps` | INT | Sim | 1-1024 | O número de etapas de acumulação de gradiente a serem usadas para o treinamento (padrão: 1). |
| `steps` | INT | Sim | 1-100000 | O número de etapas para treinar o LoRA (padrão: 16). |
| `learning_rate` | FLOAT | Sim | 0.0000001-1.0 | A taxa de aprendizado a ser usada para o treinamento (padrão: 0.0005). |
| `rank` | INT | Sim | 1-128 | A classificação (rank) das camadas LoRA (padrão: 8). |
| `optimizer` | COMBO | Sim | "AdamW"<br>"Adam"<br>"SGD"<br>"RMSprop" | O otimizador a ser usado para o treinamento (padrão: "AdamW"). |
| `loss_function` | COMBO | Sim | "MSE"<br>"L1"<br>"Huber"<br>"SmoothL1" | A função de perda a ser usada para o treinamento (padrão: "MSE"). |
| `seed` | INT | Sim | 0-18446744073709551615 | A semente a ser usada para o treinamento (usada no gerador para inicialização dos pesos do LoRA e amostragem de ruído) (padrão: 0). |
| `training_dtype` | COMBO | Sim | "bf16"<br>"fp32" | O tipo de dado (dtype) a ser usado para o treinamento (padrão: "bf16"). |
| `lora_dtype` | COMBO | Sim | "bf16"<br>"fp32" | O tipo de dado (dtype) a ser usado para o LoRA (padrão: "bf16"). |
| `algorithm` | COMBO | Sim | Múltiplas opções disponíveis | O algoritmo a ser usado para o treinamento. |
| `gradient_checkpointing` | BOOLEAN | Sim | - | Usar verificação de gradiente (gradient checkpointing) para o treinamento (padrão: True). |
| `existing_lora` | COMBO | Sim | Múltiplas opções disponíveis | O LoRA existente ao qual anexar. Defina como None para um novo LoRA (padrão: "[None]"). |

**Observação:** O número de entradas de condicionamento positivo deve corresponder ao número de imagens latentes. Se apenas um condicionamento positivo for fornecido com múltiplas imagens, ele será automaticamente repetido para todas as imagens.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `model_with_lora` | MODEL | O modelo original com o LoRA treinado aplicado. |
| `lora` | LORA_MODEL | Os pesos do LoRA treinado que podem ser salvos ou aplicados a outros modelos. |
| `loss` | LOSS_MAP | Um dicionário contendo os valores de perda de treinamento ao longo do tempo. |
| `steps` | INT | O número total de etapas de treinamento concluídas (incluindo quaisquer etapas anteriores de um LoRA existente). |
