# CLIPSave

O nó `CLIPSave` salva em disco um modelo codificador de texto CLIP no formato SafeTensors. Ele é projetado para fluxos de trabalho avançados de mesclagem de modelos e separa automaticamente o modelo CLIP em suas partes componentes (como CLIP-L, CLIP-G ou T5XXL) com base na estrutura interna do modelo, salvando cada componente como um arquivo separado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `clip` | O modelo CLIP a ser salvo. | CLIP | Sim | - |
| `filename_prefix` | O prefixo do caminho e do nome do arquivo para o(s) arquivo(s) salvo(s). O nó acrescenta um sufixo de componente (por exemplo, `_clip_l`, `_clip_g`) e um contador para criar nomes de arquivo únicos (padrão: `clip/ComfyUI`). | STRING | Sim | - |
| `prompt` | As informações do prompt do fluxo de trabalho, salvas como metadados no arquivo de saída. Este parâmetro fica oculto na interface. | PROMPT | Não | - |
| `extra_pnginfo` | Metadados adicionais, salvos como pares chave-valor no arquivo de saída. Este parâmetro fica oculto na interface. | EXTRA_PNGINFO | Não | - |

## Saídas

Este nó não possui conexões de saída. Ele salva os arquivos processados diretamente no diretório `ComfyUI/output/`.

### Detalhes dos arquivos salvos

O nó analisa o dicionário de estado do modelo CLIP e salva arquivos SafeTensors separados para cada componente detectado. O componente é identificado pelo prefixo de suas chaves de parâmetros. O nó verifica os seguintes prefixos, em ordem:

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
- Prefixo vazio (outros componentes do CLIP)

Para cada componente detectado, o nó cria um arquivo com o nome `{filename}_{counter:05}_.safetensors` (por exemplo, `ComfyUI_clip_l_00001_.safetensors`), em que o nome do componente é anexado ao prefixo do nome do arquivo e o contador garante nomes de arquivo únicos. Quando um componente é salvo, o prefixo `transformer.` é removido de suas chaves de parâmetros.

Os metadados gravados em cada arquivo incluem o prompt do fluxo de trabalho e quaisquer informações extras de PNG, a menos que a gravação de metadados esteja desativada pelo argumento de linha de comando `--disable-metadata`.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPSave/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4ab9171e4245b10f738f78bac8a5b564c0957dde352e207ec3f9865e4fac0cab`
