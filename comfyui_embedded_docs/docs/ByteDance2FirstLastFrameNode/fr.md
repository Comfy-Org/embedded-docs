# ByteDance Seedance 2.0 Première-Dernière-Image vers Vidéo

Ce nœud génère une vidéo à partir d'une première image de frame requise et d'une dernière image de frame facultative à l'aide des modèles ByteDance Seedance. Vous décrivez la vidéo avec une invite textuelle ; la première image de frame guide le début de la vidéo et la dernière image de frame guide la fin. Il prend en charge Seedance 2.5 et la famille Seedance 2.0 (Seedance 2.0, Seedance 2.0 Fast et Seedance 2.0 Mini).

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Seedance 2.5 pour le modèle le plus récent, vidéos jusqu'à 30 secondes et sortie mp4/mov ; Seedance 2.0 pour une qualité maximale et 4k ; Fast pour l'optimisation de la vitesse ; Mini pour la génération la plus rapide et la moins coûteuse. La sélection d'un modèle révèle des entrées spécifiques au modèle ci-dessous. | DYNAMIC_COMBO | Oui | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `première image` | Image de la première frame de la vidéo. | IMAGE | Non | - |
| `dernière image` | Image de la dernière frame de la vidéo. | IMAGE | Non | - |
| `first_frame_asset_id` | asset_id Seedance à utiliser comme première frame. Mutuellement exclusif avec l'entrée d'image `first_frame`. Par défaut, chaîne vide. | STRING | Non | - |
| `last_frame_asset_id` | asset_id Seedance à utiliser comme dernière frame. Mutuellement exclusif avec l'entrée d'image `last_frame`. Par défaut, chaîne vide. | STRING | Non | - |
| `seed` | La seed contrôle si le nœud doit être relancé ; les résultats sont non déterministes quelle que soit la seed. Par défaut, 0. | INT | Oui | 0 à 2147483647 |
| `filigrane` | Indique s'il faut ajouter un filigrane à la vidéo. Par défaut, False. | BOOLEAN | Oui | False<br>True |

### Entrées Seedance 2.5

Ces entrées apparaissent lorsque `Seedance 2.5` est sélectionné.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Invite textuelle pour la génération de la vidéo. Mettez les répliques parlées entre guillemets pour orienter le dialogue généré. | STRING | Oui | - |
| `resolution` | Résolution de la vidéo de sortie. Par défaut, 720p. | COMBO | Oui | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `duration` | Durée de la vidéo de sortie en secondes (4-30). Par défaut, 5. | INT | Oui | 4 à 30 |
| `generate_audio` | Activer la génération audio pour la vidéo de sortie. Par défaut, True. | BOOLEAN | Oui | False<br>True |
| `output_format` | Format de conteneur de la vidéo de sortie. Par défaut, mp4. | COMBO | Oui | `"mp4"` |

### Entrées Seedance 2.0

Ces entrées apparaissent lorsque `Seedance 2.0` est sélectionné.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Invite textuelle pour la génération de la vidéo. | STRING | Oui | - |
| `resolution` | Résolution de la vidéo de sortie. | COMBO | Oui | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Ratio d'aspect de la vidéo de sortie. Par défaut, `adaptive`, qui utilise le ratio pris en charge le plus proche du ratio d'aspect de la frame d'entrée. | COMBO | Oui | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Durée de la vidéo de sortie en secondes (4-15). Par défaut, 7. | INT | Oui | 4 à 15 |
| `generate_audio` | Activer la génération audio pour la vidéo de sortie. Par défaut, True. | BOOLEAN | Oui | False<br>True |

### Entrées Seedance 2.0 Fast et Seedance 2.0 Mini

Partagées par `Seedance 2.0 Fast` et `Seedance 2.0 Mini`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Invite textuelle pour la génération de la vidéo. | STRING | Oui | - |
| `resolution` | Résolution de la vidéo de sortie. | COMBO | Oui | `"480p"`<br>`"720p"` |
| `ratio` | Ratio d'aspect de la vidéo de sortie. Par défaut, `adaptive`, qui utilise le ratio pris en charge le plus proche du ratio d'aspect de la frame d'entrée. | COMBO | Oui | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Durée de la vidéo de sortie en secondes (4-15). Par défaut, 7. | INT | Oui | 4 à 15 |
| `generate_audio` | Activer la génération audio pour la vidéo de sortie. Par défaut, True. | BOOLEAN | Oui | False<br>True |

**Contraintes de paramètres**

- Vous devez fournir la première frame soit comme image `first_frame`, soit comme `first_frame_asset_id`. Fournir les deux provoque une erreur ; n'en fournir aucun provoque également une erreur.
- Les entrées `last_frame` et `last_frame_asset_id` sont facultatives, mais vous ne pouvez pas fournir les deux pour la même frame.
- Les asset_ids doivent référencer des assets Seedance Image existants et actifs.
- L'entrée `prompt` est requise et ne peut pas être vide.
- Avec `Seedance 2.5`, le ratio d'aspect de sortie est toujours adaptatif et suit le ratio d'aspect propre à la première frame, donc aucune entrée `ratio` n'est affichée.
- Avec les modèles de la famille Seedance 2.0 et les images de frame locales, les images sont recadrées au centre et redimensionnées à la résolution et au ratio de sortie cibles avant la génération. Lorsque `ratio` est `adaptive`, le ratio pris en charge le plus proche de l'image d'entrée est utilisé.
- Les images de frame locales sont validées pour le ratio d'aspect et les dimensions pris en charge ; les images surdimensionnées sont réduites.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | La vidéo générée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2FirstLastFrameNode/fr.md)

---
**Source fingerprint (SHA-256):** `bc2eb5f43c935986ad870703cfbc92dd99a53d6f0ac91cf0cad46bee33ff2cc0`
