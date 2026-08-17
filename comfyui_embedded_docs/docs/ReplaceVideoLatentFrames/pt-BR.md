# ReplaceVideoLatentFrames

O nó ReplaceVideoLatentFrames insere quadros de um vídeo latente de origem em um vídeo latente de destino, começando em um índice de quadro especificado. Se o latent de origem não for fornecido, o latent de destino é retornado inalterado. O nó lida com indexação negativa e emitirá um aviso se os quadros de origem não couberem no destino.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Range |
| --- | --- | --- | --- | --- |
| `destination` | O latent de destino onde os quadros serão substituídos. | LATENT | Sim | - |
| `source` | O latent de origem que fornece os quadros a serem inseridos no latent de destino. Se não for fornecido, o latent de destino é retornado inalterado. | LATENT | Não | - |
| `index` | O índice do quadro latente inicial no latent de destino onde os quadros do latent de origem serão colocados. Valores negativos contam a partir do final (padrão: 0). | INT | Sim | -MAX_RESOLUTION a MAX_RESOLUTION (passo: 1) |

**Restrições:**

* O `index` deve estar dentro dos limites da contagem de quadros do latent de destino. Se não estiver, um aviso é registrado e o destino é retornado inalterado.
* Os quadros do latent de origem devem caber nos quadros do latent de destino a partir do `index` especificado. Se não couberem, um aviso é registrado e o destino é retornado inalterado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | O vídeo latente resultante após a operação de substituição de quadros. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReplaceVideoLatentFrames/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5b98d875bdeaec63521bff19fecbc5510036c8b4f90322d8296b216688b557bf`
