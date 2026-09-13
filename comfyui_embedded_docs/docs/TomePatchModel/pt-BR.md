# TomePatchModel

TomePatchModel aplica Token Merging (ToMe) a um modelo de difusão para reduzir o custo computacional durante a inferência. Ele funciona fundindo tokens semelhantes dentro do mecanismo de atenção do modelo, de modo que o modelo processa menos tokens enquanto mantém a qualidade da saída em grande parte intacta.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo de difusão ao qual aplicar a fusão de tokens | MODEL | Sim | - |
| `ratio` | A proporção de tokens a fundir (padrão: 0.3). Valores mais altos fundem mais tokens, o que pode proporcionar maior aceleração, mas potencialmente menor qualidade. | FLOAT | Sim | 0.0 - 1.0 |

Observação: Se o número de tokens em um bloco de atenção for pequeno o suficiente para que nenhum downsampling seja necessário, as funções de fusão são substituídas por no-ops, e o modelo é executado sem alterações para esse bloco.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo modificado com a fusão de tokens aplicada | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TomePatchModel/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1202c0df17f357440cd156fa0920f70c18a318e32c41dc04cecff11613f0072f`
