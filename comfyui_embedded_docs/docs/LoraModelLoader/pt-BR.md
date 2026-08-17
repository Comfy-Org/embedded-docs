# Carregar Modelo LoRA

O nó LoraModelLoader aplica pesos LoRA (Low-Rank Adaptation) treinados a um modelo de difusão. Ele modifica o modelo base carregando pesos LoRA de um modelo LoRA treinado e ajustando sua força de influência. Isso permite personalizar o comportamento de modelos de difusão sem retreiná-los do zero.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo de difusão ao qual o LoRA será aplicado. | MODEL | Sim | - |
| `lora` | O modelo LoRA a ser aplicado ao modelo de difusão. | LORA_MODEL | Sim | - |
| `strength_model` | O quanto modificar o modelo de difusão. Este valor pode ser negativo (padrão: 1.0). | FLOAT | Sim | -100.0 a 100.0 |
| `bypass` | Quando ativado, aplica o LoRA no modo bypass sem modificar os pesos do modelo base. Útil para treinamento e quando os pesos do modelo são descarregados (padrão: False). | BOOLEAN | Sim | True ou False |

**Observação:** Quando `strength_model` é definido como 0, o nó retorna o modelo original sem aplicar nenhuma modificação LoRA.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `model` | O modelo de difusão modificado. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraModelLoader/pt-BR.md)

---
**Source fingerprint (SHA-256):** `81eb2a9b0376fe7453f6e7e422414472e80a3d1b92bb6874b91df6de8aed0d9a`
