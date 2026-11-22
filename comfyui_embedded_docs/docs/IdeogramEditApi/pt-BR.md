# Ideogram 4.5 Editar

Edite ou combine até 5 imagens guiado por um prompt de texto com o Ideogram 4.6 ou 4.5. A imagem 1 é a imagem a ser editada, e as imagens seguintes são referências opcionais. A imagem inteira é renderizada novamente, portanto o tamanho ou a proporção do resultado podem mudar; use o Ideogram Precise Edit para manter os pixels intocados inalterados e editar uma região nele quando uma origem grande precisar manter sua resolução exata, porque uma edição da imagem inteira é reduzida primeiro.

## Entradas

A seleção de um `model` determina quais entradas aparecem. O Ideogram 4.6 adiciona `background`, tamanhos `(4K)` e tamanhos personalizados de até 8192 pixels por lado; o 4.5 mantém as predefinições `(1K)` e `(2K)` com no máximo 4608 pixels por lado. Ambos os modelos oferecem aqui os níveis de qualidade `very_low`, `low`, `medium` e `high`.

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `modelo` | Modelo a usar. `"ideogram-4.6"` renderiza até 4K com um fundo transparente opcional; `"ideogram-4.5"` é o modelo anterior (padrão: `"ideogram-4.6"`). | DYNAMIC_COMBO | Sim | `"ideogram-4.6"`<br>`"ideogram-4.5"` |
| `images` | Slot expansível: a imagem 1 é a imagem a ser editada, e as imagens 2 a 5 são referências opcionais (`image_1` ... `image_5`). Refira-se a elas no prompt como @Image1, @Image2, ...; uma entrada em lote conta uma vez por imagem. Cada imagem deve ter uma proporção entre 1:6 e 6:1. | IMAGE | Sim | 1 a 5 imagens |
| `prompt` | Instruções de edição. Suporta referências no estilo @Image1 para as imagens conectadas (padrão: string vazia). | STRING | Sim | 1 a 10000 caracteres |
| `seed` | Semente para a geração. As mesmas imagens, prompt, configurações e seed produzem o mesmo resultado ou um resultado muito semelhante (padrão: 42). | INT | Sim | 0 a 2147483647 |

### Entradas do Ideogram 4.6

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `size` | Tamanho da saída. `"auto"` escolhe uma tela de aproximadamente 2K a partir das imagens e do prompt, `"source"` mantém o tamanho da imagem 1 (imagens acima de 16,7 MP, ou com qualquer lado acima de 8192 pixels, são reduzidas primeiro), e uma predefinição com uma proporção diferente recompõe a cena. Selecione `"custom"` para usar a largura e a altura abaixo (padrão: `"auto"`). | COMBO | Sim | `"auto"`<br>`"source"`<br>`"(1K) 1024x1024 (1:1)"`<br>`"(1K) 896x1120 (4:5)"`<br>`"(1K) 1120x896 (5:4)"`<br>`"(1K) 864x1152 (3:4)"`<br>`"(1K) 1152x864 (4:3)"`<br>`"(1K) 832x1248 (2:3)"`<br>`"(1K) 1248x832 (3:2)"`<br>`"(1K) 800x1280 (5:8)"`<br>`"(1K) 1280x800 (8:5)"`<br>`"(2K) 2048x2048 (1:1)"`<br>`"(2K) 1440x2880 (1:2)"`<br>`"(2K) 2880x1440 (2:1)"`<br>`"(2K) 1664x2496 (2:3)"`<br>`"(2K) 2496x1664 (3:2)"`<br>`"(2K) 1792x2240 (4:5)"`<br>`"(2K) 2240x1792 (5:4)"`<br>`"(2K) 1440x2560 (9:16)"`<br>`"(2K) 2560x1440 (16:9)"`<br>`"(2K) 1600x2560 (5:8)"`<br>`"(2K) 2560x1600 (8:5)"`<br>`"(2K) 1728x2304 (3:4)"`<br>`"(2K) 2304x1728 (4:3)"`<br>`"(2K) 1152x2944 (9:23)"`<br>`"(2K) 2944x1152 (23:9)"`<br>`"(2K) 1248x3328 (3:8)"`<br>`"(2K) 3328x1248 (8:3)"`<br>`"(2K) 1280x3072 (5:12)"`<br>`"(2K) 3072x1280 (12:5)"`<br>`"(2K) 1024x3072 (1:3)"`<br>`"(2K) 3072x1024 (3:1)"`<br>`"(4K) 4096x4096 (1:1)"`<br>`"(4K) 2880x5760 (1:2)"`<br>`"(4K) 5760x2880 (2:1)"`<br>`"(4K) 3328x4992 (2:3)"`<br>`"(4K) 4992x3328 (3:2)"`<br>`"(4K) 3584x4480 (4:5)"`<br>`"(4K) 4480x3584 (5:4)"`<br>`"(4K) 2880x5120 (9:16)"`<br>`"(4K) 5120x2880 (16:9)"`<br>`"(4K) 3200x5120 (5:8)"`<br>`"(4K) 5120x3200 (8:5)"`<br>`"(4K) 3456x4608 (3:4)"`<br>`"(4K) 4608x3456 (4:3)"`<br>`"(4K) 2304x5888 (9:23)"`<br>`"(4K) 5888x2304 (23:9)"`<br>`"(4K) 2496x6656 (3:8)"`<br>`"(4K) 6656x2496 (8:3)"`<br>`"(4K) 2560x6144 (5:12)"`<br>`"(4K) 6144x2560 (12:5)"`<br>`"(4K) 2048x6144 (1:3)"`<br>`"(4K) 6144x2048 (3:1)"`<br>`"custom"` |
| `width` | Largura personalizada da saída em pixels, usada apenas quando `size` é `"custom"` (padrão: 2048). | INT | Sim | 256 a 8192 (passo 32) |
| `height` | Altura personalizada da saída em pixels, usada apenas quando `size` é `"custom"` (padrão: 2048). | INT | Sim | 256 a 8192 (passo 32) |
| `quality` | Nível de qualidade. Níveis mais altos custam mais e levam mais tempo (padrão: `"medium"`). | COMBO | Sim | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |
| `background` | `"transparent"` retorna a imagem com canal alfa, `"opaque"` força um fundo sólido, `"auto"` segue o prompt (padrão: `"auto"`). | COMBO | Sim | `"auto"`<br>`"opaque"`<br>`"transparent"` |

