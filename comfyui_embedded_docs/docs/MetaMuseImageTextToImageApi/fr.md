# MetaMuseImageTextToImageApi

Meta Muse Image Text to Image génère des images à partir d'un prompt texte en utilisant le modèle Muse Image de Meta. Le modèle raisonne sur le prompt avant la génération et peut utiliser la recherche web, la recherche d'images et l'exécution de code lors de la planification de l'image. Le nœud appelle l'API Muse Image et retourne l'image ou les images résultantes.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Modèle à utiliser. | DYNAMIC_COMBO | Oui | `"muse-image-1.0"` |

La sélection d'un modèle dans la liste affiche les paramètres pris en charge par ce modèle. Le seul modèle disponible est `muse-image-1.0` ; ses paramètres sont énumérés ci-dessous.

### Entrées muse-image-1.0

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Prompt décrivant l'image. Le modèle raisonne sur le prompt et peut utiliser sa recherche web et d'images intégrée avant la génération. | STRING | Oui | Texte multiligne, minimum 1 caractère |
| `aspect_ratio` | Format d'image de la sortie. Les images sont générées à environ 2,5 mégapixels (1:1 est 1600x1600, 16:9 est 2048x1152) ; « auto » laisse le modèle choisir à partir du prompt. | COMBO | Oui | `"auto"`<br>`"1:1"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"5:4"`<br>`"4:5"`<br>`"16:9"`<br>`"9:16"`<br>`"21:9"`<br>`"9:21"`<br>`"2:1"`<br>`"1:2"` |
| `reasoning_strength` | Degré de réflexion, de planification et d'auto-affinage du modèle avant la génération. | COMBO | Oui | `"high"`<br>`"low"` |
| `enable_web_search` | Permet au modèle de rechercher sur le web des informations factuelles et en temps réel pendant la planification de l'image. | BOOLEAN | Non | True<br>False (défaut : True) |
| `enable_image_search` | Permet au modèle de rechercher des images de référence pendant la planification de l'image. | BOOLEAN | Non | True<br>False (défaut : True) |
| `enable_shell` | Permet au modèle d'exécuter du code pendant la planification, pour des mises en page, graphiques et diagrammes précis ; désactivé, les quantités et l'alignement sont approximatifs. | BOOLEAN | Non | True<br>False (défaut : True) |
| `seed` | Seed déterminant si le nœud doit se réexécuter ; l'API ne possède pas de seed, donc les résultats réels sont non déterministes quelle que soit cette valeur. | INT | Oui | 0 – 2147483647 (défaut : 42) |

Remarque : Le prompt doit contenir au moins un caractère. Lorsque `aspect_ratio` est défini sur « auto », aucune taille explicite n'est envoyée à l'API et le modèle décide de la taille de sortie à partir du prompt. Le paramètre `seed` contrôle uniquement le moment où le nœud se réexécute ; il n'est pas envoyé à l'API, par conséquent les résultats générés sont non déterministes.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L'image générée retournée par l'API, décodée et fournie sous forme d'image groupée. Si la réponse de l'API contient plusieurs images, elles sont combinées en un seul lot. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MetaMuseImageTextToImageApi/fr.md)

---
**Source fingerprint (SHA-256):** `59ebd72fab3db44a35ceac723606de4eabb5fe2b690d0b701db50e0e22a9e699`
