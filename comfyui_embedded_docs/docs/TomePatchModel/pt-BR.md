# TomePatchModel

TomePatchModel aplica Token Merging (ToMe) a um modelo de difusão para reduzir os requisitos computacionais durante a inferência. Ele funciona mesclando seletivamente tokens semelhantes no mecanismo de atenção, permitindo que o modelo processe menos tokens enquanto mantém a qualidade da imagem. Essa técnica ajuda a acelerar a geração sem perda significativa de qualidade.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo de difusão ao qual aplicar a fusão de tokens | MODEL | Sim | - |
| `proporção` | A proporção de tokens a mesclar (padrão: 0.3). Valores maiores mesclam mais tokens, resultando em maior aceleração, mas potencialmente menor qualidade. | FLOAT | Sim | 0.0 - 1.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo modificado com fusão de tokens aplicada | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TomePatchModel/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1202c0df17f357440cd156fa0920f70c18a318e32c41dc04cecff11613f0072f`
