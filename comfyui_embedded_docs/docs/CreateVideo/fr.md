# Créer une vidéo

Le nœud Create Video génère un fichier vidéo à partir d'une séquence d'images. Vous pouvez définir la vitesse de lecture en images par seconde, ajouter éventuellement de l'audio, et choisir la profondeur de bits ainsi que l'espace colorimétrique de la vidéo résultante.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `images` | Les images à partir desquelles créer une vidéo. | IMAGE | Oui | - |
| `fps` | Le nombre d'images par seconde pour la vitesse de lecture de la vidéo (par défaut : 30.0). | FLOAT | Oui | 1.0 - 120.0 |
| `audio` | L'audio à ajouter à la vidéo. | AUDIO | Non | - |
| `bit_depth` | Auto utilise 8 bits pour sRGB et 10 bits pour HDR. Les choix explicites 8 bits et 10 bits sont indépendants de l'espace colorimétrique. (par défaut : « auto ») | COMBO | Non | `"auto"`<br>8<br>10 |
| `color_space` | Espace colorimétrique des images d'entrée. HDR sélectionne BT.2020/HLG et HDR PQ sélectionne BT.2020/PQ. (par défaut : « sRGB ») | COMBO | Non | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |

Remarque : Lorsque `bit_depth` est défini sur « auto », le nœud utilise 10 bits pour les espaces colorimétriques HDR et HDR PQ, et 8 bits pour sRGB.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | La vidéo générée contenant les images d'entrée et l'audio facultatif. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateVideo/fr.md)

---
**Source fingerprint (SHA-256):** `2fa73f38b0609de4159e557b6abe73652c5bebab9d34ffdda743b0eac6049f13`
