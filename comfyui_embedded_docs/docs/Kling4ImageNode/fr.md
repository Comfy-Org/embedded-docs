# Kling 4.0 Image

Générez ou modifiez des images avec Kling 4.0 à partir d'un prompt textuel et d'un maximum de 10 images de référence. Demandez une image unique, ou laissez le nœud renvoyer une série d'images liées qui conservent les mêmes personnages et le même style.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `reference_images` | Emplacements extensibles pour les images de référence (`image_1` ... `image_10`). Faites-y référence dans le prompt sous la forme `@Image1`, `@Image2`, etc. | AUTOGROW | Non | 0 à 10 images |
| `prompt` | Description de l'image. Faites référence aux images connectées sous la forme `@Image1`, `@Image2`, ... Par défaut : chaîne vide. | STRING | Oui | Texte multiligne |
| `resolution` | Résolution de l'image de sortie. Par défaut : `"2K"`. | COMBO | Oui | `"2K"`<br>`"4K"`<br>`"8K"` |
| `aspect_ratio` | Rapport d'aspect de l'image de sortie. `"auto"` suit les images de référence, sinon le prompt. Par défaut : `"auto"`. | COMBO | Oui | `"auto"`<br>`"9:16"`<br>`"2:3"`<br>`"3:4"`<br>`"1:1"`<br>`"4:3"`<br>`"3:2"`<br>`"16:9"`<br>`"21:9"` |
| `series_amount` | Génère une série d'images liées qui conservent les mêmes personnages et le même style. `"auto"` laisse le modèle choisir 2 à 10 images. Par défaut : `"disabled"`. | COMBO | Oui | `"disabled"`<br>`"auto"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` |
| `seed` | La graine contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine. Par défaut : 42. | INT | Oui | 0 à 2147483647 |

**Contraintes et comportement :**

* Au maximum 10 images de référence peuvent être connectées.
* Chaque image doit mesurer au moins 300x300 pixels avec un rapport d'aspect compris entre 2:5 et 5:2.
* Un prompt qui mentionne `@ImageN` déclenche une erreur lorsque moins de N images sont connectées.
* Avec `series_amount` défini sur `"disabled"`, le nœud renvoie une image ; toute autre valeur renvoie un lot de ce nombre d'images.
* Le prix d'un appel évolue en fonction de la résolution, du nombre d'images de référence et du nombre d'images dans la série.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L'image générée, ou un lot d'images lorsque `series_amount` est activé. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4ImageNode/fr.md)

---
**Source fingerprint (SHA-256):** `7840b108419e759942aed332456cab73e748d9f018462011da3b1293646a4ffe`
