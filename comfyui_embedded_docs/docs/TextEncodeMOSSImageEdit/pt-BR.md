# Text Encode MOSS-Image Edit

Codifica uma instrução de edição junto com imagens de referência em condicionamento para um LoRA de edição MOSS-Image. Conecte a saída como o condicionamento positivo e execute uma segunda instância com as mesmas referências para o condicionamento negativo. As referências são usadas no tamanho em que chegam, portanto, redimensione-as antes de conectar. Este nó está marcado como experimental no ComfyUI.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `clip` | O modelo CLIP que tokeniza a instrução e a codifica. | CLIP | Sim | - |
| `prompt` | A instrução que descreve a edição. Suporta texto multilinha e prompts dinâmicos. | STRING | Sim | Qualquer texto |
| `vae` | A VAE usada para codificar as imagens de referência em latentes de referência. | VAE | Sim | - |
| `edit_format` | O layout com o qual o LoRA de edição foi treinado. Ele seleciona o método de latentes de referência e se o codificador de texto também vê as referências. | COMBO | Sim | `"ai-toolkit"`<br>`"ai-toolkit (kv_cache off)"`<br>`"Moss-Image-Edit"` |
| `images` | Slot expansível: conecte uma ou mais imagens de referência (`image_1`, `image_2`, ...). Cada imagem é usada no tamanho em que chega, tem seu canal alfa descartado e é codificada pela VAE em um latente de referência. | IMAGE | Sim | 1 ou mais imagens |

**Nota:** Com `"ai-toolkit"` e `"ai-toolkit (kv_cache off)"`, o codificador de texto também vê cada referência, reduzida para no máximo 384x384 pixels e precedida por um marcador `Picture N:` no prompt, para que a instrução possa se referir a elas por número. Com `"Moss-Image-Edit"`, as referências chegam ao modelo apenas como latentes de referência, e o codificador de texto vê apenas a instrução. `"ai-toolkit (kv_cache off)"` também mantém as referências fazendo atenção à imagem que está sendo gerada, portanto, elas são recalculadas a cada etapa de amostragem.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `conditioning` | A instrução codificada com os latentes de referência e o método de latentes de referência correspondente anexados. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeMOSSImageEdit/pt-BR.md)

---
**Source fingerprint (SHA-256):** `30e4edbb129f647cdce4ec95f78c002ecdc9a4f8fc5a45f1477fdc555b541dae`
