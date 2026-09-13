# Guia DualCFG

O nó Dual CFG Guider cria um sistema de orientação para amostragem que usa duas entradas de condicionamento junto com uma entrada de condicionamento negativo. Ele aplica duas escalas de orientação separadas para controlar quão fortemente cada condicionamento influencia o resultado gerado, e oferece suporte a duas formas de combinar essas escalas: "regular" e "nested".

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo a ser usado para orientação | MODEL | Sim | - |
| `cond1` | A primeira entrada de condicionamento positivo | CONDITIONING | Sim | - |
| `cond2` | A segunda entrada de condicionamento, usada como referência entre o primeiro condicionamento positivo e o condicionamento negativo | CONDITIONING | Sim | - |
| `negative` | A entrada de condicionamento negativo | CONDITIONING | Sim | - |
| `cfg_conds` | Escala de orientação aplicada ao primeiro condicionamento positivo (padrão: 8.0) | FLOAT | Sim | 0.0 - 100.0 |
| `cfg_cond2_negative` | Escala de orientação aplicada entre o segundo condicionamento e o condicionamento negativo (padrão: 8.0) | FLOAT | Sim | 0.0 - 100.0 |
| `style` | O estilo de orientação a aplicar (padrão: "regular"). Quando definido como "nested", a orientação é aplicada de forma aninhada | COMBO | Sim | "regular"<br>"nested" |

Nota: No estilo `regular`, `cfg_cond2_negative` é aplicado entre `cond2` e `negative`, e `cfg_conds` é aplicado entre `cond1` e `cond2`. No estilo `nested`, `cfg_conds` é aplicado primeiro entre `cond1` e `cond2`, e a previsão resultante é então orientada para longe de `negative` usando `cfg_cond2_negative`.

Nota: No estilo `regular`, quando `cfg_cond2_negative` é igual a 1.0, o condicionamento negativo é ignorado, e quando `cfg_conds` também é igual a 1.0, o segundo condicionamento também é ignorado. Isso reduz o número de avaliações do modelo realizadas.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `GUIDER` | Um sistema de orientação configurado e pronto para uso com amostragem | GUIDER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCFGGuider/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ef28d109149cb545bcd76215fd99535905c1d395222149a029c1c210e2912e97`
