# Cortar Latent de Vídeo

O nó TrimVideoLatent remove quadros do início de uma representação latente de vídeo. Ele recebe uma amostra de vídeo latente e corta um número especificado de quadros do início, retornando a parte restante do vídeo. Isso permite encurtar sequências de vídeo removendo os quadros iniciais.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `samples` | A representação latente de vídeo de entrada contendo os quadros de vídeo a serem removidos | LATENT | Sim | - |
| `trim_amount` | O número de quadros a remover do início do vídeo (padrão: 0) | INT | Sim | 0 a 99999 |

## Saídas

| Nome de Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | A representação latente de vídeo cortada, com o número especificado de quadros removidos do início | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrimVideoLatent/pt-BR.md)

---
**Source fingerprint (SHA-256):** `33b7a899f2002e9a7008f2ca93de853c08dd0629a4c6867fb42aae4ec2eb864b`
