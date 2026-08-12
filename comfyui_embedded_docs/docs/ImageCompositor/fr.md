# ImageCompositor

Ce nœud combine plusieurs calques d'image en une seule image composée. Il prend une pile de calques construite avec le nœud Add Layer et, éventuellement, une composition enregistrée à partir de l'éditeur de composition, puis fusionne les calques entre eux en utilisant leur positionnement, leur taille, leur rotation, leur opacité et leur mode de fusion.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `layers` | Pile de calques à composer ; construisez-la avec Add Layer. Les éléments sont empilés par z_index, les frames de lot d'un élément s'étendent en calques consécutifs, et le positionnement, l'opacité et le mode de fusion de l'élément définissent la composition initiale. Sans canevas de document explicite, la taille correspond à une étendue maximale calculée au mieux à partir des calques placés. Une composition enregistrée qui correspond aux entrées actuelles a la priorité. | LAYERS | Oui | Maximum 50 calques |
| `compositor` | Composition en couches enregistrée par l'éditeur de composition. | COMPOSITOR | Non | None |

**Remarques sur les contraintes :**

- La pile de calques prend en charge un maximum de 50 calques (frames étendues) ; en fournir plus génère une erreur.
- Seuls les calques raster sont actuellement pris en charge ; les autres types d'éléments de calque génèrent une erreur.
- La version du document `layers` doit être 1 ; les autres versions génèrent une erreur.
- L'état `compositor` enregistré n'est rejoué que lorsque ses empreintes d'entrée enregistrées correspondent à la pile de calques actuelle. Si elles ne correspondent pas, le nœud revient à une composition à partir des propriétés des calques et marque l'état enregistré comme obsolète.
- L'opacité des calques est limitée à la plage 0.0 à 1.0.
- Le placement horizontal/vertical des calques (`x`, `y`) est limité à la résolution maximale autorisée.
- La largeur et la hauteur des calques reviennent à la taille naturelle de l'image lorsqu'elles sont définies à zéro ou moins, et sont plafonnées à la résolution maximale autorisée.
- La taille du canevas composé ne doit pas dépasser la résolution maximale autorisée.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | Image composée. Comporte un canal alpha lorsque la composition présente des zones transparentes (par exemple, un arrière-plan masqué), sinon RVB simple. | IMAGE |
| `MASK` | Transparence de la composition (1 = entièrement transparent). Tous les zéros lorsque la composition est opaque. | MASK |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCompositor/fr.md)

---
**Source fingerprint (SHA-256):** `1eca5c151b3737ccf76e6fd7a83cd1458b2acc314609753d597eec711bcf4bd8`