### Entradas do Ideogram 4.5

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `size` | Tamanho da saída. `"auto"` escolhe uma tela de aproximadamente 2K a partir das imagens e do prompt, `"source"` mantém o tamanho da imagem 1 (imagens acima de cerca de 4 MP, ou com qualquer lado acima de 4608 pixels, são reduzidas primeiro), e uma predefinição com uma proporção diferente recompõe a cena. Selecione `"custom"` para usar a largura e a altura abaixo (padrão: `"auto"`). | COMBO | Sim | `"auto"`<br>`"source"`<br>`"(2K) 2048x2048 (1:1)"`<br>`"(2K) 1440x2880 (1:2)"`<br>`"(2K) 2880x1440 (2:1)"`<br>`"(2K) 1664x2496 (2:3)"`<br>`"(2K) 2496x1664 (3:2)"`<br>`"(2K) 1792x2240 (4:5)"`<br>`"(2K) 2240x1792 (5:4)"`<br>`"(2K) 1440x2560 (9:16)"`<br>`"(2K) 2560x1440 (16:9)"`<br>`"(2K) 1600x2560 (5:8)"`<br>`"(2K) 2560x1600 (8:5)"`<br>`"(2K) 1728x2304 (3:4)"`<br>`"(2K) 2304x1728 (4:3)"`<br>`"(2K) 1152x2944 (9:23)"`<br>`"(2K) 2944x1152 (23:9)"`<br>`"(2K) 1248x3328 (3:8)"`<br>`"(2K) 3328x1248 (8:3)"`<br>`"(2K) 1280x3072 (5:12)"`<br>`"(2K) 3072x1280 (12:5)"`<br>`"(2K) 1024x3072 (1:3)"`<br>`"(2K) 3072x1024 (3:1)"`<br>`"(1K) 1024x1024 (1:1)"`<br>`"(1K) 896x1120 (4:5)"`<br>`"(1K) 1120x896 (5:4)"`<br>`"(1K) 864x1152 (3:4)"`<br>`"(1K) 1152x864 (4:3)"`<br>`"(1K) 832x1248 (2:3)"`<br>`"(1K) 1248x832 (3:2)"`<br>`"(1K) 800x1280 (5:8)"`<br>`"(1K) 1280x800 (8:5)"`<br>`"custom"` |
| `width` | Largura personalizada da saída em pixels, usada apenas quando `size` é `"custom"` (padrão: 2048). | INT | Sim | 256 a 4608 (passo 32) |
| `height` | Altura personalizada da saída em pixels, usada apenas quando `size` é `"custom"` (padrão: 2048). | INT | Sim | 256 a 4608 (passo 32) |
| `quality` | Nível de qualidade. Níveis mais altos custam mais e levam mais tempo (padrão: `"medium"`). | COMBO | Sim | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |

### Restrições dos parâmetros

- **Contagem de imagens:** pelo menos 1 e no máximo 5 imagens; uma entrada em lote conta uma vez por imagem. A imagem 1 é a imagem a ser editada; as demais são referências.
- **Proporção das imagens:** cada imagem não pode ser mais larga que 6x sua altura nem mais alta que 6x sua largura (entre 1:6 e 6:1).
- **Tags do prompt:** `@ImageN` é correspondido sem diferenciar maiúsculas de minúsculas e não deve exceder o número de imagens conectadas; o prompt não pode conter apenas espaços em branco e deve ter no máximo 10000 caracteres.
- **Tamanho personalizado:** a largura vezes a altura não deve exceder 16,7 MP (4096x4096) no 4.6 e 4194304 pixels (2048x2048) no 4.5, e o lado mais longo não deve exceder 6x o lado mais curto. A largura e a altura são ajustadas para múltiplos de 32.
- **Dimensionamento no upload:** o 4.6 envia a imagem 1 com até 16,7 MP e 8192 pixels por lado, recodificando-a como JPEG quando isso a mantém abaixo do limite de upload; o 4.5 reduz a imagem 1 acima de cerca de 4 MP ou 4608 pixels por lado.
- **Segurança de conteúdo:** se o filtro de segurança de conteúdo do Ideogram bloquear o resultado, o nó gera um erro em vez de retornar uma imagem.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `IMAGE` | A imagem editada ou combinada como um lote. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramEditApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `58c189d65502373ff7b56f5f32d9f2e7ee8019fc58f1bbbb80abc859cf978f67`
