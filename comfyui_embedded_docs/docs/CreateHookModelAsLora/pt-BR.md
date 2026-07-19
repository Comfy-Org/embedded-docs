# Criar Hook Modelo como LoRA

Este nó cria um modelo de hook como um LoRA (Adaptação de Baixa Classificação) carregando pesos de checkpoint e aplicando ajustes de intensidade tanto nos componentes do modelo quanto do CLIP. Ele permite aplicar modificações no estilo LoRA a modelos existentes por meio de uma abordagem baseada em hooks, possibilitando ajuste fino e adaptação sem alterações permanentes no modelo. O nó pode combinar com hooks anteriores e armazena em cache os pesos carregados para maior eficiência.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `ckpt_name` | O arquivo de checkpoint para carregar os pesos (selecione entre os checkpoints disponíveis) | STRING | Sim | Múltiplas opções disponíveis |
| `força_modelo` | O multiplicador de intensidade aplicado aos pesos do modelo (padrão: 1.0) | FLOAT | Sim | -20.0 a 20.0 |
| `força_clip` | O multiplicador de intensidade aplicado aos pesos do CLIP (padrão: 1.0) | FLOAT | Sim | -20.0 a 20.0 |
| `hooks_anteriores` | Hooks anteriores opcionais para combinar com os novos hooks LoRA criados | HOOKS | Não | - |

**Restrições dos Parâmetros:**

- O parâmetro `ckpt_name` carrega checkpoints da pasta de checkpoints disponíveis
- Ambos os parâmetros de intensidade aceitam valores de -20.0 a 20.0 com incrementos de 0.01
- Quando `prev_hooks` não é fornecido, o nó cria um novo grupo de hooks
- O nó armazena em cache os pesos carregados para evitar recarregar o mesmo checkpoint várias vezes

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `HOOKS` | Os hooks LoRA criados, combinados com quaisquer hooks anteriores, se fornecidos | HOOKS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookModelAsLora/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8c0dd6b2e8e99e1d7dbc864aa802c0713842fb0d4ee018ea5cbedfb7896a770d`
