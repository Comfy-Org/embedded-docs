> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageTextSetFromFolderNode/pt-BR.md)

Carrega um lote de imagens e suas respectivas legendas de texto de um diretório especificado para fins de treinamento. O nó busca automaticamente por arquivos de imagem e seus arquivos de legenda de texto associados, processa as imagens de acordo com as configurações de redimensionamento especificadas e codifica as legendas usando o modelo CLIP fornecido.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `folder` | STRING | Sim | - | A pasta de onde carregar as imagens. |
| `clip` | CLIP | Sim | - | O modelo CLIP usado para codificar o texto. |
| `resize_method` | COMBO | Não | "None"<br>"Stretch"<br>"Crop"<br>"Pad" | O método usado para redimensionar as imagens (padrão: "None"). |
| `width` | INT | Não | -1 a 10000 | A largura para redimensionar as imagens. -1 significa usar a largura original (padrão: -1). |
| `height` | INT | Não | -1 a 10000 | A altura para redimensionar as imagens. -1 significa usar a altura original (padrão: -1). |

**Observação:** A entrada CLIP deve ser válida e não pode ser None. Se o modelo CLIP for proveniente de um nó carregador de checkpoint, certifique-se de que o checkpoint contenha um modelo CLIP ou codificador de texto válido.

**Observação sobre a estrutura de pastas:** O nó suporta a estrutura de pastas do kohya-ss/sd-scripts. Se o nome de uma subpasta começar com um número seguido de um sublinhado (ex.: `5_myclass`), esse número é usado como uma contagem de repetição, e as imagens dentro dessa subpasta serão carregadas esse número de vezes.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `IMAGE` | IMAGE | O lote de imagens carregadas e processadas. |
| `CONDITIONING` | CONDITIONING | Os dados de condicionamento codificados a partir das legendas de texto. |

---
**Source fingerprint (SHA-256):** `ffd6399783fc281a58bae811112d9ecacb51ab8ea3b512befa9b9fab2c6860de`
