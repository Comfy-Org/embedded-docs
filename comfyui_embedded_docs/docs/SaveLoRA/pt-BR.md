> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLoRA/pt-BR.md)

O nó SaveLoRA salva um modelo LoRA (Adaptação de Baixa Classificação) em um arquivo. Ele recebe um modelo LoRA como entrada e o grava em um arquivo `.safetensors` no diretório de saída. Você pode especificar um prefixo para o nome do arquivo e, opcionalmente, um número de etapas a ser incluído no nome final do arquivo.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `lora` | LORA_MODEL | Sim | N/A | O modelo LoRA a ser salvo. Não use o modelo com camadas LoRA. |
| `prefixo` | STRING | Sim | N/A | O prefixo a ser usado para o arquivo LoRA salvo (padrão: "loras/ComfyUI_trained_lora"). |
| `etapas` | INT | Não | N/A | Opcional: O número de etapas em que o LoRA foi treinado, usado para nomear o arquivo salvo. |

**Observação:** A entrada `lora` deve ser um modelo LoRA puro. Não forneça um modelo base que tenha camadas LoRA aplicadas a ele.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| *Nenhum* | N/A | Este nó não produz nenhum dado para o fluxo de trabalho. É um nó de saída que salva um arquivo em disco. |

---
**Source fingerprint (SHA-256):** `e68a449d741c908f23fc1585d848254d78c310ad19efbd139c33c9ddef3145c7`
