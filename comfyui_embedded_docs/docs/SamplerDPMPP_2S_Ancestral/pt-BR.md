# SamplerDPMPP_2S_Ancestral

O nó SamplerDPMPP_2S_Ancestral cria um amostrador que utiliza o método de amostragem ancestral DPM++ 2S para gerar imagens. Este amostrador combina elementos determinísticos e estocásticos para produzir resultados variados, mantendo alguma consistência. Ele permite controlar a aleatoriedade e os níveis de ruído durante o processo de amostragem.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `eta` | Controla a quantidade de ruído estocástico adicionado durante a amostragem (padrão: 1.0) | FLOAT | Sim | 0.0 - 100.0 |
| `s_ruído` | Controla a escala do ruído aplicado durante o processo de amostragem (padrão: 1.0) | FLOAT | Sim | 0.0 - 100.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `sampler` | Retorna um objeto amostrador configurado que pode ser utilizado no pipeline de amostragem | SAMPLER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_2S_Ancestral/pt-BR.md)

---
**Source fingerprint (SHA-256):** `9634c96934850f5b746cd7c8b29727396af534133b8d54b6bdac12e9e0975189`
