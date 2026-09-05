# VideoCrop

Este nó recorta um vídeo para uma região retangular selecionada, mantendo apenas a parte interna desse retângulo. Ele também cria uma pré-visualização do vídeo recortado para que você veja o resultado. Se a largura e a altura do recorte forem zero, o vídeo completo é mantido inalterado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `video` | O vídeo de origem que será recortado. | VIDEO | Sim | Qualquer vídeo |
| `crop` | Região de recorte em pixels. Largura/altura zero mantém o quadro completo. O retângulo de recorte fornece os valores `x`, `y`, `width` e `height`, todos com padrão 0. | VIDEO_EDIT | Sim | `x` ≥ 0<br>`y` ≥ 0<br>`width` ≥ 0<br>`height` ≥ 0<br>Todos os valores têm padrão 0 |

Nota: A região de recorte é descrita em coordenadas de pixel. Quando a largura e a altura são 0, nenhum recorte é aplicado e o nó produz o vídeo de entrada completo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `video` | O vídeo recortado para a região retangular selecionada. Quando a largura e a altura do recorte são 0, a saída é o vídeo de entrada completo. O resultado recortado também é salvo como um arquivo MP4 temporário e exibido como uma pré-visualização do vídeo. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoCrop/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0c4ebd51027669fc232fe42a5e8840b5e4e95083b6794cd7b4c43123ddc0341b`
