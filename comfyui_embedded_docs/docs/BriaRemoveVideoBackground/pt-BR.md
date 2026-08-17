# Bria Remover Fundo do Vídeo

Este nó remove o fundo de um vídeo usando o serviço de IA da Bria. Ele processa o vídeo de entrada e substitui o fundo original por uma cor sólida de sua escolha. A operação é realizada por meio de uma API externa, e o resultado é retornado como um novo arquivo de vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `video` | O arquivo de vídeo de entrada do qual o fundo será removido. | VIDEO | Sim | N/A |
| `background_color` | Cor de fundo para o vídeo de saída. | COMBO | Sim | `"Black"`<br>`"White"`<br>`"Gray"`<br>`"Red"`<br>`"Green"`<br>`"Blue"`<br>`"Yellow"`<br>`"Cyan"`<br>`"Magenta"`<br>`"Orange"` |
| `seed` | O seed controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente do seed. (padrão: 0) | INT | Sim | 0 a 2147483647 |

**Nota:** O vídeo de entrada deve ter duração de 60 segundos ou menos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `output` | O arquivo de vídeo processado com o fundo removido e substituído pela cor selecionada. O vídeo de saída é codificado como MP4 com H.264. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveVideoBackground/pt-BR.md)

---
**Source fingerprint (SHA-256):** `dbd6b7393f893be5a40322fc96b90bb3d5f1818bdda7b8109b28f48baac44d59`
