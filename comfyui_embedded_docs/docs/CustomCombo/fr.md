> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CustomCombo/fr.md)

Le nœud Custom Combo vous permet de créer un menu déroulant personnalisé avec votre propre liste d'options textuelles. Il s'agit d'un nœud axé sur l'interface utilisateur qui fournit une représentation backend pour garantir la compatibilité au sein de votre flux de travail. Lorsque vous sélectionnez une option dans le menu déroulant, le nœud génère ce texte sous forme de chaîne de caractères ainsi que sa position d'index.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `choice` | COMBO | Oui | Défini par l'utilisateur | L'option textuelle sélectionnée dans le menu déroulant personnalisé. La liste des options disponibles est définie par l'utilisateur dans l'interface utilisateur du nœud. |
| `index` | INT | Non | 0 | Une valeur entière pouvant être utilisée pour spécifier un index. Valeur par défaut : 0. |

**Remarque :** La validation de l'entrée de ce nœud est intentionnellement désactivée. Cela vous permet de définir toutes les options textuelles personnalisées souhaitées dans l'interface utilisateur sans que le backend ne vérifie si votre sélection provient d'une liste prédéfinie.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `STRING` | STRING | La chaîne de caractères correspondant à l'option sélectionnée dans la zone de liste déroulante personnalisée. |
| `INDEX` | INT | La position d'index de l'option sélectionnée dans la liste déroulante. |

---
**Source fingerprint (SHA-256):** `d950207b94deee37abce294eb3dab035e622925dc1118fe37f9c874784dc1672`
