> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BasicGuider/pt-BR.md)

O nó BasicGuider cria um mecanismo de orientação simples para o processo de amostragem. Ele recebe um modelo e dados de condicionamento como entradas e produz um objeto guia que pode ser usado para orientar o processo de geração durante a amostragem. Este nó fornece a funcionalidade de orientação fundamental necessária para a geração controlada.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `modelo` | MODEL | Sim | - | O modelo a ser usado para orientação |
| `condicionamento` | CONDITIONING | Sim | - | Os dados de condicionamento que orientam o processo de geração |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `GUIDER` | GUIDER | Um objeto guia que pode ser usado durante o processo de amostragem para orientar a geração |

---
**Source fingerprint (SHA-256):** `012171caea6aacfadaabacb746be104ca783ae5ea5834cc4a67088233b835654`
