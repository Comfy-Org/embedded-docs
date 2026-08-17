# Salvar Pesos LoRA

O nó SaveLoRA salva um modelo LoRA (Adaptação de Baixo Posto) em um arquivo. Ele grava o modelo LoRA como um arquivo `.safetensors` no diretório de saída. Você pode especificar um prefixo para o nome do arquivo e uma contagem opcional de etapas; quando fornecida, a contagem de etapas é incluída no nome do arquivo salvo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `lora` | O modelo LoRA a ser salvo. Não use o modelo com camadas LoRA. | LORA_MODEL | Sim | N/A |
| `prefix` | O prefixo a ser usado para o arquivo LoRA salvo (padrão: "loras/ComfyUI_trained_lora"). | STRING | Sim | N/A |
| `steps` | Opcional: o número de etapas para o qual o LoRA foi treinado, usado para nomear o arquivo salvo. | INT | Não | N/A |

**Nota:** A entrada `lora` deve ser um modelo LoRA puro. Não forneça um modelo base com camadas LoRA aplicadas.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| *None* | Este nó não envia nenhum dado para o fluxo de trabalho. É um nó de saída que salva um arquivo em disco. | N/A |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLoRA/pt-BR.md)

---
**Source fingerprint (SHA-256):** `02f1d15dd7a5181666f2dbf06c45c07b12c4a178985464e07b5f613bd628f906`
