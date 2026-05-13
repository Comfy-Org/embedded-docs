> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookLora/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookLora/en.md)

O nó Create Hook LoRA gera objetos de hook para aplicar modificações LoRA (Low-Rank Adaptation) em modelos. Ele carrega um arquivo LoRA específico e cria hooks que podem ajustar as forças do modelo e do CLIP, em seguida, combina esses hooks com quaisquer hooks existentes passados para ele. O nó gerencia eficientemente o carregamento de LoRA armazenando em cache arquivos LoRA previamente carregados para evitar operações redundantes.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `lora_name` | STRING | Sim | Múltiplas opções disponíveis | O nome do arquivo LoRA a ser carregado do diretório loras |
| `strength_model` | FLOAT | Sim | -20.0 a 20.0 | O multiplicador de força para ajustes do modelo (padrão: 1.0) |
| `strength_clip` | FLOAT | Sim | -20.0 a 20.0 | O multiplicador de força para ajustes do CLIP (padrão: 1.0) |
| `prev_hooks` | HOOKS | Não | N/A | Grupo de hooks existente opcional para combinar com os novos hooks LoRA |

**Restrições dos Parâmetros:**

- Se tanto `strength_model` quanto `strength_clip` estiverem definidos como 0, o nó pulará a criação de novos hooks LoRA e retornará os hooks existentes inalterados
- O nó armazena em cache o último arquivo LoRA carregado para otimizar o desempenho quando o mesmo LoRA é usado repetidamente

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `HOOKS` | HOOKS | Um grupo de hooks contendo os hooks LoRA combinados e quaisquer hooks anteriores |

---
**Source fingerprint (SHA-256):** `42d5d776bfc9b239191952e2bce23513d183f904fc3c15039469381a547486f8`
