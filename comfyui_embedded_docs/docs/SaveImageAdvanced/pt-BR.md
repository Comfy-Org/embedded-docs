# Salvar Imagem (Avançado)

O nó **SaveImageAdvanced** salva imagens no seu diretório de saída do ComfyUI com controle avançado sobre formato de arquivo, profundidade de bits e espaço de cor. Ele permite salvar como arquivos PNG ou EXR e pode incorporar metadados do fluxo de trabalho nos arquivos salvos.

## Entradas

### Entradas Comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `images` | As imagens a serem salvas. | IMAGE | Sim | - |
| `filename_prefix` | O prefixo para o arquivo a ser salvo. Pode incluir tokens de formatação como `%date:yyyy-MM-dd%` ou `%Empty Latent Image.width%`. (padrão: "ComfyUI") | STRING | Sim | - |
| `format` | O formato de arquivo no qual salvar a imagem. Selecionar um formato revela opções adicionais para esse formato. | DYNAMIC_COMBO | Sim | `"png"`<br>`"exr"` |

### Entradas PNG

Estas entradas são exibidas quando `format` está definido como `"png"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `bit_depth` | A profundidade de bits usada ao salvar a imagem. (padrão: "8-bit") | COMBO | Sim (condicional) | `"8-bit"`<br>`"16-bit"` |
| `input_color_space` | O espaço de cor do tensor de entrada. (padrão: "sRGB") | COMBO | Sim (condicional) | `"sRGB"` |

### Entradas EXR

Estas entradas são exibidas quando `format` está definido como `"exr"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `bit_depth` | A profundidade de bits usada ao salvar a imagem. (padrão: "32-bit float") | COMBO | Sim (condicional) | `"32-bit float"` |
| `input_color_space` | Espaço de cor do tensor de entrada. O EXR é sempre gravado como linear de cena na gama correspondente. (padrão: "sRGB") | COMBO | Sim (condicional) | `"sRGB"`<br>`"HDR"`<br>`"linear"` |

**Notas sobre dependências de parâmetros e comportamento dos arquivos:**

- `bit_depth` e `input_color_space` só aparecem quando o `format` pai está selecionado.
- Para o formato PNG, apenas as profundidades de bits `"8-bit"` e `"16-bit"` estão disponíveis, e apenas o espaço de cor `"sRGB"`. A seleção de espaço de cor não modifica os pixels PNG — arquivos PNG são sempre salvos como imagens codificadas em sRGB.
- Para o formato EXR, apenas a profundidade de bits `"32-bit float"` está disponível, com os espaços de cor `"sRGB"`, `"HDR"` ou `"linear"`.
- O parâmetro `input_color_space` para EXR determina como o tensor de entrada é interpretado antes de salvar:
  - `"sRGB"` — a entrada é codificada em sRGB Rec.709; a EOTF sRGB inversa é aplicada.
  - `"HDR"` — a entrada é codificada em HLG Rec.2020 (BT.2100); a OETF HLG inversa é aplicada para obter luz linear de cena.
  - `"linear"` — a entrada já é linear de cena (primárias Rec.709); gravada diretamente, sem alterações. Use esta opção para saída de renderizador/compositor.
- Metadados do fluxo de trabalho (prompt e informações extras de PNG) são incorporados aos arquivos PNG e EXR salvos, a menos que a gravação de metadados esteja desabilitada pelo argumento de linha de comando `--disable-metadata`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `images` | As imagens que foram salvas (as mesmas imagens passadas para a entrada `images`). O resultado da interface do nó inclui uma lista dos arquivos salvos, cada um reportado com seu nome de arquivo, subpasta e tipo ("output"). | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageAdvanced/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b03a822a90cf50d30fbf4397ab280393951f08d2339dd48c0dbaf75d9c415bca`
