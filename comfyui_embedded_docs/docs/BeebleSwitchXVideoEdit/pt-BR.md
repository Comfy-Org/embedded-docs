# Beeble SwitchX Edição de Vídeo

Edite um vídeo com Beeble SwitchX. Este nó pode alterar qualquer elemento da cena (fundo, iluminação, figurino) enquanto preserva os pixels e o movimento do sujeito original. Forneça uma imagem de referência e/ou um prompt de texto para descrever a nova aparência.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `vídeo` | O vídeo de entrada para editar. Máximo de 240 quadros, máximo de ~2,77 megapixels por quadro. | VIDEO | Sim | N/A |
| `prompt` | Uma descrição textual da nova aparência desejada para a cena. | STRING | Sim | N/A |
| `alpha_mode` | O modo de máscara alfa. O modo "fill" não possui máscara separada e preenche todo o quadro. O modo "select" usa uma única imagem de quadro-chave para definir a área a ser editada. O modo "custom" usa um vídeo alfa completo para definir a área a ser editada quadro a quadro. | COMBO | Sim | `"fill"`<br>`"select"`<br>`"custom"` |
| `resolução_máxima` | A resolução máxima para o vídeo de saída (padrão: "1080p"). | COMBO | Sim | `"720p"`<br>`"1080p"` |
| `seed` | Um valor de semente para reprodutibilidade. Usar a mesma semente com as mesmas entradas produzirá o mesmo resultado. | INT | Sim | 0 a 2147483647 |
| `imagem_de_referência` | Uma imagem de referência opcional que descreve a nova aparência desejada para a cena. | IMAGE | Não | N/A |

### Detalhes do Modo Alfa

O parâmetro `alpha_mode` controla quais partes do vídeo são editadas:

- **fill**: O quadro inteiro do vídeo é editado. Nenhuma máscara alfa separada é produzida.
- **select**: Você fornece uma única imagem de quadro-chave que define a área a ser editada. O nó usará isso para determinar quais partes do vídeo serão alteradas.
- **custom**: Você fornece um vídeo alfa completo que define a área a ser editada quadro a quadro. Isso oferece controle preciso sobre quais partes de cada quadro são editadas.

Ao usar o modo `select`, você deve fornecer a imagem `alpha_keyframe`. Ao usar o modo `custom`, você deve fornecer o vídeo `alpha_mask`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `vídeo` | O vídeo editado com as alterações de cena aplicadas. | VIDEO |
| `alpha` | A máscara alfa usada pelo Beeble. Fica vazia no modo "fill", que não possui máscara separada. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BeebleSwitchXVideoEdit/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e2d67b037863f024f42c97943ec0d2daf32b547b232a7dfedd6de398f4b7ba28`
