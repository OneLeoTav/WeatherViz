# WeatherViz

### Installation

**Virtual Environment Setup**
Before setting up the virtual environment, ensure that you have Python 3.9 or higher installed on your system.
1. Clone the project repository: `git clone https://github.com/p-omahony/score_sde_benchmark.git`
2. Create a virtual environment: `virtualenv env` on Linux/MacOS or `python -m venv venv` on Windows
3. Then activate the virtual environment:
- On Linux/MacOS:
  ```bash
  virtualenv env && source env/bin/activate
  ```
- On Windows:
    ```bash
    python -m virtualenv env && source env/Scripts/activate
    ```
4. Install project dependencies: `pip install -r requirements.txt
5. Launch the application locally: `python -B app.py`
6. Open your preferred web brower and access: http://127.0.0.1:8080

**Run with Docker**
After having cloned the repository, go to the root of the project, open a new terminal:
1. Build the image: `docker build -t weatherviz -f Dockerfile.txt .`
2. Run the image: `docker run -it -p 5000:5000 weatherviz`
3. Open your preferred web brower and access: http://127.0.0.1:8080
Alternatively, you can use Docker Compose to simplify the process by executing the following command in the terminal `docker compose up`, then access the application at the aforementioned local address.

## Project Outline
Experience real-time weather forecasts with this Weather Visualization App. Utilizing the capabilities of Flask and Bokeh, this user-friendly interface provides users with intuitive and interactive visualizations of weather data for cities across France. From tracking temperature fluctuations to monitoring wind speeds and precipitation forecasts, stay informed with this dynamic weather visualization tool.
### Main Features
- **City-Specific Data:** Obtain exhaustive weather information for any city in France.
- **Weather Forecast:** Access weather forecasts for the next six days.
- **Interactive Visualizations:** Explore temperature variations, precipitation levels, wind speeds, and humidity levels through interactive Bokeh plots.
- **Hourly Forecast:** Hourly weather predictions for each day for more granular insights.

### Frameworks and Programming Languages Used
- **Flask:** Utilized as the web framework for building the backend of the application, handling HTTP requests, and rendering HTML templates.
- **Bokeh:** Leveraged for creating interactive and dynamic visualizations of weather data, enhancing user engagement and understanding.
- **Python:** Primary programming language for backend development, data processing, and integration of Flask and Bokeh functionalities.
- **HTML/CSS/JavaScript:** Used for designing and styling the user interface, ensuring a visually appealing and responsive web application.
- **Docker:** Dockerfile and docker-compose.yml files included for containerized deployment and easy setup.
- **Requests:** Utilized for making HTTP requests to an external API to obtain weather data.
- **PyTest & Unittest:** Employed for automated testing, ensuring the reliability and robustness of the application under different scenarios.

## Aperçu du Projet
Découvrez les prévisions météorologiques en temps réel avec notre application Web. En utilisant les capacités de Flask et Bokeh, cette plateforme ergonomique fournit aux utilisateurs des visualisations intuitives et interactives des prévisions météorologiques pour les villes de France. Des fluctuations de température à la carte des vents, aux niveaux d'humidité et de pluviométrie, restez informé et préparé avec notre outil de visualisation météorologique dynamique.

**Principales fonctionnalités :**
1. **Données spécifiques à la ville :** Obtenez des informations météorologiques détaillées pour n'importe quelle ville en France.
2. **Prévisions météorologiques :** Accédez aux prévisions météorologiques pour les six prochains jours.
3. **Visualisations interactives :** Explorez les variations de température, les niveaux de précipitations et les niveaux d'humidité grâce à des graphiques interactifs Bokeh.
4. **Prévision horaire :** Analysez les prédictions météorologiques heure par heure pour une information plus précise.

**Technologie utilisées :**
- **Flask :** Framework Web utilisé pour construire le backend de l'application, administrer les requêtes HTTP et générer le contenu HTML à renvoyer.
- **Bokeh :** Utilisé pour créer des visualisations interactives et dynamiques des données météorologiques, améliorant l’ergonomie et l’expérience utilisateur.
- **Python :** Langage de programmation principal pour le développement backend, le traitement des données et l'intégration des fonctionnalités de Flask et Bokeh.
- **HTML/CSS/JavaScript :** Utilisés pour concevoir l'UI, assurant une application Web réactive et visuellement engageante.
- **Docker :** Les fichiers Dockerfile et docker-compose.yml sont inclus pour un déploiement conteneurisé et une configuration facile.
- **Requests :** Utilisé pour effectuer des requêtes HTTP vers une API externe afin d'obtenir des données climatiques.
- **PyTest & Unittest :** Employés pour les tests automatisés, assurant la fiabilité et la robustesse de l'application.
  
## Panorama del Proyecto
Explore las previsiones meteorológicas en tiempo real con nuestra aplicación web. Al aprovechar las capacidades de Flask y Bokeh, esta plataforma intuitiva ofrece a los usuarios visualizaciones interactivas e intuitivas de las previsiones meteorológicas para las ciudades de Francia. Desde las fluctuaciones de temperatura hasta el mapa de vientos, pasando por los niveles de humedad y precipitación, manténgase informado y preparado con nuestra herramienta de visualización meteorológica dinámica.

**Funcionalidades principales:**
1. **Datos específicos por ciudad:** Obtenga información meteorológica detallada para cualquier ciudad en Francia.
2. **Pronósticos meteorológicos:** Acceda a los pronósticos meteorológicos para los próximos seis días.
3. **Visualizaciones interactivas:** Explore las variaciones de temperatura, los niveles de precipitación, las velocidades del viento y los niveles de humedad a través de gráficos interactivos de Bokeh.
4. **Pronóstico por hora:** Analice las previsiones meteorológicas hora por hora para obtener información más precisa.

**Tecnologías utilizadas:**
- **Flask:** Framework web utilizado para construir el backend de la aplicación, administrar las solicitudes HTTP y generar el contenido HTML a devolver.
- **Bokeh:** Utilizado para crear visualizaciones interactivas y dinámicas de los datos meteorológicos, mejorando la experiencia del usuario.
- **Python:** Lenguaje de programación principal para el desarrollo backend, el procesamiento de datos y la integración de las funcionalidades de Flask y Bokeh.
- **HTML/CSS/JavaScript:** Utilizados para diseñar la interfaz de usuario, asegurando una aplicación web receptiva y visualmente atractiva.
- **Docker:** Se incluyen los archivos Dockerfile y docker-compose.yml para una implementación contenerizada y una configuración sencilla.
- **Requests:** Utilizado para realizar solicitudes HTTP a una API externa para obtener datos climáticos.
- **PyTest & Unittest:** Empleado para pruebas automatizadas, garantizando la fiabilidad y la robustez de la aplicación.