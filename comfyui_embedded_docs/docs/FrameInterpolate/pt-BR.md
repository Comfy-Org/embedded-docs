# Interpolação de Quadros

O nó Frame Interpolate cria novos quadros entre os existentes em uma sequência de imagens, aumentando efetivamente a taxa de quadros. Ele usa um modelo de IA para prever como os quadros intermediários devem se parecer, o que pode ser usado para criar efeitos suaves de câmera lenta ou para aumentar a suavidade de um vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `interp_model` | O modelo de interpolação de quadros a ser usado para gerar quadros intermediários | INTERP_MODEL | Sim | - |
| `imagens` | Um lote de imagens consecutivas (quadros) para interpolar. Requer pelo menos 2 imagens. Se forem fornecidos menos de 2 quadros, o nó retorna as imagens de entrada inalteradas. | IMAGE | Sim | - |
| `multiplicador` | O número de vezes para multiplicar a contagem de quadros. Por exemplo, um multiplicador de 2 dobra o número de quadros. (padrão: 2) | INT | Sim | 2 a 16 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `IMAGE` | Um novo lote de imagens com os quadros interpolados inseridos entre os quadros originais, resultando em uma sequência mais suave. O número total de quadros de saída é `(number of input frames - 1) * multiplier + 1`. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolate/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e0b9dd6ec3b09e665bcc0f95d2b7a0209d9045ba9b96828e46f126e6914f049c`
