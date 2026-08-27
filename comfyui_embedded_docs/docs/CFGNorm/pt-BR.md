# CFGNorm

CFGNorm aplica uma técnica de normalização ao processo de orientação sem classificador (CFG) em modelos de difusão. Ele ajusta a escala da predição denoised ao comparar as normas das saídas condicional e incondicional e, em seguida, aplica um multiplicador de intensidade para controlar o efeito. Por padrão, a normalização apenas atenua a saída da orientação, mas habilitar `pre_cfg` reescala o ruído combinado antes da combinação CFG do amostrador, sem limitação de faixa, o que pode amplificar.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo de difusão ao qual aplicar a normalização CFG | MODEL | Sim | - |
| `força` | Controla a intensidade do efeito de normalização aplicado à escala do CFG (padrão: 1.0) | FLOAT | Sim | 0.0 a 100.0 |
| `pre_cfg` | Se true, reescala o ruído combinado ANTES da combinação CFG do amostrador, sem limitação (pode amplificar). Corresponde ao CFG com escala de norma usado por modelos como Lens. O padrão false mantém o comportamento original de pós-CFG no espaço x0, com apenas atenuação. (padrão: False) | BOOLEAN | Não | true / false |

Nota: Este nó está marcado como experimental.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `modelo_patchado` | Retorna o modelo modificado com a normalização CFG aplicada ao seu processo de amostragem | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGNorm/pt-BR.md)

---
**Source fingerprint (SHA-256):** `427dda498ebda2642489aa2591f063355a77b1e064e0dc7fa8570ed8200c2734`
