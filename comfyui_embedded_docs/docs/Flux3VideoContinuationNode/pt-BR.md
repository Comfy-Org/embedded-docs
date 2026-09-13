# Flux 3 Continuação de Vídeo

Este nó continua um clipe de vídeo existente com o FLUX 3: o novo clipe continua a partir dos quadros finais do vídeo que você fornece. Ele faz upload do seu clipe de origem, envia o prompt e as configurações para o serviço de geração e retorna o vídeo de continuação resultante quando estiver pronto.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `video` | O clipe a ser continuado. | VIDEO | Sim | Um único clipe de vídeo |
| `prompt` | O que a continuação deve mostrar; o prompt é interpretado e expandido antes da geração. (padrão: "") | STRING | Sim | Texto não vazio (mínimo de 1 caractere) |
| `aspect_ratio` | Proporção de aspecto de saída. 'auto' escolhe uma com base no prompt e nas entradas. (padrão: "auto") | COMBO | Sim | "auto" (padrão)<br>Múltiplas opções predefinidas |
| `duration` | Duração do clipe em segundos. 'auto' ajusta a duração ao conteúdo. (padrão: "auto") | COMBO | Sim | "auto" (padrão)<br>Valores numéricos em segundos |
| `resolution` | Resolução de saída. (padrão: "720p") | COMBO | Sim | "720p" (padrão)<br>"1080p"<br>Outras opções predefinidas |
| `generate_audio` | Gera áudio sincronizado (ambiente, fala, efeitos). Quando desativado, produz um vídeo sem faixa de áudio. (padrão: true) | BOOLEAN | Sim | true<br>false |
| `safety_tolerance` | Tolerância de moderação; 0 é o mais restrito. Solicitações que enviam imagens ou vídeo são limitadas a 2, independentemente do que você definir aqui. (parâmetro avançado, padrão: 2) | INT | Sim | 0 - 4 (máximo efetivo: 2 para solicitações de vídeo) |
| `seed` | Seed para determinar se o nó deve ser executado novamente; o FLUX 3 escolhe sua própria seed, então os resultados reais são não determinísticos independentemente deste valor. (padrão: 42) | INT | Sim | 0 - 4294967295 (0xFFFFFFFF) |

### Notas

- `prompt` deve conter pelo menos um caractere; caso contrário, a geração falha. Embora o campo tenha como padrão uma string vazia, um prompt não vazio é obrigatório para executar o nó.
- `safety_tolerance` aceita qualquer valor de 0 a 4, mas, como este nó envia um vídeo para a API, a tolerância efetiva é limitada a 2 independentemente do valor selecionado.
- Quando `duration` é definido como um número, ele é convertido em um número inteiro de segundos. O valor especial "auto" permite que o serviço ajuste a duração ao conteúdo.
- As listas exatas de opções para `aspect_ratio`, `duration` e `resolution` são definidas internamente pelo nó. As opções de resolução incluem pelo menos "720p" (o padrão) e "1080p". O preço é calculado com base na `resolution` e na `duration` selecionadas; "1080p" é cobrado a $0.7579 por segundo, enquanto outras resoluções são cobradas a $0.5863 por segundo.
- `seed` controla apenas se o nó será executado novamente; ela não é enviada ao serviço de geração.
- Os campos de autenticação e identificação do nó (`auth_token_comfy_org`, `api_key_comfy_org`, `unique_id`) ficam ocultos e são tratados automaticamente pela plataforma.

## Saídas

| Nome de saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `video` | O clipe de continuação gerado produzido pelo FLUX 3, que continua a partir do final do vídeo de origem. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3VideoContinuationNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `129ad0eb62c368854cebb010cc886aecac4caab00f9111143b883d028d7c30d9`
