> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TCFG/fr.md)

TCFG (Tangential Damping CFG) met en œuvre une technique de guidage qui affine les prédictions non conditionnelles (négatives) pour mieux les aligner avec les prédictions conditionnelles (positives). Cette méthode améliore la qualité des résultats en appliquant un amortissement tangentiel au guidage non conditionnel, basé sur le document de recherche référencé sous le numéro 2503.18137. Le nœud modifie le comportement d'échantillonnage du modèle en ajustant la manière dont les prédictions non conditionnelles sont traitées pendant le processus de guidage sans classifieur.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle auquel appliquer l'amortissement tangentiel CFG |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `patched_model` | MODEL | Le modèle modifié avec l'amortissement tangentiel CFG appliqué |
