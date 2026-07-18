# LumaRay32TextToVideoNode

Ce nœud génère une vidéo à partir d'une invite textuelle en utilisant le modèle Ray 3.2 de Luma. Il envoie votre invite et vos paramètres vidéo à l'API Luma et retourne la vidéo générée ainsi qu'un identifiant de génération.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Invite textuelle pour la génération de la vidéo. | STRING | Oui | 1-6000 caractères |
| `ratio d’aspect` | Le rapport hauteur/largeur de la vidéo générée. | STRING | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"` |
| `résolution` | La résolution de sortie de la vidéo (par défaut : "720p"). | STRING | Oui | `"360p"`<br>`"540p"`<br>`"720p"`<br>`"1080p"` |
| `durée` | La durée de la vidéo générée. | STRING | Oui | `"5s"`<br>`"10s"` |
| `boucle` | Permet de boucler la vidéo de manière fluide. Disponible uniquement avec une durée de 5s. | BOOLEAN | Non | True/False (par défaut : False) |
| `seed` | Graine pour une génération reproductible. | INT | Non | 0 à 2147483647 |

**Remarque :** Le paramètre `loop` ne peut être activé que lorsque `duration` est réglé sur "5s". Si vous sélectionnez une durée de "10s" et activez le bouclage, le nœud retournera une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `identifiant_génération` | Le fichier vidéo généré. | VIDEO |
| `identifiant_génération` | L'identifiant unique de la demande de génération vidéo. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32TextToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `04358a872530e5a2622bf0f148a694f2c707ce8535586d8f860bdf9911e1fa6a`
