> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TemporalScoreRescaling/fr.md)

Ce nœud applique le Rescaling Temporel des Scores (TSR) à un modèle de diffusion. Il modifie le comportement d'échantillonnage du modèle en re-échelonnant le bruit ou le score prédit pendant le processus de dé-bruitage, ce qui peut orienter la diversité de la sortie générée. Ceci est implémenté en tant que fonction post-CFG (Classifier-Free Guidance).

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle de diffusion à modifier avec la fonction TSR. |
| `tsr_k` | FLOAT | Non | 0.01 - 100.0 | Contrôle l'intensité du re-échelonnage. Un k plus faible produit des résultats plus détaillés ; un k plus élevé produit des résultats plus lisses en génération d'image. Régler k = 1 désactive le re-échelonnage. (par défaut : 0.95) |
| `tsr_sigma` | FLOAT | Non | 0.01 - 100.0 | Contrôle à quel moment le re-échelonnage prend effet. Des valeurs plus grandes prennent effet plus tôt. (par défaut : 1.0) |

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `patched_model` | MODEL | Le modèle d'entrée, maintenant modifié avec la fonction de Rescaling Temporel des Scores appliquée à son processus d'échantillonnage. |
