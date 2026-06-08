Voici la traduction en français de la documentation du nœud SAM3 Detect :

# Nœud SAM3 Detect

## Aperçu

Le nœud SAM3 Detect effectue une détection et une segmentation à vocabulaire ouvert à l'aide de descriptions textuelles, de boîtes englobantes ou d'invites ponctuelles. Il peut identifier et segmenter des objets dans une image en fonction de ce que vous décrivez dans le texte, de l'endroit où vous dessinez des boîtes ou de l'endroit où vous cliquez sur des points.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle SAM3 à utiliser pour la détection et la segmentation | MODEL | Oui | - |
| `image` | L'image d'entrée à traiter | IMAGE | Oui | - |
| `conditionnement` | Conditionnement textuel provenant de CLIPTextEncode. Requis lors de l'utilisation d'invites textuelles pour la détection | CONDITIONING | Non | - |
| `boîtes_englobantes` | Boîtes englobantes dans lesquelles segmenter. Peut être une seule boîte (appliquée à toutes les images), une liste de boîtes (appliquée à toutes les images) ou une liste de listes (boîtes par image). Lorsqu'elles sont fournies sans conditionnement textuel, le nœud segmente à l'intérieur de chaque boîte | BOUNDING_BOX | Non | - |
| `coords_positives` | Invites ponctuelles positives au format JSON `[{"x": int, "y": int}, ...]` utilisant les coordonnées en pixels. Ce sont les points que vous souhaitez inclure dans la segmentation | STRING | Non | - |
| `coords_négatives` | Invites ponctuelles négatives au format JSON `[{"x": int, "y": int}, ...]` utilisant les coordonnées en pixels. Ce sont les points que vous souhaitez exclure de la segmentation | STRING | Non | - |
| `seuil` | Seuil de confiance pour les détections basées sur le texte. Seules les détections dont les scores sont supérieurs à cette valeur sont conservées (par défaut : 0.5) | FLOAT | Non | 0.0 à 1.0 |
| `itérations_affinage` | Nombre de passes de raffinement du décodeur SAM. Des valeurs plus élevées peuvent améliorer la qualité des masques. Réglez sur 0 pour utiliser les masques bruts du détecteur sans raffinement (par défaut : 2) | INT | Non | 0 à 5 |
| `masques_individuels` | Lorsqu'il est activé, produit des masques séparés pour chaque objet détecté au lieu de les combiner en un seul masque (par défaut : Faux) | BOOLEAN | Non | Vrai/Faux |

### Contraintes et remarques sur les paramètres

- **Invites textuelles** : Pour utiliser la détection basée sur le texte, vous devez fournir l'entrée `conditioning`. Lorsqu'un conditionnement textuel est fourni, le nœud exécute une détection guidée par le texte sur l'image.
- **Invites par boîtes** : Lorsque des `bboxes` sont fournies sans conditionnement textuel, le nœud segmente la zone à l'intérieur de chaque boîte englobante.
- **Invites ponctuelles** : Lorsque `positive_coords` ou `negative_coords` sont fournis, le nœud utilise une segmentation basée sur les points. Les points sont automatiquement mis à l'échelle en fonction de la résolution interne du modèle.
- **Types d'invites multiples** : Vous pouvez combiner différents types d'invites. Par exemple, vous pouvez fournir à la fois un conditionnement textuel et des boîtes englobantes pour restreindre la détection textuelle à des zones spécifiques.
- **Traitement par lots** : Le nœud prend en charge les images par lots. Lors du traitement de plusieurs images, les boîtes englobantes peuvent être fournies par image en utilisant un format de liste de listes.
- **Format JSON pour les points** : Les coordonnées des points doivent être fournies sous forme de chaînes JSON valides au format `[{"x": 100, "y": 200}, {"x": 150, "y": 250}]`.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `boîtes_englobantes` | Masques de segmentation. Lorsque `masques_individuels` est Faux (par défaut), renvoie un seul masque combiné par image. Lorsqu'il est Vrai, renvoie des masques individuels pour chaque objet détecté | MASK |
| `boîtes_englobantes` | Boîtes englobantes détectées avec les coordonnées et les scores de confiance. Chaque boîte inclut les valeurs `x`, `y`, `width`, `height` et `score` | BOUNDING_BOX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_Detect/fr.md)

---
**Source fingerprint (SHA-256):** `d073bda7eca934f3c64e1be740f5fb5249d27046a8be5902ea5d2245d5f679ea`
