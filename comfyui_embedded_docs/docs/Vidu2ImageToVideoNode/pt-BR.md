> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2ImageToVideoNode/pt-BR.md)

O nó Vidu2 de Geração de Vídeo a partir de Imagem cria uma sequência de vídeo a partir de uma única imagem de entrada. Ele utiliza um modelo Vidu2 especificado para animar a cena com base em um prompt de texto opcional, controlando a duração, resolução e intensidade do movimento do vídeo.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `modelo` | COMBO | Sim | `"viduq2-pro-fast"`<br>`"viduq2-pro"`<br>`"viduq2-turbo"` | O modelo Vidu2 a ser usado para geração de vídeo. Diferentes modelos oferecem diferentes compensações entre velocidade e qualidade. |
| `imagem` | IMAGE | Sim | - | Uma imagem a ser usada como quadro inicial do vídeo gerado. Apenas uma imagem é permitida. |
| `prompt` | STRING | Não | - | Um prompt de texto opcional para geração de vídeo (máximo de 2000 caracteres). O padrão é uma string vazia. |
| `duração` | INT | Sim | 1 a 10 | A duração do vídeo gerado em segundos. O padrão é 5. |
| `semente` | INT | Não | 0 a 2147483647 | Um valor de semente para geração de números aleatórios, garantindo resultados reproduzíveis. O padrão é 1. |
| `resolução` | COMBO | Sim | `"720p"`<br>`"1080p"` | A resolução de saída do vídeo gerado. Este parâmetro é avançado. |
| `amplitude_de_movimento` | COMBO | Sim | `"auto"`<br>`"small"`<br>`"medium"`<br>`"large"` | A amplitude de movimento dos objetos no quadro. Este parâmetro é avançado. |

**Restrições:**

* A entrada `image` deve conter exatamente uma imagem.
* A proporção de aspecto da imagem de entrada deve estar entre 1:4 e 4:1.
* O texto do `prompt` é limitado a um máximo de 2000 caracteres.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | VIDEO | O arquivo de vídeo gerado. |

---
**Source fingerprint (SHA-256):** `204f8d2b9edf17c2c180480f98a852718416a54725d92e5fec574b8517ada398`
