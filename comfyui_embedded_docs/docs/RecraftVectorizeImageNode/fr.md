# Vectoriser une image avec Recraft

Génère des graphiques vectoriels SVG à partir d'une image d'entrée. Ce nœud convertit les images matricielles en format vectoriel évolutif en envoyant chaque image à l'API Recraft et en combinant les résultats en une sortie SVG unique.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `image` | L'image d'entrée à convertir au format SVG. Prend en charge le traitement par lots de plusieurs images. | IMAGE | Oui | - |
| `version` | La version du vectoriseur : `v1` est la version standard, et `v1_pro` (Vectorizer Pro) produit des SVG plus propres avec des courbes lisses, des lignes droites et des angles nets, idéal pour le lettrage et les formes complexes (par défaut : "v1"). | COMBO | Non | "v1"<br>"v1_pro" |
| `shape_stacking` | Comment les formes sont empilées dans le SVG : `hierarchical` superpose les formes les unes sur les autres ; `cut_out` crée des formes qui ne se chevauchent jamais, pour les traceurs, les découpeuses vinyle et la sérigraphie (par défaut : "hierarchical"). | COMBO | Non | "hierarchical"<br>"cut_out" |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `SVG` | La sortie de graphiques vectoriels générée combinant toutes les images traitées en un seul document SVG. | SVG |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftVectorizeImageNode/fr.md)

---
**Source fingerprint (SHA-256):** `b7f8245de0597e8d3ceeef5a15b378e0903965a7e15c1825cacdf2387b278c7e`
