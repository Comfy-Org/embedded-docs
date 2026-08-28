# RenormCFG

O nó RenormCFG modifica o processo de orientação livre de classificador (CFG) em modelos de difusão aplicando escala e normalização condicionais. Ele ajusta o processo de remoção de ruído com base em limites de etapas de tempo especificados e fatores de renormalização para controlar a influência das previsões condicionais versus incondicionais durante a geração de imagens.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo de difusão ao qual aplicar o CFG renormalizado | MODEL | Sim | - |
| `cfg_trunc` | Limite de etapa de tempo para aplicar o ajuste de CFG. Quando a etapa de tempo atual está abaixo desse valor, o ajuste de CFG é aplicado; caso contrário, apenas a previsão condicional é usada (padrão: 100.0) | FLOAT | Não | 0.0 - 100.0 |
| `renorm_cfg` | Fator de renormalização que limita a norma máxima da previsão ajustada por CFG em relação à previsão condicional original. Um valor de 0.0 desativa a renormalização (padrão: 1.0) | FLOAT | Não | 0.0 - 100.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo modificado com a função CFG renormalizada aplicada | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenormCFG/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5925bdfe2d62ef7261d73cda661834102ae6600b1afe53f4093568a6e83ec2ab`
