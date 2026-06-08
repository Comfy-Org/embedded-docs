O nó TrimVideoLatent remove quadros do início de uma representação latente de vídeo. Ele recebe uma amostra de vídeo latente e remove um número especificado de quadros do início, retornando a parte restante do vídeo. Isso permite encurtar sequências de vídeo removendo os quadros iniciais.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `amostras` | A representação latente de vídeo de entrada contendo os quadros a serem removidos | LATENT | Sim | - |
| `quantidade_de_corte` | O número de quadros a serem removidos do início do vídeo (padrão: 0) | INT | Sim | 0 a 99999 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | A representação latente de vídeo com o número especificado de quadros removidos do início | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrimVideoLatent/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7fd482533d1f63219565a3a25776173c77c419fbf5086015d42136f5bfdfbed2`
