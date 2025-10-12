> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringTrim/fr.md)

Le nœud StringTrim supprime les caractères d'espacement du début, de la fin, ou des deux côtés d'une chaîne de texte. Vous pouvez choisir de supprimer les espaces du côté gauche, du côté droit, ou des deux côtés de la chaîne. Ceci est utile pour nettoyer les entrées de texte en supprimant les espaces, tabulations ou caractères de nouvelle ligne indésirables.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | Oui | - | La chaîne de texte à traiter. Prend en charge l'entrée multiligne. |
| `mode` | COMBO | Oui | "Both"<br>"Left"<br>"Right" | Spécifie quel(s) côté(s) de la chaîne traiter. "Both" supprime les espaces des deux extrémités, "Left" supprime uniquement du début, "Right" supprime uniquement de la fin. |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | STRING | La chaîne de texte traitée avec les espaces supprimés selon le mode sélectionné. |
