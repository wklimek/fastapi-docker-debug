## Zdalne debuggowanie projektu w kontenerze Docker

1. VSCode z następującymi rozszerzeniami:
- Python (Microsoft) - zapewnia obsługę pythona
  - zapewnia uruchamianie skryptów python, linting
- WSL (Microsoft) - tylko, gdy korzystamy z Windows i usługi WSL do Ubuntu
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

4. Uruchomienie i debuggowanie projektu:

	- W Windows z WSL
		- uruchomienie projektu w docker
			- w PowerShell uruchamiamy WSL, wchodzimy do konsoli WSL i dalej do projektu (pamiętaj, aby projekt był umieszczony w przestrzeni WSL (po wejściu cd ~), a nie w Windows)
			- uruchamiamy kontenery: docker compose up
		- otwarcie projektu w vscode
			- uruchamiamy w Windows vscode
			- łączymy się z WSL (ctr+shift+P i connect to WSL)
			- otwieramy folder projektu - przy wyborze już prowadzi nas do folderu na WSL
			- gdy wczytuje się projekt i napotka odpowiednio skonfigurowany plik devcontainer.json, to zapyta nas czy chcemy otworzyć projekt bezpośrednio w kontenerze - zgadzamy się. W ten sposób vscode widzi zainstalowane w konenerze pakiety itp.
		- teraz możemy już ustawiać breakpointy i rozpcząć debuggowanie (kluczowe jest ustawienie w launch.json "request": "attach", które mówi vscode, że nie ma uruchamiać swojego interpretera python, tylko podłączyć się do tego uruchomionego w kontenerze)
		- endpointy ruchamiamy w przeglądarce lub kliencie np. postman w Windows jako localhost.

	- Bezpośrednio w Linux
		- uruchomienie projektu w docker
			- w konsoli Linux wchodzimy do folderu projektu
			- uruchamiamy kontenery: docker compose up
		- otwarcie projektu w vscode
			- uruchamiamy w Linux vscode
			- otwieramy folder projektu
			- gdy wczytuje się projekt i napotka odpowiednio skonfigurowany plik devcontainer.json, to zapyta nas czy chcemy otworzyć projekt bezpośrednio w kontenerze - zgadzamy się. W ten sposób vscode widzi zainstalowane w konenerze pakiety itp.
			- jeżeli się nie zgodzimy, to nadal dzięki odpowiedniej konfiguracji pliu launch.json będziemy mogli debuggować zdalnie projekt w kontenerze, ale będziemy mieli lokalnie otwarty projekt w vscode i nie będziemy widzieli zainstalowanych pakietów w kontenerze (vscode nie rozpozna ich np. fastapi)
		- teraz możemy już ustawiać breakpointy i rozpcząć debuggowanie (kluczowe jest ustawienie w launch.json "request": "attach", które mówi vscode, że nie ma uruchamiać swojego interpretera python, tylko podłączyć się do tego uruchomionego w kontenerze)
		- endpointy ruchamiamy w przeglądarce lub kliencie np. postman w Windows jako localhost.


