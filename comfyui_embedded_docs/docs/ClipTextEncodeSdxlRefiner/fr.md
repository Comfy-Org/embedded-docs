# CLIPTextEncodeSDXLRefiner

Ce nœud est spécialement conçu pour le modèle SDXL Refiner afin de convertir des invites textuelles en informations de conditionnement en intégrant des scores esthétiques et des informations dimensionnelles, améliorant ainsi les conditions pour les tâches de génération et optimisant l'effet de raffinement final. Il agit comme un directeur artistique professionnel, non seulement en transmettant votre intention créative, mais aussi en injectant des normes esthétiques précises et des exigences de spécifications dans l'œuvre.

## À propos de SDXL Refiner

SDXL Refiner est un modèle de raffinement spécialisé qui se concentre sur l'amélioration des détails et de la qualité des images à partir du modèle de base SDXL. Ce processus s'apparente à l'intervention d'un retoucheur d'art :

1. Il reçoit d'abord les images préliminaires ou les descriptions textuelles générées par le modèle de base
2. Ensuite, il guide le processus de raffinement grâce à une notation esthétique précise et des paramètres dimensionnels
3. Enfin, il se concentre sur le traitement des détails d'image haute fréquence pour améliorer la qualité globale

Le Refiner peut être utilisé de deux manières :

- Comme une étape de raffinement autonome pour le post-traitement des images générées par le modèle de base
- Comme partie d'un système d'intégration expert, prenant le relais du traitement pendant la phase de faible bruit de la génération

## Entrées

| Nom du paramètre | Description | Type de données | Type d'entrée | Valeur par défaut | Plage de valeurs |
| --- | --- | --- | --- | --- | --- |
| `clip` | Instance du modèle CLIP utilisée pour la tokenisation et l'encodage du texte, composant central pour convertir le texte en un format compréhensible par le modèle | CLIP | Requis | - | - |
| `ascore` | Contrôle la qualité visuelle et l'esthétique des images générées, similaire à la définition de normes de qualité pour une œuvre d'art :<br/>- Scores élevés (7.5-8.5) : Recherche d'effets plus raffinés et riches en détails<br/>- Scores moyens (6.0-7.0) : Contrôle de qualité équilibré<br/>- Scores faibles (2.0-3.0) : Adapté aux invites négatives | FLOAT | Optionnel | 6.0 | 0.0-1000.0 |
| `largeur` | Spécifie la largeur de l'image de sortie (en pixels), doit être un multiple de 8. SDXL donne les meilleurs résultats lorsque le nombre total de pixels est proche de 1024×1024 (environ 1 million de pixels) | INT | Requis | 1024 | 64-16384 |
| `hauteur` | Spécifie la hauteur de l'image de sortie (en pixels), doit être un multiple de 8. SDXL donne les meilleurs résultats lorsque le nombre total de pixels est proche de 1024×1024 (environ 1 million de pixels) | INT | Requis | 1024 | 64-16384 |
| `texte` | Description textuelle de l'invite, prend en charge la saisie multi-lignes et la syntaxe d'invite dynamique. Dans le Refiner, les invites textuelles doivent se concentrer davantage sur la description de la qualité visuelle et des caractéristiques de détail souhaitées | STRING | Requis | - | - |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `CONDITIONING` | Sortie conditionnelle raffinée contenant l'encodage intégré de la sémantique du texte, des normes esthétiques et des informations dimensionnelles, spécifiquement conçue pour guider le modèle SDXL Refiner dans un raffinement précis de l'image | CONDITIONING |

## Remarques

1. Ce nœud est spécifiquement optimisé pour le modèle SDXL Refiner et diffère des nœuds CLIPTextEncode classiques
2. Un score esthétique de 7,5 est recommandé comme valeur de référence, ce qui correspond au réglage standard utilisé dans l'entraînement de SDXL
3. Tous les paramètres dimensionnels doivent être des multiples de 8, et un nombre total de pixels proche de 1024×1024 (environ 1 million de pixels) est recommandé
4. Le modèle Refiner se concentre sur l'amélioration des détails et de la qualité de l'image, donc les invites textuelles doivent mettre l'accent sur les effets visuels souhaités plutôt que sur le contenu de la scène
5. En pratique, le Refiner est généralement utilisé dans les dernières étapes de la génération (environ les 20% d'étapes restantes), en se concentrant sur l'optimisation des détails

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeSDXLRefiner/fr.md)
