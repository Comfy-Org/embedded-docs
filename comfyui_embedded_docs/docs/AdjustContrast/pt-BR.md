O nó Ajustar Contraste modifica o nível de contraste de uma imagem de entrada. Ele funciona ajustando a diferença entre as áreas claras e escuras da imagem. Um fator de 1,0 mantém a imagem inalterada, valores abaixo de 1,0 reduzem o contraste e valores acima de 1,0 aumentam o contraste.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `image` | A imagem de entrada que terá seu contraste ajustado. | IMAGE | Sim | - |
| `fator` | Fator de contraste. 1,0 = sem alteração, <1,0 = menos contraste, >1,0 = mais contraste. (padrão: 1,0) | FLOAT | Não | 0,0 - 2,0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `image` | A imagem resultante com o contraste ajustado. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustContrast/pt-BR.md)

---
**Source fingerprint (SHA-256):** `01148cdd9d951e78c712c1c3159c5562a680a5147bd4a76e33d91543d5245854`
