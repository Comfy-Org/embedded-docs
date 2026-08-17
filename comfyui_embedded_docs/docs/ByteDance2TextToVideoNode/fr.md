# ByteDance Seedance 2.0 Texte vers Vidéo

Ce nœud génère une vidéo à partir d’une description textuelle en utilisant les modèles Seedance 2.5 ou 2.0 de ByteDance. Il envoie votre prompt au modèle sélectionné, attend que la vidéo soit traitée, puis renvoie le résultat final.

## Entrées

Le paramètre `model` est une liste dynamique. Lorsque vous sélectionnez un modèle, plusieurs entrées spécifiques au modèle apparaissent et doivent être renseignées, notamment le prompt textuel, la résolution, le ratio d’aspect, la durée et le paramètre de génération audio.

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle à utiliser pour la génération de vidéos. Seedance 2.5 est le modèle le plus récent, générant des vidéos jusqu’à 30 secondes avec sortie mp4/mov ; Seedance 2.0 offre une qualité maximale avec 1080p/4k ; Fast est optimisé pour la vitesse ; Mini est le plus rapide et le moins coûteux. | DYNAMIC_COMBO | Oui | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `seed` | Contrôle si le nœud doit se réexécuter ; les résultats sont non déterministes quelle que soit la valeur de départ (par défaut : 0). | INT | Non | 0 à 2147483647 |
| `watermark` | Indique s’il faut ajouter un filigrane à la vidéo (par défaut : False). Il s’agit d’un paramètre avancé. | BOOLEAN | Non | True / False |

### Entrées Seedance 2.5

Ces entrées apparaissent lorsque `model` est défini sur `Seedance 2.5`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Prompt textuel pour la génération de vidéo. Mettez les répliques parlées entre guillemets pour orienter le dialogue généré (par défaut : vide). | STRING | Oui | Texte libre |
| `resolution` | Résolution de la vidéo de sortie (par défaut : « 720p »). | COMBO | Oui | `"480p"`<br>`"720p"` |
| `ratio` | Ratio d’aspect de la vidéo de sortie (par défaut : « 16:9 »). | COMBO | Oui | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Durée de la vidéo de sortie en secondes (par défaut : 5). | INT | Oui | 4 à 30 |
| `generate_audio` | Active la génération audio pour la vidéo de sortie (par défaut : True). | BOOLEAN | Non | True / False |
| `output_format` | Format conteneur de la vidéo de sortie (par défaut : « mp4 »). | COMBO | Oui | `"mp4"` |

### Entrées Seedance 2.0

Ces entrées apparaissent lorsque `model` est défini sur `Seedance 2.0`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Prompt textuel pour la génération de vidéo (par défaut : vide). | STRING | Oui | Texte libre |
| `resolution` | Résolution de la vidéo de sortie. | COMBO | Oui | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Ratio d’aspect de la vidéo de sortie (par défaut : « 16:9 »). | COMBO | Oui | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Durée de la vidéo de sortie en secondes (par défaut : 7). | INT | Oui | 4 à 15 |
| `generate_audio` | Active la génération audio pour la vidéo de sortie (par défaut : True). | BOOLEAN | Non | True / False |

### Entrées Seedance 2.0 Fast et Seedance 2.0 Mini

Ces entrées apparaissent lorsque `model` est défini sur `Seedance 2.0 Fast` ou `Seedance 2.0 Mini`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Prompt textuel pour la génération de vidéo (par défaut : vide). | STRING | Oui | Texte libre |
| `resolution` | Résolution de la vidéo de sortie. | COMBO | Oui | `"480p"`<br>`"720p"` |
| `ratio` | Ratio d’aspect de la vidéo de sortie (par défaut : « 16:9 »). | COMBO | Oui | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Durée de la vidéo de sortie en secondes (par défaut : 7). | INT | Oui | 4 à 15 |
| `generate_audio` | Active la génération audio pour la vidéo de sortie (par défaut : True). | BOOLEAN | Non | True / False |

**Remarque :** Le `prompt` doit contenir au moins 1 caractère après suppression des espaces, sinon la tâche échoue à la validation. Les limites de durée dépendent du modèle : Seedance 2.5 prend en charge 4 à 30 secondes, tandis que Seedance 2.0, Seedance 2.0 Fast et Seedance 2.0 Mini prennent en charge 4 à 15 secondes. Les options de résolution diffèrent également selon le modèle : Seedance 2.5 prend en charge 480p et 720p ; Seedance 2.0 prend en charge 480p, 720p, 1080p et 4k ; Seedance 2.0 Fast et Seedance 2.0 Mini ne prennent en charge que 480p et 720p.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2TextToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `66d200f4ddf674b897def63604b0f29dcbf655e00b4e9b9c11e31b671ead94bc`
