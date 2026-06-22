# RenormCFG

O nó RenormCFG modifica o processo de orientação livre de classificador (CFG) em modelos de difusão, aplicando normalização e escalonamento condicional. Ele ajusta o processo de remoção de ruído com base em limites de timestep especificados e fatores de renormalização para controlar a influência das previsões condicionais versus não condicionais durante a geração de imagens.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo de difusão ao qual será aplicado o CFG renormalizado | MODEL | Sim | - |
| `cfg_trunc` | Limite de timestep para aplicação do escalonamento CFG. Quando o timestep atual está abaixo deste valor, o escalonamento CFG é aplicado; caso contrário, apenas a previsão condicional é usada (padrão: 100.0) | FLOAT | Não | 0.0 - 100.0 |
| `renorm_cfg` | Fator de renormalização que limita a norma máxima da previsão escalonada por CFG em relação à previsão condicional original. Um valor de 0.0 desativa a renormalização (padrão: 1.0) | FLOAT | Não | 0.0 - 100.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `modelo` | O modelo modificado com a função CFG renormalizada aplicada | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenormCFG/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b59929606f7519574b7ad14a3caacee51e4f141dd6be3abb594217bcfdbc401e`
