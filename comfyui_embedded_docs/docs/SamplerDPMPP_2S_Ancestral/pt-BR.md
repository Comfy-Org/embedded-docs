# SamplerDPMPP_2S_Ancestral

O nó SamplerDPMPP_2S_Ancestral cria um amostrador que usa o método de amostragem DPM++ 2S Ancestral para gerar imagens. Esse amostrador combina elementos determinísticos e estocásticos para produzir resultados variados, mantendo alguma consistência. Ele permite controlar a aleatoriedade e os níveis de ruído durante o processo de amostragem.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `eta` | Controla a quantidade de ruído estocástico adicionado durante a amostragem (padrão: 1.0) | FLOAT | Sim | 0.0 - 100.0 (passo 0.01) |
| `s_noise` | Controla a escala de ruído aplicada durante o processo de amostragem (padrão: 1.0) | FLOAT | Sim | 0.0 - 100.0 (passo 0.01) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `sampler` | Retorna um objeto amostrador configurado que pode ser usado no pipeline de amostragem | SAMPLER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_2S_Ancestral/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8d20ec21e6c699965753413d9ef8b6191553c4b7b606d93c10470aa9d988a308`
