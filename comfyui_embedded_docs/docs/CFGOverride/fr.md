# Remplacement CFG

Le nœud CFG Override remplace l'échelle CFG (Classifier-Free Guidance) par une valeur fixe sur une plage de pourcentage (sigma) du processus d'échantillonnage. Lorsque plusieurs nœuds CFG Override sont utilisés, le remplacement le plus proche de l'échantillonneur l'emporte sur les plages qui se chevauchent.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle auquel appliquer le remplacement du CFG. | MODEL | Oui | |
| `cfg` | La valeur fixe de l'échelle CFG à utiliser pendant la plage de remplacement. Par défaut : 1.0. | FLOAT | Oui | 0.0 à 100.0 (pas : 0.1) |
| `start_percent` | Le point de départ de la plage de remplacement en pourcentage du processus d'échantillonnage. Par défaut : 0.0. | FLOAT | Oui | 0.0 à 1.0 (pas : 0.001) |
| `end_percent` | Le point de fin de la plage de remplacement en pourcentage du processus d'échantillonnage. Par défaut : 1.0. | FLOAT | Oui | 0.0 à 1.0 (pas : 0.001) |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `MODEL` | Le modèle auquel l'enveloppe de remplacement du CFG est appliquée. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGOverride/fr.md)

---
**Source fingerprint (SHA-256):** `94c7d3751d90b42479f9cec4bdb3c95eeda405f51224f85d313ff12ec071ec58`
