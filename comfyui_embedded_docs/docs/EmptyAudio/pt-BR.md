# Áudio Vazio

O nó EmptyAudio gera um clipe de áudio silencioso com duração, taxa de amostragem e configuração de canais especificadas. Ele cria uma forma de onda contendo todos os zeros, produzindo silêncio completo durante a duração definida. Este nó é útil para criar áudio de espaço reservado ou gerar segmentos silenciosos em fluxos de trabalho de áudio.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `duração` | Duração do clipe de áudio vazio em segundos (padrão: 60,0) | FLOAT | Sim | 0,0 a 1,8446744073709552e+19 |
| `taxa_de_amostragem` | Taxa de amostragem do clipe de áudio vazio (padrão: 44100) | INT | Sim | 1 a 192000 |
| `canais` | Número de canais de áudio (1 para mono, 2 para estéreo) (padrão: 2) | INT | Sim | 1 a 2 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `AUDIO` | O clipe de áudio silencioso gerado contendo dados de forma de onda e informações de taxa de amostragem | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `61b9cd6c8e518f28533b7586fdd1f909e5c356c7f2f7690da4e1ec7965d53c5d`
