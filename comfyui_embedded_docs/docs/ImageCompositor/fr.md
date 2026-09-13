# Créer une image en couches

Ce nœud combine plusieurs calques d’image en une seule image composite. Il prend une pile de calques construite avec le nœud Add Layer et applique éventuellement les paramètres de composition enregistrés depuis l’éditeur de composition, en mélangeant les calques selon leur placement, leur taille, leur rotation, leur opacité et leur mode de fusion. Une composition enregistrée qui correspond aux entrées actuelles est prioritaire ; sinon, le nœud effectue la composition à partir des propriétés des calques et marque l’état enregistré comme obsolète.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `layers` | Pile de calques à composer ; construisez-la avec Add Layer. Les éléments sont empilés par z_index, les images de lot à l’intérieur d’un élément sont développées en calques consécutifs, et le placement, l’opacité et le mode de fusion de l’élément définissent la composition initiale. Sans canevas de document explicite, la taille correspond à l’étendue maximale approximative des calques placés. Une composition enregistrée qui correspond aux entrées actuelles est prioritaire. | LAYERS | Oui | Maximum 50 calques |
| `compositor` | Composition en calques enregistrée par l’éditeur de composition. | COMPOSITOR | Non | Aucune |

**Remarques sur les contraintes :**

- La pile de calques prend en charge un maximum de 50 calques développés ; en fournir davantage déclenche une erreur.
- Seuls les éléments de calque raster sont actuellement pris en charge ; les autres types d’éléments déclenchent une erreur.
- La version du document `layers` doit être 1 ; les autres versions déclenchent une erreur.
- L’état `compositor` enregistré n’est rejoué que lorsque les empreintes d’entrée enregistrées correspondent à la pile de calques actuelle. Si ce n’est pas le cas, le nœud revient à une composition à partir des propriétés des calques et marque l’état enregistré comme obsolète.
- L’opacité des calques est limitée à la plage 0.0 à 1.0.
- Le placement horizontal et vertical des calques (`x`, `y`) est limité à la limite de résolution maximale.
- La largeur et la hauteur des calques reviennent à la taille naturelle de l’image lorsqu’elles sont définies à zéro ou moins, et sont plafonnées à la limite de résolution maximale.
- La taille du canevas composite ne doit pas dépasser la limite de résolution maximale.
- Lorsqu’aucun calque n’est fourni, une image de substitution 64x64 est renvoyée.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | Image composite. Contient un canal alpha lorsque le composite présente des zones transparentes (par ex. un arrière-plan masqué), sinon du RGB simple. | IMAGE |
| `MASK` | Transparence du composite (1 = entièrement transparent). Toutes les valeurs sont à zéro lorsque le composite est opaque. | MASK |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCompositor/fr.md)

---
**Source fingerprint (SHA-256):** `76e5e57ade89f9ee172c5e1f0b82579d846d15bafb52b2052246f1f2ad7f0034`
