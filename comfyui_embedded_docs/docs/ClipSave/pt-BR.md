O nó `CLIPSave` salva um modelo de codificador de texto CLIP no disco no formato SafeTensors. Ele é projetado para fluxos de trabalho avançados de mesclagem de modelos e separa automaticamente o modelo CLIP em suas partes componentes (como CLIP-L, CLIP-G ou T5XXL) com base na estrutura interna do modelo, salvando cada componente como um arquivo separado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Tipo de Entrada | Padrão | Faixa |
| --- | --- | --- | --- | --- | --- |
| `clip` | O modelo CLIP a ser salvo. | CLIP | Obrigatório | - | - |
| `filename_prefix` | O caminho do prefixo e nome do arquivo para o(s) arquivo(s) salvo(s). O nó anexará um sufixo de componente (por exemplo, `_clip_l`, `_clip_g`) e um contador para criar nomes de arquivo únicos. | STRING | Obrigatório | `clip/ComfyUI` | - |
| `prompt` | As informações do prompt do fluxo de trabalho, salvas como metadados no arquivo de saída. | PROMPT | Oculta | - | - |
| `extra_pnginfo` | Metadados adicionais, salvos como pares chave-valor no arquivo de saída. | EXTRA_PNGINFO | Oculta | - | - |

## Saídas

Este nó não possui conexões de saída. Ele salva os arquivos processados diretamente no diretório `ComfyUI/output/`.

### Detalhes do Arquivo Salvo

O nó analisa o dicionário de estado do modelo CLIP e salva arquivos SafeTensors separados para cada componente detectado. O componente é identificado pelo prefixo de suas chaves de parâmetro. Os seguintes prefixos são verificados:

- `clip_l.` (codificador de texto CLIP-L)
- `clip_g.` (codificador de texto CLIP-G)
- `clip_h.` (codificador de texto CLIP-H)
- `t5xxl.` (codificador de texto T5-XXL)
- `pile_t5xl.` (codificador de texto Pile-T5-XL)
- `mt5xl.` (codificador de texto mT5-XL)
- `umt5xxl.` (codificador de texto UMT5-XXL)
- `t5base.` (codificador de texto T5-Base)
- `gemma2_2b.` (codificador de texto Gemma 2 2B)
- `llama.` (codificador de texto LLaMA)
- `hydit_clip.` (codificador de texto Hydit CLIP)
- Prefixo vazio (outros componentes CLIP)

Para cada componente detectado, o nó cria um arquivo com o nome `{filename_prefix}_{counter:05}_.safetensors`, onde o prefixo do componente é anexado ao prefixo do nome do arquivo (por exemplo, `clip/ComfyUI_clip_l_00001_.safetensors`). O prefixo `transformer.` é removido das chaves de parâmetro durante o salvamento.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPSave/pt-BR.md)

---
**Source fingerprint (SHA-256):** `039b39cbfb9b04ccebc5fc885ebe75dfde14838530d38133d0a3a6311e392059`
