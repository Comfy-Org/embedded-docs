# Ideogram 4.5 Texto para Imagem

Gerar imagens a partir de um prompt de texto com o Ideogram 4.6 ou 4.5. O prompt também aceita uma legenda JSON estruturada do Ideogram, por exemplo o `final_prompt` retornado por uma execução anterior, que oferece controle exato sobre strings de texto, cores e layout. O nó retorna a imagem junto com a legenda a partir da qual a imagem foi realmente gerada.

## Entradas

Selecionar um `model` determina quais entradas aparecem. O Ideogram 4.6 adiciona `background`, o nível de qualidade `very_low`, tamanhos `(4K)` e largura e altura personalizadas; o 4.5 mantém as predefinições `(1K)` e `(2K)`.

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Range |
|-----------|-------------|-----------|----------|-------|
| `modelo` | Modelo a usar. `"ideogram-4.6"` renderiza até 4K com fundo transparente opcional; `"ideogram-4.5"` é o modelo anterior (padrão: `"ideogram-4.6"`). | DYNAMIC_COMBO | Sim | `"ideogram-4.6"`<br>`"ideogram-4.5"` |
| `prompt` | Prompt de texto, ou uma legenda JSON estruturada do Ideogram, como um `final_prompt` anterior (padrão: string vazia). | STRING | Sim | 1 a 10000 caracteres |
| `magic_prompt` | Reescreve o prompt em uma legenda estruturada detalhada antes de gerar; `"off"` mantém sua formulação o mais literal possível. A legenda é retornada como `final_prompt` (padrão: `"auto"`). Esta é uma configuração avançada. | COMBO | Sim | `"auto"`<br>`"on"`<br>`"off"` |
| `seed` | Semente para a geração. Texto-para-imagem não é reproduzível apenas a partir da semente porque o prompt é reescrito a cada execução; para reproduzir uma imagem, reutilize seu `final_prompt` com `magic_prompt` definido como `"off"`, a mesma semente e as mesmas configurações de modelo, tamanho, qualidade e fundo (padrão: 42). | INT | Sim | 0 a 2147483647 |

### Entradas do Ideogram 4.6

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Range |
|-----------|-------------|-----------|----------|-------|
| `size` | Tamanho de saída. `"auto"` permite que o modelo escolha uma tela que se adeque ao prompt. Uma predefinição fixa tanto o tamanho em pixels quanto a proporção; os níveis `(1K)`, `(2K)` e `(4K)` descrevem o orçamento de pixels em vez de um lado longo fixo. Selecione `"custom"` para usar a largura e a altura abaixo (padrão: `"auto"`). | COMBO | Sim | `"auto"`<br>`"(1K) 1024x1024 (1:1)"`<br>`"(1K) 896x1120 (4:5)"`<br>`"(1K) 1120x896 (5:4)"`<br>`"(1K) 864x1152 (3:4)"`<br>`"(1K) 1152x864 (4:3)"`<br>`"(1K) 832x1248 (2:3)"`<br>`"(1K) 1248x832 (3:2)"`<br>`"(1K) 800x1280 (5:8)"`<br>`"(1K) 1280x800 (8:5)"`<br>`"(2K) 2048x2048 (1:1)"`<br>`"(2K) 1440x2880 (1:2)"`<br>`"(2K) 2880x1440 (2:1)"`<br>`"(2K) 1664x2496 (2:3)"`<br>`"(2K) 2496x1664 (3:2)"`<br>`"(2K) 1792x2240 (4:5)"`<br>`"(2K) 2240x1792 (5:4)"`<br>`"(2K) 1440x2560 (9:16)"`<br>`"(2K) 2560x1440 (16:9)"`<br>`"(2K) 1600x2560 (5:8)"`<br>`"(2K) 2560x1600 (8:5)"`<br>`"(2K) 1728x2304 (3:4)"`<br>`"(2K) 2304x1728 (4:3)"`<br>`"(2K) 1152x2944 (9:23)"`<br>`"(2K) 2944x1152 (23:9)"`<br>`"(2K) 1248x3328 (3:8)"`<br>`"(2K) 3328x1248 (8:3)"`<br>`"(2K) 1280x3072 (5:12)"`<br>`"(2K) 3072x1280 (12:5)"`<br>`"(2K) 1024x3072 (1:3)"`<br>`"(2K) 3072x1024 (3:1)"`<br>`"(4K) 4096x4096 (1:1)"`<br>`"(4K) 2880x5760 (1:2)"`<br>`"(4K) 5760x2880 (2:1)"`<br>`"(4K) 3328x4992 (2:3)"`<br>`"(4K) 4992x3328 (3:2)"`<br>`"(4K) 3584x4480 (4:5)"`<br>`"(4K) 4480x3584 (5:4)"`<br>`"(4K) 2880x5120 (9:16)"`<br>`"(4K) 5120x2880 (16:9)"`<br>`"(4K) 3200x5120 (5:8)"`<br>`"(4K) 5120x3200 (8:5)"`<br>`"(4K) 3456x4608 (3:4)"`<br>`"(4K) 4608x3456 (4:3)"`<br>`"(4K) 2304x5888 (9:23)"`<br>`"(4K) 5888x2304 (23:9)"`<br>`"(4K) 2496x6656 (3:8)"`<br>`"(4K) 6656x2496 (8:3)"`<br>`"(4K) 2560x6144 (5:12)"`<br>`"(4K) 6144x2560 (12:5)"`<br>`"(4K) 2048x6144 (1:3)"`<br>`"(4K) 6144x2048 (3:1)"`<br>`"custom"` |
| `width` | Largura de saída personalizada em pixels, usada apenas quando `size` é `"custom"` (padrão: 2048). | INT | Sim | 256 a 8192 (passo 32) |
| `height` | Altura de saída personalizada em pixels, usada apenas quando `size` é `"custom"` (padrão: 2048). | INT | Sim | 256 a 8192 (passo 32) |
| `quality` | Nível de qualidade. Níveis mais altos custam mais e demoram mais (padrão: `"medium"`). | COMBO | Sim | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |
| `background` | `"transparent"` retorna a imagem com canal alfa, `"opaque"` força um fundo sólido, `"auto"` segue o prompt (padrão: `"auto"`). | COMBO | Sim | `"auto"`<br>`"opaque"`<br>`"transparent"` |

