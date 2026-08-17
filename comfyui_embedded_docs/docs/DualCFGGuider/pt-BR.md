# Guia DualCFG

O nó DualCFGGuider cria um sistema de orientação para amostragem de orientação livre de classificador dupla. Ele combina duas entradas de condicionamento positivas com uma entrada de condicionamento negativa, aplicando diferentes escalas de orientação a cada par de condicionamento para controlar o quão fortemente cada prompt influencia a saída gerada.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo a ser usado para orientação. | MODEL | Sim | - |
| `cond1` | A primeira entrada de condicionamento positivo. | CONDITIONING | Sim | - |
| `cond2` | A segunda entrada de condicionamento positivo, tratada como o condicionamento intermediário. | CONDITIONING | Sim | - |
| `negative` | A entrada de condicionamento negativa. | CONDITIONING | Sim | - |
| `cfg_conds` | Escala de orientação aplicada entre `cond1` e `cond2` (padrão: 8.0). | FLOAT | Sim | 0.0 - 100.0 |
| `cfg_cond2_negative` | Escala de orientação aplicada entre `cond2` e o condicionamento negativo (padrão: 8.0). | FLOAT | Sim | 0.0 - 100.0 |
| `style` | O estilo de orientação a aplicar (padrão: "regular"). "regular" combina ambas as escalas de orientação em uma única etapa; "nested" aplica `cfg_conds` primeiro e depois escala o resultado com `cfg_cond2_negative` em relação ao condicionamento negativo. | COMBO | Sim | "regular"<br>"nested" |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `GUIDER` | Um sistema de orientação configurado pronto para uso com amostragem. | GUIDER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCFGGuider/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ef28d109149cb545bcd76215fd99535905c1d395222149a029c1c210e2912e97`
