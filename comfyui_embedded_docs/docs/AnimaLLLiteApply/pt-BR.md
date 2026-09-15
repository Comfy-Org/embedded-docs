# Aplicar Anima LLLite

AnimaLLLiteApply aplica um patch de animação leve a um modelo de difusão, permitindo geração imagem para imagem controlada com força e temporização ajustáveis. Ele integra um patch de modelo pré-configurado com uma imagem de entrada e uma máscara opcional, modificando as camadas de atenção e MLP do modelo para influenciar o processo de geração.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo de difusão base ao qual aplicar o patch | MODEL | Sim | |
| `model_patch` | O patch de animação pré-configurado a ser aplicado | MODEL_PATCH | Sim | |
| `imagem` | A imagem de referência para guiar a geração. Apenas os 3 primeiros canais de cor (RGB) são usados | IMAGE | Sim | |
| `intensidade` | A força do efeito do patch (padrão: 1.0, passo: 0.01) | FLOAT | Sim | -10.0 a 10.0 |
| `percentual_inicial` | A porcentagem do processo de remoção de ruído em que o patch começa a fazer efeito (padrão: 0.0, passo: 0.001) | FLOAT | Sim | 0.0 a 1.0 |
| `percentual_final` | A porcentagem do processo de remoção de ruído em que o patch para de fazer efeito (padrão: 1.0, passo: 0.001) | FLOAT | Sim | 0.0 a 1.0 |
| `mask` | Uma máscara opcional para limitar o efeito do patch a áreas específicas da imagem | MASK | Não | |

**Nota sobre restrições de parâmetros:** Se o `model_patch` tiver 4 canais de entrada e nenhuma `mask` for fornecida, uma máscara zero será criada automaticamente para corresponder às dimensões da imagem. Se o `model_patch` não tiver 4 canais de entrada, o parâmetro `mask` será ignorado e definido como `None`. Apenas os 3 primeiros canais de cor da imagem de entrada são usados. Este nó está marcado como experimental no ComfyUI.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `MODEL` | O modelo de difusão modificado com o patch de animação aplicado | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AnimaLLLiteApply/pt-BR.md)

---
**Source fingerprint (SHA-256):** `48e455b767509a5a8c329365d5ffded86d6f4545d575c9fdc5ffbaf4da7c2287`
