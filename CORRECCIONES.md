**Taller DevOps CI Workshop**

Meylin Ximena Callejas Sepúlveda  
 Maria Lucia Torres Portela 

Correcciones

Error 1

Archivo: app.py

Problema: La aplicación estaba configurada inicialmente en el puerto 5001, mientras que Docker y el pipeline trabajaban sobre el puerto 5000\.

Solución: Se modificó port=5001 por port=5000 para mantener consistencia entre todos los servicios.

Error 2

Archivo: app.py

Problema: El endpoint de métricas estaba definido como /metric, lo que ocasionaba errores 404 durante las pruebas automáticas y en Prometheus.

Solución: Se cambió la ruta a /metrics para coincidir con los tests, Prometheus y el pipeline CI/CD.

Error 3

Archivo: app.py

Problema: El endpoint /health no incluía el campo uptime\_seconds, requerido por las pruebas automatizadas.

Solución: Se agregó el cálculo de tiempo de ejecución usando la librería time y se añadió el campo uptime\_seconds a la respuesta JSON.

Error 4

Archivo: test\_app.py

Problema: Las pruebas no validaban correctamente los nuevos campos del endpoint /health.

Solución: Se actualizaron los tests para verificar la existencia de uptime\_seconds y validar el estado de salud de la aplicación.

Error 5

Archivo: requirements.txt

Problema: El pipeline fallaba con el error pytest: command not found porque la librería pytest no estaba instalada.

Solución: Se agregó pytest al archivo requirements.txt.

Error 6

Archivo: ci.yml

Problema: El contenedor Docker no tenía suficiente tiempo para iniciar antes de ejecutar las pruebas.

Solución: Se aumentó el tiempo de espera utilizando sleep 10\.

Error 7

Archivo: app.py

Problema: Se utilizó \_name\_ y \_main\_ en lugar de \_\_name\_\_ y \_\_main\_\_, generando errores de ejecución en Python.

Solución: Se corrigieron las variables especiales utilizando doble guion bajo correctamente.

Error 8

Archivo: prometheus.yml

Problema: Prometheus no podía obtener las métricas de la aplicación debido a que el endpoint configurado era incorrecto.

Solución: Se actualizó la configuración de Prometheus para consultar correctamente el endpoint /metrics.

Error 9

Archivo: docker-compose.yml

Problema: Existía inconsistencia entre los puertos expuestos por Docker y los utilizados por la aplicación y Prometheus.

Solución: Se ajustó la configuración de puertos para que la API utilizara correctamente el puerto 5000 y Prometheus el puerto 9090\.

Instalar dependencias

33 Downloading markupsafe-3.0.3-cp311-cp311-manylinux2014\_x86\_64.manylinux\_2\_17\_x86\_64.manylinux\_2\_28\_x86\_64.whl (22 kB)

34 Downloading werkzeug-3.1.8-py3-none-any.whl (226 kB)

35 Installing collected packages: psutil, MarkupSafe, itsdangerous, click, blinker, werkzeug, Jinja2, flask

37 Successfully installed Jinja2-3.1.6 MarkupSafe-3.0.3 Werkzeug-3.1.8 blinker-1.9.0 click-8.3.3 flask-3.0.0 itsdangerous-2.2.0 psutil-5.9.8

39 Notice: A new release of pip is available: 26.0.1 \-\> 26.1.1

40 Notice: To update, run: pip install \--upgrade pip

\============================= test session starts \=============================

platform linux \-- Python 3.11.15, pytest-8.0.0, pluggy-1.6.0

rootdir: /home/runner/work/devops-ci-workshop/devops-ci-workshop

collected 3 items

test\_app.py ..F                                                   \[100%\]

\=================================== FAILURES \===================================

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ test\_health \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

def test\_health():

    client \= app.app.test\_client()

    response \= client.get('/health')

    assert response.status\_code \== 200

    data \= response.get\_json()

\>   assert "uptime\_seconds" in data

E   AssertionError: assert 'uptime\_seconds' in {'cpu\_percent': 33.3, 'memory\_percent': 5.9, 'status': 'healthy'}

test\_app.py:16: AssertionError

\=========================== short test summary info \============================

FAILED test\_app.py::test\_health \- AssertionError: assert 'uptime\_seconds' in {'cpu\_percent': 33.3, 'memory\_percent': 5.9, 'status': 'healthy'}

\========================= 1 failed, 2 passed in 0.13s \=========================

Error: Process completed with exit code 1\.

