# Remplacement CFG

Le nœud CFG Override vous permet de définir une valeur fixe de CFG (Classifier-Free Guidance) pour une plage spécifique du processus d'échantillonnage, définie en pourcentage du nombre total d'étapes. Lorsque plusieurs nœuds CFG Override sont connectés, celui qui est le plus proche de l'échantillonneur dans la chaîne a priorité pour les plages qui se chevauchent.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Le modèle auquel appliquer la substitution CFG | MODEL | Oui | |
| `cfg` | La valeur fixe de CFG à utiliser pendant la plage de substitution (par défaut : 1.0) | FLOAT | Oui | 0.0 à 100.0 |
| `pourcentage_début` | Le point de départ de la plage de substitution en pourcentage du processus d'échantillonnage (par défaut : 0.0) | FLOAT | Oui | 0.0 à 1.0 |
| `pourcentage_fin` | Le point de fin de la plage de substitution en pourcentage du processus d'échantillonnage (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `MODEL` | Le modèle avec l'enveloppe de substitution CFG appliquée | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGOverride/fr.md)

---
**Source fingerprint (SHA-256):** `1fe57a4e78a2f18c4e7da49fa7a6c473d64dc0ebf6662535dfb5379c37936662`
