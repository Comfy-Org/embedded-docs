# Ideogram Vector Generate SVG

Ce nœud génère un SVG modifiable à partir d'un prompt textuel avec Ideogram Vector, éventuellement guidé par jusqu'à 5 images de référence. Le résultat est un balisage vectoriel plutôt qu'une image raster, de sorte que les formes restent modifiables dans un éditeur vectoriel.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Modèle à utiliser. Par défaut : `"ideogram-vector-1"`. | DYNAMIC_COMBO | Oui | `"ideogram-vector-1"` |
| `images` | Images de référence facultatives. L'image 1 est la source principale et les images 2 à 5 sont des références supplémentaires ; mentionnez-les dans le prompt sous la forme `@Image1`, `@Image2`, etc. Une entrée en lot est comptée une fois par image. | AUTOGROW | Non | 0 à 5 images |
| `prompt` | Description du SVG. Prend en charge les références de style `@Image1` vers les images d'entrée. | STRING | Oui | 1 à 9500 caractères |
| `aspect_ratio` | `"auto"` suit l'image 1, ou le prompt lorsqu'aucune image n'est connectée. Par défaut : `"auto"`. | COMBO | Oui | `"auto"`<br>`"1:3"`<br>`"1:2"`<br>`"9:16"`<br>`"10:16"`<br>`"2:3"`<br>`"3:4"`<br>`"4:5"`<br>`"1:1"`<br>`"5:4"`<br>`"4:3"`<br>`"3:2"`<br>`"16:10"`<br>`"16:9"`<br>`"2:1"`<br>`"3:1"` |
| `quality` | Niveau de qualité. Les niveaux plus élevés coûtent plus cher et prennent plus de temps. Par défaut : `"medium"`. | COMBO | Oui | `"low"`<br>`"medium"`<br>`"high"` |
| `seed` | Graine pour la génération. Les mêmes prompt, images, paramètres et graine donnent le même SVG. Par défaut : 42. | INT | Oui | 0 à 2147483647 |

**Contraintes :**

* Le prompt doit contenir entre 1 et 9500 caractères.
* `images` accepte au maximum 5 images, comptées individuellement lorsque l'entrée est en lot, et chaque image doit avoir un rapport d'aspect compris entre 1:6 et 6:1.
* Les images dont le côté le plus long dépasse 2048 pixels sont réduites avant l'envoi.
* Référencer une image qui n'est pas connectée, par exemple `@Image4` avec seulement deux images fournies, génère une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `SVG` | Le SVG généré sous forme de balisage vectoriel modifiable. | SVG |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramVectorGenerateApi/fr.md)

---
**Source fingerprint (SHA-256):** `5bd24ad48d6c26daf43f84544a9c22a18961dea645799104591f3785a851f819`
