> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetUnionControlNetType/pt-BR.md)

O nó SetUnionControlNetType permite que você especifique o tipo de rede de controle a ser usado para o condicionamento. Ele recebe uma rede de controle existente e define seu tipo de controle com base na sua seleção, criando uma cópia modificada da rede de controle com a configuração de tipo especificada.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `control_net` | CONTROL_NET | Sim | - | A rede de controle a ser modificada com uma nova configuração de tipo |
| `type` | STRING | Sim | `"auto"`<br>Todas as chaves UNION_CONTROLNET_TYPES disponíveis | O tipo de rede de controle a aplicar. Use "auto" para detecção automática de tipo ou selecione um tipo de rede de controle específico dentre as opções disponíveis |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `control_net` | CONTROL_NET | A rede de controle modificada com a configuração de tipo especificada aplicada |
