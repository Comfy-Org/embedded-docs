> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerpNegGuider/pt-BR.md)

O nó PerpNegGuider cria um sistema de orientação para controlar a geração de imagens usando condicionamento negativo perpendicular. Ele recebe entradas de condicionamento positivo, negativo e vazio e aplica um algoritmo de orientação especializado para direcionar o processo de geração. Este nó foi projetado para fins de teste e oferece controle refinado sobre a força da orientação e a escala negativa.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo a ser usado para a geração da orientação |
| `positive` | CONDITIONING | Sim | - | O condicionamento positivo que orienta a geração em direção ao conteúdo desejado |
| `negative` | CONDITIONING | Sim | - | O condicionamento negativo que orienta a geração para longe de conteúdo indesejado |
| `empty_conditioning` | CONDITIONING | Sim | - | O condicionamento vazio ou neutro usado como referência de base |
| `cfg` | FLOAT | Não | 0.0 - 100.0 | A escala de orientação livre de classificador que controla a intensidade com que o condicionamento influencia a geração (padrão: 8.0) |
| `neg_scale` | FLOAT | Não | 0.0 - 100.0 | O fator de escala negativa que ajusta a força do condicionamento negativo (padrão: 1.0) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `guider` | GUIDER | Um sistema de orientação configurado e pronto para uso no pipeline de geração |
