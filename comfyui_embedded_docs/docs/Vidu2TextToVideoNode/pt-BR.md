> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2TextToVideoNode/pt-BR.md)

O nó de Geração de Vídeo de Texto para Vídeo Vidu2 cria um vídeo a partir de uma descrição textual. Ele se conecta a uma API externa para gerar conteúdo de vídeo com base no seu prompt, permitindo controlar a duração, o estilo visual e o formato do vídeo.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `modelo` | COMBO | Sim | `"viduq2"` | O modelo de IA a ser usado para geração de vídeo. Atualmente, apenas um modelo está disponível. |
| `prompt` | STRING | Sim | - | Uma descrição textual para geração de vídeo, com comprimento máximo de 2000 caracteres. |
| `duração` | INT | Não | 1 a 10 | A duração do vídeo gerado em segundos. O valor pode ser ajustado usando um controle deslizante (padrão: 5). |
| `semente` | INT | Não | 0 a 2147483647 | Um número usado para controlar a aleatoriedade da geração, permitindo resultados reproduzíveis. Pode ser controlado após a geração (padrão: 1). |
| `proporção` | COMBO | Não | `"16:9"`<br>`"9:16"`<br>`"3:4"`<br>`"4:3"`<br>`"1:1"` | A relação proporcional entre a largura e a altura do vídeo. |
| `resolução` | COMBO | Não | `"720p"`<br>`"1080p"` | As dimensões em pixels do vídeo gerado. Este é um parâmetro avançado. |
| `música_de_fundo` | BOOLEAN | Não | - | Se deve adicionar música de fundo ao vídeo gerado (padrão: False). Este é um parâmetro avançado. |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | VIDEO | O arquivo de vídeo gerado. |

---
**Source fingerprint (SHA-256):** `1e9e3629806e9b5a66d8f830d8ec33ef208a7a27b53caf43b44f7b746a85014b`
