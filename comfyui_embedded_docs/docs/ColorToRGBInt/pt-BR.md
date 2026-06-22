# Cor para RGB Int

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ColorToRGBInt/en.md)

O nó ColorToRGBInt converte uma cor especificada em formato hexadecimal em um único valor inteiro. Ele recebe uma string de cor como `#FF5733` e calcula o inteiro RGB correspondente combinando os componentes vermelho, verde e azul.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `cor` | Um valor de cor no formato hexadecimal `#RRGGBB`. | STRING | Sim | N/A |

**Nota:** A string de entrada `color` deve ter exatamente 7 caracteres e começar com o símbolo `#`, seguido por seis dígitos hexadecimais (por exemplo, `#FF0000` para vermelho). O nó gerará um erro se o formato estiver incorreto.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `rgb_int` | O valor inteiro RGB calculado. Isso é derivado da fórmula: `(Vermelho * 65536) + (Verde * 256) + Azul`. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ColorToRGBInt/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5b8617d6b28caaa5f01dad1c6a302fa321f1bd53a0454451d468e36747e70e8f`
