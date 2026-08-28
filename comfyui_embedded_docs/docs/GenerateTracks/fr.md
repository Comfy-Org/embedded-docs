# GenerateTracks

Le nœud `GenerateTracks` crée plusieurs trajectoires de mouvement parallèles (pistes) pour la génération vidéo. Il définit une trajectoire principale d'une position de départ à une position d'arrivée, puis génère un ensemble de pistes parallèles à cette trajectoire, espacées uniformément. Vous pouvez contrôler la forme de la trajectoire (ligne droite ou courbe de Bézier), la vitesse de déplacement le long de celle-ci, ainsi que les images dans lesquelles les pistes sont visibles.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `largeur` | La largeur de l'image vidéo en pixels. La valeur par défaut est 832. | INT | Oui | 16 - 4096 |
| `hauteur` | La hauteur de l'image vidéo en pixels. La valeur par défaut est 480. | INT | Oui | 16 - 4096 |
| `départ_x` | Coordonnée X normalisée (0-1) pour la position de départ. La valeur par défaut est 0.0. | FLOAT | Oui | 0.0 - 1.0 |
| `départ_y` | Coordonnée Y normalisée (0-1) pour la position de départ. La valeur par défaut est 0.0. | FLOAT | Oui | 0.0 - 1.0 |
| `fin_x` | Coordonnée X normalisée (0-1) pour la position d'arrivée. La valeur par défaut est 1.0. | FLOAT | Oui | 0.0 - 1.0 |
| `fin_y` | Coordonnée Y normalisée (0-1) pour la position d'arrivée. La valeur par défaut est 1.0. | FLOAT | Oui | 0.0 - 1.0 |
| `nombre_d_images` | Le nombre total d'images pour lequel générer les positions des pistes. La valeur par défaut est 81. | INT | Oui | 1 - 1024 |
| `nombre_de_pistes` | Le nombre de pistes parallèles à générer. La valeur par défaut est 5. | INT | Oui | 1 - 100 |
| `écartement_des_pistes` | Distance normalisée entre les pistes. Les pistes sont réparties perpendiculairement à la direction du mouvement. La valeur par défaut est 0.025. | FLOAT | Oui | 0.0 - 1.0 |
| `bezier` | Active une trajectoire en courbe de Bézier utilisant le point médian comme point de contrôle. La valeur par défaut est False. | BOOLEAN | Oui | True / False |
| `milieu_x` | Point de contrôle X normalisé pour la courbe de Bézier. Utilisé uniquement lorsque 'bezier' est activé. La valeur par défaut est 0.5. | FLOAT | Oui | 0.0 - 1.0 |
| `milieu_y` | Point de contrôle Y normalisé pour la courbe de Bézier. Utilisé uniquement lorsque 'bezier' est activé. La valeur par défaut est 0.5. | FLOAT | Oui | 0.0 - 1.0 |
| `interpolation` | Contrôle le rythme/la vitesse du mouvement le long de la trajectoire (défaut : "linear") :<br>"linear" - vitesse constante<br>"ease_in" - commence lentement et accélère<br>"ease_out" - commence vite et ralentit<br>"ease_in_out" - accélération et décélération fluides<br>"constant" - conserve toutes les positions au point de départ | COMBO | Oui | `"linear"`<br>`"ease_in"`<br>`"ease_out"`<br>`"ease_in_out"`<br>`"constant"` |
| `masque_de_piste` | Masque optionnel pour indiquer les images visibles. S'il est fourni, les images où le masque a un pixel non nul sont marquées comme visibles pour toutes les pistes. | MASK | Non | - |

**Remarque :** Les paramètres `mid_x` et `mid_y` ne sont utilisés que lorsque le paramètre `bezier` est défini sur `True`. Lorsque `bezier` est `False`, la trajectoire est une ligne droite du point de départ au point d'arrivée.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `TRACKS` | Un objet de pistes contenant les coordonnées de trajectoire générées et les informations de visibilité pour toutes les pistes sur toutes les images. | TRACKS |
| `longueur_de_piste` | Le nombre d'images pour lequel les pistes ont été générées, correspondant à l'entrée `num_frames`. | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GenerateTracks/fr.md)

---
**Source fingerprint (SHA-256):** `4bd4d03a84f4b7ea260555b43f217af0b90dd4ca5196aca94e8f3886875ab912`
