# Carregar Vídeo-Texto (da Pasta)

Este nó carrega um conjunto de dados de arquivos de vídeo e suas respectivas legendas em texto a partir de uma subpasta especificada dentro do diretório de entrada do ComfyUI. Ele retorna duas listas: referências preguiçosas de vídeo (os quadros são decodificados apenas quando necessário em nós downstream) e suas legendas associadas. O nó suporta formatos de vídeo comuns, como MP4, AVI, MOV, WEBM, MKV e FLV, e também pode lidar com estruturas de pastas aninhadas com prefixos de contagem de repetição (ex.: `5_classname/`) usados por ferramentas como kohya‑ss/sd‑scripts.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-----------|--------------|-------------|-------|
| `pasta` | A subpasta contendo arquivos de vídeo e arquivos de legenda `.txt`. Selecione entre as subpastas disponíveis no diretório de entrada do ComfyUI. | STRING | Sim | Combo: lista dinâmica de todos os subdiretórios dentro da pasta de entrada do ComfyUI |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-----------|--------------|
| `videos` | Referências preguiçosas para os arquivos de vídeo carregados. Os quadros são decodificados apenas quando conectados a um nó downstream que os processe. Cada elemento corresponde a um vídeo da pasta de entrada. | VIDEO (lista) |
| `texts` | Lista de legendas em texto, uma por vídeo. Se um vídeo não tiver um arquivo `.txt` correspondente, sua legenda será uma string vazia. | STRING (lista) |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoTextDataSetFromFolder/pt-BR.md)

---
**Source fingerprint (SHA-256):** `91236fcb1e42b8de1a1100b0aecaad49bd49c159d7d8f502032cd7f5b2b54845`
