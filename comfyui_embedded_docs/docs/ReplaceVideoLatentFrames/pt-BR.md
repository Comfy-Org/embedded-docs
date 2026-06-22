# ReplaceVideoLatentFrames

O nó ReplaceVideoLatentFrames insere quadros de um vídeo latente de origem em um vídeo latente de destino, começando em um índice de quadro especificado. Se a origem latente não for fornecida, o destino latente é retornado inalterado. O nó lida com indexação negativa e emitirá um aviso se os quadros de origem não couberem no destino.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `destino` | O destino latente onde os quadros serão substituídos. | LATENT | Sim | - |
| `origem` | A origem latente que fornece os quadros a serem inseridos no destino latente. Se não for fornecida, o destino latente é retornado inalterado. | LATENT | Não | - |
| `índice` | O índice inicial do quadro latente no destino latente onde os quadros da origem latente serão colocados. Valores negativos contam a partir do final (padrão: 0). | INT | Sim | -MAX_RESOLUTION a MAX_RESOLUTION |

**Restrições:**

* O `index` deve estar dentro dos limites da contagem de quadros do destino latente. Caso contrário, um aviso é registrado e o destino é retornado inalterado.
* Os quadros da origem latente devem caber dentro dos quadros do destino latente a partir do `index` especificado. Caso contrário, um aviso é registrado e o destino é retornado inalterado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | O vídeo latente resultante após a operação de substituição de quadros. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReplaceVideoLatentFrames/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b4e2b3dcdaa5c400fefc30262ae05cd1849896e6cb6bbb3a1bd6ce4d31583e23`
