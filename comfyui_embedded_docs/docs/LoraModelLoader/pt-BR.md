> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraModelLoader/pt-BR.md)

O nó LoraModelLoader aplica pesos de LoRA (Adaptação de Baixa Classificação) treinados a um modelo de difusão. Ele modifica o modelo base carregando pesos de LoRA de um modelo LoRA treinado e ajustando sua intensidade de influência. Isso permite personalizar o comportamento de modelos de difusão sem precisar retreiná-los do zero.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `modelo` | MODEL | Sim | - | O modelo de difusão ao qual o LoRA será aplicado. |
| `lora` | LORA_MODEL | Sim | - | O modelo LoRA a ser aplicado ao modelo de difusão. |
| `força_modelo` | FLOAT | Sim | -100.0 a 100.0 | O quão fortemente modificar o modelo de difusão. Este valor pode ser negativo (padrão: 1.0). |
| `bypass` | BOOLEAN | Sim | Verdadeiro ou Falso | Quando ativado, aplica o LoRA em modo de bypass sem modificar os pesos do modelo base. Útil para treinamento e quando os pesos do modelo são descarregados (padrão: Falso). |

**Nota:** Quando `strength_model` é definido como 0, o nó retorna o modelo original sem aplicar nenhuma modificação do LoRA.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `modelo` | MODEL | O modelo de difusão modificado com os pesos do LoRA aplicados. |

---
**Source fingerprint (SHA-256):** `82afa7dbbc990f1a9f202f920aaf8fad7fe69dc35e75ed8a95eb63c9dec74961`
