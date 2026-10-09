# Load LoRA (Text Encoder)

Aplique uma pilha de LoRAs a um codificador de texto CLIP em um único nó. Cada linha de `loras` contém um arquivo LoRA, sua força e um interruptor de ativar/desativar, e as linhas são aplicadas de cima para baixo, de modo que cada linha aplica um patch ao resultado da linha acima. Arquivos LoRA que alteram o codificador de texto geralmente também são aplicados ao modelo, então este nó normalmente é usado em conjunto com Load LoRA (Model) utilizando as mesmas linhas.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `clip` | O codificador de texto CLIP ao qual os LoRAs serão aplicados. | CLIP | Sim | - |
| `loras` | Grupo expansível de LoRAs, aplicados ao codificador de texto na ordem das linhas (`loras.0`, `loras.1` e assim por diante). Adicione uma linha por LoRA; cada linha contém um arquivo, uma força e um interruptor de ativar/desativar. | DYNAMIC_GROUP | Sim | 1 a 20 linhas |

### Campos da linha de `loras`

Cada linha repete os seguintes campos, e cada campo é obrigatório dentro de uma linha enviada.

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `lora_name` | O nome do arquivo LoRA a aplicar. | COMBO | Sim | Múltiplas opções disponíveis |
| `strength` | Com que intensidade aplicar este LoRA ao codificador de texto. `0` o desativa, e um valor negativo inverte o efeito. (padrão: 1.0) | FLOAT | Sim | -100 a 100 (passo 0.01) |
| `enabled` | Desative para ignorar este LoRA sem alterar seu arquivo ou sua força. (padrão: true) | BOOLEAN | Sim | false / true |

### Restrições de parâmetros

- **Número de linhas:** pelo menos uma linha deve ser enviada e no máximo 20 linhas são aceitas, portanto o maior índice de linha é 19.
- **Linhas ignoradas:** uma linha é ignorada quando seu arquivo está vazio, quando `enabled` está desativado ou quando `strength` é `0`. Uma força negativa é repassada em vez de ignorada.
- **Ordem das linhas:** as linhas são aplicadas na ordem em que aparecem, e cada linha parte do codificador de texto retornado pela linha anterior.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `CLIP` | O codificador de texto CLIP com todas as linhas de LoRA habilitadas aplicadas. | CLIP |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadLoraTextEncoder/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0b290d2caddc3937e962e65c70a5c99cbd4cdb40ab6f86bba8f0c270e5cebf00`
