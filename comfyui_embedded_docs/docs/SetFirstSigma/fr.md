# DéfinirPremierSigma

Le nœud SetFirstSigma modifie une séquence de sigma en remplaçant uniquement sa première valeur par une valeur sigma personnalisée. Il prend une séquence de sigma existante et une nouvelle valeur sigma, puis renvoie une nouvelle séquence de sigma où toutes les valeurs sauf la première restent inchangées.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `sigmas` | La séquence d’entrée des valeurs sigma à modifier | SIGMAS | Oui | - |
| `sigma` | La nouvelle valeur sigma à définir comme premier élément de la séquence (par défaut : 136.0) | FLOAT | Oui | 0.0 à 20000.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sigmas` | La séquence de sigma modifiée, dont le premier élément a été remplacé par la valeur sigma personnalisée | SIGMAS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetFirstSigma/fr.md)

---
**Source fingerprint (SHA-256):** `5302bc61a7ca094fee9ee2ad8c9dc32997ef0bbf27c9945acd7287e7df6b6db3`
