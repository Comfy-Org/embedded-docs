> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageSetNode/pt-BR.md)

O nó LoadImageSetNode carrega múltiplas imagens do diretório de entrada para processamento em lote e fins de treinamento. Ele suporta diversos formatos de imagem e pode opcionalmente redimensionar as imagens usando diferentes métodos. Este nó processa todas as imagens selecionadas como um lote e as retorna como um único tensor.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `images` | IMAGE | Sim | Múltiplos arquivos de imagem | Selecione múltiplas imagens do diretório de entrada. Suporta os formatos PNG, JPG, JPEG, WEBP, BMP, GIF, JPE, APNG, TIF e TIFF. Permite seleção em lote de imagens. |
| `resize_method` | STRING | Não | "None"<br>"Stretch"<br>"Crop"<br>"Pad" | Método opcional para redimensionar as imagens carregadas (padrão: "None"). Escolha "None" para manter os tamanhos originais, "Stretch" para forçar o redimensionamento, "Crop" para manter a proporção cortando a imagem ou "Pad" para manter a proporção adicionando preenchimento. |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `IMAGE` | IMAGE | Um tensor contendo todas as imagens carregadas como um lote para processamento posterior. |

---
**Source fingerprint (SHA-256):** `acf0255bcf170ef3ac3b86a3f3e060c3b81064ca8924918a026ec8e3b86f7ac0`
