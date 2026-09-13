# Áudio Latente AceStep Vazio

O nó Empty Ace Step 1.0 Latent Audio cria amostras de áudio latentes vazias para uma duração selecionada. Ele preenche um lote de latentes de áudio silenciosos (todos zerados), em que o comprimento é calculado a partir da entrada `seconds` usando parâmetros de processamento de áudio. Isso normalmente é usado para inicializar fluxos de trabalho de áudio que precisam de uma representação latente como ponto de partida.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `seconds` | A duração do áudio em segundos (padrão: 120.0, passo: 0.1) | FLOAT | Sim | 1.0 - 1000.0 |
| `batch_size` | O número de imagens latentes no lote (padrão: 1) | INT | Sim | 1 - 4096 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | Retorna amostras de áudio latentes vazias preenchidas com zeros. A saída contém um tensor `samples` e um campo `type` definido como "audio". | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStepLatentAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8268eb582a28c7acc495c52831cc6edd8f8fdd1b294857451ce94abc37ca0d14`
