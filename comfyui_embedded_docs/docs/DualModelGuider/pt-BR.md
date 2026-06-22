# Orientador CFG de Dois Modelos

Este nó permite usar dois modelos diferentes durante o processo de amostragem guiada por CFG: um modelo para a passagem positiva (condicional) e um modelo separado para a passagem negativa (incondicional). Quando nenhum modelo negativo é fornecido, ele se comporta como um guia CFG padrão usando um único modelo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-----------|---------------|-------------|-------|
| `modelo` | Modelo usado para a passagem positiva (condicional). | MODEL | Sim | |
| `modelo_negativo` | Modelo usado para a passagem negativa (incondicional). Use o mesmo modelo para CFG comum. | MODEL | Não | |
| `positivo` | A entrada de condicionamento positivo. | CONDITIONING | Sim | |
| `cfg` | O valor da escala CFG (padrão: 4.0). | FLOAT | Sim | 0.0 a 100.0 (passo: 0.1) |
| `negativo` | Condicionamento negativo executado no modelo negativo. Deixe desconectado para uma passagem incondicional sem texto (apenas imagem). | CONDITIONING | Não | |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-----------|---------------|
| `GUIDER` | Um objeto guia configurado com os modelos e condicionamentos especificados para uso na amostragem. | GUIDER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualModelGuider/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a60803156e98d2ffe975d39922dfbeacafd1a2155d88dd2e285ac1426a1e7a33`
