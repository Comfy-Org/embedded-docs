> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookModelAsLora/pt-BR.md)

Este nó cria um modelo de hook como um LoRA (Adaptação de Baixa Classificação) carregando pesos de checkpoint e aplicando ajustes de força aos componentes do modelo e do CLIP. Ele permite que você aplique modificações no estilo LoRA a modelos existentes por meio de uma abordagem baseada em hooks, possibilitando ajustes finos e adaptações sem alterações permanentes no modelo. O nó pode combinar com hooks anteriores e armazena em cache os pesos carregados para eficiência.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `ckpt_name` | COMBO | Sim | Múltiplas opções disponíveis | O arquivo de checkpoint do qual carregar os pesos (selecione entre os checkpoints disponíveis) |
| `strength_model` | FLOAT | Sim | -20.0 a 20.0 | O multiplicador de força aplicado aos pesos do modelo (padrão: 1.0) |
| `strength_clip` | FLOAT | Sim | -20.0 a 20.0 | O multiplicador de força aplicado aos pesos do CLIP (padrão: 1.0) |
| `prev_hooks` | HOOKS | Não | - | Hooks anteriores opcionais para combinar com os novos hooks LoRA criados |

**Restrições dos Parâmetros:**

- O parâmetro `ckpt_name` carrega checkpoints da pasta de checkpoints disponíveis
- Ambos os parâmetros de força aceitam valores de -20.0 a 20.0 com incrementos de 0.01
- Quando `prev_hooks` não é fornecido, o nó cria um novo grupo de hooks
- O nó armazena em cache os pesos carregados para evitar recarregar o mesmo checkpoint várias vezes

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `HOOKS` | HOOKS | Os hooks LoRA criados, combinados com quaisquer hooks anteriores, se fornecidos |
