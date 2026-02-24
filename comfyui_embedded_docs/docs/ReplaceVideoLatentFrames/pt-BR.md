> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReplaceVideoLatentFrames/pt-BR.md)

O nó ReplaceVideoLatentFrames insere quadros de um vídeo latente de origem em um vídeo latente de destino, começando em um índice de quadro especificado. Se o latente de origem não for fornecido, o latente de destino é retornado inalterado. O nó lida com indexação negativa e emitirá um aviso se os quadros de origem não couberem dentro do destino.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `destination` | LATENT | Sim | - | O latente de destino onde os quadros serão substituídos. |
| `source` | LATENT | Não | - | O latente de origem que fornece os quadros para inserir no latente de destino. Se não fornecido, o latente de destino é retornado inalterado. |
| `index` | INT | Não | -MAX_RESOLUTION a MAX_RESOLUTION | O índice do quadro latente inicial no latente de destino onde os quadros do latente de origem serão colocados. Valores negativos contam a partir do final (padrão: 0). |

**Restrições:**

* O `index` deve estar dentro dos limites da contagem de quadros do latente de destino. Caso contrário, um aviso é registrado e o destino é retornado inalterado.
* Os quadros do latente de origem devem caber dentro dos quadros do latente de destino a partir do `index` especificado. Caso contrário, um aviso é registrado e o destino é retornado inalterado.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | LATENT | O vídeo latente resultante após a operação de substituição de quadros. |
