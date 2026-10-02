# Flux 3 Image

Flux 3 Image génère une image avec FLUX 3 à partir d'un prompt, ou modifie et combine des images de référence. Écrivez ce que vous voulez comme instruction, puis connectez jusqu'à 10 images de référence et référencez-les dans le prompt sous la forme image 1, image 2, etc. Le prompt est interprété et développé avant la génération, et le résultat est rendu au rapport d'aspect et à la résolution que vous choisissez.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Ce qu'il faut générer, ou la modification à apporter. Le prompt est interprété et développé avant la génération. Référencez les images de référence connectées sous la forme image 1, image 2, etc. (par défaut : "") | STRING | Oui | 1 à 15000 caractères |
| `images` | Emplacement extensible pour les images de référence ; connectez-en jusqu'à 10 au total. Chaque image doit mesurer au moins 256x256 pixels, et son rapport d'aspect ne peut pas être plus extrême que 64:1. | IMAGE | Non | 0 à 10 images |
| `bounding_boxes` | Zones facultatives provenant du nœud Create Bounding Boxes qui placent des objets ou du texte dans la sortie. Les positions sont relatives au canevas, donc donnez au nœud le rapport d'aspect de la sortie. | ARRAY | Non | - |
| `aspect_ratio` | Rapport d'aspect de l'image générée. "auto" suit la première image de référence, ou choisit un ratio à partir du prompt. (par défaut : "auto") | COMBO | Oui | `"auto"`<br>`"21:9"`<br>`"2:1"`<br>`"16:9"`<br>`"3:2"`<br>`"7:5"`<br>`"4:3"`<br>`"5:4"`<br>`"1:1"`<br>`"4:5"`<br>`"3:4"`<br>`"5:7"`<br>`"2:3"`<br>`"9:16"`<br>`"1:2"`<br>`"9:21"` |
| `resolution` | Taille de sortie au rapport d'aspect choisi : 0.75K correspond à environ 0,6 mégapixel, 1K à 1 MP, 1.5K à 2,4 MP, 2K à 4,2 MP, 4K à 16,8 MP. (par défaut : "2K") | COMBO | Oui | `"0.75K"`<br>`"1K"`<br>`"1.5K"`<br>`"2K"`<br>`"4K"` |
| `grounding` | Permet au modèle d'effectuer des recherches sur le prompt avec la recherche Web et la recherche d'images avant de générer. (par défaut : True) | BOOLEAN | Oui | True<br>False |
| `safety_tolerance` | Tolérance de modération, 0 étant la plus stricte. (par défaut : 4) | INT | Oui | 0 à 4 |
| `seed` | Graine déterminant si le nœud doit être réexécuté ; FLUX 3 choisit sa propre graine, donc les résultats réels sont non déterministes quelle que soit cette valeur. (par défaut : 42) | INT | Oui | 0 à 4294967295 |

`safety_tolerance` est une entrée avancée, et `seed` inclut les contrôles Control After Generate dans l'interface utilisateur.

Les images de référence sont téléversées avant l'envoi de la requête. Un même emplacement peut contenir un lot, et chaque image de chaque lot compte dans la limite de 10 images.

Les lignes de `bounding_boxes` sont ajoutées au prompt, donc le prompt et les descriptions des zones doivent totaliser 15000 caractères ou moins.

Le prix affiché dépend de `resolution` : 0,05863 $ en 0.75K, 0,06864 $ en 1K, 0,1001 $ en 1.5K, 0,143 $ en 2K et 0,86801 $ en 4K.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | L'image générée, téléchargée depuis le résultat FLUX 3. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3ImageNode/fr.md)

---
**Source fingerprint (SHA-256):** `f32a90887227f9ce9e6ed04a76cde452a70f36fb97d8c36d7c55140855c1f593`
