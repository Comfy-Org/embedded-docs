# PerpNegGuider

O nó PerpNegGuider cria um sistema de orientação para controlar a geração de imagens usando condicionamento negativo perpendicular. Ele recebe entradas de condicionamento positivo, negativo e vazio e aplica um algoritmo de orientação especializado para direcionar o processo de geração. Este nó foi projetado para testes experimentais e oferece controle refinado sobre a intensidade da orientação e o escalonamento negativo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model` | O modelo a ser usado para a geração da orientação | MODEL | Sim | - |
| `positive` | O condicionamento positivo que guia a geração em direção ao conteúdo desejado | CONDITIONING | Sim | - |
| `negative` | O condicionamento negativo que afasta a geração de conteúdo indesejado | CONDITIONING | Sim | - |
| `empty_conditioning` | O condicionamento vazio ou neutro usado como referência de linha de base | CONDITIONING | Sim | - |
| `cfg` | A escala de orientação livre de classificador que controla o quanto o condicionamento influencia a geração (padrão: 8.0) | FLOAT | Sim | 0.0 - 100.0 |
| `neg_scale` | O fator de escalonamento negativo que ajusta a intensidade do condicionamento negativo (padrão: 1.0) | FLOAT | Sim | 0.0 - 100.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `guider` | Um sistema de orientação configurado pronto para uso no pipeline de geração | GUIDER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerpNegGuider/pt-BR.md)

---
**Source fingerprint (SHA-256):** `efd3f78d461ade9d16885923875bacffb5afeafcbe32fc2d207598e0efe3a8c6`
