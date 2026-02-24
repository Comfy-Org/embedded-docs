> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanRefinerLatent/pt-BR.md)

O nó HunyuanRefinerLatent processa condicionamentos e entradas latentes para operações de refinamento. Ele aplica aumento de ruído tanto ao condicionamento positivo quanto ao negativo, incorporando dados de imagem latente, e gera uma nova saída latente com dimensões específicas para processamento posterior.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sim | - | A entrada de condicionamento positivo a ser processada |
| `negative` | CONDITIONING | Sim | - | A entrada de condicionamento negativo a ser processada |
| `latent` | LATENT | Sim | - | A entrada de representação latente |
| `noise_augmentation` | FLOAT | Sim | 0.0 - 1.0 | A quantidade de aumento de ruído a ser aplicada (padrão: 0.10) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | O condicionamento positivo processado, com aumento de ruído aplicado e concatenação da imagem latente |
| `negative` | CONDITIONING | O condicionamento negativo processado, com aumento de ruído aplicado e concatenação da imagem latente |
| `latent` | LATENT | Uma nova saída latente com dimensões [batch_size, 32, altura, largura, canais] |
