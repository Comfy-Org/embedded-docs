# Grok Référence-vers-Vidéo

Le nœud Grok Reference-to-Video génère une vidéo à partir d'une invite textuelle, en utilisant jusqu'à sept images de référence pour guider le style et le contenu de la sortie. Avec le modèle `grok-imagine-video-1.5`, vous pouvez également attacher jusqu'à trois références vocales prédéfinies et faire référence aux images et aux voix directement dans l'invite à l'aide des balises `@ImageN` et `@AudioN`. Le nœud envoie la requête à une API externe, attend la fin de la génération et télécharge la vidéo résultante.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `invite` | Description textuelle de la vidéo souhaitée. Doit être une chaîne non vide. | STRING | Oui | N/A |
| `modèle` | Le modèle à utiliser pour la génération de la vidéo. | COMBO | Oui | `"grok-imagine-video-1.5"`<br>`"grok-imagine-video"` |
| `graine` | Seed pour déterminer si le nœud doit être relancé ; les résultats réels sont non déterministes quel que soit le seed (par défaut : 0). | INT | Non | 0 à 2147483647 |

### Grok Imagine Video 1.5 Entrées

Disponible lorsque `model` est défini sur `grok-imagine-video-1.5`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `voice_1` | Référence vocale prédéfinie facultative ; faites-y référence dans l'invite sous la forme @Audio1. L'API ne prend en charge que ces voix prédéfinies, pas d'audio personnalisé (par défaut : none). | COMBO | Non | Options de voix prédéfinies (y compris `"none"`) |
| `voice_2` | Deuxième référence vocale facultative ; @Audio2 dans l'invite (par défaut : none). | COMBO | Non | Options de voix prédéfinies (y compris `"none"`) |
| `voice_3` | Troisième référence vocale facultative ; @Audio3 dans l'invite (par défaut : none). | COMBO | Non | Options de voix prédéfinies (y compris `"none"`) |
| `resolution` | La résolution de la vidéo de sortie. | COMBO | Oui | `"480p"`<br>`"720p"` |
| `aspect_ratio` | Le rapport hauteur/largeur de la vidéo de sortie. | COMBO | Oui | `"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` |
| `duration` | La durée de la vidéo de sortie en secondes (par défaut : 6). | INT | Oui | 1 à 15 |

### Grok Imagine Video Entrées

Disponible lorsque `model` est défini sur `grok-imagine-video`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `resolution` | La résolution de la vidéo de sortie. | COMBO | Oui | `"480p"`<br>`"720p"` |
| `aspect_ratio` | Le rapport hauteur/largeur de la vidéo de sortie. | COMBO | Oui | `"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` |
| `duration` | La durée de la vidéo de sortie en secondes (par défaut : 6). | INT | Oui | 2 à 10 |

### Entrées de référence

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `reference_images` | Emplacement extensible : connectez de 1 à 7 images de référence pour guider la génération de la vidéo. Avec `grok-imagine-video-1.5`, faites-y référence dans l'invite sous la forme @Image1 ... @Image7, numérotées dans l'ordre des entrées ; une entrée par lot compte pour une image. | IMAGE | Oui | 1 à 7 images |

**Remarque :** Les sous-paramètres affichés dépendent du `model` sélectionné ; `grok-imagine-video-1.5` ajoute les entrées `voice_1`, `voice_2` et `voice_3`. Au moins une image de référence est requise et le total est plafonné à 7 (une entrée par lot compte pour une image). Avec `grok-imagine-video-1.5`, l'invite peut référencer les images connectées sous la forme `@Image1` ... `@Image7` et les voix activées sous la forme `@Audio1`, `@Audio2`, `@Audio3` ; le fait de référencer une image non connectée ou une voix définie sur `none` provoque une erreur. L'API ne prend en charge que les voix prédéfinies, pas l'audio personnalisé.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoReferenceNode/fr.md)

---
**Source fingerprint (SHA-256):** `ac068b34ad7efe786d29f51052a623eaf324041a99b124f6b5f81fadea661a83`
