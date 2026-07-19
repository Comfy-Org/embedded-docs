# LoadImageSetFromFolderNode

O nó LoadImageSetFromFolderNode carrega múltiplas imagens de um diretório de pasta especificado para fins de treinamento. Ele detecta automaticamente formatos de imagem comuns e pode opcionalmente redimensionar as imagens usando diferentes métodos antes de retorná-las como um lote.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `folder` | A pasta de onde carregar as imagens. | STRING | Sim | Múltiplas opções disponíveis |
| `resize_method` | O método a ser usado para redimensionar as imagens (padrão: "Nenhum"). | STRING | Não | "Nenhum"<br>"Esticar"<br>"Cortar"<br>"Preencher" |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `IMAGE` | O lote de imagens carregadas como um único tensor. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageSetFromFolderNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `46fcfbf6a2ad95e707e32e54ed7b4c06bfd1cc290df122042187689f41bed828`
