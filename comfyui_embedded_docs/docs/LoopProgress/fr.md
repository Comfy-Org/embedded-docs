# LoopProgress

LoopProgress est un nœud d’assistance réservé au développement qui signale la progression d’une boucle à l’interface du serveur ComfyUI. À chaque exécution, il envoie le texte « Iteration X / Y » au client et renvoie la position d’itération actuelle inchangée, ce qui lui permet de s’insérer en ligne dans une boucle sans altérer le flux de données.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `start_id` | Identifiant de l’instance de prompt/boucle à laquelle le message de progression appartient. Le premier élément de la liste fournie sert à acheminer le texte de progression vers l’exécution en cours correcte. | STRING | Oui | - |
| `position` | La position d’itération actuelle (index). Le premier élément de la liste fournie est utilisé dans le message de progression et est également renvoyé comme sortie. | INT | Oui | - |
| `total` | Le nombre total d’itérations. Utilisé avec `position` pour construire le message de progression « Iteration X / Y ». | INT | Oui | - |

Remarque : ce nœud est déclaré avec des entrées de type liste (`is_input_list=True`) et accepte toutes les entrées, donc chaque valeur connectée est traitée comme une liste et seul son premier élément est lu. Le nœud s’exécute toujours (son empreinte d’entrée est fixe), il se réexécute donc à chaque passage de boucle.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `position` | La position d’itération actuelle, transmise sans modification depuis l’entrée `position`. | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoopProgress/fr.md)

---
**Source fingerprint (SHA-256):** `505ba814b93533679516b4f4239f5eee0dbac125d7ea16746c6cdbb7a68f803d`
