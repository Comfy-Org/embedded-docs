> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmosPredict2_14B/pt-BR.md)

O nó ModelMergeCosmosPredict2_14B permite mesclar dois modelos de IA ajustando a influência de diferentes componentes dos modelos. Ele oferece controle refinado sobre quanto cada parte do segundo modelo contribui para o modelo mesclado final, usando pesos de mistura para camadas e componentes específicos do modelo.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Sim | - | O modelo base para mesclar |
| `model2` | MODEL | Sim | - | O modelo secundário a ser mesclado no modelo base |
| `pos_embedder.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do incorporador de posição (padrão: 1.0) |
| `x_embedder.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do incorporador de entrada (padrão: 1.0) |
| `t_embedder.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do incorporador de tempo (padrão: 1.0) |
| `t_embedding_norm.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura da normalização da incorporação de tempo (padrão: 1.0) |
| `blocks.0.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do Bloco 0 (padrão: 1.0) |
| `blocks.1.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do Bloco 1 (padrão: 1.0) |
| `blocks.2.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do Bloco 2 (padrão: 1.0) |
| `blocks.3.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do Bloco 3 (padrão: 1.0) |
| `blocks.4.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do Bloco 4 (padrão: 1.0) |
| `blocks.5.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do Bloco 5 (padrão: 1.0) |
| `blocks.6.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do Bloco 6 (padrão: 1.0) |
| `blocks.7.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do Bloco 7 (padrão: 1.0) |
| `blocks.8.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do Bloco 8 (padrão: 1.0) |
| `blocks.9.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do Bloco 9 (padrão: 1.0) |
| `blocks.10.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do Bloco 10 (padrão: 1.0) |
| `blocks.11.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do Bloco 11 (padrão: 1.0) |
| `blocks.12.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do Bloco 12 (padrão: 1.0) |
| `blocks.13.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do Bloco 13 (padrão: 1.0) |
| `blocks.14.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do Bloco 14 (padrão: 1.0) |
| `blocks.15.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do Bloco 15 (padrão: 1.0) |
| `blocks.16.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do Bloco 16 (padrão: 1.0) |
| `blocks.17.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do Bloco 17 (padrão: 1.0) |
| `blocks.18.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do Bloco 18 (padrão: 1.0) |
| `blocks.19.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do Bloco 19 (padrão: 1.0) |
| `blocks.20.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do Bloco 20 (padrão: 1.0) |
| `blocks.21.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do Bloco 21 (padrão: 1.0) |
| `blocks.22.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do Bloco 22 (padrão: 1.0) |
| `blocks.23.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do Bloco 23 (padrão: 1.0) |
| `blocks.24.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do Bloco 24 (padrão: 1.0) |
| `blocks.25.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do Bloco 25 (padrão: 1.0) |
| `blocks.26.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do Bloco 26 (padrão: 1.0) |
| `blocks.27.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do Bloco 27 (padrão: 1.0) |
| `blocks.28.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do Bloco 28 (padrão: 1.0) |
| `blocks.29.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do Bloco 29 (padrão: 1.0) |
| `blocks.30.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do Bloco 30 (padrão: 1.0) |
| `blocks.31.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do Bloco 31 (padrão: 1.0) |
| `blocks.32.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do Bloco 32 (padrão: 1.0) |
| `blocks.33.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do Bloco 33 (padrão: 1.0) |
| `blocks.34.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do Bloco 34 (padrão: 1.0) |
| `blocks.35.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do Bloco 35 (padrão: 1.0) |
| `final_layer.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura da camada final (padrão: 1.0) |

**Observação:** Todos os parâmetros de peso de mistura aceitam valores entre 0.0 e 1.0, onde 0.0 significa nenhuma contribuição do `model2` e 1.0 significa contribuição total do `model2` para aquele componente específico.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo mesclado que combina características de ambos os modelos de entrada |
