> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetUnionControlNetType/pt-BR.md)

O nó SetUnionControlNetType permite especificar o tipo de rede de controle a ser usada para condicionamento. Ele recebe uma rede de controle existente e define seu tipo de controle com base na sua seleção, criando uma cópia modificada da rede de controle com a configuração de tipo especificada.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `control_net` | CONTROL_NET | Sim | - | A rede de controle a ser modificada com uma nova configuração de tipo |
| `tipo` | STRING | Sim | `"auto"`<br>Todas as chaves UNION_CONTROLNET_TYPES disponíveis | O tipo de rede de controle a ser aplicado. Use "auto" para detecção automática de tipo ou selecione um tipo específico de rede de controle entre as opções disponíveis |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `control_net` | CONTROL_NET | A rede de controle modificada com a configuração de tipo especificada aplicada |

---
**Source fingerprint (SHA-256):** `a64308aec96784f08b6f3f8e96e85f532bd1c536301739e7252b2c7978921b5a`
