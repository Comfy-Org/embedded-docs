# Luma Imagem para Imagem

Modifica imagens de forma síncrona com base em um prompt de texto e na proporção original da imagem. Este nó recebe uma imagem de entrada e a transforma de acordo com o prompt fornecido, usando um peso de imagem configurável para controlar o quanto a imagem original é alterada.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `image` | A imagem de entrada a ser modificada | IMAGE | Sim | - |
| `prompt` | Prompt para a geração da imagem (padrão: "") | STRING | Sim | - |
| `image_weight` | Peso da imagem; quanto mais próximo de 1.0, menos a imagem será modificada (padrão: 0.1). Internamente, esse valor é invertido (1.0 - image_weight) e limitado entre 0.0 e 0.98. | FLOAT | Não | 0.0-0.98 |
| `model` | O modelo Luma a ser usado para modificar a imagem. Modelos diferentes têm custos diferentes. | STRING | Sim | `"photon-flash-1"`<br>`"photon-1"`<br>`"photon"` |
| `seed` | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos independentemente da semente (padrão: 0) | INT | Não | 0-18446744073709551615 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `image` | A imagem modificada gerada pelo modelo Luma | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageModifyNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `078542bdba19945037c95fefa30d1b403ebf58e29270c8067dcb8ff21a99b7e0`
