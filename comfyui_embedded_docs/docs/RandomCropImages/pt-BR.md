# Corte Aleatório de Imagens

O nó Random Crop Images seleciona aleatoriamente uma seção retangular de cada imagem de entrada e a recorta para uma largura e altura especificadas. Isso é comumente usado para aumento de dados (data augmentation) a fim de criar variações de imagens de treinamento. A posição aleatória do recorte é determinada por um valor de semente (seed), garantindo que o mesmo recorte possa ser reproduzido.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `image` | A imagem a ser recortada. | IMAGE | Sim | - |
| `largura` | A largura da área de recorte (padrão: 512). | INT | Não | 1 - 8192 |
| `altura` | A altura da área de recorte (padrão: 512). | INT | Não | 1 - 8192 |
| `semente` | Um número usado para controlar a posição aleatória do recorte (padrão: 0). | INT | Não | 0 - 18446744073709551615 |

**Observação:** Os parâmetros `width` e `height` devem ser menores ou iguais às dimensões da imagem de entrada. Se uma dimensão especificada for maior que a imagem, o recorte será limitado ao limite da imagem.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `image` | A imagem resultante após a aplicação do recorte aleatório. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RandomCropImages/pt-BR.md)

---
**Source fingerprint (SHA-256):** `bc4aca8cc63bde28fee906a92463b73436ba48ba69d7c1ff13881ac900e252a8`
