1. VSCode z następującymi rozszerzeniami:
- Python (Microsoft) - zapewnia obsługę pythona
  - zapewnia uruchamianie skryptów python, linting
- WSL (Microsoft)
	- otwieranie folderów i projektów bezpośrednio w WSL,
- Docker (Microsoft)
	- debugowanie aplikacji działających w kontenerach,
	- integracja z Dev Containers
- Dev Containers (Microsoft)
	- otwieranie projektu w kontenerze Docker jako pełnym środowisku deweloperskim,

2. Pliki konfiguracyjne, które trzeba zawrzeć w projekcie
- launch.json
	- należy do folderu .vscode i służy do definiowania jak VS Code ma uruchamiać i debugować Twój projekt.
	- aby każdy członek zespołu mógł uruchamiać projekt w identyczny sposób,
	- aby debugowanie było powtarzalne i zautomatyzowane
- devcontainer.json (wykorzystywany przez rozszerzenie Dev Containers)
	- aby vscode otwierał się jakby wewnątrz kontenera
	- aby nie instalować zależności w systemie – wszystko jest w kontenerze

3. W projekcie dodatkowo zawrzeć trzeba pliki umożliwiające pełną dokeryzację projektu
	- Dockerfile
	- docker-compose.yml
	- requirements.txt
