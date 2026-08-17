# CFGNorm

CFGNorm aplica uma técnica de normalização ao processo de orientação livre de classificador (CFG) em modelos de difusão. Ela ajusta a escala da previsão com ruído removido comparando as normas das saídas condicional e incondicional e, em seguida, aplica um multiplicador de intensidade para controlar o efeito. Isso ajuda a estabilizar o processo de geração, prevenindo valores extremos na escala da orientação. Quando `pre_cfg` está habilitado, o reescalonamento é aplicado ao ruído combinado antes da combinação CFG do amostrador.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo de difusão ao qual aplicar a normalização CFG | MODEL | Sim | - |
| `strength` | Controla a intensidade do efeito de normalização aplicado à escala CFG (padrão: 1.0) | FLOAT | Sim | 0.0 a 100.0 (passo 0.01) |
| `pre_cfg` | Se verdadeiro, reescala o ruído combinado ANTES da combinação CFG do amostrador, sem limitação (pode amplificar). Corresponde ao CFG com escala normalizada usado por modelos como Lens. O padrão falso mantém o comportamento original pós-CFG no espaço x0, apenas atenuando. (padrão: Falso) | BOOLEAN | Não | Verdadeiro<br>Falso |

Nota: No modo pós-CFG padrão, o fator de reescalonamento é limitado entre 0.0 e 1.0, portanto só pode atenuar (reduzir) a escala da previsão. Quando `pre_cfg` está habilitado, nenhuma limitação é aplicada, então o ruído combinado pode ser amplificado. Nesse modo, um valor de `strength` diferente de 1.0 combina o resultado de volta em direção ao CFG linear padrão.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `patched_model` | Retorna o modelo modificado com a normalização CFG aplicada ao seu processo de amostragem | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGNorm/pt-BR.md)

---
**Source fingerprint (SHA-256):** `427dda498ebda2642489aa2591f063355a77b1e064e0dc7fa8570ed8200c2734`
