# ModelComputeDtype

O nó ModelComputeDtype altera o tipo de dados computacional (precisão) usado por um modelo durante o processamento. Ele cria uma cópia do modelo de entrada e aplica a configuração de precisão selecionada, o que pode ajudar a otimizar o uso de memória e o desempenho dependendo do seu hardware. Isso é útil para depurar e testar diferentes configurações de precisão.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model` | O modelo de entrada a ser modificado com um novo tipo de dados computacional | MODEL | Sim | - |
| `dtype` | O tipo de dados computacional a ser aplicado ao modelo (padrão: "default"). Este parâmetro é marcado como uma configuração avançada na interface do usuário. | COMBO | Sim | "default"<br>"fp32"<br>"fp16"<br>"bf16" |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo modificado com o novo tipo de dados computacional aplicado | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelComputeDtype/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ad9c39e1217fd2e343ad4f49df9d1acabbc4708966dadec5340bb975adb59854`
