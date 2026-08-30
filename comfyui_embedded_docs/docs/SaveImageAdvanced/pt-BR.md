# Salvar Imagem (Avançado)

O nó **Save Image (Advanced)** salva as imagens de entrada no diretório de saída do ComfyUI com controle avançado sobre formato de arquivo, profundidade de bits e espaço de cores. Ele suporta salvar arquivos PNG, EXR ou AVIF (incluindo AVIF animado) e pode incorporar metadados do fluxo de trabalho nos arquivos salvos.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `imagens` | As imagens a salvar. | IMAGE | Sim | - |
| `prefixo_do_nome_do_arquivo` | O prefixo para o arquivo a salvar. Pode incluir tokens de formatação como `%date:yyyy-MM-dd%` ou `%Empty Latent Image.width%`. (padrão: "ComfyUI") | STRING | Sim | - |
| `formato` | O formato de arquivo no qual salvar a imagem. Selecionar um formato revela opções adicionais para esse formato. | DYNAMIC_COMBO | Sim | `"png"`<br>`"exr"`<br>`"avif"` |

### Entradas de PNG

Estas opções aparecem quando `format` está definido como `"png"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `bit_depth` | A profundidade de bits para o arquivo PNG salvo. (padrão: "8-bit") | COMBO | Sim (condicional) | `"8-bit"`<br>`"16-bit"` |
| `input_color_space` | Espaço de cores do tensor de entrada. Apenas sRGB está disponível para o formato PNG. (padrão: "sRGB") | COMBO | Sim (condicional) | `"sRGB"` |

### Entradas de EXR

Estas opções aparecem quando `format` está definido como `"exr"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `bit_depth` | A profundidade de bits para o arquivo EXR salvo. (padrão: "32-bit float") | COMBO | Sim (condicional) | `"32-bit float"` |
| `input_color_space` | Espaço de cores do tensor de entrada. O EXR é sempre gravado como linear de cena na gama de cores correspondente.<br>`"sRGB"` — a entrada é codificada em sRGB Rec.709; a EOTF sRGB inversa é aplicada.<br>`"HDR"` — a entrada é codificada em HLG Rec.2020 (BT.2100); a OETF HLG inversa é aplicada para obter luz linear de cena.<br>`"linear"` — a entrada já está em linear de cena (primárias Rec.709); é gravada sem alteração. Use esta opção para saída de renderizador/compositor. (padrão: "sRGB") | COMBO | Sim (condicional) | `"sRGB"`<br>`"HDR"`<br>`"linear"` |

### Entradas de AVIF

Estas opções aparecem quando `format` está definido como `"avif"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `bit_depth` | A profundidade de bits para o arquivo AVIF salvo. Auto usa YUV420 de 8 bits para sRGB e YUV420 de 10 bits para HDR. (padrão: "auto") | COMBO | Sim (condicional) | `"auto"`<br>`"8-bit YUV420"`<br>`"10-bit YUV420"` |
| `input_color_space` | Espaço de cores das imagens de entrada. HDR seleciona BT.2020/HLG e HDR PQ seleciona BT.2020/PQ. (padrão: "sRGB") | COMBO | Sim (condicional) | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |
| `crf` | Valores menores produzem maior qualidade e arquivos maiores. (padrão: 18) | INT | Sim (condicional) | 1 a 63 |
| `save_mode` | O modo de salvamento para o arquivo AVIF. `"still images"` salva cada imagem do lote como um arquivo estático separado; `"animated"` salva o lote inteiro como um único arquivo AVIF animado e revela `fps` e `loop_count`. (padrão: "still images") | DYNAMIC_COMBO | Sim (condicional) | `"still images"`<br>`"animated"` |

### Opções de AVIF animado

Estas opções aparecem quando `save_mode` está definido como `"animated"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `fps` | A taxa de quadros da animação. (padrão: 6.0) | FLOAT | Sim (condicional) | 0.01 a 1000.0 |
| `loop_count` | Número de vezes para repetir a animação. 0 repete para sempre. (padrão: 0) | INT | Sim (condicional) | 0 a 1000 |

**Notas sobre dependências de parâmetros:**

- Os parâmetros específicos do formato (`bit_depth`, `input_color_space` e, para AVIF, também `crf` e `save_mode`) estão disponíveis apenas quando um `format` específico é selecionado.
- Para o formato PNG, apenas profundidades de bits "8-bit" e "16-bit" estão disponíveis, e apenas o espaço de cores "sRGB".
- Para o formato EXR, apenas a profundidade de bits "32-bit float" está disponível, com os espaços de cores "sRGB", "HDR" ou "linear".
- Para o formato AVIF, `fps` e `loop_count` estão disponíveis apenas quando `save_mode` está definido como `"animated"`.
- Imagens PNG e EXR devem ter 1 (tons de cinza), 3 (RGB) ou 4 (RGBA) canais; outras contagens de canais não são suportadas e geram erro.
- AVIF suporta apenas imagens de 1 canal em tons de cinza e 3 canais RGB; imagens RGBA (alfa) não são suportadas e geram erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `imagens` | As imagens de entrada, repassadas sem alteração. A saída da interface do nó fornece uma lista dos resultados de imagens salvas, cada um contendo o nome do arquivo, a subpasta e o tipo ("output"). | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageAdvanced/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d3df3caca99d58d973d0bc2ff7c22c4626185d390ec2acf870d4014331c4c335`
