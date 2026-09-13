# CFGNorm

CFGNorm ajusta como a orientação livre de classificador (CFG) é aplicada em modelos de difusão ao comparar o tamanho (norma) da previsão condicional com a previsão guiada e reescalonar o resultado. Um valor de `strength` controla quanto do ajuste é aplicado. Por padrão, o escalonamento apenas atenua a saída de orientação, enquanto habilitar `pre_cfg` reescalona o ruído combinado antes da combinação CFG do amostrador, sem clamping, o que pode amplificar o resultado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo de difusão ao qual aplicar a normalização de CFG | MODEL | Sim | - |
| `strength` | Controla a intensidade do efeito de normalização aplicado ao escalonamento CFG (padrão: 1.0) | FLOAT | Sim | 0.0 a 100.0 (passo 0.01) |
| `pre_cfg` | Se true, reescalona o ruído combinado ANTES da combinação CFG do amostrador, sem clamping (pode amplificar). Corresponde ao CFG com escala por norma usado por modelos como Lens. O padrão false mantém o comportamento original pós-CFG no espaço x0 de apenas atenuação. (padrão: False) | BOOLEAN | Não | true / false |

Observação: Este nó está marcado como experimental.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `patched_model` | Retorna o modelo modificado com a normalização de CFG aplicada ao seu processo de amostragem | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGNorm/pt-BR.md)

---
**Source fingerprint (SHA-256):** `427dda498ebda2642489aa2591f063355a77b1e064e0dc7fa8570ed8200c2734`
