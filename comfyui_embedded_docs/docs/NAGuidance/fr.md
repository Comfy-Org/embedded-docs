# Guidage d’Attention Normalisée

Le nœud NAGuidance applique le guidage d'attention normalisé à un modèle. Cette technique permet l'utilisation de prompts négatifs avec des modèles distillés ou schnell en modifiant le mécanisme d'attention du modèle pendant le processus d'échantillonnage afin d'orienter la génération à l'écart des concepts indésirables.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle auquel appliquer le guidage d'attention normalisé. | MODEL | Oui | - |
| `nag_scale` | Le facteur d'échelle de guidage. Des valeurs plus élevées éloignent davantage la génération du prompt négatif. (par défaut : 5.0) | FLOAT | Oui | 0.0 - 50.0 |
| `nag_alpha` | Le facteur de mélange pour l'attention normalisée. Une valeur de 1.0 remplace entièrement l'attention d'origine, tandis qu'une valeur de 0.0 n'a aucun effet. (par défaut : 0.5) | FLOAT | Oui | 0.0 - 1.0 |
| `nag_tau` | Un facteur d'échelle utilisé pour limiter le rapport de normalisation. (par défaut : 1.5) | FLOAT | Oui | 1.0 - 10.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle patché avec le guidage d'attention normalisé activé. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NAGuidance/fr.md)

---
**Source fingerprint (SHA-256):** `42b4d601312dcbb1c934c6a79bbb5e9fd6598fa5f32b18f5c0affcb596672cba`
