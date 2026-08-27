# Salvar Imagem (Avançado)

O nó **Save Image (Advanced)** salva as imagens de entrada no diretório de saída do seu ComfyUI com controle avançado sobre o formato do arquivo, a profundidade de bits e o espaço de cores. Ele oferece suporte ao salvamento de arquivos PNG ou EXR e pode incorporar metadados do fluxo de trabalho nos arquivos salvos.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `imagens` | As imagens a serem salvas. | IMAGE | Sim | - |
| `prefixo_do_nome_do_arquivo` | O prefixo para o arquivo a ser salvo. Pode incluir tokens de formatação como `%date:yyyy-MM-dd%` ou `%Empty Latent Image.width%`. (padrão: "ComfyUI") | STRING | Sim | - |
| `formato` | O formato de arquivo no qual salvar a imagem. Selecionar um formato exibe opções adicionais para esse formato. | DYNAMIC_COMBO | Sim | `"png"`<br>`"exr"` |

### Entradas PNG

Essas opções aparecem quando `format` está definido como `"png"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `bit_depth` | A profundidade de bits para o arquivo PNG salvo. (padrão: "8-bit") | COMBO | Sim (condicional) | `"8-bit"`<br>`"16-bit"` |
| `input_color_space` | Espaço de cores do tensor de entrada. Apenas sRGB está disponível para o formato PNG. (padrão: "sRGB") | COMBO | Sim (condicional) | `"sRGB"` |

### Entradas EXR

Essas opções aparecem quando `format` está definido como `"exr"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `bit_depth` | A profundidade de bits para o arquivo EXR salvo. (padrão: "32-bit float") | COMBO | Sim (condicional) | `"32-bit float"` |
| `input_color_space` | Espaço de cores do tensor de entrada. O EXR é sempre gravado como linear de cena na gama de cores correspondente.<br>`"sRGB"` — a entrada é codificada em sRGB (Rec.709); a EOTF inversa de sRGB é aplicada.<br>`"HDR"` — a entrada é codificada em HLG (Rec.2020, BT.2100); a OETF inversa de HLG é aplicada para obter luz linear de cena.<br>`"linear"` — a entrada já é linear de cena (primárias Rec.709); é gravada inalterada. Use esta opção para saída de renderizador/compositor. (padrão: "sRGB") | COMBO | Sim (condicional) | `"sRGB"`<br>`"HDR"`<br>`"linear"` |

**Notas sobre dependências de parâmetros:**
- Os parâmetros `bit_depth` e `input_color_space` só estão disponíveis quando um `format` específico é selecionado.
- Para o formato PNG, apenas as profundidades de bits "8-bit" e "16-bit" estão disponíveis, e apenas o espaço de cores "sRGB".
- Para o formato EXR, apenas a profundidade de bits "32-bit float" está disponível, com os espaços de cores "sRGB", "HDR" ou "linear".
- As imagens devem ter 1 canal (tons de cinza), 3 canais (RGB) ou 4 canais (RGBA); outras quantidades de canais não são suportadas e geram um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `imagens` | As imagens de entrada, repassadas inalteradas. A saída da interface do nó fornece uma lista de resultados de imagens salvas, cada um contendo o nome do arquivo, a subpasta e o tipo ("output"). | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageAdvanced/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b03a822a90cf50d30fbf4397ab280393951f08d2339dd48c0dbaf75d9c415bca`
