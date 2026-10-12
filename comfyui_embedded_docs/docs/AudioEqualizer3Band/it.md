# Equalizzatore Audio (3 Bande)

Il nodo Audio Equalizer (3-Band) consente di regolare le frequenze dei bassi, delle medie e degli alti di una forma d'onda audio. Applica tre filtri separati: un filtro low shelf per i bassi, un filtro peaking per le medie e un filtro high shelf per gli alti. Ogni banda può essere controllata in modo indipendente con impostazioni di guadagno, frequenza e larghezza di banda.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `audio` | I dati audio di input contenenti la forma d'onda e la frequenza di campionamento. | AUDIO | Sì | - |
| `low_gain_dB` | Guadagno per le basse frequenze (bassi). I valori positivi amplificano, i valori negativi attenuano. (predefinito: 0.0) | FLOAT | No | da -24.0 a 24.0 |
| `low_freq` | Frequenza di taglio per il filtro low shelf in Hertz (Hz). (predefinito: 100) | INT | No | da 20 a 500 |
| `mid_gain_dB` | Guadagno per le frequenze medie. I valori positivi amplificano, i valori negativi attenuano. (predefinito: 0.0) | FLOAT | No | da -24.0 a 24.0 |
| `mid_freq` | Frequenza centrale per il filtro peaking delle medie in Hertz (Hz). (predefinito: 1000) | INT | No | da 200 a 4000 |
| `mid_q` | Fattore Q (larghezza di banda) per il filtro peaking delle medie. Valori più bassi creano una banda più ampia, valori più alti creano una banda più stretta. (predefinito: 0.707) | FLOAT | No | da 0.1 a 10.0 |
| `high_gain_dB` | Guadagno per le alte frequenze (alti). I valori positivi amplificano, i valori negativi attenuano. (predefinito: 0.0) | FLOAT | No | da -24.0 a 24.0 |
| `high_freq` | Frequenza di taglio per il filtro high shelf in Hertz (Hz). (predefinito: 5000) | INT | No | da 1000 a 15000 |

**Nota:** I parametri `low_gain_dB`, `mid_gain_dB` e `high_gain_dB` vengono applicati solo quando il loro valore non è zero. Se un guadagno è impostato su 0.0, lo stadio di filtro corrispondente viene saltato.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `audio` | I dati audio elaborati con l'equalizzazione applicata, contenenti la forma d'onda modificata e la frequenza di campionamento originale. | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEqualizer3Band/it.md)

---
**Source fingerprint (SHA-256):** `be3a0981d8285885cb465e82717c3f56c9d301d55708962f9a9dd5b2c400ec81`
