> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_Detect/fr.md)

# Nœud SAM3 Detect

## Présentation

Le nœud SAM3 Detect effectue une détection et une segmentation à vocabulaire ouvert à l'aide de descriptions textuelles, de boîtes englobantes ou d'invites par points. Il peut identifier et segmenter des objets dans une image en fonction de ce que vous décrivez en texte, de l'endroit où vous dessinez des boîtes ou de l'endroit où vous cliquez sur des points.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle SAM3 à utiliser pour la détection et la segmentation |
| `image` | IMAGE | Oui | - | L'image d'entrée à traiter |
| `conditioning` | CONDITIONING | Non | - | Conditionnement textuel provenant de CLIPTextEncode. Requis lors de l'utilisation d'invites textuelles pour la détection |
| `bboxes` | BOUNDING_BOX | Non | - | Boîtes englobantes dans lesquelles segmenter. Peut être une seule boîte (appliquée à toutes les images), une liste de boîtes (appliquée à toutes les images) ou une liste de listes (boîtes par image). Lorsqu'il est fourni sans conditionnement textuel, le nœud segmente à l'intérieur de chaque boîte |
| `positive_coords` | STRING | Non | - | Invites par points positifs au format JSON `[{"x": int, "y": int}, ...]` utilisant les coordonnées en pixels. Ce sont les points que vous souhaitez inclure dans la segmentation |
| `negative_coords` | STRING | Non | - | Invites par points négatifs au format JSON `[{"x": int, "y": int}, ...]` utilisant les coordonnées en pixels. Ce sont les points que vous souhaitez exclure de la segmentation |
| `threshold` | FLOAT | Non | 0,0 à 1,0 | Seuil de confiance pour les détections basées sur le texte. Seules les détections avec des scores supérieurs à cette valeur sont conservées (par défaut : 0,5) |
| `refine_iterations` | INT | Non | 0 à 5 | Nombre de passes d'affinement du décodeur SAM. Des valeurs plus élevées peuvent améliorer la qualité des masques. Mettre à 0 pour utiliser les masques bruts du détecteur sans affinement (par défaut : 2) |
| `individual_masks` | BOOLEAN | Non | Vrai/Faux | Lorsqu'il est activé, produit des masques séparés pour chaque objet détecté au lieu de les combiner en un seul masque (par défaut : Faux) |

### Contraintes et remarques sur les paramètres

- **Invites textuelles** : Pour utiliser la détection basée sur le texte, vous devez fournir l'entrée `conditioning`. Lorsqu'un conditionnement textuel est fourni, le nœud effectue une détection guidée par le texte sur l'image.
- **Invites par boîtes** : Lorsque des `bboxes` sont fournies sans conditionnement textuel, le nœud segmente la zone à l'intérieur de chaque boîte englobante.
- **Invites par points** : Lorsque `positive_coords` ou `negative_coords` sont fournis, le nœud utilise une segmentation basée sur les points. Les points sont automatiquement mis à l'échelle selon la résolution interne du modèle.
- **Types d'invites multiples** : Vous pouvez combiner différents types d'invites. Par exemple, vous pouvez fournir à la fois un conditionnement textuel et des boîtes englobantes pour restreindre la détection textuelle à des zones spécifiques.
- **Traitement par lots** : Le nœud prend en charge les images par lots. Lors du traitement de plusieurs images, les boîtes englobantes peuvent être fournies par image en utilisant un format de liste de listes.
- **Format JSON pour les points** : Les coordonnées des points doivent être fournies sous forme de chaînes JSON valides au format `[{"x": 100, "y": 200}, {"x": 150, "y": 250}]`.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `masks` | MASK | Masques de segmentation. Lorsque `individual_masks` est Faux (par défaut), renvoie un seul masque combiné par image. Lorsqu'il est Vrai, renvoie des masques individuels pour chaque objet détecté |
| `bboxes` | BOUNDING_BOX | Boîtes englobantes détectées avec coordonnées et scores de confiance. Chaque boîte inclut les valeurs `x`, `y`, `width`, `height` et `score` |