# Text Encode MOSS-Image Edit

Codifica uma instrução de edição junto com imagens de referência em condicionamento para um LoRA de edição MOSS-Image. Conecte a saída como o condicionamento positivo e execute uma segunda instância com as mesmas referências para o condicionamento negativo. As referências são usadas no tamanho em que chegam, portanto, redimensione-as antes de conectar. Este nó está marcado como experimental no ComfyUI. Sem uma VAE, as imagens vão apenas ao codificador de texto.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `clip` | O modelo CLIP que tokeniza a instrução e a codifica. | CLIP | Sim | - |
| `prompt` | A instrução que descreve a edição. Suporta texto multilinha e prompts dinâmicos. | STRING | Sim | Qualquer texto |
| `vae` | A VAE usada para codificar as imagens de referência em latentes de referência. Opcional: sem ela, as imagens vão apenas ao codificador de texto.| VAE | Não | - |
| `edit_format` | O layout com o qual o LoRA de edição foi treinado. Ele seleciona o método de latentes de referência e se o codificador de texto também vê as referências. | COMBO | Sim | `"ai-toolkit"`<br>`"ai-toolkit (kv_cache off)"`<br>`"Moss-Image-Edit"` |
| `images` | Slot expansível: conecte uma ou mais imagens de referência (`image_1`, `image_2`, ...). Cada imagem é usada no tamanho em que chega, tem seu canal alfa descartado e é codificada pela VAE em um latente de referência. Com uma VAE conectada, o canal alfa é descartado e cada imagem é codificada em um latente de referência; sem VAE, as imagens vão apenas ao codificador de texto.| IMAGE | Sim | 1 ou mais imagens |
| `image_strength` | Escala o quanto o modelo atende às imagens que o codificador de texto vê (formatos ai-toolkit, ou sem VAE): 0 as ignora, 1 inalterado, acima de 1 as enfatiza. Avançado. Padrão: 1.0. | FLOAT | Sim | 0.0 to 100.0 (step 0.05) |

**Nota:** With `"ai-toolkit"` and `"ai-toolkit (kv_cache off)"`, or when no VAE is connected and `image_strength` is above 0, the text encoder also sees every reference, downscaled to at most 384x384 pixels and preceded by a `Picture N:` marker in the prompt, so the instruction can refer to them by number. With `"Moss-Image-Edit"` and a VAE connected, the references reach the model only as reference latents and the text encoder sees the instruction alone. `"ai-toolkit (kv_cache off)"` additionally keeps the references attending to the image being generated, so they are recomputed on every sampling step.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `conditioning` | A instrução codificada com os latentes de referência e o método de latentes de referência correspondente anexados. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeMOSSImageEdit/pt-BR.md)

---
**Source fingerprint (SHA-256):** `673f098df6a8e466a5c8060009f446eac8f7556311a870de626c5f4bfc3ab196`
