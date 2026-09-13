# Appliquer une texture au maillage

Ce nœud attache des images de textures précalculées à la disposition UV d'un maillage afin qu'elles puissent être exportées avec le maillage par le nœud SaveGLB. Fournissez-lui le même maillage déplié en UV que celui à partir duquel vous avez précalculé les textures, ainsi que les cartes d'images précalculées. Les cartes metallic, roughness et occlusion optionnelles sont regroupées dans une seule texture ORM, et fournir une normal map stocke également les normales de sommets lissées et la base tangentielle nécessaires à un ombrage correct.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `mesh` | Le maillage déplié en UV auquel les textures précalculées seront attachées. Doit être le même maillage que celui utilisé lors du précalcul ; une erreur est levée si le maillage n'a pas d'UV. | MESH | Oui | — |
| `base_color` | L'image de couleur de base précalculée. Stockée comme texture du maillage et bornée à la plage 0-1. | IMAGE | Oui | — |
| `metallic` | La carte metallic précalculée. Utilisée comme canal bleu de la texture ORM combinée ; vaut 0 par défaut lorsqu'elle n'est pas fournie. | IMAGE | Non | — |
| `roughness` | La carte roughness précalculée. Utilisée comme canal vert de la texture ORM combinée ; vaut 1 par défaut lorsqu'elle n'est pas fournie. | IMAGE | Non | — |
| `occlusion` | La carte d'occlusion ambiante précalculée. Utilisée comme canal rouge de la texture ORM combinée ; vaut 1 par défaut lorsqu'elle n'est pas fournie. Lorsqu'elle est fournie, la texture ORM est également marquée comme texture d'occlusion pour SaveGLB. | IMAGE | Non | — |
| `normal_map` | La carte normale en espace tangent précalculée. Lorsqu'elle est fournie, le nœud recalcule les tangentes par sommet et exporte des normales de sommets lissées afin que la carte normale soit ombrée correctement. | IMAGE | Non | — |

Remarque : L'entrée `mesh` doit avoir des coordonnées UV ; si ce n'est pas le cas, le nœud lève une erreur vous demandant de connecter le même maillage déplié en UV que celui utilisé pour le précalcul.

Remarque : Lorsque l'une des entrées `metallic`, `roughness` ou `occlusion` est connectée, les trois sont regroupées dans une seule texture ORM glTF avec les canaux R = occlusion, G = roughness, B = metallic. Les cartes manquantes sont remplies avec les valeurs par défaut (occlusion 1, roughness 1, metallic 0), et les cartes ayant des résolutions différentes sont redimensionnées à la plus grande largeur et à la plus grande hauteur parmi les cartes fournies.

Remarque : Lorsque `normal_map` est connectée, les normales stockées du maillage sont remplacées par des normales de sommets lissées calculées et une base tangentielle par sommet est ajoutée. Les coordonnées UV qui se trouvent en dehors de la plage [0,1] sont mises à l'échelle uniformément dans [0,1] tout en préservant le rapport d'aspect ; un avertissement est consigné si l'étendue UV ressemble à une disposition tuilée/UDIM. Pour les maillages par lots, la normalisation UV est appliquée séparément à chaque élément du lot en utilisant la même logique que l'étape de précalcul, afin que les deux restent alignés.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `mesh` | Le maillage d'entrée avec les images de textures attachées à sa disposition UV, prêt à être enregistré par SaveGLB. | MESH |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ApplyTextureToMesh/fr.md)

---
**Source fingerprint (SHA-256):** `7492922c9c7c0117366cb8b9017fc192eb8dd6b6594fd429044d60408693210e`
