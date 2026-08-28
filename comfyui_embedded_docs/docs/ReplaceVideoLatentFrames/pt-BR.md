# ReplaceVideoLatentFrames

ReplaceVideoLatentFrames substitui um intervalo de quadros em um vídeo latente de destino por quadros de um vídeo latente de origem, começando em um índice de quadro especificado. Se nenhum latente de origem for fornecido, o latente de destino é retornado inalterado. O nó suporta índices negativos e registra um aviso quando os quadros de origem não cabem no destino.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `destino` | O latente de destino onde os quadros serão substituídos. | LATENT | Sim | - |
| `origem` | O latente de origem que fornece os quadros a inserir no latente de destino. Se não for fornecido, o latente de destino é retornado inalterado. | LATENT | Não | - |
| `índice` | O índice de quadro latente inicial no latente de destino onde os quadros do latente de origem serão colocados. Valores negativos contam a partir do final (padrão: 0). | INT | Sim | -MAX_RESOLUTION to MAX_RESOLUTION |

**Restrições:**

* Um `index` negativo é ajustado sendo somado à contagem de quadros do destino, portanto ele conta de trás para frente a partir do final do latente de destino.
* Se o `index` apontar além da contagem de quadros do destino, ou se os quadros de origem não couberem no destino a partir do `index`, um aviso é registrado e o latente de destino é retornado inalterado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | O vídeo latente resultante após a operação de substituição de quadros. Se a substituição não puder ser realizada, o latente de destino é retornado inalterado. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReplaceVideoLatentFrames/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5b98d875bdeaec63521bff19fecbc5510036c8b4f90322d8296b216688b557bf`
