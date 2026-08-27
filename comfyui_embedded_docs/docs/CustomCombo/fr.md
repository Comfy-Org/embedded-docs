# Combo personnalisé

Le nœud Custom Combo vous permet de créer un menu déroulant personnalisé avec votre propre liste d’options textuelles. Il s’agit d’un nœud orienté frontend qui inclut une représentation backend afin de préserver la compatibilité de votre workflow. Lorsque vous sélectionnez une option dans le menu déroulant, le nœud renvoie ce texte sous forme de chaîne de caractères ainsi que sa position d’index.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `choix` | L’option textuelle sélectionnée dans le menu déroulant personnalisé. La liste des options disponibles est définie par l’utilisateur dans l’interface frontend du nœud. | COMBO | Oui | Défini par l’utilisateur |
| `index` | Une valeur entière pouvant être utilisée pour spécifier un index. Défaut : 0. | INT | Non | Tout entier (défaut : 0) |

**Remarque :** La validation des entrées de ce nœud est volontairement désactivée. Cela vous permet d’écrire des options textuelles personnalisées dans le frontend sans que le backend vérifie si votre sélection correspond à une liste prédéfinie. Les widgets autres que le menu déroulant combo sont entièrement définis dans le frontend. Ce nœud est marqué comme expérimental.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `STRING` | La chaîne de caractères correspondant à l’option sélectionnée dans le menu déroulant personnalisé. | STRING |
| `INDEX` | La position d’index de l’option sélectionnée dans la liste déroulante. | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CustomCombo/fr.md)

---
**Source fingerprint (SHA-256):** `143eafcf32de7ebaf72b5387537154b5deee7d3e3a520a0b2c12ac4fb67890f8`
