# Guider CFG Double Modèle

Ce nœud vous permet d'utiliser deux modèles différents pendant le processus d'échantillonnage CFG guidé : un modèle pour le passage positif (conditionnel) et un modèle distinct pour le passage négatif (inconditionnel). Lorsqu'aucun modèle négatif n'est fourni, il se comporte comme un guideur CFG standard utilisant un seul modèle.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Modèle utilisé pour le passage positif (conditionnel). | MODEL | Oui | |
| `modèle_négatif` | Modèle utilisé pour le passage négatif (inconditionnel). Utilisez le même modèle pour un CFG ordinaire. | MODEL | Non | |
| `positif` | L'entrée de conditionnement positive. | CONDITIONING | Oui | |
| `cfg` | La valeur d'échelle CFG (par défaut : 4,0). | FLOAT | Oui | 0,0 à 100,0 (pas : 0,1) |
| `négatif` | Conditionnement négatif exécuté sur le modèle négatif. Laissez déconnecté pour un passage inconditionnel sans texte (image uniquement). | CONDITIONING | Non | |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `GUIDER` | Un objet guideur configuré avec les modèles et conditionnements spécifiés pour une utilisation dans l'échantillonnage. | GUIDER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualModelGuider/fr.md)

---
**Source fingerprint (SHA-256):** `a60803156e98d2ffe975d39922dfbeacafd1a2155d88dd2e285ac1426a1e7a33`
