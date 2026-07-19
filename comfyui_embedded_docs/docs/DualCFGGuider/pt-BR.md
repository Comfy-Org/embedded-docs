# Guia DualCFG

O nó DualCFGGuider cria um sistema de orientação para amostragem dupla com orientação livre de classificador. Ele combina duas entradas de condicionamento positivo com uma entrada de condicionamento negativo, aplicando diferentes escalas de orientação a cada par de condicionamento para controlar a influência de cada prompt na saída gerada.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo a ser usado para orientação | MODEL | Sim | - |
| `cond1` | A primeira entrada de condicionamento positivo | CONDITIONING | Sim | - |
| `cond2` | A segunda entrada de condicionamento positivo | CONDITIONING | Sim | - |
| `negativo` | A entrada de condicionamento negativo | CONDITIONING | Sim | - |
| `cfg_conds` | Escala de orientação para o primeiro condicionamento positivo (padrão: 8.0) | FLOAT | Sim | 0.0 - 100.0 |
| `cfg_cond2_negativo` | Escala de orientação para o segundo condicionamento positivo e negativo (padrão: 8.0) | FLOAT | Sim | 0.0 - 100.0 |
| `estilo` | O estilo de orientação a ser aplicado (padrão: "regular"). Quando definido como "nested", a orientação é aplicada de forma aninhada | COMBO | Sim | "regular"<br>"nested" |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `GUIDER` | Um sistema de orientação configurado pronto para uso com amostragem | GUIDER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCFGGuider/pt-BR.md)

---
**Source fingerprint (SHA-256):** `802e07f2e64dc2d55e86290db7e94dffd46079a9180480a560035d0bb6350325`
