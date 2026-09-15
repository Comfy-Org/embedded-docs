# Flux 3 Texto para Vídeo

Gera um vídeo com áudio sincronizado a partir de um prompt de texto usando o FLUX 3. O nó envia seu prompt para o serviço FLUX 3, aguarda a conclusão da geração e retorna o clipe de vídeo pronto.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | O que você deseja, em linguagem natural; o prompt é interpretado e expandido antes da geração. Descreva som ambiente, música e fala separadamente para obter um áudio em camadas. (padrão: "") | STRING | Sim | Texto multilinha |
| `aspect_ratio` | Proporção de aspecto da saída. 'auto' escolhe uma com base no prompt e nas entradas. (padrão: "auto") | COMBO | Sim | Várias opções disponíveis, incluindo `"auto"` |
| `duration` | Duração do clipe em segundos. 'auto' ajusta a duração ao conteúdo. (padrão: "auto") | COMBO | Sim | Várias opções disponíveis, incluindo `"auto"` |
| `resolution` | Resolução da saída. (padrão: "720p") | COMBO | Sim | `"720p"`<br>`"1080p"` |
| `generate_audio` | Gera áudio sincronizado (ambiente, fala, efeitos). Desativado, produz um vídeo sem faixa de áudio. (padrão: True) | BOOLEAN | Sim | True<br>False |
| `safety_tolerance` | Tolerância de moderação; 0 é a mais restritiva. Requisições que enviam imagens ou vídeo ficam limitadas a 2, independentemente do que for definido aqui. (padrão: 2) | INT | Sim | 0 a 4 |
| `seed` | Semente para determinar se o nó deve ser executado novamente; o FLUX 3 escolhe sua própria semente, portanto os resultados reais são não determinísticos independentemente deste valor. (padrão: 42) | INT | Sim | 0 a 4294967295 |

Observação: `safety_tolerance` é uma entrada avançada. A entrada `seed` inclui os controles de Control After Generate na interface. O preço exibido é baseado em `resolution` e `duration`: HD (720p) é cobrado a $0.2431 por segundo e FHD (1080p) a $0.4147 por segundo. Quando uma duração fixa é escolhida, o custo total estimado do clipe é exibido; quando `duration` é "auto", a taxa por segundo é exibida.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `video` | O clipe de vídeo gerado, com áudio sincronizado quando `generate_audio` está ativado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3TextToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `9957c78291c320b1a8a6a9c0edeefae5f1ccc21a6b58f0b39069c2df8decd100`
