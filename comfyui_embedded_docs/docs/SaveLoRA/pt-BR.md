# Salvar Pesos LoRA

O nó SaveLoRA salva um modelo LoRA (Low-Rank Adaptation) em um arquivo. Ele recebe um modelo LoRA como entrada e o grava em um arquivo `.safetensors` no diretório de saída. Você pode especificar um prefixo para o nome do arquivo e uma contagem opcional de passos para ser incluída no nome final do arquivo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `lora` | O modelo LoRA a ser salvo. Não use o modelo com camadas LoRA. | LORA_MODEL | Sim | N/A |
| `prefixo` | O prefixo a ser usado para o arquivo LoRA salvo (padrão: "loras/ComfyUI_trained_lora"). | STRING | Sim | N/A |
| `etapas` | Opcional: o número de passos para os quais o LoRA foi treinado, usado para nomear o arquivo salvo. | INT | Não | N/A |

**Observação:** A entrada `lora` deve ser um modelo LoRA puro. Não forneça um modelo base que tenha camadas LoRA aplicadas.

**Observação:** O arquivo é salvo no diretório de saída do ComfyUI com a extensão `.safetensors`. O nome do arquivo é composto pelo `prefix` e um contador com zeros à esquerda (5 dígitos) para evitar sobrescrever arquivos existentes. Quando `steps` é fornecido, a contagem de passos também é incluída no nome do arquivo (por exemplo, `1000_steps` para 1000 passos).

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| *None* | Este nó não gera nenhum dado para o fluxo de trabalho. É um nó de saída que salva um arquivo em disco. | N/A |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLoRA/pt-BR.md)

---
**Source fingerprint (SHA-256):** `02f1d15dd7a5181666f2dbf06c45c07b12c4a178985464e07b5f613bd628f906`
