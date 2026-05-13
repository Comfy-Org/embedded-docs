> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2TextToVideoNode/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2TextToVideoNode/en.md)

Este nó utiliza a API Seedance 2.0 da ByteDance para gerar um vídeo a partir de uma descrição textual. Ele envia seu prompt para o modelo selecionado, aguarda o processamento do vídeo e retorna o resultado final.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `model` | COMBO | Sim | `"Seedance 2.0"`<br>`"Seedance 2.0 Fast"` | O modelo a ser usado para geração de vídeo. Selecionar um modelo revelará entradas adicionais obrigatórias para o prompt, resolução, proporção de aspecto, duração e geração de áudio. "Seedance 2.0" é para máxima qualidade; "Seedance 2.0 Fast" é para otimização de velocidade. |
| `seed` | INT | Não | 0 a 2147483647 | Um valor de semente (padrão: 0). O nó será executado novamente se este valor mudar, mas os resultados são não determinísticos independentemente da semente. |
| `watermark` | BOOLEAN | Não | Verdadeiro / Falso | Se deve adicionar uma marca d'água ao vídeo (padrão: Falso). Esta é uma configuração avançada. |

**Nota:** O parâmetro `model` é uma combinação dinâmica. Ao selecionar um modelo, ele revelará vários subparâmetros obrigatórios que precisam ser preenchidos, incluindo o prompt de texto, resolução, proporção de aspecto, duração e se deve gerar áudio. O texto do prompt deve ter pelo menos 1 caractere após a remoção de espaços em branco.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `video` | VIDEO | O arquivo de vídeo gerado. |

---
**Source fingerprint (SHA-256):** `f8552e47667ff4b1ad3c8c1c074d70bdc45227b79b026b4b3c06986443655473`
