# Grok Référence-vers-Vidéo

Le nœud Grok Reference-to-Video génère une vidéo à partir d'un prompt textuel, en utilisant jusqu'à sept images de référence pour guider le style et le contenu de la sortie. Avec le modèle `grok-imagine-video-1.5`, vous pouvez également ajouter jusqu'à trois références vocales prédéfinies et faire référence directement aux images et aux voix dans le prompt à l'aide des balises `@ImageN` et `@AudioN`. Le nœud envoie la requête à une API externe, attend la fin de la génération et télécharge la vidéo résultante.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Le modèle à utiliser pour la génération vidéo. | DYNAMIC_COMBO | Oui | `"grok-imagine-video-1.5"`<br>`"grok-imagine-video"` |
| `invite` | Description textuelle de la vidéo souhaitée. Doit être une chaîne non vide. | STRING | Oui | N/A |
| `graine` | Graine pour déterminer si le nœud doit se réexécuter ; les résultats réels sont non déterministes quelle que soit la graine (défaut : 0). | INT | Oui | 0 à 2147483647 |

### Entrées Grok Imagine Video 1.5

Disponible lorsque `model` est défini sur `grok-imagine-video-1.5`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `voice_1` | Référence vocale prédéfinie facultative ; faites-y référence dans le prompt sous la forme @Audio1. L'API ne prend en charge que ces voix prédéfinies, pas d'audio personnalisé (défaut : none). | COMBO | Non | Options de voix prédéfinies, y compris `"none"` |
| `voice_2` | Deuxième référence vocale facultative ; @Audio2 dans le prompt (défaut : none). | COMBO | Non | Options de voix prédéfinies, y compris `"none"` |
| `voice_3` | Troisième référence vocale facultative ; @Audio3 dans le prompt (défaut : none). | COMBO | Non | Options de voix prédéfinies, y compris `"none"` |
| `resolution` | La résolution de la vidéo de sortie. | COMBO | Oui | `"480p"`<br>`"720p"` |
| `aspect_ratio` | Le rapport d'aspect de la vidéo de sortie. | COMBO | Oui | `"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` |
| `duration` | La durée de la vidéo de sortie en secondes (défaut : 6). | INT | Oui | 1 à 15 |

### Entrées Grok Imagine Video

Disponible lorsque `model` est défini sur `grok-imagine-video`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `resolution` | La résolution de la vidéo de sortie. | COMBO | Oui | `"480p"`<br>`"720p"` |
| `aspect_ratio` | Le rapport d'aspect de la vidéo de sortie. | COMBO | Oui | `"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` |
| `duration` | La durée de la vidéo de sortie en secondes (défaut : 6). | INT | Oui | 2 à 10 |

### Entrées de référence

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `reference_images` | Emplacement extensible : connectez 1 à 7 images de référence pour guider la génération vidéo. Avec `grok-imagine-video-1.5`, faites-y référence dans le prompt sous la forme @Image1 ... @Image7, numérotées dans l'ordre des entrées ; une entrée par lot compte une fois par image. | IMAGE | Oui | 1 à 7 images |

**Remarque :** Les sous-paramètres affichés dépendent du `model` sélectionné ; `grok-imagine-video-1.5` ajoute les entrées `voice_1`, `voice_2` et `voice_3`. Au moins une image de référence est requise, et le total est plafonné à 7 (une entrée par lot compte une fois par image). Avec `grok-imagine-video-1.5`, le prompt peut référencer les images connectées comme `@Image1` ... `@Image7` et les emplacements vocaux comme `@Audio1`, `@Audio2`, `@Audio3` ; un `@image` ou `@audio` non numéroté fait référence au premier. `@AudioN` fait référence au widget `voice_N`, et non à l'ordre des voix activées. Référencer une image non connectée ou un emplacement vocal défini sur `none` provoque une erreur. L'API ne prend en charge que les voix prédéfinies, pas d'audio personnalisé.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoReferenceNode/fr.md)

---
**Source fingerprint (SHA-256):** `e584c450563eaa7fcb7751d2325f9ef847fa34a4342df01f2bd9ce2e4ff8f2c3`
