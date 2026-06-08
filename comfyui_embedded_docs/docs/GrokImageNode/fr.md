Le nœud Grok Image génère une ou plusieurs images basées sur une description textuelle en utilisant le modèle IA Grok. Il envoie votre invite à un service externe et retourne les images générées sous forme de tenseurs utilisables dans votre workflow.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle Grok spécifique à utiliser pour la génération d'images. Différents modèles peuvent offrir une qualité, une vitesse ou des fonctionnalités variables. | COMBO | Oui | `"grok-imagine-image-quality"`<br>`"grok-imagine-image-pro"`<br>`"grok-imagine-image"`<br>`"grok-imagine-image-beta"` |
| `invite` | L'invite textuelle utilisée pour générer l'image. Cette description guide l'IA sur ce qu'elle doit créer. Doit contenir au moins 1 caractère. | STRING | Oui | N/A |
| `rapport d'aspect` | Le rapport largeur/hauteur souhaité pour l'image générée. | COMBO | Oui | `"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"9:16"`<br>`"16:9"`<br>`"9:19.5"`<br>`"19.5:9"`<br>`"9:20"`<br>`"20:9"`<br>`"1:2"`<br>`"2:1"` |
| `nombre d'images` | Nombre d'images à générer (par défaut : 1). | INT | Non | 1 à 10 |
| `graine` | Une valeur de graine pour déterminer si le nœud doit se réexécuter. Les résultats d'image réels sont non déterministes et varieront même avec la même graine (par défaut : 0). | INT | Non | 0 à 2147483647 |
| `résolution` | La résolution de sortie souhaitée pour les images générées (par défaut : "1K"). | COMBO | Non | `"1K"`<br>`"2K"` |

**Remarque :** Le paramètre `seed` est principalement utilisé pour contrôler quand le nœud se réexécute dans un workflow. En raison de la nature du service IA externe, les images générées ne seront pas reproductibles ni identiques entre les exécutions, même avec une graine identique.

**Remarque sur la tarification :** Le coût de génération des images dépend du `model`, de la `resolution` et du `number_of_images` sélectionnés. Par exemple, le modèle "grok-imagine-image-quality" avec une résolution "1K" coûte 0,05 $ par image, tandis que la résolution "2K" coûte 0,07 $ par image. Le modèle "grok-imagine-image-pro" coûte 0,07 $ par image, et les autres modèles coûtent 0,02 $ par image.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | L'image générée ou un lot d'images. Si `nombre d'images` est 1, un tenseur d'image unique est retourné. S'il est supérieur à 1, un lot de tenseurs d'image est retourné. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageNode/fr.md)

---
**Source fingerprint (SHA-256):** `5c8a76d3636dea8bcc6ade0d8adb6e6d1610b518a31e15fc7fce3f107fe63953`
