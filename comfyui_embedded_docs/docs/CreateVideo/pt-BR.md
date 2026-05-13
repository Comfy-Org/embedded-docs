> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateVideo/pt-BR.md)

Este documento foi gerado por IA. Se encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateVideo/en.md)

O nó Criar Vídeo gera um arquivo de vídeo a partir de uma sequência de imagens. Você pode especificar a velocidade de reprodução usando quadros por segundo e, opcionalmente, adicionar áudio ao vídeo. O nó combina suas imagens em um formato de vídeo que pode ser reproduzido com a taxa de quadros especificada.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `images` | IMAGE | Sim | - | As imagens para criar um vídeo. |
| `fps` | FLOAT | Sim | 1.0 - 120.0 | Os quadros por segundo para a velocidade de reprodução do vídeo (padrão: 30.0). |
| `audio` | AUDIO | Não | - | O áudio a ser adicionado ao vídeo. |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | VIDEO | O arquivo de vídeo gerado contendo as imagens de entrada e o áudio opcional. |

---
**Source fingerprint (SHA-256):** `6da9a09542b5e357c0180c30018ec10facf06d1bdd3e4edee8172b8426802e3d`
