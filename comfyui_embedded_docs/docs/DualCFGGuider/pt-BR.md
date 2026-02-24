> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCFGGuider/pt-BR.md)

O nó DualCFGGuider cria um sistema de orientação para amostragem com orientação dupla livre de classificador. Ele combina duas entradas de condicionamento positivo com uma entrada de condicionamento negativo, aplicando diferentes escalas de orientação a cada par de condicionamento para controlar a influência de cada prompt na saída gerada.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo a ser usado para orientação |
| `cond1` | CONDITIONING | Sim | - | A primeira entrada de condicionamento positivo |
| `cond2` | CONDITIONING | Sim | - | A segunda entrada de condicionamento positivo |
| `negative` | CONDITIONING | Sim | - | A entrada de condicionamento negativo |
| `cfg_conds` | FLOAT | Sim | 0.0 - 100.0 | Escala de orientação para o primeiro condicionamento positivo (padrão: 8.0) |
| `cfg_cond2_negative` | FLOAT | Sim | 0.0 - 100.0 | Escala de orientação para o segundo condicionamento positivo e o condicionamento negativo (padrão: 8.0) |
| `style` | COMBO | Sim | "regular"<br>"nested" | O estilo de orientação a ser aplicado (padrão: "regular") |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `GUIDER` | GUIDER | Um sistema de orientação configurado e pronto para uso com amostragem |
