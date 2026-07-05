# GenerateTracks

Le nœud `GenerateTracks` crée plusieurs trajectoires de mouvement parallèles pour la génération vidéo. Il définit un chemin principal d'un point de départ à un point d'arrivée, puis génère un ensemble de pistes parallèles à ce chemin, espacées de manière uniforme. Vous pouvez contrôler la forme du chemin (ligne droite ou courbe de Bézier), la vitesse de déplacement le long de celui-ci et les images dans lesquelles les pistes sont visibles.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `largeur` | La largeur de l'image vidéo en pixels. La valeur par défaut est 832. | INT | Oui | 16 - 4096 |
| `hauteur` | La hauteur de l'image vidéo en pixels. La valeur par défaut est 480. | INT | Oui | 16 - 4096 |
| `départ_x` | Coordonnée X normalisée (0-1) pour la position de départ. La valeur par défaut est 0.0. | FLOAT | Oui | 0.0 - 1.0 |
| `départ_y` | Coordonnée Y normalisée (0-1) pour la position de départ. La valeur par défaut est 0.0. | FLOAT | Oui | 0.0 - 1.0 |
| `fin_x` | Coordonnée X normalisée (0-1) pour la position d'arrivée. La valeur par défaut est 1.0. | FLOAT | Oui | 0.0 - 1.0 |
| `fin_y` | Coordonnée Y normalisée (0-1) pour la position d'arrivée. La valeur par défaut est 1.0. | FLOAT | Oui | 0.0 - 1.0 |
| `nombre_d_images` | Le nombre total d'images pour lesquelles générer les positions des pistes. La valeur par défaut est 81. | INT | Oui | 1 - 1024 |
| `nombre_de_pistes` | Le nombre de pistes parallèles à générer. La valeur par défaut est 5. | INT | Oui | 1 - 100 |
| `écartement_des_pistes` | Distance normalisée entre les pistes. Les pistes sont réparties perpendiculairement à la direction du mouvement. La valeur par défaut est 0.025. | FLOAT | Oui | 0.0 - 1.0 |
| `bezier` | Activer le chemin en courbe de Bézier en utilisant le point milieu comme point de contrôle. La valeur par défaut est Faux. | BOOLEAN | Oui | Vrai / Faux |
| `milieu_x` | Point de contrôle X normalisé pour la courbe de Bézier. Utilisé uniquement lorsque 'bezier' est activé. La valeur par défaut est 0.5. | FLOAT | Oui | 0.0 - 1.0 |
| `milieu_y` | Point de contrôle Y normalisé pour la courbe de Bézier. Utilisé uniquement lorsque 'bezier' est activé. La valeur par défaut est 0.5. | FLOAT | Oui | 0.0 - 1.0 |
| `interpolation` | Contrôle le timing/la vitesse du mouvement le long du chemin. La valeur par défaut est "linear". | COMBO | Oui | `"linear"`<br>`"ease_in"`<br>`"ease_out"`<br>`"ease_in_out"`<br>`"constant"` |
| `masque_de_piste` | Masque optionnel pour indiquer les images visibles. | MASK | Non | - |

**Remarque :** Les paramètres `mid_x` et `mid_y` sont utilisés uniquement lorsque le paramètre `bezier` est défini sur `True`. Lorsque `bezier` est `False`, le chemin est une ligne droite du point de départ au point d'arrivée.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `longueur_de_piste` | Un objet pistes contenant les coordonnées du chemin généré et les informations de visibilité pour toutes les pistes sur toutes les images. | TRACKS |
| `longueur_de_piste` | Le nombre d'images pour lesquelles les pistes ont été générées, correspondant à la valeur d'entrée `nombre_d_images`. | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GenerateTracks/fr.md)

---
**Source fingerprint (SHA-256):** `3dca1cabaee8738e2a68acafed47ad347019d03c9b7f0d1392b3fdf97d0e8add`
