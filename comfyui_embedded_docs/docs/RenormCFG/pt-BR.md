> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenormCFG/pt-BR.md)

O nó RenormCFG modifica o processo de orientação sem classificador (CFG) em modelos de difusão aplicando escalonamento e normalização condicionais. Ele ajusta o processo de remoção de ruído com base em limites de passo de tempo e fatores de renormalização especificados para controlar a influência das previsões condicionais versus incondicionais durante a geração de imagens.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo de difusão ao qual aplicar o CFG renormalizado |
| `cfg_trunc` | FLOAT | Não | 0.0 - 100.0 | Limite do passo de tempo para aplicar o escalonamento CFG (padrão: 100.0) |
| `renorm_cfg` | FLOAT | Não | 0.0 - 100.0 | Fator de renormalização para controlar a força da orientação condicional (padrão: 1.0) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo modificado com a função CFG renormalizada aplicada |
