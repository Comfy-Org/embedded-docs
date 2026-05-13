> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAudio/pt-BR.md)

O nó EmptyAudio gera um clipe de áudio silencioso com duração, taxa de amostragem e configuração de canais especificadas. Ele cria uma forma de onda contendo todos os zeros, produzindo silêncio completo durante a duração definida. Este nó é útil para criar áudio de espaço reservado ou gerar segmentos silenciosos em fluxos de trabalho de áudio.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `duração` | FLOAT | Sim | 0,0 a 1,8446744073709552e+19 | Duração do clipe de áudio vazio em segundos (padrão: 60,0) |
| `taxa_de_amostragem` | INT | Sim | 1 a 192000 | Taxa de amostragem do clipe de áudio vazio (padrão: 44100) |
| `canais` | INT | Sim | 1 a 2 | Número de canais de áudio (1 para mono, 2 para estéreo) (padrão: 2) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `AUDIO` | AUDIO | O clipe de áudio silencioso gerado contendo dados de forma de onda e informações de taxa de amostragem |

---
**Source fingerprint (SHA-256):** `61b9cd6c8e518f28533b7586fdd1f909e5c356c7f2f7690da4e1ec7965d53c5d`
