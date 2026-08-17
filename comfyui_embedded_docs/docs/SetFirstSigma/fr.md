# DéfinirPremierSigma

Le nœud SetFirstSigma modifie une séquence de valeurs sigma en remplaçant la première valeur sigma de la séquence par une valeur personnalisée. Il prend une séquence sigma existante et une nouvelle valeur sigma en entrées, puis renvoie une nouvelle séquence sigma où seul le premier élément a été modifié, tandis que toutes les autres valeurs sigma restent inchangées.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `sigmas` | La séquence de valeurs sigma d’entrée à modifier | SIGMAS | Oui | - |
| `sigma` | La nouvelle valeur sigma à définir comme premier élément de la séquence (défaut : 136.0) | FLOAT | Oui | 0.0 à 20000.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sigmas` | La séquence sigma modifiée avec le premier élément remplacé par la valeur sigma personnalisée | SIGMAS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetFirstSigma/fr.md)

---
**Source fingerprint (SHA-256):** `5302bc61a7ca094fee9ee2ad8c9dc32997ef0bbf27c9945acd7287e7df6b6db3`
