> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMAdaptative/pt-BR.md)

O nó SamplerDPMAdaptative implementa um amostrador DPM (Modelo Probabilístico de Difusão) adaptativo que ajusta automaticamente os tamanhos dos passos durante o processo de amostragem. Ele utiliza um controle de erro baseado em tolerância para determinar os tamanhos de passo ideais, equilibrando eficiência computacional com precisão da amostragem. Esta abordagem adaptativa ajuda a manter a qualidade enquanto potencialmente reduz o número de passos necessários.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `order` | INT | Sim | 2-3 | A ordem do método do amostrador (padrão: 3) |
| `rtol` | FLOAT | Sim | 0.0-100.0 | Tolerância relativa para controle de erro (padrão: 0.05) |
| `atol` | FLOAT | Sim | 0.0-100.0 | Tolerância absoluta para controle de erro (padrão: 0.0078) |
| `h_init` | FLOAT | Sim | 0.0-100.0 | Tamanho inicial do passo (padrão: 0.05) |
| `pcoeff` | FLOAT | Sim | 0.0-100.0 | Coeficiente proporcional para controle do tamanho do passo (padrão: 0.0) |
| `icoeff` | FLOAT | Sim | 0.0-100.0 | Coeficiente integral para controle do tamanho do passo (padrão: 1.0) |
| `dcoeff` | FLOAT | Sim | 0.0-100.0 | Coeficiente derivativo para controle do tamanho do passo (padrão: 0.0) |
| `accept_safety` | FLOAT | Sim | 0.0-100.0 | Fator de segurança para aceitação do passo (padrão: 0.81) |
| `eta` | FLOAT | Sim | 0.0-100.0 | Parâmetro de estocasticidade (padrão: 0.0) |
| `s_noise` | FLOAT | Sim | 0.0-100.0 | Fator de escala de ruído (padrão: 1.0) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Retorna uma instância configurada do amostrador DPM adaptativo |
