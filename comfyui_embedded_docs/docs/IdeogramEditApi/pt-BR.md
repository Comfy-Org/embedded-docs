# Ideogram 4.5 Edit

Edite ou combine até 5 imagens guiado por um prompt de texto com o Ideogram 4.5. A imagem 1 é a imagem a ser editada e as imagens seguintes são referências opcionais. A imagem inteira é renderizada novamente, então o tamanho ou a proporção do resultado pode mudar; use o Ideogram 4.5 Precise Edit para manter os pixels intocados inalterados.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modelo a usar. (padrão: `"ideogram-4.5"`) | DYNAMIC_COMBO | Sim | `"ideogram-4.5"` |
| `images` | Slot expansível: a imagem 1 é a imagem a ser editada e as imagens 2 a 5 são referências opcionais (`image_1` ... `image_5`). Consulte-as no prompt como @Image1, @Image2, ...; uma entrada em lote conta uma vez por imagem. Cada imagem deve ter uma proporção entre 1:6 e 6:1. | IMAGE | Sim | 1 a 5 imagens |
| `prompt` | Instruções de edição. Suporta referências no estilo @Image1 para as imagens conectadas. (padrão: string vazia) | STRING | Sim | 1 a 10000 caracteres |
| `size` | Tamanho de saída. `"auto"` escolhe uma tela de aproximadamente 2K a partir das imagens e do prompt, `"source"` mantém o tamanho da imagem 1 (imagens acima de cerca de 4 MP são reduzidas primeiro), e um preset com uma proporção diferente recompõe a cena. Selecione `"custom"` para usar a largura e a altura abaixo. (padrão: `"auto"`) | COMBO | Sim | `"auto"`<br>`"source"`<br>`"(2K) 2048x2048 (1:1)"`<br>`"(2K) 1440x2880 (1:2)"`<br>`"(2K) 2880x1440 (2:1)"`<br>`"(2K) 1664x2496 (2:3)"`<br>`"(2K) 2496x1664 (3:2)"`<br>`"(2K) 1792x2240 (4:5)"`<br>`"(2K) 2240x1792 (5:4)"`<br>`"(2K) 1440x2560 (9:16)"`<br>`"(2K) 2560x1440 (16:9)"`<br>`"(2K) 1600x2560 (5:8)"`<br>`"(2K) 2560x1600 (8:5)"`<br>`"(2K) 1728x2304 (3:4)"`<br>`"(2K) 2304x1728 (4:3)"`<br>`"(2K) 1152x2944 (9:23)"`<br>`"(2K) 2944x1152 (23:9)"`<br>`"(2K) 1248x3328 (3:8)"`<br>`"(2K) 3328x1248 (8:3)"`<br>`"(2K) 1280x3072 (5:12)"`<br>`"(2K) 3072x1280 (12:5)"`<br>`"(2K) 1024x3072 (1:3)"`<br>`"(2K) 3072x1024 (3:1)"`<br>`"(1K) 1024x1024 (1:1)"`<br>`"(1K) 896x1120 (4:5)"`<br>`"(1K) 1120x896 (5:4)"`<br>`"(1K) 864x1152 (3:4)"`<br>`"(1K) 1152x864 (4:3)"`<br>`"(1K) 832x1248 (2:3)"`<br>`"(1K) 1248x832 (3:2)"`<br>`"(1K) 800x1280 (5:8)"`<br>`"(1K) 1280x800 (8:5)"`<br>`"custom"` |
| `width` | Largura de saída personalizada em pixels. Usada apenas quando `size` é `"custom"`. (padrão: 2048) | INT | Sim | 256 a 4608 (passo: 32) |
| `height` | Altura de saída personalizada em pixels. Usada apenas quando `size` é `"custom"`. (padrão: 2048) | INT | Sim | 256 a 4608 (passo: 32) |
| `quality` | Nível de qualidade. Níveis mais altos custam mais e demoram mais. (padrão: `"medium"`) | COMBO | Sim | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |
| `seed` | Semente para geração. As mesmas imagens, prompt, configurações e semente geram o mesmo resultado. (padrão: 42) | INT | Sim | 0 a 2147483647 |

### Restrições de parâmetros

- **Contagem de imagens:** pelo menos 1 e no máximo 5 imagens; uma entrada em lote conta uma vez por imagem. A imagem 1 é a imagem a ser editada, as demais são referências.
- **Proporção das imagens:** cada imagem não pode ser mais larga que 6x sua altura nem mais alta que 6x sua largura (entre 1:6 e 6:1).
- **Tags do prompt:** `@ImageN` é correspondido sem diferenciar maiúsculas e minúsculas e não deve exceder o número de imagens conectadas; o prompt deve conter algo além de espaços em branco e ter no máximo 10000 caracteres.
- **Tamanho personalizado:** usado apenas quando `size` é `"custom"`. A largura vezes a altura não deve exceder 4194304 pixels (2048x2048), e o lado maior não deve exceder 6x o lado menor. A largura e a altura devem estar entre 256 e 4608 e são ajustadas para múltiplos de 32.
- **Escalonamento de upload:** imagens maiores que cerca de 4 MP, ou maiores que 4608 px no lado maior, são reduzidas antes de serem enviadas.
- **Segurança de conteúdo:** se o filtro de segurança de conteúdo do Ideogram bloquear o resultado, o nó gera um erro em vez de retornar uma imagem.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `IMAGE` | A(s) imagem(ns) editada(s) ou combinada(s) como um lote. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramEditApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `58c189d65502373ff7b56f5f32d9f2e7ee8019fc58f1bbbb80abc859cf978f67`
