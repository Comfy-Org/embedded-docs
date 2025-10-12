> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetFirstSigma/fr.md)

Le nœud SetFirstSigma modifie une séquence de valeurs sigma en remplaçant la première valeur sigma de la séquence par une valeur personnalisée. Il prend en entrée une séquence sigma existante et une nouvelle valeur sigma, puis retourne une nouvelle séquence sigma dans laquelle seul le premier élément a été modifié, toutes les autres valeurs sigma restant inchangées.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `sigmas` | SIGMAS | Oui | - | La séquence de valeurs sigma en entrée à modifier |
| `sigma` | FLOAT | Oui | 0.0 à 20000.0 | La nouvelle valeur sigma à définir comme premier élément de la séquence (par défaut : 136.0) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `sigmas` | SIGMAS | La séquence sigma modifiée avec le premier élément remplacé par la valeur sigma personnalisée |