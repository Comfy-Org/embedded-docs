O nó SamplerDPMAdaptative implementa um amostrador DPM (Modelo Probabilístico de Difusão) adaptativo que ajusta automaticamente os tamanhos dos passos durante o processo de amostragem. Ele utiliza controle de erro baseado em tolerância para determinar tamanhos de passo ideais, equilibrando eficiência computacional com precisão na amostragem. Essa abordagem adaptativa ajuda a manter a qualidade enquanto potencialmente reduz o número de passos necessários.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `ordem` | A ordem do método do amostrador (padrão: 3) | INT | Sim | 2-3 |
| `rtol` | Tolerância relativa para controle de erro (padrão: 0,05) | FLOAT | Sim | 0,0-100,0 |
| `atol` | Tolerância absoluta para controle de erro (padrão: 0,0078) | FLOAT | Sim | 0,0-100,0 |
| `h_init` | Tamanho inicial do passo (padrão: 0,05) | FLOAT | Sim | 0,0-100,0 |
| `pcoeff` | Coeficiente proporcional para controle do tamanho do passo (padrão: 0,0) | FLOAT | Sim | 0,0-100,0 |
| `icoeff` | Coeficiente integral para controle do tamanho do passo (padrão: 1,0) | FLOAT | Sim | 0,0-100,0 |
| `dcoeff` | Coeficiente derivativo para controle do tamanho do passo (padrão: 0,0) | FLOAT | Sim | 0,0-100,0 |
| `aceitar_segurança` | Fator de segurança para aceitação do passo (padrão: 0,81) | FLOAT | Sim | 0,0-100,0 |
| `eta` | Parâmetro de estocasticidade (padrão: 0,0) | FLOAT | Sim | 0,0-100,0 |
| `s_ruído` | Fator de escala de ruído (padrão: 1,0) | FLOAT | Sim | 0,0-100,0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `sampler` | Retorna uma instância configurada do amostrador DPM adaptativo | SAMPLER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMAdaptative/pt-BR.md)

---
**Source fingerprint (SHA-256):** `2815ba8c3325d3d099de685edc99e9ff8e90736c1f4bd0188165969179cb99fa`
