> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NAGuidance/fr.md)

Le nœud NAGuidance applique le guidage d'attention normalisé (Normalized Attention Guidance) à un modèle. Cette technique permet d'utiliser des prompts négatifs avec des modèles distillés ou schnell en modifiant le mécanisme d'attention du modèle pendant le processus d'échantillonnage pour orienter la génération à l'écart des concepts indésirables.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle auquel appliquer le guidage d'attention normalisé. |
| `nag_scale` | FLOAT | Oui | 0.0 - 50.0 | Le facteur d'échelle du guidage. Des valeurs plus élevées éloignent davantage la génération du prompt négatif. (par défaut : 5.0) |
| `nag_alpha` | FLOAT | Oui | 0.0 - 1.0 | Le facteur de mélange pour l'attention normalisée. Une valeur de 1.0 remplace complètement l'attention d'origine, tandis que 0.0 n'a aucun effet. (par défaut : 0.5) |
| `nag_tau` | FLOAT | Oui | 1.0 - 10.0 | Un facteur d'échelle utilisé pour limiter le ratio de normalisation. (par défaut : 1.5) |

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model` | MODEL | Le modèle modifié avec le guidage d'attention normalisé activé. |