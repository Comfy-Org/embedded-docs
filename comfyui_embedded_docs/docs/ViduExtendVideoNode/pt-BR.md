# Extensão de Vídeo Vidu

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduExtendVideoNode/en.md)

O ViduExtendVideoNode gera quadros adicionais para estender a duração de um vídeo existente. Ele usa um modelo de IA especificado para criar uma continuação contínua com base no vídeo de origem e em um prompt de texto opcional.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo de IA a ser usado para extensão de vídeo. Selecionar um modelo revela suas configurações específicas de duração e resolução. | COMBO | Sim | `"viduq2-pro"`<br>`"viduq2-turbo"` |
| `model.duration` | A duração do vídeo estendido em segundos (padrão: 4). Esta configuração aparece após selecionar um modelo. | INT | Sim | 1 a 7 |
| `model.resolution` | A resolução do vídeo de saída. Esta configuração aparece após selecionar um modelo. | COMBO | Sim | `"720p"`<br>`"1080p"` |
| `vídeo` | O vídeo de origem a ser estendido. | VIDEO | Sim | - |
| `prompt` | Um prompt de texto opcional para orientar o conteúdo do vídeo estendido (máximo de 2000 caracteres, padrão: vazio). | STRING | Não | - |
| `semente` | Um valor de semente para controlar a aleatoriedade da geração (padrão: 1). | INT | Não | 0 a 2147483647 |
| `quadro_final` | Uma imagem opcional para usar como quadro final alvo para a extensão. Se fornecida, sua proporção de aspecto deve estar entre 1:4 e 4:1, e suas dimensões devem ter pelo menos 128x128 pixels. | IMAGE | Não | - |

**Nota:** O `video` de origem deve ter uma duração entre 4 e 55 segundos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | O arquivo de vídeo recém-gerado contendo a filmagem estendida. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduExtendVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `44b942413c8aed2fc0049386a31c441f6f870ba4220b0c439dfc436079229446`
