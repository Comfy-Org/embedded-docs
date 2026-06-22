# ByteDance Seedance 2.0 Primeiro-Último-Frame para Vídeo

Este nó utiliza o modelo Seedance 2.0 da ByteDance para gerar um vídeo. Ele cria o vídeo com base em um prompt de texto e uma imagem obrigatória do primeiro quadro. Opcionalmente, você pode fornecer uma imagem do último quadro para orientar o final da sequência de vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo a ser usado para a geração de vídeo. Seedance 2.0 é para máxima qualidade, enquanto Seedance 2.0 Fast é otimizado para velocidade. Selecionar um modelo revelará entradas adicionais para `prompt`, `resolution`, `ratio`, `duration` e `generate_audio`. | COMBO | Sim | `"Seedance 2.0"`<br>`"Seedance 2.0 Fast"` |
| `primeiro_frame` | A imagem a ser usada como o primeiro quadro do vídeo. | IMAGE | Não | - |
| `último_frame` | A imagem a ser usada como o último quadro do vídeo. | IMAGE | Não | - |
| `first_frame_asset_id` | Um asset_id do Seedance para usar como primeiro quadro. Não pode ser usado ao mesmo tempo que a entrada de imagem `primeiro_frame`. O padrão é uma string vazia. | STRING | Não | - |
| `last_frame_asset_id` | Um asset_id do Seedance para usar como último quadro. Não pode ser usado ao mesmo tempo que a entrada de imagem `último_frame`. O padrão é uma string vazia. | STRING | Não | - |
| `semente` | Um valor de semente. Alterar esta semente fará com que o nó seja executado novamente, mas os resultados são não determinísticos. O padrão é 0. | INT | Não | 0 a 2147483647 |
| `marca_d'água` | Se deve adicionar uma marca d'água ao vídeo gerado. O padrão é Falso. | BOOLEAN | Não | - |

**Restrições dos Parâmetros:**
*   Você deve fornecer **ou** uma imagem `first_frame` **ou** um `first_frame_asset_id`. Fornecer ambos causará um erro.
*   Você não pode fornecer uma imagem `last_frame` e um `last_frame_asset_id` para o mesmo quadro.
*   A entrada `model` é uma combinação dinâmica. Após selecionar um modelo, você também deve preencher o campo `prompt` revelado (uma descrição em texto) e configurar os outros parâmetros revelados (`resolution`, `ratio`, `duration`, `generate_audio`).

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | O vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2FirstLastFrameNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `2c9c1fe8fddd0c3e1c356d2b93a06a07f83db8f7a0380e94629a91ce1ff1e29a`
