# Flux Prova Virtual de Roupas

Este nó realiza prova virtual de roupas, vestindo uma pessoa com uma imagem de vestuário fornecida. Ele usa a API BFL Flux VTO para gerar uma imagem realista da pessoa usando a peça de vestuário especificada.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `pessoa` | Imagem da pessoa a ser vestida. | IMAGE | Sim | - |
| `roupa` | Imagem da peça de vestuário a ser aplicada. | IMAGE | Sim | - |
| `prompt` | Instrução de estilo opcional em linguagem natural (por exemplo, como a peça deve se ajustar). (padrão: vazio) | STRING | Não | - |
| `semente` | A semente aleatória usada para gerar o ruído. (padrão: 0) | INT | Não | 0 a 18446744073709551615 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `image` | A imagem resultante mostrando a pessoa vestindo a peça de vestuário fornecida. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxVTONode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5e0777dedcbd6275e31a16f6f5d78f4166147266c0c88531c5843a027702e594`
