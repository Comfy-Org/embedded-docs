# Interpolação de Quadros

## Visão Geral

O nó de Interpolação de Quadros cria novos quadros entre os existentes em uma sequência de imagens, aumentando efetivamente a taxa de quadros. Ele utiliza um modelo de IA para prever como devem ser os quadros intermediários, podendo ser usado para criar efeitos de câmera lenta suaves ou aumentar a suavidade de um vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `interp_model` | O modelo de interpolação de quadros a ser usado para gerar quadros intermediários | MODEL | Sim | - |
| `imagens` | Um lote de imagens consecutivas (quadros) para interpolar. Requer pelo menos 2 imagens. | IMAGE | Sim | - |
| `multiplicador` | O número de vezes para multiplicar a contagem de quadros. Por exemplo, um multiplicador de 2 dobra o número de quadros. (padrão: 2) | INT | Sim | 2 a 16 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `IMAGE` | Um novo lote de imagens com os quadros interpolados inseridos entre os quadros originais, resultando em uma sequência mais suave. O número total de quadros de saída é `(número de quadros de entrada - 1) * multiplicador + 1`. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolate/pt-BR.md)

---
**Source fingerprint (SHA-256):** `05fdac188d9d7c7d5cac9ade55ba22cc743395b3c659a519ca03fe293b9a6e34`
