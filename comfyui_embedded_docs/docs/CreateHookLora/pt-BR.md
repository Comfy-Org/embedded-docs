> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookLora/pt-BR.md)

O nó Create Hook LoRA gera objetos de hook para aplicar modificações LoRA (Low-Rank Adaptation) a modelos. Ele carrega um arquivo LoRA especificado e cria hooks que podem ajustar as intensidades do modelo e do CLIP, depois combina esses hooks com quaisquer hooks existentes passados para ele. O nó gerencia o carregamento de LoRA de forma eficiente, armazenando em cache arquivos LoRA previamente carregados para evitar operações redundantes.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `lora_name` | STRING | Sim | Múltiplas opções disponíveis | O nome do arquivo LoRA a ser carregado do diretório de loras |
| `strength_model` | FLOAT | Sim | -20.0 a 20.0 | O multiplicador de intensidade para ajustes do modelo (padrão: 1.0) |
| `strength_clip` | FLOAT | Sim | -20.0 a 20.0 | O multiplicador de intensidade para ajustes do CLIP (padrão: 1.0) |
| `prev_hooks` | HOOKS | Não | N/A | Grupo de hooks existente opcional para combinar com os novos hooks LoRA |

**Restrições dos Parâmetros:**

- Se tanto `strength_model` quanto `strength_clip` forem definidos como 0, o nó ignorará a criação de novos hooks LoRA e retornará os hooks existentes inalterados
- O nó armazena em cache o último arquivo LoRA carregado para otimizar o desempenho quando o mesmo LoRA é usado repetidamente

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `HOOKS` | HOOKS | Um grupo de hooks contendo os hooks LoRA combinados e quaisquer hooks anteriores |
