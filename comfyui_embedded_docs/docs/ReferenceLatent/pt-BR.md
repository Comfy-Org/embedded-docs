> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceLatent/pt-BR.md)

Este nó define a latente guia para um modelo de edição. Ele recebe dados de condicionamento e uma entrada latente opcional, em seguida, modifica o condicionamento para incluir informações de latente de referência. Se o modelo suportar, você pode encadear vários nós ReferenceLatent para definir várias imagens de referência.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `conditioning` | CONDITIONING | Sim | - | Os dados de condicionamento a serem modificados com informações de latente de referência |
| `latent` | LATENT | Não | - | Dados latentes opcionais para usar como referência para o modelo de edição |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | CONDITIONING | Os dados de condicionamento modificados contendo informações de latente de referência |

---
**Source fingerprint (SHA-256):** `d233778cfa7d6f057509f93f8445a0bbf151308e430fc50e28577f48cf136b53`
