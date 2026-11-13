# Salvar Imagem (Avançado)

O nó **Save Image (Advanced)** salva as imagens de entrada no diretório de saída do ComfyUI com controle avançado sobre formato de arquivo, profundidade de bits e espaço de cor. Ele oferece suporte a salvar como arquivos PNG, EXR ou AVIF (incluindo AVIF animado) e pode incorporar metadados do fluxo de trabalho nos arquivos salvos.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `images` | As imagens a salvar. | IMAGE | Sim | - |
| `filename_prefix` | O prefixo do arquivo a salvar. Pode incluir tokens de formatação como `%date:yyyy-MM-dd%` ou `%Empty Latent Image.width%`. (padrão: "ComfyUI") | STRING | Sim | - |
| `format` | O formato de arquivo no qual salvar a imagem. Selecionar um formato revela opções adicionais para esse formato. | DYNAMIC_COMBO | Sim | `"png"`<br>`"exr"`<br>`"avif"` |

### Entradas PNG

Estas opções aparecem quando `format` está definido como `"png"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `bit_depth` | A profundidade de bits do arquivo PNG salvo. (padrão: "8-bit") | COMBO | Sim (condicional) | `"8-bit"`<br>`"16-bit"` |
| `input_color_space` | Espaço de cor do tensor de entrada. Apenas sRGB está disponível para o formato PNG. (padrão: "sRGB") | COMBO | Sim (condicional) | `"sRGB"` |
| `channels` | Quais canais gravar no PNG. `"auto"` mantém os canais de entrada, escala de cinza converte RGB em brilho e descarta o alfa, RGB salva cor sem alfa, e RGBA mantém o alfa ou adiciona um totalmente opaco. (padrão: `"auto"`) | COMBO | Não | `"auto"`<br>`"grayscale (1 channel)"`<br>`"RGB (3 channels)"`<br>`"RGBA (4 channels)"` |

### Entradas EXR

Estas opções aparecem quando `format` está definido como `"exr"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `bit_depth` | A profundidade de bits do arquivo EXR salvo. (padrão: "16-bit float") | COMBO | Sim (condicional) | `"16-bit float"`<br>`"32-bit float"` |
| `input_color_space` | Espaço de cor do tensor de entrada. O EXR é sempre gravado como linear de cena (scene-linear) no gamut correspondente.<br>`"sRGB"` — a entrada é Rec.709 codificada em sRGB; a EOTF sRGB inversa é aplicada.<br>`"HDR"` — a entrada é Rec.2020 (BT.2100) codificada em HLG; a OETF HLG inversa é aplicada para obter luz linear de cena.<br>`"linear"` — a entrada já é linear de cena (primárias Rec.709); gravada sem alterações. Use isto para saída de renderizador/compositor.<br>`"linear ACEScg"` — a entrada já é ACEScg linear de cena (AP1 / D60); gravada sem alterações com cromaticidades ACEScg. (padrão: "sRGB") | COMBO | Sim (condicional) | `"sRGB"`<br>`"HDR"`<br>`"linear"`<br>`"linear ACEScg"` |

### Entradas AVIF

Estas opções aparecem quando `format` está definido como `"avif"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `bit_depth` | A profundidade de bits do arquivo AVIF salvo. A opção automática usa YUV420 de 8 bits para sRGB e YUV420 de 10 bits para HDR. (padrão: "auto") | COMBO | Sim (condicional) | `"auto"`<br>`"8-bit YUV420"`<br>`"10-bit YUV420"` |
| `input_color_space` | Espaço de cor das imagens de entrada. HDR seleciona BT.2020/HLG e HDR PQ seleciona BT.2020/PQ. (padrão: "sRGB") | COMBO | Sim (condicional) | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |
| `crf` | Valores menores produzem maior qualidade e arquivos maiores. (padrão: 18) | INT | Sim (condicional) | 1 a 63 |
| `save_mode` | O modo de salvamento do arquivo AVIF. `"still images"` salva cada imagem do lote como um arquivo estático separado; `"animated"` salva o lote inteiro como um único arquivo AVIF animado e exibe `fps` e `loop_count`. (padrão: "still images") | DYNAMIC_COMBO | Sim (condicional) | `"still images"`<br>`"animated"` |

### Opções de AVIF animado

Estas opções aparecem quando `save_mode` está definido como `"animated"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `fps` | A taxa de quadros da animação. (padrão: 6.0) | FLOAT | Sim (condicional) | 0.01 a 1000.0 |
| `loop_count` | Número de vezes que a animação deve ser repetida. 0 repete infinitamente. (padrão: 0) | INT | Sim (condicional) | 0 a 1000 |

**Notas sobre dependências de parâmetros:**
- Os parâmetros específicos de formato (`bit_depth`, `input_color_space` e, para AVIF, também `crf` e `save_mode`) só estão disponíveis quando um `format` específico é selecionado.
- Para o formato PNG, apenas as profundidades de bits "8-bit" e "16-bit" estão disponíveis, e apenas o espaço de cor "sRGB".
- Para o formato EXR, tanto as profundidades de bits "16-bit float" quanto "32-bit float" estão disponíveis, com os espaços de cor "sRGB", "HDR", "linear" ou "linear ACEScg". "16-bit float" é o padrão e produz arquivos menores.
- Para o formato AVIF, `fps` e `loop_count` só estão disponíveis quando `save_mode` está definido como `"animated"`.
- Imagens PNG e EXR devem ter 1 (escala de cinza), 3 (RGB) ou 4 (RGBA) canais; outras contagens de canais não são suportadas e geram um erro.
- O AVIF suporta apenas imagens em escala de cinza de 1 canal e RGB de 3 canais; imagens RGBA (alfa) não são suportadas e geram um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `images` | As imagens de entrada, repassadas sem alterações. A saída de UI do nó fornece uma lista de resultados de imagens salvas, cada um contendo o nome do arquivo, a subpasta e o tipo ("output"). Para AVIF animado com mais de uma imagem, a saída de UI também inclui um sinalizador `animated`. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageAdvanced/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4e8a92c5f1bba35bc4cdf8c858cc9a6fe57cf08436e2dc303d8204c726108216`
