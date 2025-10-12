> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CaseConverter/fr.md)

Le nœud Case Converter transforme les chaînes de texte en différents formats de casse. Il prend une chaîne d'entrée et la convertit selon le mode sélectionné, produisant une chaîne de sortie avec le formatage de casse spécifié appliqué. Le nœud prend en charge quatre options différentes de conversion de casse pour modifier la capitalisation de votre texte.

## Entrées

| Paramètre | Type de données | Type d'entrée | Défaut | Plage | Description |
|-----------|-----------|------------|---------|-------|-------------|
| `string` | STRING | Chaîne | - | - | La chaîne de texte à convertir dans un format de casse différent |
| `mode` | STRING | Combo | - | ["UPPERCASE", "lowercase", "Capitalize", "Title Case"] | Le mode de conversion de casse à appliquer : UPPERCASE convertit toutes les lettres en majuscules, lowercase convertit toutes les lettres en minuscules, Capitalize met uniquement la première lettre en majuscule, Title Case met la première lettre de chaque mot en majuscule |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | STRING | La chaîne d'entrée convertie dans le format de casse spécifié |
