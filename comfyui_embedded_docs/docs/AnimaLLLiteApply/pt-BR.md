# AnimaLLLiteApply

Este nó aplica um patch de animação leve a um modelo de difusão, permitindo a geração controlada de imagem para imagem com intensidade e temporização ajustáveis. Ele integra um patch de modelo pré-configurado com uma imagem de entrada e uma máscara opcional, modificando as camadas de atenção e MLP do modelo para influenciar o processo de geração.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|--------------|-------------|-------|
| `model` | O modelo de difusão base no qual aplicar o patch | MODEL | Sim | |
| `model_patch` | O patch de animação pré-configurado a ser aplicado | MODEL_PATCH | Sim | |
| `image` | A imagem de referência para guiar a geração | IMAGE | Sim | |
| `strength` | A intensidade do efeito do patch (padrão: 1.0) | FLOAT | Sim | -10.0 a 10.0 |
| `start_percent` | A porcentagem do processo de remoção de ruído na qual o patch começa a fazer efeito (padrão: 0.0) | FLOAT | Sim | 0.0 a 1.0 |
| `end_percent` | A porcentagem do processo de remoção de ruído na qual o patch para de fazer efeito (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `mask` | Uma máscara opcional para limitar o efeito do patch a áreas específicas da imagem | MASK | Não | |

**Observação sobre restrições de parâmetros:** Se o `model_patch` tiver 4 canais de entrada e nenhuma `mask` for fornecida, uma máscara zero é criada automaticamente para corresponder às dimensões da imagem. Se o `model_patch` não tiver 4 canais de entrada, o parâmetro `mask` é ignorado e definido como `None`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-------------|--------------|
| `MODEL` | O modelo de difusão com patch aplicado, contendo o patch de animação | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AnimaLLLiteApply/pt-BR.md)

---
**Source fingerprint (SHA-256):** `291dc6a6619faab1c1100110c71c47381addcd80dbaf933dd8025a376bc2bee7`
