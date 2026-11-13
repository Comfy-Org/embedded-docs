# LTX Video AlphaGen

Extrai um matte alfa em escala de cinza, branco para o primeiro plano, que corresponde ao vídeo de entrada quadro a quadro. Forneça o matte para Get Video Components e Image To Mask para transformá-lo em uma máscara. O áudio não é mantido.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `video` | Vídeo para gerar o matte, com até 10 segundos e 3840x2160 em qualquer orientação. | VIDEO | Sim | - |
| `seed` | Controla se o nó é executado novamente; os resultados são não determinísticos independentemente da seed. Padrão: 42. | INT | Não | 0 a 4294967295 |

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `matte` | O matte alfa como vídeo, um quadro para cada quadro de entrada e sem áudio. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApiVideoAlphaGen/pt-BR.md)

---
**Source fingerprint (SHA-256):** `54a8304c2d092a736ad7fb86c8497aceda6340886beb81b6068a3de5a387a746`
