# Flux Virtual Try-On

Este nó realiza uma prova virtual de roupas, vestindo uma pessoa com a imagem de uma peça de vestuário fornecida. Ele utiliza a API BFL Flux VTO para gerar uma imagem realista da pessoa usando a peça especificada.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `pessoa` | Imagem da pessoa a ser vestida. | IMAGE | Sim | - |
| `roupa` | Imagem da peça de vestuário a ser aplicada. | IMAGE | Sim | - |
| `prompt` | Instrução opcional de estilo em linguagem natural (ex.: como a peça deve se ajustar). | STRING | Não | - |
| `semente` | A semente aleatória usada para criar o ruído. | INT | Não | 0 a 18446744073709551615 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `image` | A imagem resultante mostrando a pessoa vestindo a peça de vestuário fornecida. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxVTONode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `137c4cf91a539605ade93a428567619fea9e6a71459dd92354878fa2f2ea4afa`
