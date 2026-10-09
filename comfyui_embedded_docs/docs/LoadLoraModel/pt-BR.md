# Load LoRA (Model)

Aplique uma pilha de LoRAs a um modelo de difusão em um único nó. Cada linha de `loras` contém um arquivo LoRA, sua força e um interruptor liga/desliga, e as linhas são aplicadas de cima para baixo, de modo que cada linha aplica um patch ao resultado da linha acima. Use este nó em vez de encadear vários carregadores de LoRA individuais quando um fluxo de trabalho aplica uma longa lista de LoRAs ao mesmo modelo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo de difusão ao qual os LoRAs serão aplicados. | MODEL | Sim | - |
| `loras` | Grupo expansível de LoRAs, aplicado ao modelo na ordem das linhas (`loras.0`, `loras.1` e assim por diante). Adicione uma linha por LoRA; cada linha contém um arquivo, uma força e um interruptor liga/desliga. | DYNAMIC_GROUP | Sim | 1 a 20 linhas |

### Campos das linhas de `loras`

Cada linha repete os seguintes campos, e cada campo é obrigatório dentro de uma linha enviada.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `lora_name` | O nome do arquivo LoRA a ser aplicado. | COMBO | Sim | Várias opções disponíveis |
| `strength` | Com que intensidade aplicar este LoRA. `0` desativa, e um valor negativo inverte o efeito. (padrão: 1.0) | FLOAT | Sim | -100 a 100 (passo 0.01) |
| `enabled` | Desative para pular este LoRA sem alterar seu arquivo ou força. (padrão: true) | BOOLEAN | Sim | false / true |

### Restrições dos parâmetros

- **Contagem de linhas:** pelo menos uma linha deve ser enviada e no máximo 20 linhas são aceitas, então o maior índice de linha é 19.
- **Linhas ignoradas:** uma linha é ignorada quando seu arquivo está vazio, quando `enabled` está desativado ou quando `strength` é `0`. Uma força negativa é repassada em vez de ignorada.
- **Ordem das linhas:** as linhas são aplicadas na ordem em que aparecem, e cada linha parte do modelo retornado pela linha anterior.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `MODEL` | O modelo de difusão com cada linha de LoRA habilitada aplicada. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadLoraModel/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a656bba0248d2f6d4eb65e15e3a19f2e76edecd4b34710921a02f3ba5c598e1d`
