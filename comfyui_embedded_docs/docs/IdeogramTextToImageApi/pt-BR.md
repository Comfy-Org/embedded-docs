# Ideogram 4.5 Text to Image

Gere imagens a partir de um prompt de texto com o Ideogram 4.5. O prompt também aceita uma legenda JSON estruturada do Ideogram, por exemplo o `final_prompt` retornado por uma execução anterior, o que oferece controle exato sobre strings de texto, cores e layout. O nó retorna a(s) imagem(ns) gerada(s) junto com a legenda a partir da qual a imagem foi realmente gerada.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `modelo` | Modelo a usar. (padrão: `"ideogram-4.5"`) | DYNAMIC_COMBO | Sim | `"ideogram-4.5"` |
| `prompt` | Prompt de texto, ou uma legenda JSON estruturada do Ideogram, como um `final_prompt` anterior. (padrão: string vazia) | STRING | Sim | 1 a 10000 caracteres |
| `size` | Tamanho da saída. `"auto"` permite que o modelo escolha uma tela que se adeque ao prompt. Um preset `(2K)` ou `(1K)` fixa tanto o tamanho em pixels quanto a proporção de aspecto. (padrão: `"auto"`) | COMBO | Sim | `"auto"`<br>`"(2K) 2048x2048 (1:1)"`<br>`"(2K) 1440x2880 (1:2)"`<br>`"(2K) 2880x1440 (2:1)"`<br>`"(2K) 1664x2496 (2:3)"`<br>`"(2K) 2496x1664 (3:2)"`<br>`"(2K) 1792x2240 (4:5)"`<br>`"(2K) 2240x1792 (5:4)"`<br>`"(2K) 1440x2560 (9:16)"`<br>`"(2K) 2560x1440 (16:9)"`<br>`"(2K) 1600x2560 (5:8)"`<br>`"(2K) 2560x1600 (8:5)"`<br>`"(2K) 1728x2304 (3:4)"`<br>`"(2K) 2304x1728 (4:3)"`<br>`"(2K) 1296x3168 (9:22)"`<br>`"(2K) 3168x1296 (22:9)"`<br>`"(2K) 1152x2944 (9:23)"`<br>`"(2K) 2944x1152 (23:9)"`<br>`"(2K) 1248x3328 (3:8)"`<br>`"(2K) 3328x1248 (8:3)"`<br>`"(2K) 1280x3072 (5:12)"`<br>`"(2K) 3072x1280 (12:5)"`<br>`"(2K) 1024x3072 (1:3)"`<br>`"(2K) 3072x1024 (3:1)"`<br>`"(1K) 1024x1024 (1:1)"`<br>`"(1K) 896x1120 (4:5)"`<br>`"(1K) 1120x896 (5:4)"`<br>`"(1K) 864x1152 (3:4)"`<br>`"(1K) 1152x864 (4:3)"`<br>`"(1K) 832x1248 (2:3)"`<br>`"(1K) 1248x832 (3:2)"`<br>`"(1K) 800x1280 (5:8)"`<br>`"(1K) 1280x800 (8:5)"`<br>`"(1K) 720x1280 (9:16)"`<br>`"(1K) 1280x720 (16:9)"`<br>`"(1K) 720x1440 (1:2)"`<br>`"(1K) 1440x720 (2:1)"` |
| `quality` | Nível de qualidade. Níveis mais altos custam mais e demoram mais. (padrão: `"medium"`) | COMBO | Sim | `"low"`<br>`"medium"`<br>`"high"` |
| `magic_prompt` | Reescreve o prompt em uma legenda estruturada detalhada antes de gerar; `"off"` mantém sua formulação o mais literal possível. A legenda é retornada como `final_prompt`. (padrão: `"auto"`) Esta é uma configuração avançada. | COMBO | Sim | `"auto"`<br>`"on"`<br>`"off"` |
| `seed` | Semente para geração. Texto para imagem não é reproduzível apenas com a semente porque o prompt é reescrito a cada execução; para reproduzir uma imagem, reutilize seu `final_prompt` com `magic_prompt` definido como `"off"` e a mesma semente. (padrão: 42) | INT | Sim | 0 a 2147483647 |

### Restrições dos parâmetros

- **Prompt obrigatório:** o prompt deve conter pelo menos um caractere que não seja espaço em branco e no máximo 10000 caracteres. Defina `magic_prompt` como `"off"` ao fornecer sua própria legenda JSON ou texto exato.
- **Tamanho:** `"auto"` permite que o modelo escolha. Presets `(2K)` têm cerca de 3 a 4 megapixels e presets `(1K)` cerca de 1 megapixel, então o rótulo do nível descreve o orçamento de pixels em vez de um lado maior fixo; a proporção de aspecto do preset é respeitada. Apenas a parte do tamanho em pixels do preset é enviada para a API.
- **Reprodutibilidade:** com `magic_prompt` definido como `"auto"` ou `"on"`, o prompt é reescrito a cada execução, então a mesma semente ainda pode produzir uma imagem diferente. Para reproduzir uma imagem, envie seu `final_prompt` de volta com `magic_prompt` definido como `"off"` e a mesma semente.
- **Segurança de conteúdo:** se o filtro de segurança de conteúdo do Ideogram bloquear a geração, o nó lança um erro em vez de retornar uma imagem.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `IMAGE` | A(s) imagem(ns) gerada(s) como um lote. | IMAGE |
| `final_prompt` | A legenda estruturada a partir da qual a imagem foi gerada. Envie-a de volta com `magic_prompt` definido como `"off"` e a mesma semente para reproduzir a imagem. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramTextToImageApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a21f1faed9ca7a7bc63dae74003cc7599f11013075f718af9e5860d2cd666828`
