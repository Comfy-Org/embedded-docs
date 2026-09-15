# RecraftStyleV3VectorIllustrationNode

Ce nœud sélectionne un style pour l'API Recraft, plus précisément la catégorie de style d'illustration vectorielle. Vous pouvez éventuellement choisir un sous-style plus spécifique dans cette catégorie. Le nœud produit un objet de configuration de style qui peut être transmis à d'autres nœuds Recraft.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `substyle` | Un style plus spécifique dans la catégorie d'illustration vectorielle. Les options disponibles sont les sous-styles définis pour le style `vector_illustration` par l'API Recraft. Si aucun sous-style n'est choisi, le style de base `vector_illustration` est utilisé. | COMBO | Oui | Plusieurs options disponibles (liste de sous-styles chargée dynamiquement pour le style `vector_illustration`) |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `recraft_style` | Un objet de configuration de style Recraft contenant le style d'illustration vectorielle sélectionné et le sous-style facultatif. Il peut être connecté à d'autres nœuds Recraft. | STYLEV3 |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3VectorIllustrationNode/fr.md)

---
**Source fingerprint (SHA-256):** `e88e7ea35b18acb55ec59814981cb36451d922d3287d23dcdb504289ea9f541b`
