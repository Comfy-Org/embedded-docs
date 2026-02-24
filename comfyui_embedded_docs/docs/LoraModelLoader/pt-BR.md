> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraModelLoader/pt-BR.md)

O nó LoraModelLoader aplica pesos LoRA (Low-Rank Adaptation) treinados a um modelo de difusão. Ele modifica o modelo base carregando os pesos de um modelo LoRA treinado e ajustando a intensidade de sua influência. Isso permite personalizar o comportamento dos modelos de difusão sem a necessidade de retreiná-los do zero.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo de difusão ao qual o LoRA será aplicado. |
| `lora` | LORA_MODEL | Sim | - | O modelo LoRA a ser aplicado ao modelo de difusão. |
| `strength_model` | FLOAT | Sim | -100.0 a 100.0 | A intensidade com que o modelo de difusão será modificado. Este valor pode ser negativo (padrão: 1.0). |

**Observação:** Quando `strength_model` é definido como 0, o nó retorna o modelo original sem aplicar nenhuma modificação LoRA.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo de difusão modificado com os pesos LoRA aplicados. |
