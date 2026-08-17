# Interpolação de Quadros

O nó Frame Interpolate cria novos quadros entre os já existentes em uma sequência de imagens, aumentando efetivamente a taxa de quadros. Ele usa um modelo de IA para prever como os quadros intermediários devem ser, o que pode ser usado para criar efeitos de câmera lenta suaves ou para aumentar a suavidade de um vídeo. Para cada par consecutivo de quadros, o nó gera `multiplier - 1` novos quadros e os insere entre os originais.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `interp_model` | O modelo de interpolação de quadros a ser usado para gerar os quadros intermediários (por exemplo, modelos RIFE ou FILM) | INTERP_MODEL | Sim | - |
| `images` | Um lote de imagens consecutivas (quadros) entre os quais interpolar. Requer pelo menos 2 imagens; se forem fornecidas menos, o nó retorna as imagens de entrada inalteradas. | IMAGE | Sim | - |
| `multiplier` | O fator pelo qual multiplicar a contagem de quadros. Por exemplo, um multiplicador de 2 dobra o número de quadros. (padrão: 2) | INT | Sim | 2 a 16 |

Nota: O lote de imagens de entrada deve conter pelo menos 2 quadros, pois a interpolação ocorre entre pares consecutivos de quadros. O número total de quadros na saída é `(número de quadros de entrada - 1) * multiplicador + 1`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `IMAGE` | Um novo lote de imagens com os quadros interpolados inseridos entre os quadros originais, resultando em uma sequência mais suave. O número total de quadros de saída é `(número de quadros de entrada - 1) * multiplicador + 1`. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolate/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e0b9dd6ec3b09e665bcc0f95d2b7a0209d9045ba9b96828e46f126e6914f049c`
