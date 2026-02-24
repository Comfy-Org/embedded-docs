> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CustomCombo/fr.md)

## Vue d'ensemble

Le nœud Custom Combo vous permet de créer un menu déroulant personnalisé avec votre propre liste d'options textuelles. C'est un nœud axé sur l'interface utilisateur qui fournit une représentation côté backend pour garantir la compatibilité au sein de votre flux de travail. Lorsque vous sélectionnez une option dans le menu déroulant, le nœud renvoie ce texte sous forme de chaîne de caractères.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `choice` | COMBO | Oui | Définie par l'utilisateur | L'option textuelle sélectionnée dans le menu déroulant personnalisé. La liste des options disponibles est définie par l'utilisateur dans l'interface frontale du nœud. |

**Note :** La validation de l'entrée de ce nœud est intentionnellement désactivée. Cela vous permet de définir n'importe quelle option textuelle personnalisée dans l'interface sans que le backend ne vérifie si votre sélection provient d'une liste prédéfinie.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | STRING | La chaîne de caractères correspondant à l'option sélectionnée dans la boîte combinée personnalisée. |
