> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveStringMultiline/fr.md)

Le nœud PrimitiveStringMultiline fournit un champ de saisie de texte multiligne permettant d'entrer et de transmettre des valeurs de chaîne de caractères dans votre flux de travail. Il accepte une saisie de texte sur plusieurs lignes et renvoie la même valeur de chaîne de caractères sans modification. Ce nœud est utile lorsque vous devez saisir du contenu textuel long ou du texte formaté s'étendant sur plusieurs lignes.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `value` | STRING | Oui | N/A | La valeur de saisie de texte qui peut s'étendre sur plusieurs lignes |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | STRING | La même valeur de chaîne de caractères qui a été fournie en entrée |