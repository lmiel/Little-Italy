# Little-Italy

Link Github: https://github.com/lmiel/Little-Italy.git

## Contribuidores

Lucía Mielgo Torres (lmiel & matzull)
Martina González García (martinagg7)

Este es un proyecto de una página web interactiva para un restaurante italiano, diseñada para ofrecer a los usuarios la posibilidad de explorar un menú digital, hacer pedidos en línea y conocer más sobre las recetas auténticas italianas y sus valores nutricionales.

## Descripción

El sitio web presenta un diseño atractivo que incluye secciones para productos destacados, información sobre el proceso artesanal de la cocina, y la opción de hacer pedidos. El menú está completamente interactivo, con imágenes de alta calidad y descripciones detalladas de cada plato.

### Funcionalidades

- **Explora nuestros productos**: Los usuarios pueden explorar diversas categorías de platos como pizzas, pastas y postres, con información detallada sobre cada uno.
  
- **Realiza tu pedido en línea**: Los clientes pueden agregar artículos a su carrito y realizar pedidos directamente desde la web. Aunque la funcionalidad de pago aún no está completamente implementada, se contempla integrar la API de [Stripe](https://stripe.com) para procesar pagos de forma segura en el futuro.

- **Recetas a través de Spoonacular**: Nos hemos integrado con la API de [Spoonacular](https://spoonacular.com/food-api) para proporcionar recetas detalladas de los platos que ofrecemos, permitiendo a los usuarios descubrir cómo hacer las recetas en casa.

- **Información nutricional con Edamam**: Usamos la API de [Edamam](https://developer.edamam.com/) para obtener información nutricional precisa sobre los productos del menú, ayudando a los usuarios a tomar decisiones informadas sobre su alimentación.

## Implementación de Pagos

Actualmente, el sistema de pagos no está completamente implementado. Se planifica integrar la API de Stripe para permitir pagos seguros y eficientes en línea. Esto facilitaría a los usuarios realizar pedidos y pagar de manera fácil y rápida.

## Instalación

Para ejecutar este proyecto en tu máquina local, sigue los siguientes pasos:

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/restaurante-italiano.git
   
2. Navega al directorio del proyecto:
   ```bash
   cd little_italy

3. Crea un archivo .env: En el directorio raíz del proyecto, crea un archivo .env y añade las claves de las APIs necesarias. El archivo debe tener el siguiente formato:
   ```bash
   SPOONACULAR_API_KEY=tu_clave_de_api_spoonacular_1
   SPOONACULAR_API_KEY2=tu_clave_de_api_spoonacular_2

   EDAMAM_APPLICATION_ID=tu_id_de_aplicacion_edamam
   EDAMAM_API_KEY=tu_clave_de_api_edamam

   DATABASE_URL=postgres://usuario:contraseña@host:puerto/base_de_datos?sslmode=require
   DATABASE_URL_UNPOOLED=postgresql://usuario:contraseña@host:puerto/base_de_datos?sslmode=require

   PGHOST=host
   PGHOST_UNPOOLED=host
   PGUSER=usuario
   PGDATABASE=base_de_datos
   PGPASSWORD=contraseña

   POSTGRES_URL=postgres://usuario:contraseña@host:puerto/base_de_datos?sslmode=require
   POSTGRES_URL_NON_POOLING=postgres://usuario:contraseña@host:puerto/base_de_datos?sslmode=require
   POSTGRES_USER=usuario
   POSTGRES_HOST=host
   POSTGRES_PASSWORD=contraseña
   POSTGRES_DATABASE=base_de_datos
   POSTGRES_URL_NO_SSL=postgres://usuario:contraseña@host:puerto/base_de_datos
   POSTGRES_PRISMA_URL=postgres://usuario:contraseña@host:puerto/base_de_datos?pgbouncer=true&connect_timeout=15&sslmode=require

4. Instalar dependencias: Si hay dependencias que instalar, ejecuta el siguiente comando:
   ```bash
   pip install -r requirements.txt

5. Ejecutar el servidor: Para ejecutar el servidor de desarrollo de Django, usa el siguiente comando:
   ```bash
   python manage.py runserver

