Este documento foi gerado por IA. Se encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateVideo/en.md)

O nó Criar Vídeo gera um arquivo de vídeo a partir de uma sequência de imagens. Você pode especificar a velocidade de reprodução usando quadros por segundo e, opcionalmente, adicionar áudio ao vídeo. O nó combina suas imagens em um formato de vídeo que pode ser reproduzido com a taxa de quadros especificada.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `imagens` | As imagens para criar um vídeo. | IMAGE | Sim | - |
| `fps` | Os quadros por segundo para a velocidade de reprodução do vídeo (padrão: 30.0). | FLOAT | Sim | 1.0 - 120.0 |
| `áudio` | O áudio a ser adicionado ao vídeo. | AUDIO | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | O arquivo de vídeo gerado contendo as imagens de entrada e o áudio opcional. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `6da9a09542b5e357c0180c30018ec10facf06d1bdd3e4edee8172b8426802e3d`
