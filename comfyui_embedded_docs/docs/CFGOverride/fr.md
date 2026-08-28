# Remplacement CFG

Le nœud CFG Override vous permet de définir une valeur d'échelle CFG (Classifier-Free Guidance) fixe pour une plage spécifique du processus d'échantillonnage, définie en pourcentage du nombre total d'étapes. Lorsque plusieurs nœuds CFG Override sont connectés, celui qui est le plus proche de l'échantillonneur dans la chaîne a la priorité pour les plages qui se chevauchent.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Le modèle auquel appliquer le CFG override | MODEL | Oui | |
| `cfg` | La valeur d'échelle CFG fixe à utiliser pendant la plage d'override (par défaut : 1.0) | FLOAT | Oui | 0.0 à 100.0 |
| `pourcentage_début` | Le point de départ de la plage d'override en pourcentage du processus d'échantillonnage (par défaut : 0.0) | FLOAT | Oui | 0.0 à 1.0 |
| `pourcentage_fin` | Le point de fin de la plage d'override en pourcentage du processus d'échantillonnage (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `MODEL` | Le modèle avec l'override CFG appliqué via le wrapper | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGOverride/fr.md)

---
**Source fingerprint (SHA-256):** `94c7d3751d90b42479f9cec4bdb3c95eeda405f51224f85d313ff12ec071ec58`
