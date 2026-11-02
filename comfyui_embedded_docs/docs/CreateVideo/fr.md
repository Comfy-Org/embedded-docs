# Créer une vidéo

Le nœud Create Video combine une séquence d'images en une vidéo. Vous pouvez définir la vitesse de lecture en images par seconde, ajouter éventuellement de l'audio, et choisir le format de compression, la profondeur de bits et l'espace colorimétrique de la vidéo résultante.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `images` | Les images à partir desquelles créer une vidéo. | IMAGE | Oui | - |
| `fps` | Le nombre d'images par seconde pour la vitesse de lecture de la vidéo (par défaut : 30.0). | FLOAT | Oui | 1.0 - 120.0 |
| `audio` | L'audio à ajouter à la vidéo. | AUDIO | Non | - |
| `bit_depth` | L'option `auto` utilise 8 bits pour sRGB et 10 bits pour HDR et HDR PQ. Les choix explicites 8 bits et 10 bits sont indépendants de l'espace colorimétrique. (par défaut : "auto") | COMBO | Non | `"auto"`<br>8<br>10 |
| `color_space` | Espace colorimétrique des images d'entrée. HDR sélectionne BT.2020/HLG et HDR PQ sélectionne BT.2020/PQ. (par défaut : "sRGB") | COMBO | Non | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |
| `chroma_subsampling` | 444 conserve la résolution chromatique complète, 422 divise par deux la résolution chromatique horizontale et 420 divise par deux les deux axes. `auto` utilise la valeur par défaut du codec. Les choix non pris en charge utilisent le mode pris en charge le plus proche et affichent un avertissement dans la console. (par défaut : "auto") | COMBO | Non | `"auto"`<br>`"444"`<br>`"422"`<br>`"420"` |
| `codec` | Permet d'encoder éventuellement la vidéo immédiatement. `none` conserve les images sous forme de tenseur ; `auto` utilise H.264. (par défaut : "none") | COMBO | Non | `"none"`<br>Options de codec vidéo disponibles dans la liste des codecs vidéo (par ex. `"auto"` et autres codecs pris en charge) |

Remarque : lorsque `bit_depth` est défini sur `"auto"`, le nœud utilise automatiquement 10 bits pour les espaces colorimétriques HDR et HDR PQ, et 8 bits pour sRGB.

Remarque : le paramètre `codec` est une option avancée. Lorsqu'il reste sur `"none"`, la sortie reste sous forme de tenseur ; sélectionner tout autre codec encode la vidéo immédiatement.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | La vidéo générée contenant les images d'entrée et éventuellement l'audio. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateVideo/fr.md)

---
**Source fingerprint (SHA-256):** `614285ac3a38eedb63fd72f8b70f776b441b1b043707f4b21f587f70e2e071fa`
