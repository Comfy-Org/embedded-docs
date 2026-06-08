Voici la traduction de la documentation technique du nœud ComfyUI **Beeble SwitchX Video Edit** :

# Beeble SwitchX Video Edit

Modifiez une vidéo avec Beeble SwitchX. Ce nœud peut changer n'importe quel élément de la scène (arrière-plan, éclairage, costume) tout en préservant les pixels et le mouvement du sujet d'origine. Fournissez une image de référence et/ou une invite textuelle pour décrire le nouvel aspect souhaité.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `vidéo` | La vidéo d'entrée à éditer. Maximum 240 images, maximum ~2,77 mégapixels par image. | VIDEO | Oui | N/D |
| `invite` | Une description textuelle du nouvel aspect souhaité pour la scène. | STRING | Oui | N/D |
| `mode alpha` | Le mode de mat alpha. Le mode "fill" n'a pas de mat séparé et remplit l'image entière. Le mode "select" utilise une seule image clé pour définir la zone à éditer. Le mode "custom" utilise une vidéo alpha complète pour définir la zone à éditer image par image. | COMBO | Oui | `"fill"`<br>`"select"`<br>`"custom"` |
| `résolution maximale` | La résolution maximale pour la vidéo de sortie (par défaut : "1080p"). | COMBO | Oui | `"720p"`<br>`"1080p"` |
| `graine` | Une valeur de graine pour la reproductibilité. L'utilisation de la même graine avec les mêmes entrées produira le même résultat. | INT | Oui | 0 à 2147483647 |
| `image de référence` | Une image de référence optionnelle décrivant le nouvel aspect souhaité pour la scène. | IMAGE | Non | N/D |

### Détails du mode Alpha

Le paramètre `alpha_mode` contrôle les parties de la vidéo qui sont éditées :

- **fill** : L'image vidéo entière est éditée. Aucun mat alpha séparé n'est produit.
- **select** : Vous fournissez une seule image clé qui définit la zone à éditer. Le nœud l'utilise pour déterminer les parties de la vidéo à modifier.
- **custom** : Vous fournissez une vidéo alpha complète qui définit la zone à éditer image par image. Cela vous donne un contrôle précis sur les parties de chaque image à éditer.

Lorsque vous utilisez le mode `select`, vous devez fournir l'image `alpha_keyframe`. Lorsque vous utilisez le mode `custom`, vous devez fournir la vidéo `alpha_mask`.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `alpha` | La vidéo éditée avec les changements de scène appliqués. | VIDEO |
| `alpha` | Le mat alpha utilisé par Beeble. Il est vide pour le mode "fill", qui n'a pas de mat séparé. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BeebleSwitchXVideoEdit/fr.md)

---
**Source fingerprint (SHA-256):** `e2d67b037863f024f42c97943ec0d2daf32b547b232a7dfedd6de398f4b7ba28`
