O nó ModelComputeDtype altera o tipo de dado computacional (precisão) usado por um modelo durante o processamento. Ele cria uma cópia do modelo de entrada e aplica a configuração de precisão selecionada, o que pode ajudar a otimizar o uso de memória e o desempenho dependendo do seu hardware. Isso é útil para depuração e teste de diferentes configurações de precisão.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo de entrada a ser modificado com um novo tipo de dado computacional | MODEL | Sim | - |
| `dtype` | O tipo de dado computacional a ser aplicado ao modelo (padrão: "default") | STRING | Sim | "default"<br>"fp32"<br>"fp16"<br>"bf16" |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `modelo` | O modelo modificado com o novo tipo de dado computacional aplicado | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelComputeDtype/pt-BR.md)

---
**Source fingerprint (SHA-256):** `bc65f1e452d0122ad175a8b95f38a36503253c9908157037c516496e65c828e6`
