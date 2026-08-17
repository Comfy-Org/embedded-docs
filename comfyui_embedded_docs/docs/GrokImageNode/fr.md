# Grok Image

Le nœud Grok Image génère une ou plusieurs images à partir d'une invite texte en utilisant les modèles d'IA d'image Grok. Il envoie l'invite et les paramètres à un service externe et retourne les images générées sous forme de tenseurs pouvant être utilisés ailleurs dans le workflow.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle Grok spécifique à utiliser pour la génération d'images. Différents modèles peuvent offrir une qualité, une vitesse ou des fonctionnalités variables. | COMBO | Oui | `"grok-imagine-image-2.0"`<br>`"grok-imagine-image-quality"`<br>`"grok-imagine-image-pro"`<br>`"grok-imagine-image"` |
| `prompt` | L'invite texte utilisée pour générer l'image. Cette description guide l'IA sur ce qu'elle doit créer. Doit contenir au moins 1 caractère non blanc. | STRING | Oui | N/A |
| `aspect_ratio` | Le rapport largeur/hauteur souhaité pour l'image générée. | COMBO | Oui | `"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"9:16"`<br>`"16:9"`<br>`"9:19.5"`<br>`"19.5:9"`<br>`"9:20"`<br>`"20:9"`<br>`"1:2"`<br>`"2:1"` |
| `number_of_images` | Nombre d'images à générer (défaut : 1). | INT | Oui | 1 to 10 |
| `seed` | Graine (seed) pour déterminer si le nœud doit se ré-exécuter ; les résultats réels sont non déterministes quelle que soit la graine (défaut : 0). | INT | Oui | 0 to 2147483647 |
| `resolution` | La résolution de sortie souhaitée pour les images générées (défaut : « 1K »). | COMBO | Non | `"1K"`<br>`"2K"` |
| `quality` | Niveau de qualité, pris en charge uniquement par le modèle grok-imagine-image-2.0 (défaut : « medium »). | COMBO | Non | Plusieurs options disponibles |

**Remarque :** Le paramètre `quality` n'est appliqué que lorsque `model` est défini sur « grok-imagine-image-2.0 ». Pour tous les autres modèles, ce paramètre est ignoré.

**Remarque :** Le paramètre `seed` est principalement utilisé pour contrôler quand le nœud se ré-exécute dans un workflow. En raison de la nature du service IA externe, les images générées ne sont pas reproductibles d'une exécution à l'autre, même avec une graine identique.

**Remarque sur la tarification :** Le coût de génération des images dépend du `model`, de la `resolution`, de la `quality` et du `number_of_images` sélectionnés ; le prix total est le tarif par image multiplié par `number_of_images`. Pour le modèle « grok-imagine-image-2.0 », le tarif par image est de 0,04 $ en résolution « 1K » et de 0,06 $ en « 2K » avec une qualité « low », ou de 0,06 $ en « 1K » et de 0,08 $ en « 2K » avec les autres niveaux de qualité. Le modèle « grok-imagine-image-quality » coûte 0,05 $ par image en « 1K » et 0,07 $ par image en « 2K ». Le modèle « grok-imagine-image-pro » coûte 0,07 $ par image. Les autres modèles coûtent 0,02 $ par image.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | L'image générée ou un lot d'images. Si `number_of_images` est 1, un tenseur d'image unique est retourné. S'il est supérieur à 1, un lot de tenseurs d'images est retourné. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageNode/fr.md)

---
**Source fingerprint (SHA-256):** `a89f5df0d4827f45013f1af92541d36b5b8c8edc8626e07af4fe2d85ee5486e7`
