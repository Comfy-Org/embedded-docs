# Cortar Imagens ao Centro

O nó Center Crop Images recorta uma imagem a partir de seu centro para uma largura e altura especificadas. Ele calcula a região central da imagem de entrada e extrai uma área retangular com as dimensões definidas. Se o tamanho do recorte solicitado for maior que a imagem, o recorte será limitado aos limites da imagem.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `image` | A imagem de entrada a ser recortada. | IMAGE | Sim | - |
| `largura` | A largura da área de recorte (padrão: 512). | INT | Sim | 1 a 8192 |
| `altura` | A altura da área de recorte (padrão: 512). | INT | Sim | 1 a 8192 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `image` | A imagem resultante após a operação de recorte central. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CenterCropImages/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4361b6630ab1833e035d6ab04a130fb36fff33cddc36b54ff5a2d8e04534a555`
