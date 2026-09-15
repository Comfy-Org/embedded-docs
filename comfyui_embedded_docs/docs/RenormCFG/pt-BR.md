# RenormCFG

O nó RenormCFG modifica o processo de orientação sem classificador (CFG) em modelos de difusão, aplicando escalonamento condicional e normalização. Ele ajusta o processo de remoção de ruído com base em um limite de timestep especificado e um fator de renormalização, controlando a influência das previsões condicionais versus incondicionais durante a geração de imagens. O modelo resultante é retornado com esse comportamento de CFG modificado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo de difusão ao qual aplicar o CFG renormalizado | MODEL | Sim | - |
| `cfg_trunc` | Limite de timestep para aplicar o escalonamento do CFG. Quando o timestep atual estiver abaixo deste valor, o escalonamento e a renormalização do CFG são aplicados; caso contrário, apenas a previsão condicional é usada (padrão: 100.0) | FLOAT | Não | 0.0 - 100.0 (passo 0.01) |
| `renorm_cfg` | Fator de renormalização que limita a norma máxima da previsão escalonada pelo CFG em relação à previsão condicional original. Um valor de 0.0 desativa a renormalização (padrão: 1.0) | FLOAT | Não | 0.0 - 100.0 (passo 0.01) |

Observação: `cfg_trunc` e `renorm_cfg` são parâmetros avançados. A renormalização só tem efeito quando `renorm_cfg` é maior que 0.0 e o timestep atual está abaixo de `cfg_trunc`; se a norma da nova previsão já estiver abaixo do máximo calculado, nenhum reescalonamento é realizado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo modificado com a função de CFG renormalizada aplicada | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenormCFG/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5925bdfe2d62ef7261d73cda661834102ae6600b1afe53f4093568a6e83ec2ab`
