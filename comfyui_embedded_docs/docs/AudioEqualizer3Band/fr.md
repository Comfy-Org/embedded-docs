> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEqualizer3Band/fr.md)

Voici la traduction en français de la documentation du nœud Audio Equalizer (3-Band) :

L'égaliseur audio (3 bandes) vous permet d'ajuster les fréquences graves, médiums et aiguës d'une forme d'onde audio. Il applique trois filtres distincts : un filtre passe-bas pour les graves, un filtre en cloche pour les médiums et un filtre passe-haut pour les aiguës. Chaque bande peut être contrôlée indépendamment avec des réglages de gain, de fréquence et de largeur de bande.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `audio` | AUDIO | Oui | - | Les données audio d'entrée contenant la forme d'onde et la fréquence d'échantillonnage. |
| `low_gain_dB` | FLOAT | Non | -24,0 à 24,0 | Gain pour les basses fréquences (Graves). Les valeurs positives augmentent, les valeurs négatives réduisent. (par défaut : 0,0) |
| `low_freq` | INT | Non | 20 à 500 | Fréquence de coupure du filtre passe-bas en Hertz (Hz). (par défaut : 100) |
| `mid_gain_dB` | FLOAT | Non | -24,0 à 24,0 | Gain pour les fréquences médiums. Les valeurs positives augmentent, les valeurs négatives réduisent. (par défaut : 0,0) |
| `mid_freq` | INT | Non | 200 à 4000 | Fréquence centrale du filtre en cloche pour les médiums en Hertz (Hz). (par défaut : 1000) |
| `mid_q` | FLOAT | Non | 0,1 à 10,0 | Facteur Q (largeur de bande) du filtre en cloche pour les médiums. Des valeurs plus faibles créent une bande plus large, des valeurs plus élevées créent une bande plus étroite. (par défaut : 0,707) |
| `high_gain_dB` | FLOAT | Non | -24,0 à 24,0 | Gain pour les hautes fréquences (Aiguës). Les valeurs positives augmentent, les valeurs négatives réduisent. (par défaut : 0,0) |
| `high_freq` | INT | Non | 1000 à 15000 | Fréquence de coupure du filtre passe-haut en Hertz (Hz). (par défaut : 5000) |

**Remarque :** Les paramètres `low_gain_dB`, `mid_gain_dB` et `high_gain_dB` ne sont appliqués que lorsque leur valeur est différente de zéro. Si un gain est réglé sur 0,0, l'étape de filtre correspondante est ignorée.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `audio` | AUDIO | Les données audio traitées avec l'égalisation appliquée, contenant la forme d'onde modifiée et la fréquence d'échantillonnage d'origine. |

---
**Source fingerprint (SHA-256):** `7aeaec2959f1af6144e46d8e6c558a16193669846923df1db23ae9d47e5cc173`