### Entradas do Ideogram 4.5

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Range |
|-----------|-------------|-----------|----------|-------|
| `size` | Tamanho de saída. `"auto"` permite que o modelo escolha uma tela que se adeque ao prompt; uma predefinição fixa tanto o tamanho em pixels quanto a proporção (padrão: `"auto"`). | COMBO | Sim | `"auto"`<br>`"(2K) 2048x2048 (1:1)"`<br>`"(2K) 1440x2880 (1:2)"`<br>`"(2K) 2880x1440 (2:1)"`<br>`"(2K) 1664x2496 (2:3)"`<br>`"(2K) 2496x1664 (3:2)"`<br>`"(2K) 1792x2240 (4:5)"`<br>`"(2K) 2240x1792 (5:4)"`<br>`"(2K) 1440x2560 (9:16)"`<br>`"(2K) 2560x1440 (16:9)"`<br>`"(2K) 1600x2560 (5:8)"`<br>`"(2K) 2560x1600 (8:5)"`<br>`"(2K) 1728x2304 (3:4)"`<br>`"(2K) 2304x1728 (4:3)"`<br>`"(2K) 1296x3168 (9:22)"`<br>`"(2K) 3168x1296 (22:9)"`<br>`"(2K) 1152x2944 (9:23)"`<br>`"(2K) 2944x1152 (23:9)"`<br>`"(2K) 1248x3328 (3:8)"`<br>`"(2K) 3328x1248 (8:3)"`<br>`"(2K) 1280x3072 (5:12)"`<br>`"(2K) 3072x1280 (12:5)"`<br>`"(2K) 1024x3072 (1:3)"`<br>`"(2K) 3072x1024 (3:1)"`<br>`"(1K) 1024x1024 (1:1)"`<br>`"(1K) 896x1120 (4:5)"`<br>`"(1K) 1120x896 (5:4)"`<br>`"(1K) 864x1152 (3:4)"`<br>`"(1K) 1152x864 (4:3)"`<br>`"(1K) 832x1248 (2:3)"`<br>`"(1K) 1248x832 (3:2)"`<br>`"(1K) 800x1280 (5:8)"`<br>`"(1K) 1280x800 (8:5)"`<br>`"(1K) 720x1280 (9:16)"`<br>`"(1K) 1280x720 (16:9)"`<br>`"(1K) 720x1440 (1:2)"`<br>`"(1K) 1440x720 (2:1)"` |
| `quality` | Nível de qualidade. Níveis mais altos custam mais e demoram mais (padrão: `"medium"`). | COMBO | Sim | `"low"`<br>`"medium"`<br>`"high"` |

### Restrições de parâmetros

- **Prompt:** pelo menos um caractere não em branco e no máximo 10000 caracteres. Defina `magic_prompt` como `"off"` ao fornecer sua própria legenda JSON.
- **Tamanho personalizado (4.6):** largura vezes altura não deve exceder 16,777,216 pixels (4096x4096), cada lado deve estar entre 256 e 8192 e alinhado a um múltiplo de 32, e o lado mais longo não deve exceder 6x o lado mais curto.
- **Qualidade `very_low` (4.6):** limitada a 4,194,304 pixels (2048x2048); tamanhos maiores geram um erro.
- **Reprodutibilidade:** com `magic_prompt` definido como `"auto"` ou `"on"`, o prompt é reescrito a cada execução, então a mesma semente pode produzir uma imagem diferente.
- **Segurança de conteúdo:** se o filtro de segurança de conteúdo do Ideogram bloquear a geração, o nó gera um erro em vez de retornar uma imagem.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `IMAGE` | A imagem gerada como um lote. | IMAGE |
| `final_prompt` | A legenda estruturada a partir da qual a imagem foi gerada. Realimente-a com `magic_prompt` definido como `"off"` e a mesma semente, modelo, tamanho, qualidade e fundo para reproduzir a imagem. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramTextToImageApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `953fee48c0337e6ded4e72332c27279496eeb9c108c0700c2fa14095855047f1`
